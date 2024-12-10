# -*- coding: utf-8 -*-

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDateEdit, QLCDNumber, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTimeEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 600)
        MainWindow.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        MainWindow.setMouseTracking(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lcdNumber = QLCDNumber(self.centralwidget)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setGeometry(QRect(100, 60, 261, 41))
        
        self.lcdNumber2 = QLCDNumber(self.centralwidget)
        self.lcdNumber2.setObjectName(u"lcdNumber")
        self.lcdNumber2.setGeometry(QRect(450, 60, 261, 41))
        
        self.timeEdit = QTimeEdit(self.centralwidget)
        self.timeEdit.setObjectName(u"timeEdit")
        self.timeEdit.setGeometry(QRect(260, 170, 261, 41))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(310, 130, 171, 31))
        
        #ínicio das labels
        self.horaAtual = QLabel(self.centralwidget)
        self.horaAtual.setObjectName(u"label_2")
        self.horaAtual.setGeometry(QRect(110, 20, 151, 31))
        
        self.horaMundo = QLabel(self.centralwidget)
        self.horaMundo.setObjectName(u"label_2")
        self.horaMundo.setGeometry(QRect(510, 20, 351, 31))
        
        self.setTimeBtn = QPushButton(self.centralwidget)
        self.setTimeBtn.setObjectName(u"setTimeBtn")
        self.setTimeBtn.setGeometry(QRect(260, 240, 261, 41))
        self.setTimeBtn.setFlat(False)
        
        self.dateEdit = QDateEdit(self.centralwidget)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(100, 350, 261, 41))
        
        self.dateReal = QLabel(self.centralwidget)
        self.dateReal.setObjectName(u"dataLabel")
        self.dateReal.setGeometry(QRect(450, 350, 261, 41))
        font = QFont()
        font.setPointSize(14)  # tamanho da fonte
        self.dateReal.setFont(font)
        
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(310, 310, 171, 31))
        self.setDateBtn = QPushButton(self.centralwidget)
        self.setDateBtn.setObjectName(u"setDateBtn")
        self.setDateBtn.setGeometry(QRect(260, 410, 261, 41))
        self.setDateBtn.setFlat(False)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        self.setTimeBtn.setDefault(False)
        self.setDateBtn.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"CodeTest", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Mudar horário</span></p></body></html>", None))
        self.horaAtual.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Hora atual</span></p></body></html>", None))
        self.horaMundo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Hora real Brasil</span></p></body></html>", None))
        self.setTimeBtn.setText(QCoreApplication.translate("MainWindow", u"Mudar hor\u00e1rio", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Data de hoje</span></p></body></html>", None))
        self.setDateBtn.setText(QCoreApplication.translate("MainWindow", u"Mudar data", None))
    # retranslateUi

