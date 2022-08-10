# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vimouse.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QGridLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTextBrowser, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(500, 400)
        self.formLayoutWidget = QWidget(Dialog)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(320, 10, 161, 221))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.Label = QLabel(self.formLayoutWidget)
        self.Label.setObjectName(u"Label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.Label)

        self.LineEdit = QLineEdit(self.formLayoutWidget)
        self.LineEdit.setObjectName(u"LineEdit")
        self.LineEdit.setEnabled(False)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.LineEdit)

        self.label1 = QLabel(self.formLayoutWidget)
        self.label1.setObjectName(u"label1")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label1)

        self.lineEdit1 = QLineEdit(self.formLayoutWidget)
        self.lineEdit1.setObjectName(u"lineEdit1")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit1)

        self.label2 = QLabel(self.formLayoutWidget)
        self.label2.setObjectName(u"label2")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label2)

        self.lineEdit2 = QLineEdit(self.formLayoutWidget)
        self.lineEdit2.setObjectName(u"lineEdit2")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit2)

        self.label3 = QLabel(self.formLayoutWidget)
        self.label3.setObjectName(u"label3")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label3)

        self.lineEdit3 = QLineEdit(self.formLayoutWidget)
        self.lineEdit3.setObjectName(u"lineEdit3")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.lineEdit3)

        self.label4 = QLabel(self.formLayoutWidget)
        self.label4.setObjectName(u"label4")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label4)

        self.lineEdit4 = QLineEdit(self.formLayoutWidget)
        self.lineEdit4.setObjectName(u"lineEdit4")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.lineEdit4)

        self.label5 = QLabel(self.formLayoutWidget)
        self.label5.setObjectName(u"label5")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label5)

        self.lineEdit5 = QLineEdit(self.formLayoutWidget)
        self.lineEdit5.setObjectName(u"lineEdit5")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.lineEdit5)

        self.shiftLabel = QLabel(self.formLayoutWidget)
        self.shiftLabel.setObjectName(u"shiftLabel")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.shiftLabel)

        self.shiftLineEdit = QLineEdit(self.formLayoutWidget)
        self.shiftLineEdit.setObjectName(u"shiftLineEdit")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.shiftLineEdit)

        self.Label_2 = QLabel(self.formLayoutWidget)
        self.Label_2.setObjectName(u"Label_2")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.Label_2)

        self.LineEdit_2 = QLineEdit(self.formLayoutWidget)
        self.LineEdit_2.setObjectName(u"LineEdit_2")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.LineEdit_2)

        self.gridLayoutWidget = QWidget(Dialog)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 301, 381))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.textBrowser_2 = QTextBrowser(self.gridLayoutWidget)
        self.textBrowser_2.setObjectName(u"textBrowser_2")

        self.gridLayout.addWidget(self.textBrowser_2, 1, 0, 1, 2)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u":/logo/logo_small.png"))
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton = QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 24))
        font = QFont()
        font.setPointSize(24)
        self.pushButton.setFont(font)
        self.pushButton.setMouseTracking(False)

        self.verticalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        font1 = QFont()
        font1.setPointSize(10)
        self.pushButton_2.setFont(font1)

        self.verticalLayout.addWidget(self.pushButton_2)


        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)

        self.pushButton_4 = QPushButton(Dialog)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(320, 240, 161, 31))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(400, 370, 81, 20))
        self.label_2.setOpenExternalLinks(True)
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(330, 370, 51, 21))
        self.label_3.setOpenExternalLinks(True)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.Label.setText(QCoreApplication.translate("Dialog", u"\u5f00\u542f/\u5173\u95ed", None))
        self.LineEdit.setText(QCoreApplication.translate("Dialog", u"alt + \\", None))
        self.label1.setText(QCoreApplication.translate("Dialog", u"\u6863\u4f4d1\u7cfb\u6570\uff1a", None))
        self.lineEdit1.setText(QCoreApplication.translate("Dialog", u"0.3", None))
        self.label2.setText(QCoreApplication.translate("Dialog", u"\u6863\u4f4d2\u7cfb\u6570\uff1a", None))
        self.lineEdit2.setText(QCoreApplication.translate("Dialog", u"0.6", None))
        self.label3.setText(QCoreApplication.translate("Dialog", u"\u6863\u4f4d3\u7cfb\u6570\uff1a", None))
        self.lineEdit3.setText(QCoreApplication.translate("Dialog", u"4", None))
        self.label4.setText(QCoreApplication.translate("Dialog", u"\u6863\u4f4d4\u7cfb\u6570", None))
        self.lineEdit4.setText(QCoreApplication.translate("Dialog", u"8", None))
        self.label5.setText(QCoreApplication.translate("Dialog", u"\u6863\u4f4d5\u7cfb\u6570\uff1a", None))
        self.lineEdit5.setText(QCoreApplication.translate("Dialog", u"12", None))
        self.shiftLabel.setText(QCoreApplication.translate("Dialog", u"shift\u6863\u4f4d\uff1a", None))
        self.shiftLineEdit.setText(QCoreApplication.translate("Dialog", u"2", None))
        self.Label_2.setText(QCoreApplication.translate("Dialog", u"\u7a7a\u683c\u952e\u6863\u4f4d\uff1a", None))
        self.LineEdit_2.setText(QCoreApplication.translate("Dialog", u"3", None))
        self.textBrowser_2.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u542f\u52a8\u76d1\u542c\u540e\uff0c\u5373\u53ef\u4f7f\u7528alt+\\\u5feb\u6377\u952e\u5f00\u542f\u9f20\u6807\u64cd\u7eb5\u6a21\u5f0f\u3002\u63a7\u5236\u952e\u4f4d\u4e0evim\u4e00\u81f4\u3002</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u79fb\u52a8\uff1a h(\u2190),j(\u2193),k(\u2191),l(\u2192)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text"
                        "-indent:0px;\">\u79fb\u52a8\u6863\u4f4d\uff1a \u4e3b\u952e\u76d81/2/3/4/5/\u5de6shift/\u7a7a\u683c\u952e\u3002\u6309\u4e0b\u751f\u6548\uff0c\u62ac\u8d77\u5931\u6548\u3002\u751f\u6548\u65f6\u9f20\u6807\u7684\u79fb\u52a8\u901f\u7387\u4f1a\u4ee5\u76f8\u5e94\u7684\u7cfb\u6570\u589e\u51cf\u3002</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u70b9\u51fb\uff1a i/e(\u5de6\u952e),o/w(\u53f3\u952e),d(\u4e2d\u952e)\u3002\u6309\u4e0b\u4e0e\u62ac\u8d77\u5bf9\u5e94\u76f8\u5e94\u6309\u952e\u7684\u6309\u4e0b\u4e0e\u62ac\u8d77\u3002</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u6eda\u8f6e\uff1a r(\u5411\u4e0a\u6eda\u52a8),f(\u5411\u4e0b\u6eda\u52a8)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u529f\u80fd\u952e\uff1a</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-"
                        "left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">v\uff1a\u6572\u51fb\u4e00\u6b21\u89c6\u4e3a\u5de6\u952e\u6309\u4e0b\uff0c\u518d\u6572\u51fb\u4e00\u6b21\u89c6\u4e3a\u5de6\u952e\u62ac\u8d77\u3002</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">y:ctrl-c c:ctrl-x p:ctrl-v u:ctrl-z</p></body></html>", None))
        self.label.setText("")
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u542f\u52a8", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"\u652f\u6301\u4f5c\u8005", None))
        self.pushButton_4.setText(QCoreApplication.translate("Dialog", u"\u63d0\u4ea4\u914d\u7f6e", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", "<a href='https://www.baidu.com/'>关于Vimouse</a>", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u5b98\u65b9\u7f51\u7ad9", None))
    # retranslateUi

 