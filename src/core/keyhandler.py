#-*- coding: UTF-8 -*-
from queue import Queue
from core.keyboardinterceptor import KeyboardInterceptor
from utils.action import Action,moveEventMap,clickEventMap
from threading import Event, Thread
from core.mover import Mover
import pyautogui
import copy

BUFF_SET = {1,2,3,4,5}

class KeyHandler(Thread):
    ROUND_TIME = 20
    endSignal = False
    keyBoardInterceptor = None
    actionQueue = None
    moveSet = set()
    moveSignal = None
    mover = None
    def __init__(self, keyBoardInterceptor: KeyboardInterceptor, actionQueue: Queue ,config:dict = None):
        Thread.__init__(self)
        self.keyBoardInterceptor = keyBoardInterceptor
        self.actionQueue = actionQueue 
        self.moveSignal = Event()
        self.mover = Mover(self.moveSet,self.moveSignal,config)
        self.moveEventMap = copy.copy(moveEventMap)
        if config!= None and self.validConfig(config):
            self.moveEventMap['_P_space'] = 'SPEED_BUFF_%s' % config.get("spaceBuff")
            self.moveEventMap['_R_space'] = 'SPEED_BUFF_%s_STOP' % config.get("spaceBuff")
            self.moveEventMap['_P_shift_l'] = 'SPEED_BUFF_%s' % config.get("shiftBuff")
            self.moveEventMap['_R_shift_l'] = 'SPEED_BUFF_%s_STOP' % config.get("shiftBuff")
    
    def validConfig(self,config):
        try:
            if config.get("spaceBuff") not in BUFF_SET:
                return False
            if config.get("shiftBuff") not in BUFF_SET:
                return False
        except:
            return False
        return True
        
        
    def run(self):
        self.mover.start()
        while True:
            if self.endSignal:
                self.mover.stop()
                break
            keyEvent = self.actionQueue.get()
            if keyEvent == '_EXIT_':
                self.mover.stop()
                break
            if keyEvent in self.moveEventMap:
                self.updateMoveKeySet(keyEvent)
            else:
                self.makeClick(keyEvent)
    
    def stop(self):
        self.endSignal = True
        
    def updateMoveKeySet(self, keyEvent):
        moveAction = self.moveEventMap.get(keyEvent)
        # print('moveKeyEvent: %s,moveAction: %s' % (keyEvent,moveAction))
        if moveAction == Action.MOVE_DOWN.value:
            if Action.MOVE_UP not in self.moveSet:
                self.moveSet.add(Action.MOVE_DOWN.value)
                self.moveSignal.set()
            else:
                self.moveSet.discard(Action.MOVE_UP.value)
                self.moveSignal.set()
        if moveAction == Action.MOVE_UP.value:
            if Action.MOVE_DOWN.value not in self.moveSet:
                self.moveSet.add(Action.MOVE_UP.value)
                self.moveSignal.set()
            else:
                self.moveSet.discard(Action.MOVE_DOWN.value)
                self.moveSignal.set()
        if moveAction == Action.MOVE_LEFT.value:
            if Action.MOVE_RIGHT.value not in self.moveSet:
                self.moveSet.add(Action.MOVE_LEFT.value)
                self.moveSignal.set()
            else:
                self.moveSet.discard(Action.MOVE_RIGHT.value)
                self.moveSignal.set()
        if moveAction == Action.MOVE_RIGHT.value:
            if Action.MOVE_LEFT.value not in self.moveSet:
                self.moveSet.add(Action.MOVE_RIGHT.value)
                self.moveSignal.set()
            else:
                self.moveSet.discard(Action.MOVE_LEFT.value)
                self.moveSignal.set()
        if moveAction == Action.SCROLL_UP.value:
            if Action.SCROLL_DOWN.value not in self.moveSet:
                self.moveSet.add(Action.SCROLL_UP.value)
                self.moveSignal.set()
            else:
                self.moveSet.discard(Action.SCROLL_DOWN.value)
                self.moveSignal.set()
        if moveAction == Action.SCROLL_DOWN.value:
            if Action.SCROLL_UP.value not in self.moveSet:
                self.moveSet.add(Action.SCROLL_DOWN.value)
                self.moveSignal.set()
            else:
                self.moveSet.discard(Action.SCROLL_UP.value)
                self.moveSignal.set()
        
        if moveAction == Action.SPEED_BUFF_1.value or moveAction == Action.SPEED_BUFF_2.value \
            or moveAction == Action.SPEED_BUFF_3.value or moveAction == Action.SPEED_BUFF_4.value \
            or moveAction == Action.SPEED_BUFF_5.value:
            self.moveSet.discard(Action.SPEED_BUFF_1.value)
            self.moveSet.discard(Action.SPEED_BUFF_2.value)
            self.moveSet.discard(Action.SPEED_BUFF_3.value)
            self.moveSet.discard(Action.SPEED_BUFF_4.value)
            self.moveSet.discard(Action.SPEED_BUFF_5.value)
            self.moveSet.add(moveAction)
            self.moveSignal.set()
        
        if(moveAction == Action.MOVE_DOWN_STOP.value or moveAction == Action.MOVE_UP_STOP.value 
            or moveAction == Action.MOVE_LEFT_STOP.value or moveAction == Action.MOVE_RIGHT_STOP.value
            or moveAction == Action.SCROLL_UP_STOP.value or moveAction == Action.SCROLL_DOWN_STOP.value
            or moveAction == Action.SPEED_BUFF_1_STOP.value or moveAction == Action.SPEED_BUFF_2_STOP.value
            or moveAction == Action.SPEED_BUFF_3_STOP.value or moveAction == Action.SPEED_BUFF_4_STOP.value
            or moveAction == Action.SPEED_BUFF_5_STOP.value):
            len1 = len(self.moveSet)
            self.moveSet.discard(moveAction[:-5])
            len2 = len(self.moveSet)
            if len2 != len1:
                self.moveSignal.set()
    
    def makeClick(self, keyEvent):
        if keyEvent not in clickEventMap:
            return
        clickAction = clickEventMap.get(keyEvent)
        if clickAction == Action.PRESS_LEFT.value:
            pyautogui.mouseDown(button='primary')
        if clickAction == Action.RELEASE_LEFT.value:
            pyautogui.mouseUp(button='primary')
        if clickAction == Action.PPRESS_RIGHT.value:
            pyautogui.mouseDown(button='secondary')
        if clickAction == Action.RELEASE_RIGHT.value:
            pyautogui.mouseUp(button='secondary')
        if clickAction == Action.SCROLL_PRESS.value:
            pyautogui.mouseDown(button='middle')
        if clickAction == Action.SCROLL_RELEASE.value:
            pyautogui.mouseUp(button='middle')
        
        if clickAction == Action.EDIT.value:
            pyautogui.click(button='primary')
            pyautogui.move(0, 36)
            self.keyBoardInterceptor.enable = False

        if clickAction == Action.COPY.value:
            pyautogui.hotkey('ctrl', 'c')
            pyautogui.mouseUp(button='primary')
        if clickAction == Action.CUT.value:
            pyautogui.hotkey('ctrl', 'x')
            pyautogui.mouseUp(button='primary')
        if clickAction == Action.PASTE.value:
            pyautogui.click(button='primary')
            pyautogui.hotkey('ctrl', 'v')
        if clickAction == Action.UNDO.value:
            pyautogui.hotkey('ctrl', 'z') 