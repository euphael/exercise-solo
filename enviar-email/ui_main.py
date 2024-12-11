# -*- coding: utf-8 -*-

################################################################################
import re
from PySide6.QtCore import QRegularExpression
from PySide6.QtGui import QRegularExpressionValidator

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPlainTextEdit, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(810, 712)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(180, 90, 131, 21))
        font = QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color:rgb(85, 0, 127)")
        self.label.setTextFormat(Qt.PlainText)
        
        self.user_recieves = QLineEdit(self.centralwidget)
        self.user_recieves.setObjectName(u"user_recieves")
        self.user_recieves.setGeometry(QRect(180, 115, 401, 20))
        
        self.label_subject = QLabel(self.centralwidget)
        self.label_subject.setObjectName(u"label_subject")
        self.label_subject.setGeometry(QRect(180, 145, 131, 21))
        font = QFont()
        font.setPointSize(16)
        self.label_subject.setFont(font)
        self.label_subject.setStyleSheet(u"color:rgb(85, 0, 127)")
        self.label_subject.setTextFormat(Qt.PlainText)
        
        self.subject = QLineEdit(self.centralwidget)
        self.subject.setObjectName(u"subject")
        self.subject.setGeometry(QRect(180, 170, 401, 20))
        
        
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(330, 210, 121, 31))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color:rgb(85, 0, 127)")
        self.label_2.setTextFormat(Qt.PlainText)
        
        self.body_email = QPlainTextEdit(self.centralwidget)
        self.body_email.setObjectName(u"body_email")
        self.body_email.setGeometry(QRect(100, 240, 581, 351))
        
        self.send_email_btn = QPushButton(self.centralwidget)
        self.send_email_btn.setObjectName(u"send_email_btn")
        self.send_email_btn.setGeometry(QRect(240, 610, 311, 41))
        self.send_email_btn.setStyleSheet(u"color: rgb(85, 0, 127)")
        
        self.email = QLineEdit(self.centralwidget)
        self.email.setObjectName(u"email")
        self.email.setGeometry(QRect(80, 50, 321, 20))
        email_regex = r"[^@]+@[^@]+\.[^@]+"
        regex = QRegularExpression(email_regex)
        validator_email = QRegularExpressionValidator(regex)
        self.email.setValidator(validator_email)
        #self.email.textChanged.connect(email_validator)
        
        self.password = QLineEdit(self.centralwidget)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(430, 50, 291, 20))
        self.password.setEchoMode(QLineEdit.Password)
        
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(80, 20, 131, 31))
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color:rgb(85, 0, 127)")
        self.label_3.setTextFormat(Qt.PlainText)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(430, 20, 131, 31))
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"color:rgb(85, 0, 127)")
        self.label_4.setTextFormat(Qt.PlainText)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 810, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Enviar email", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Destinat\u00e1rios:", None))
        self.label_subject.setText(QCoreApplication.translate("MainWindow", u"Assunto", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Mensagem:", None))
        self.send_email_btn.setText(QCoreApplication.translate("MainWindow", u"Enviar", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Seu login", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Sua senha", None))
    # retranslateUi

