from PySide6.QtCore import QCoreApplication, QTimer, QTime, QDate, QDateTime
from PySide6.QtWidgets import (QApplication, QMainWindow, QLCDNumber)
from ui_main import Ui_MainWindow
import sys, requests, os


class MainWindow(QMainWindow, Ui_MainWindow):
        
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Ajuste de tempo")
        
        # ########## UPDATE TIME ####################
        self.timer = QTimer()
        self.timer.timeout.connect(self.updateTime)
        self.timer.start(15000)
        self.updateTime()

        # ########## UPDATE DATE ####################
        current_date = QDate.currentDate()
        self.dateReal.setText("Data real Brasil: " + QDateTime.currentDateTime().toString("dd/MM/yyyy"))
        self.dateEdit.setDate(current_date)

        ############# PUSH BUTTON #####################
        self.setTimeBtn .clicked.connect(self.changeTime)
        self.setDateBtn.clicked.connect(self.changeDate)
        
    def updateTime(self):
        #fuso brasil real
        try:
            response = requests.get('http://worldtimeapi.org/api/timezone/America/Sao_Paulo')
            response.raise_for_status()
            data = response.json()
            time_br = data['datetime'].split('T')[1].split('.')[0][:5]
            self.lcdNumber2.display(time_br)
        except requests.exceptions.RequestException as e:
            print(f"Erro ao obter o horário do Brasil: {e}")
  
        time_now = QTime.currentTime()
        self.lcdNumber.display(time_now.toString('hh:mm'))
        

 
    def changeTime(self):
        time = self.timeEdit.time()
        command = f"time {time.toString('hh:mm')}:00"
        self.lcdNumber.display(command)
        os.system(command)
        
    def changeDate(self):
        date = self.dateEdit.date()
        command = f"date {date.toString('dd-MM-yyyy')}"
        os.system(command)
    
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()