#-*- coding: UTF-8 -*-
from pynput import keyboard

from utils.keycodeutil import KeyCodeUtil
from threading import Thread
from queue import Queue

class KeyboardInterceptor(Thread):
    MSG_PRESS = 256
    MSG_PRESS_WITH_ALT = 260
    MSG_RELEASE_WITH_ALT = 261
    MSG_RELEASE = 257
    VK_BACKSLASH = 220
    # 所有有效键位
    keySet = {'a','h','j','k','l','i','o','y','p','1','2','3','4','5','6','7','8','9','0','d','e','w','r','f','c','v','shift_l','shift_r','alt','f1'}
    # 持续生效按键 
    continuousSet = {'h','j','k','l','1','2','3','4','5','r','f','space','shift_l','shift_r'}
    # 按下触发键位
    pressTriggerSet = {'a','v','y','c','p','u','6','7','8','9','0'}
    # 首尾触发键位
    headTailTriggerSet = {'i','o','e','w','d'}
    #透传按键
    ignoreKeySet = {keyboard.Key.alt_l,keyboard.Key.ctrl_l,keyboard.Key.ctrl_r,keyboard.Key.enter,keyboard.Key.tab,keyboard.Key.backspace,keyboard.Key.home,keyboard.Key.end,keyboard.Key.insert,keyboard.Key.up,keyboard.Key.down,keyboard.Key.left,keyboard.Key.right}
    ignoreVKSet = None
    switchKeyMap = {'v':False}
    checkedSize = 0
    pressSet = set()
    actionQueue = None
    listener = None
    enable = False 
    justEnable = False 
    altLPressed = False
    ctrlPressed = False
    
    def __init__(self,  actionQueue: Queue):
        Thread.__init__(self)
        self.actionQueue = actionQueue
        self.ignoreVKSet = KeyCodeUtil.keys2Vks(self.ignoreKeySet)

        
    def run(self):
        with keyboard.Listener(win32_event_filter=self.filter, suppress=False) as self.listener:
            print('interceptor start')
            self.listener.join()

    def stop(self):
        self.actionQueue.put('_EXIT_')
        self.listener.stop()
        
    def filter(self,msg,data):
        # print('filter enable: %s, msg: %s, vkCode: %s, scanCode: %s, flags: %s, time: %s, dwExtraInfo: %s' % (self.enable, msg, data.vkCode, data.scanCode, data.flags, data.time, data.dwExtraInfo))
        if data.vkCode == KeyCodeUtil.key2Vk(keyboard.Key.alt_l) and msg == self.MSG_PRESS_WITH_ALT:
            self.altLPressed = True
        if data.vkCode == KeyCodeUtil.key2Vk(keyboard.Key.alt_l) and msg == self.MSG_RELEASE:
            self.altLPressed = False
        if data.vkCode == self.VK_BACKSLASH and msg == self.MSG_RELEASE_WITH_ALT and self.altLPressed == True:
            self.enable = not self.enable
            if self.enable:
                self.justEnable = True
            if self.controller != None:
               self.controller.updateUIStatus()
            #     self.listener.suppress_event()
        if data.vkCode == KeyCodeUtil.key2Vk(keyboard.Key.tab) and (msg == self.MSG_PRESS_WITH_ALT or msg == self.MSG_RELEASE_WITH_ALT) and self.altLPressed == True:
            return
        if not self.enable:
            return
        if self.justEnable and data.vkCode == KeyCodeUtil.key2Vk(keyboard.Key.alt_l) and msg == self.MSG_RELEASE:
            self.justEnable = False
            return
        
        if data.vkCode == KeyCodeUtil.key2Vk(keyboard.Key.ctrl_l) and msg == self.MSG_PRESS:
            self.ctrlPressed = True
        if data.vkCode == KeyCodeUtil.key2Vk(keyboard.Key.ctrl_l) and msg == self.MSG_RELEASE:
            self.ctrlPressed = False
        if self.ctrlPressed:
            return 
        if (data.vkCode != KeyCodeUtil.key2Vk(keyboard.Key.ctrl_l) and data.vkCode not in self.ignoreVKSet and (msg == self.MSG_PRESS or msg == self.MSG_PRESS_WITH_ALT)):
            # print('vk2Char: %s -> %s' % (data.vkCode, KeyCodeUtil.vk2Char(data.vkCode)))
            self.on_press(KeyCodeUtil.vk2Char(data.vkCode))
            self.listener.suppress_event()
        elif (data.vkCode != KeyCodeUtil.key2Vk(keyboard.Key.ctrl_l) and data.vkCode not in self.ignoreVKSet and (msg == self.MSG_RELEASE or msg == self.MSG_RELEASE_WITH_ALT)):
            # print('vk2Char: %s -> %s' % (data.vkCode, KeyCodeUtil.vk2Char(data.vkCode)))
            self.on_release(KeyCodeUtil.vk2Char(data.vkCode))
            self.listener.suppress_event()

    def on_press(self, key):
        if key in self.continuousSet or key in self.headTailTriggerSet:
            self.actionQueue.put('_P_'+key)
        elif key in self.pressTriggerSet:
            if key not in self.switchKeyMap:
                self.actionQueue.put('_P_'+key)
            else:
                self.switchKeyMap[key] = not self.switchKeyMap[key]
                switchKey = '_O_' + key if self.switchKeyMap[key] else '_C_' + key
                self.actionQueue.put(switchKey)

    def on_release(self,key):
        if key in self.continuousSet or key in self.headTailTriggerSet:
            self.actionQueue.put('_R_'+key)
            self.pressSet.discard(key)
 