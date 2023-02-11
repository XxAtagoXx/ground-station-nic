import io
from jinja2 import Template
import folium
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5 import QtCore, QtGui, QtWidgets    
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import QPoint, Qt, QTimer
from PyQt5.QtGui import QColor, QPainter, QPolygon
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
#import main
from PyQt5.QtWidgets import QVBoxLayout
from final import Ui_finale #importing class from python file
from compass import Compass
from PyQt5.QtCore import QUrl



class mainmap(QtWidgets.QMainWindow):
	def __init__(self, *args, **kwargs):

		super().__init__(*args, **kwargs)
		self.setWindowFlag(QtCore.Qt.FramelessWindowHint)

		self.ui = Ui_finale()
		self.ui.setupUi(self)
		# self.uicompass = Compass()
		
		#--loads the map.ui 
		
		self.setWindowTitle("Ground control")
        #layout for map
		layout = QVBoxLayout(self.ui.map)
		self.setLayout(layout)

		#layout for model
		layout2 = QVBoxLayout(self.ui.cd2)

		# layoutcompass = QVBoxLayout(self.ui.compass)
		# self.setLayout(layoutcompass)
        
        #--gps datas
        #value_chain = com.getData()
        #big_data_array = calc.all_func()
        #print(big_data_array)
        #gps_array = big_data_array[6]

		latitude = 27.717245 #gps_array[0]
		longitude = 85.323959 #gps_array[1]

        #coordinate = (latitude[17], longitude[17])

		#FOR MODEL
		self.webview = QWebEngineView()

		# Load the desired website
		self.webview.load(QUrl("http://127.0.0.1:5500/modelshow.html"))

		
       
		self.map = folium.Map(
            tiles='http://mt1.google.com/vt/lyrs=m&h1=p1Z&x={x}&y={y}&z={z}',
            name='real',
            zoom_start=19,
            max_zoom=20,
            attr='Google Map',
            location = (latitude,longitude) #coordinate replace with longitude and latitude latitude
        )
        
        #save map data to data object and layout
		data = io.BytesIO()
		self.map.save(data, close_file=False)
		self.map_view = QWebEngineView()
		self.map_view.setHtml(data.getvalue().decode())


       
		layout.addWidget(self.map_view)
		layout2.addWidget(self.webview)
		# layoutcompass.addWidget(self.uicompass)
	

		#button

		#self.clicked = [self.ui.coursebtn.clicked.connect(self.mode),self.ui.launch.clicked.connect(self.mode)]
		self.ui.cross.clicked.connect(self.close_window)


		#showing accurate direction
		# self.currentdirection =  self.uicompass.showdirection()

		# print(self.currentdirection)
	
    

        
	def mode(self):
	
	
		if self.clicked[0]:

			self.ui.direction1.setText("north")
			print("course")

		elif self.clicked == self.clicked[1]:
			self.ui.mode1.setText("launch")
			print("launch")


	
	
		
	def close_window(self):
		self.close()
      

		




if __name__ == "__main__":
	app = QtWidgets.QApplication([])
	widget = mainmap()
	widget.show()
	app.exec_()