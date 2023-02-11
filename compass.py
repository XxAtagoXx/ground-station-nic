from PyQt5.QtCore import QPoint, Qt, QTimer
from PyQt5.QtGui import QColor, QPainter, QPolygon
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
from PyQt5 import QtCore, QtGui, QtWidgets   
import serial.tools.list_ports
import serial


class Compass(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setFixedWidth(200)
        self.setFixedHeight(200)
        self.setGeometry(140, 120, 180, 180)
        

       
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(50)

    

    def paintEvent(self, event):
        side = min(self.width(), self.height())
        
        painter = QPainter(self)
        
        painter.setRenderHint(QPainter.Antialiasing)
        painter.translate(100,100)
        painter.scale(side / 100, side / 100)
        painter.setPen(Qt.NoPen)


        # Draw the compass needle
        painter.setBrush(Qt.green)
        painter.save()

        #headig to return the value
        try:
                
            heading = self.get_heading()
            painter.rotate(heading)
            painter.drawConvexPolygon(QPolygon([QPoint(0, -50), QPoint(5, 0), QPoint(-5, 0)]))
            painter.restore()
        
        except TypeError:
            pass
        
       

    def get_heading(self):

        try:

            ser = serial.Serial('COM6', 115200, timeout=5) # change 'COM6' to the appropriate serial port for your ESP32
            data = ser.readline().decode() # read the data and decode it from bytes to a string
            print(data)

            self.final_data = float(data)

            self.final_data += 0

            if self.final_data >=362:
                self.data = 0
        
            

            return self.final_data

        except UnicodeDecodeError:
        # Handle the exception
            pass
    
    def showdirection(self):
        currentdirection = self.get_heading()

        if currentdirection ==0 or currentdirection <= 44:
            return ('North')
        
        elif currentdirection == 45 or currentdirection <= 89:
            return ('NorthEast')
        elif currentdirection == 90 or currentdirection <= 134:
            return ('East')
        elif currentdirection == 135 or currentdirection <= 179:
            return ('SouthEast')
        elif currentdirection == 180 or currentdirection <= 224:
            return ('South')
        elif currentdirection == 225 or currentdirection <= 269:
            return ('SouthWest')
        elif currentdirection == 270 or currentdirection <=324:
            return ('West')
        elif currentdirection == 325 or currentdirection <=360:
            return ('NorthWest')

        else:
            return ('Calibrating')

        
    



if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    compass = Compass()
    compass.show()
   
    sys.exit(app.exec_())