#-*- coding: UTF-8 -*-
from sys import flags
from threading import Thread,Event
import time
from utils.action import MoveAction,speedBuffMap
import pyautogui
import copy

class Mover(Thread):
    ROUND_RANGE = 20
    MOVE_STEP = 6
    endSignal = False
    lastTick = None
    moveSet = None
    speedCoef= 1
    signal = None 
    roundTable = set()

    def __init__(self, moveSet: set, signal:Event,config:dict = None):
        Thread.__init__(self)
        self.moveSet = moveSet
        self.signal = signal
        self.lastTick = int(round(time.time()*1000))
        self.speedBuff = copy.copy(speedBuffMap)
        if config != None and self.validConfig(config):
            self.speedBuff['SPEED_BUFF_1'] = float(config.get("buffCoef1"))
            self.speedBuff['SPEED_BUFF_2'] = float(config.get("buffCoef2"))
            self.speedBuff['SPEED_BUFF_3'] = float(config.get("buffCoef3"))
            self.speedBuff['SPEED_BUFF_4'] = float(config.get("buffCoef4"))
            self.speedBuff['SPEED_BUFF_5'] = float(config.get("buffCoef5"))

    def validConfig(self,config):
        try:
            if config.get("buffCoef1") == None or not isinstance(config.get("buffCoef1"),float) or config.get("buffCoef1") > 100 or config.get("buffCoef1") < 0:
                return False
            if config.get("buffCoef2") == None or not isinstance(config.get("buffCoef2"),float) or config.get("buffCoef2") > 100 or config.get("buffCoef2") < 0:
                return False
            if config.get("buffCoef3") == None or not isinstance(config.get("buffCoef3"),float) or config.get("buffCoef3") > 100 or config.get("buffCoef3") < 0:
                return False
            if config.get("buffCoef4") == None or not isinstance(config.get("buffCoef4"),float) or config.get("buffCoef4") > 100 or config.get("buffCoef4") < 0:
                return False
            if config.get("buffCoef5") == None or not isinstance(config.get("buffCoef1"),float) or config.get("buffCoef5") > 100 or config.get("buffCoef5") < 0:
                return False
        except:
            return False
        return True
        
        
    def run(self):
        while True:
            # print('mover active, moveSet: %s' % self.moveSet)
            if self.endSignal:
                break
            if len(self.moveSet) == 0:
                 self.signal.clear()
                 self.signal.wait()
            nowTick = int(round(time.time()*1000))
            if nowTick - self.lastTick > self.ROUND_RANGE:
                self.roundTable.clear()
            self.setCoef()
            self.makeMove()
            self.signal.clear()
            self.signal.wait(0.01)

    def stop(self):
        self.endSignal = True
        self.signal.set()
         
    def setCoef(self):
        if(MoveAction.SPEED_BUFF_1.value in self.moveSet or MoveAction.SPEED_BUFF_2.value in self.moveSet
           or MoveAction.SPEED_BUFF_3.value in self.moveSet or MoveAction.SPEED_BUFF_4.value in self.moveSet
           or MoveAction.SPEED_BUFF_5.value in self.moveSet):
            if MoveAction.SPEED_BUFF_1.value in self.moveSet:
                self.speedCoef = self.speedBuff.get(MoveAction.SPEED_BUFF_1.value)
            if MoveAction.SPEED_BUFF_2.value in self.moveSet:
                self.speedCoef = self.speedBuff.get(MoveAction.SPEED_BUFF_2.value)
            if MoveAction.SPEED_BUFF_3.value in self.moveSet:
                self.speedCoef = self.speedBuff.get(MoveAction.SPEED_BUFF_3.value)
            if MoveAction.SPEED_BUFF_4.value in self.moveSet:
                self.speedCoef = self.speedBuff.get(MoveAction.SPEED_BUFF_4.value)
            if MoveAction.SPEED_BUFF_5.value in self.moveSet:
                self.speedCoef = self.speedBuff.get(MoveAction.SPEED_BUFF_5.value)
        else:
            self.speedCoef = 1
    
    def makeMove(self):
        if MoveAction.MOVE_DOWN.value in self.moveSet and MoveAction.MOVE_DOWN.value not in self.roundTable:
            self.roundTable.add(MoveAction.MOVE_DOWN.value)
            pyautogui.move(0,self.MOVE_STEP*self.speedCoef,0.1)
        if MoveAction.MOVE_UP.value in self.moveSet and MoveAction.MOVE_UP.value not in self.roundTable:
            self.roundTable.add(MoveAction.MOVE_UP.value)
            pyautogui.move(0,-1*self.MOVE_STEP*self.speedCoef,0.1)
        if MoveAction.MOVE_RIGHT.value in self.moveSet and MoveAction.MOVE_RIGHT.value not in self.roundTable:
            self.roundTable.add(MoveAction.MOVE_RIGHT.value)
            pyautogui.move(self.MOVE_STEP*self.speedCoef,0,0.1,) 
        if MoveAction.MOVE_LEFT.value in self.moveSet and MoveAction.MOVE_LEFT.value not in self.roundTable:
            self.roundTable.add(MoveAction.MOVE_LEFT.value)
            pyautogui.move(-1*self.MOVE_STEP*self.speedCoef,0,0.1)
        if MoveAction.SCROLL_DOWN.value in self.moveSet and MoveAction.SCROLL_DOWN.value not in self.roundTable:
            self.roundTable.add(MoveAction.SCROLL_DOWN.value)
            pyautogui.scroll(int(round(-30*self.speedCoef)))
        if MoveAction.SCROLL_UP.value in self.moveSet and MoveAction.SCROLL_UP.value not in self.roundTable:
            self.roundTable.add(MoveAction.SCROLL_UP.value)
            pyautogui.scroll(int(round(30*self.speedCoef)))