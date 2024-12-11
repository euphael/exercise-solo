from PySide6.QtCore import QCoreApplication
from PySide6.QtWidgets import (QApplication, QMainWindow)
from ui_main import Ui_MainWindow
import sys, requests, os, smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Envair email")
        self.send_email_btn.clicked.connect(self.button_send_email)

    def button_send_email(self):
        user_send = self.email.text().strip()
        password = self.password.text().strip()
        user_recieves = self.user_recieves.text().strip().split(',')
        subject = self.subject.text().strip()
        body_email = self.body_email.toPlainText().strip()
        
        self.send_email(user_send, password, user_recieves, subject, body_email)
        
    
    def send_email(self, user_send, password, user_recieves, subject, body_email):
        #Cria-se uma instância do objeto MIMEMultpart ( usado para enviar um email "rico")
        message = MIMEMultipart()
        
        #Define-se os campos do email
        message['From'] = user_send
        message['To'] = ', '.join(user_recieves) # junta vários destinatários
        message['Subject'] = subject
        
        #definindo o corpo do email ( PLAIN -> TEXTO SIMPLES ; HTML -> TEXTO RICO):
        body = MIMEText(body_email, 'plain')
        message.attach(body)
        
        #Criar uma instância para o servidor
        server = smtplib.SMTP('smtp.gmail.com', 587)
        
        #Autenticação
        server.ehlo()
        server.starttls()
        server.login(user_send, password)
        
        #Enviar email
        for user_recieve in user_recieves:
            server.sendmail(user_send, [user_recieve], message.as_string())  
        server.quit()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()