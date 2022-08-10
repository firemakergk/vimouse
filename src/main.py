#-*- coding: UTF-8 -*-
import pyautogui
import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import *
from ui.vimouseui import VimouseUI
from controller.appcontroller import AppController

pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0
import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("Vimouse")
# class MainWindow(QMainWindow):
#     def __init__(self,controller, parent = None) :
#         super().__init__(parent)
#         self.ui = VimouseUI()
#         self.controller = controller
#         self.ui.setController(controller)
#         self.ui.setupUi(self)
#         # self.ui.pushButton.clicked.connect(self.click)

#     def click(self):
#         self.ui.pushButton.setText("测试")
    
#     def closeEvent(self, event):
#         self.controller.stop()
#         event.accept()
        
if __name__ == '__main__':
    controller = AppController()
    app = QtWidgets.QApplication(sys.argv)
    # app.setQuitOnLastWindowClosed(False)
    vimouseUI = VimouseUI(app,controller)
    controller.ui = vimouseUI
    vimouseUI.setWindowTitle("Vimouse")
    vimouseUI.show()
    vimouseUI.cancelFocus()
    controller.start()
    sys.exit(app.exec())

    
    # queue = Queue()
    # interceptor = KeyboardInterceptor(queue)
    # keyHandler = KeyHandler(interceptor,queue)
    # interceptor.start()
    # keyHandler.start()
    