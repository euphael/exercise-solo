import re
from PySide6.QtCore import QRegularExpression
from PySide6.QtGui import QRegularExpressionValidator

from ui_main import Ui_MainWindow
from PySide6.QtCore import QCoreApplication
from PySide6.QtWidgets import (QApplication, QMainWindow)
import sys, requests, os, smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def email_validator(self):
    validator = self.email.validator()
    cursor_position = self.email.cursorPosition()
    state = validator.validate(self.email.text(), cursor_position)[0]
      
    if state == QRegularExpressionValidator.Acceptable:
        self.status_label.setText("Email válido!")
        self.status_label.setStyleSheet("color: green;")
    else:
        self.status_label.setText("Email inválido!")
        self.status_label.setStyleSheet("color: red;")  