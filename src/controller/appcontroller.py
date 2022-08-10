#-*- coding: UTF-8 -*-
import os
import json
import time
from core.keyboardinterceptor import KeyboardInterceptor
from queue import Queue
from core.keyhandler import KeyHandler

DEFAULT_CONFIG = {
    "buffCoef1": 0.3,
    "buffCoef2": 0.6,
    "buffCoef3": 4.0,
    "buffCoef4": 8.0,
    "buffCoef5": 12.0,
    "shiftBuff": 2,
    "spaceBuff": 3
}

class AppController:
    queue = None
    interceptor = None
    keyHandler = None
    engaged = False
    ui = None

    def __init__(self):
        pass
    
    def start(self):
        self.queue = Queue()
        self.interceptor = KeyboardInterceptor(self.queue)
        self.interceptor.controller = self
        self.keyHandler = KeyHandler(self.interceptor,self.queue,self.getConfig())
        self.interceptor.start()
        self.keyHandler.start()
        self.engaged = True
        self.updateUIStatus()
        print('controller start')
        
    def stop(self):
        print('controller stop')
        self.keyHandler.stop()
        self.interceptor.stop()
        self.engaged = False
        self.updateUIStatus()

    def startFilter(self):
        self.interceptor.enable = True

    def stopFilter(self):
        self.interceptor.enable = False

    def getConfig(self):
        configData = None
        if not os.path.exists('config.json'):
            return DEFAULT_CONFIG
        with open('config.json','r',encoding='utf8')as f:
            configData = json.load(f)
        return configData

    def submitConfig(self,configData):
        self.stop()
        with open("config.json", 'w') as f:
            json.dump(configData, f, indent=4, ensure_ascii=False)
        self.start()

    def updateUIStatus(self):
        self.ui.updateStatus(self.engaged,self.interceptor.enable)


if __name__ == '__main__':
    app = AppController()
    app.submitConfig({'buffCoef1': 0.1, 'buffCoef2': 0.6, 'buffCoef3': 99, 'buffCoef4': 8, 'buffCoef5': 12, 'shiftBuff': 2, 'spaceBuff': 3})
    time.sleep(1)
    print(app.getConfig())