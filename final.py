# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'final.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_finale(object):
    def setupUi(self, finale):
        finale.setObjectName("finale")
        finale.resize(1991, 1141)
        finale.setStyleSheet("QPushButton#cross{\n"
"background-color:red;\n"
"}")
        self.rightframe = QtWidgets.QFrame(finale)
        self.rightframe.setGeometry(QtCore.QRect(1310, 100, 601, 961))
        self.rightframe.setStyleSheet("QFrame#rightframe{font: 75 10pt \"MS Shell Dlg 2\";\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"border: none;\n"
"background-color:qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:0, stop:1 rgba(46, 46, 46, 255));\n"
"\n"
"}\n"
"\n"
"QLabel#north{\n"
"border:none;\n"
"\n"
"}\n"
"\n"
"\n"
"QLabel#south{\n"
"border:none;\n"
"color: green;\n"
"}\n"
"\n"
"\n"
"QLabel#east{\n"
"border:none;\n"
"\n"
"}\n"
"\n"
"\n"
"QLabel#west{\n"
"border:none;\n"
"\n"
"}\n"
"\n"
"QLabel#pointer{\n"
"border:none;\n"
"}\n"
"QProgressBar#pbfuel{\n"
"border:2px solid black;\n"
"}\n"
"\n"
"\n"
"QProgressBar#barleft{\n"
"border:2px solid black;\n"
"}\n"
"\n"
"QProgressBar#barright{\n"
"border:2px solid black;\n"
"}\n"
"\n"
"QLabel#speed{\n"
"border:2px solid black;\n"
"\n"
"}\n"
"QLabel{\n"
"border:2px solid black;\n"
"color: green;\n"
"font: bold;\n"
"}\n"
"QLabel#ovl4{\n"
"\n"
"font: 20pt \"MS Shell Dlg 2\";\n"
"color: green;\n"
"font: bold;\n"
"}\n"
"QLabel#altitude{\n"
"\n"
"font: 15pt \"MS Shell Dlg 2\";\n"
"color: green;\n"
"font: bold;\n"
"}\n"
"QPushButton#monitor{\n"
"\n"
"font: 17pt \"MS Shell Dlg 2\";\n"
"color: green;\n"
"font: bold;\n"
"}\n"
"QPushButton#control{\n"
"\n"
"font: 15pt \"MS Shell Dlg 2\";\n"
"color: green;\n"
"font: bold;\n"
"}\n"
"QLabel#ov1{\n"
"\n"
"font: 20pt \"MS Shell Dlg 2\";\n"
"color: green;\n"
"font: bold;\n"
"}\n"
"QLabel#speed1{\n"
"\n"
"font: 20pt \"MS Shell Dlg 2\";\n"
"color: green;\n"
"font: bold;\n"
"}\n"
"QLabel#speed{\n"
"\n"
"font: 20pt \"MS Shell Dlg 2\";\n"
"color: green;\n"
"font: bold;\n"
"}\n"
"Line#point{\n"
"\n"
"background-color: red;\n"
"}\n"
"QPushButton{\n"
"border:2px solid black;\n"
"color: green;\n"
"}\n"
"\n"
"QSlider{\n"
"border:2px solid black;\n"
"}\n"
"QDial{\n"
"background-color:rgb(0, 128, 0);\n"
"}\n"
"\n"
"")
        self.rightframe.setObjectName("rightframe")
        self.monitor = QtWidgets.QPushButton(self.rightframe)
        self.monitor.setGeometry(QtCore.QRect(0, 10, 151, 31))
        self.monitor.setCheckable(True)
        self.monitor.setObjectName("monitor")
        self.control = QtWidgets.QPushButton(self.rightframe)
        self.control.setGeometry(QtCore.QRect(160, 10, 171, 31))
        self.control.setCheckable(True)
        self.control.setObjectName("control")
        self.speed = QtWidgets.QLabel(self.rightframe)
        self.speed.setGeometry(QtCore.QRect(0, 50, 121, 41))
        self.speed.setStyleSheet("")
        self.speed.setTextFormat(QtCore.Qt.PlainText)
        self.speed.setWordWrap(False)
        self.speed.setObjectName("speed")
        self.start = QtWidgets.QPushButton(self.rightframe)
        self.start.setGeometry(QtCore.QRect(30, 720, 151, 121))
        self.start.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.start.setAutoFillBackground(False)
        self.start.setStyleSheet("")
        self.start.setObjectName("start")
        self.meter = QtWidgets.QDial(self.rightframe)
        self.meter.setGeometry(QtCore.QRect(240, 790, 161, 131))
        self.meter.setObjectName("meter")
        self.slideleft = QtWidgets.QSlider(self.rightframe)
        self.slideleft.setGeometry(QtCore.QRect(40, 170, 22, 251))
        self.slideleft.setOrientation(QtCore.Qt.Vertical)
        self.slideleft.setObjectName("slideleft")
        self.slideright = QtWidgets.QSlider(self.rightframe)
        self.slideright.setGeometry(QtCore.QRect(430, 170, 22, 251))
        self.slideright.setOrientation(QtCore.Qt.Vertical)
        self.slideright.setObjectName("slideright")
        self.battery = QtWidgets.QProgressBar(self.rightframe)
        self.battery.setGeometry(QtCore.QRect(460, 670, 51, 161))
        self.battery.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.battery.setProperty("value", 24)
        self.battery.setOrientation(QtCore.Qt.Vertical)
        self.battery.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.battery.setObjectName("battery")
        self.barright = QtWidgets.QProgressBar(self.rightframe)
        self.barright.setGeometry(QtCore.QRect(530, 670, 51, 161))
        self.barright.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.barright.setProperty("value", 24)
        self.barright.setOrientation(QtCore.Qt.Vertical)
        self.barright.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.barright.setObjectName("barright")
        self.overrideleft = QtWidgets.QLabel(self.rightframe)
        self.overrideleft.setGeometry(QtCore.QRect(10, 140, 191, 31))
        self.overrideleft.setStyleSheet("")
        self.overrideleft.setTextFormat(QtCore.Qt.PlainText)
        self.overrideleft.setWordWrap(False)
        self.overrideleft.setObjectName("overrideleft")
        self.altitude = QtWidgets.QLabel(self.rightframe)
        self.altitude.setGeometry(QtCore.QRect(10, 110, 581, 31))
        self.altitude.setStyleSheet("")
        self.altitude.setTextFormat(QtCore.Qt.PlainText)
        self.altitude.setWordWrap(False)
        self.altitude.setObjectName("altitude")
        self.lcdNumber = QtWidgets.QLCDNumber(self.rightframe)
        self.lcdNumber.setGeometry(QtCore.QRect(270, 740, 91, 23))
        self.lcdNumber.setObjectName("lcdNumber")
        self.ovl4 = QtWidgets.QLabel(self.rightframe)
        self.ovl4.setGeometry(QtCore.QRect(70, 170, 131, 251))
        self.ovl4.setWordWrap(False)
        self.ovl4.setObjectName("ovl4")
        self.ruler_2 = QtWidgets.QLabel(self.rightframe)
        self.ruler_2.setGeometry(QtCore.QRect(400, 170, 21, 251))
        self.ruler_2.setWordWrap(False)
        self.ruler_2.setObjectName("ruler_2")
        self.ruler_3 = QtWidgets.QLabel(self.rightframe)
        self.ruler_3.setGeometry(QtCore.QRect(10, 170, 21, 251))
        self.ruler_3.setWordWrap(False)
        self.ruler_3.setObjectName("ruler_3")
        self.speed1 = QtWidgets.QLabel(self.rightframe)
        self.speed1.setGeometry(QtCore.QRect(130, 50, 171, 41))
        self.speed1.setStyleSheet("")
        self.speed1.setTextFormat(QtCore.Qt.PlainText)
        self.speed1.setWordWrap(False)
        self.speed1.setObjectName("speed1")
        self.msl = QtWidgets.QLabel(self.rightframe)
        self.msl.setGeometry(QtCore.QRect(440, 20, 71, 61))
        self.msl.setStyleSheet("")
        self.msl.setTextFormat(QtCore.Qt.PlainText)
        self.msl.setWordWrap(False)
        self.msl.setObjectName("msl")
        self.speed_3 = QtWidgets.QLabel(self.rightframe)
        self.speed_3.setGeometry(QtCore.QRect(510, 20, 61, 61))
        self.speed_3.setStyleSheet("")
        self.speed_3.setTextFormat(QtCore.Qt.PlainText)
        self.speed_3.setWordWrap(False)
        self.speed_3.setObjectName("speed_3")
        self.gs = QtWidgets.QLabel(self.rightframe)
        self.gs.setGeometry(QtCore.QRect(0, 550, 41, 31))
        self.gs.setStyleSheet("")
        self.gs.setTextFormat(QtCore.Qt.PlainText)
        self.gs.setWordWrap(False)
        self.gs.setObjectName("gs")
        self.ws = QtWidgets.QLabel(self.rightframe)
        self.ws.setGeometry(QtCore.QRect(0, 590, 41, 31))
        self.ws.setStyleSheet("")
        self.ws.setTextFormat(QtCore.Qt.PlainText)
        self.ws.setWordWrap(False)
        self.ws.setObjectName("ws")
        self.gs1 = QtWidgets.QLabel(self.rightframe)
        self.gs1.setGeometry(QtCore.QRect(40, 550, 31, 31))
        self.gs1.setStyleSheet("")
        self.gs1.setTextFormat(QtCore.Qt.PlainText)
        self.gs1.setWordWrap(False)
        self.gs1.setObjectName("gs1")
        self.climb = QtWidgets.QLabel(self.rightframe)
        self.climb.setGeometry(QtCore.QRect(80, 550, 61, 31))
        self.climb.setStyleSheet("")
        self.climb.setTextFormat(QtCore.Qt.PlainText)
        self.climb.setWordWrap(False)
        self.climb.setObjectName("climb")
        self.ws1 = QtWidgets.QLabel(self.rightframe)
        self.ws1.setGeometry(QtCore.QRect(40, 590, 31, 31))
        self.ws1.setStyleSheet("")
        self.ws1.setTextFormat(QtCore.Qt.PlainText)
        self.ws1.setWordWrap(False)
        self.ws1.setObjectName("ws1")
        self.temp = QtWidgets.QLabel(self.rightframe)
        self.temp.setGeometry(QtCore.QRect(80, 590, 91, 31))
        self.temp.setStyleSheet("")
        self.temp.setTextFormat(QtCore.Qt.PlainText)
        self.temp.setWordWrap(False)
        self.temp.setObjectName("temp")
        self.gps = QtWidgets.QLabel(self.rightframe)
        self.gps.setGeometry(QtCore.QRect(400, 550, 71, 31))
        self.gps.setStyleSheet("")
        self.gps.setTextFormat(QtCore.Qt.PlainText)
        self.gps.setWordWrap(False)
        self.gps.setObjectName("gps")
        self.agl = QtWidgets.QLabel(self.rightframe)
        self.agl.setGeometry(QtCore.QRect(400, 590, 71, 31))
        self.agl.setStyleSheet("")
        self.agl.setTextFormat(QtCore.Qt.PlainText)
        self.agl.setWordWrap(False)
        self.agl.setObjectName("agl")
        self.climb1 = QtWidgets.QLabel(self.rightframe)
        self.climb1.setGeometry(QtCore.QRect(140, 550, 61, 31))
        self.climb1.setStyleSheet("")
        self.climb1.setTextFormat(QtCore.Qt.PlainText)
        self.climb1.setWordWrap(False)
        self.climb1.setObjectName("climb1")
        self.temp1 = QtWidgets.QLabel(self.rightframe)
        self.temp1.setGeometry(QtCore.QRect(170, 590, 71, 31))
        self.temp1.setStyleSheet("")
        self.temp1.setTextFormat(QtCore.Qt.PlainText)
        self.temp1.setWordWrap(False)
        self.temp1.setObjectName("temp1")
        self.compass = QtWidgets.QWidget(self.rightframe)
        self.compass.setGeometry(QtCore.QRect(200, 140, 191, 191))
        self.compass.setStyleSheet("")
        self.compass.setObjectName("compass")
        self.north = QtWidgets.QLabel(self.compass)
        self.north.setGeometry(QtCore.QRect(70, 10, 61, 41))
        self.north.setWordWrap(False)
        self.north.setObjectName("north")
        self.south = QtWidgets.QLabel(self.compass)
        self.south.setGeometry(QtCore.QRect(80, 150, 41, 31))
        self.south.setWordWrap(False)
        self.south.setObjectName("south")
        self.west = QtWidgets.QLabel(self.compass)
        self.west.setGeometry(QtCore.QRect(20, 80, 31, 31))
        self.west.setWordWrap(False)
        self.west.setObjectName("west")
        self.east = QtWidgets.QLabel(self.compass)
        self.east.setGeometry(QtCore.QRect(150, 80, 31, 31))
        self.east.setWordWrap(False)
        self.east.setObjectName("east")
        self.d1 = QtWidgets.QLabel(self.rightframe)
        self.d1.setGeometry(QtCore.QRect(80, 430, 141, 31))
        self.d1.setStyleSheet("")
        self.d1.setTextFormat(QtCore.Qt.PlainText)
        self.d1.setWordWrap(False)
        self.d1.setObjectName("d1")
        self.d1_value = QtWidgets.QLabel(self.rightframe)
        self.d1_value.setGeometry(QtCore.QRect(250, 430, 241, 31))
        self.d1_value.setStyleSheet("")
        self.d1_value.setText("")
        self.d1_value.setTextFormat(QtCore.Qt.PlainText)
        self.d1_value.setWordWrap(False)
        self.d1_value.setObjectName("d1_value")
        self.gps1 = QtWidgets.QLabel(self.rightframe)
        self.gps1.setGeometry(QtCore.QRect(480, 550, 91, 31))
        self.gps1.setStyleSheet("")
        self.gps1.setText("")
        self.gps1.setTextFormat(QtCore.Qt.PlainText)
        self.gps1.setWordWrap(False)
        self.gps1.setObjectName("gps1")
        self.agl1 = QtWidgets.QLabel(self.rightframe)
        self.agl1.setGeometry(QtCore.QRect(480, 590, 91, 31))
        self.agl1.setStyleSheet("")
        self.agl1.setText("")
        self.agl1.setTextFormat(QtCore.Qt.PlainText)
        self.agl1.setWordWrap(False)
        self.agl1.setObjectName("agl1")
        self.point_2 = QtWidgets.QFrame(self.rightframe)
        self.point_2.setGeometry(QtCore.QRect(50, 530, 491, 16))
        self.point_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.point_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.point_2.setObjectName("point_2")
        self.point_4 = QtWidgets.QFrame(self.rightframe)
        self.point_4.setGeometry(QtCore.QRect(50, 90, 491, 16))
        self.point_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.point_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.point_4.setObjectName("point_4")
        self.ov1 = QtWidgets.QLabel(self.rightframe)
        self.ov1.setGeometry(QtCore.QRect(460, 170, 131, 251))
        self.ov1.setWordWrap(False)
        self.ov1.setObjectName("ov1")
        self.overrideleft_2 = QtWidgets.QLabel(self.rightframe)
        self.overrideleft_2.setGeometry(QtCore.QRect(400, 140, 191, 31))
        self.overrideleft_2.setStyleSheet("")
        self.overrideleft_2.setTextFormat(QtCore.Qt.PlainText)
        self.overrideleft_2.setWordWrap(False)
        self.overrideleft_2.setObjectName("overrideleft_2")
        self.d2 = QtWidgets.QLabel(self.rightframe)
        self.d2.setGeometry(QtCore.QRect(80, 470, 141, 31))
        self.d2.setStyleSheet("")
        self.d2.setTextFormat(QtCore.Qt.PlainText)
        self.d2.setWordWrap(False)
        self.d2.setObjectName("d2")
        self.d2_value = QtWidgets.QLabel(self.rightframe)
        self.d2_value.setGeometry(QtCore.QRect(250, 470, 241, 31))
        self.d2_value.setStyleSheet("")
        self.d2_value.setText("")
        self.d2_value.setTextFormat(QtCore.Qt.PlainText)
        self.d2_value.setWordWrap(False)
        self.d2_value.setObjectName("d2_value")
        self.d3_value = QtWidgets.QLabel(self.rightframe)
        self.d3_value.setGeometry(QtCore.QRect(180, 630, 271, 81))
        self.d3_value.setStyleSheet("")
        self.d3_value.setText("")
        self.d3_value.setTextFormat(QtCore.Qt.PlainText)
        self.d3_value.setWordWrap(False)
        self.d3_value.setObjectName("d3_value")
        self.raw = QtWidgets.QLabel(self.rightframe)
        self.raw.setGeometry(QtCore.QRect(30, 630, 141, 81))
        self.raw.setStyleSheet("")
        self.raw.setTextFormat(QtCore.Qt.PlainText)
        self.raw.setWordWrap(False)
        self.raw.setObjectName("raw")
        self.menu = QtWidgets.QPushButton(finale)
        self.menu.setGeometry(QtCore.QRect(1800, 70, 89, 27))
        self.menu.setStyleSheet("")
        self.menu.setCheckable(True)
        self.menu.setObjectName("menu")
        self.back = QtWidgets.QWidget(finale)
        self.back.setGeometry(QtCore.QRect(-30, 0, 2001, 1161))
        self.back.setStyleSheet("QWidget{\n"
"background-color:qlineargradient(spread:pad, x1:0.675, y1:1, x2:1, y2:0, stop:1 rgba(24, 24, 24, 233));\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color:white;\n"
"}")
        self.back.setObjectName("back")
        self.map = QtWidgets.QWidget(self.back)
        self.map.setGeometry(QtCore.QRect(50, 90, 1281, 971))
        self.map.setObjectName("map")
        self.menu2 = QtWidgets.QPushButton(self.back)
        self.menu2.setGeometry(QtCore.QRect(1730, 70, 89, 27))
        self.menu2.setStyleSheet("")
        self.menu2.setCheckable(True)
        self.menu2.setObjectName("menu2")
        self.cd = QtWidgets.QWidget(self.back)
        self.cd.setGeometry(QtCore.QRect(1449, 580, 481, 481))
        self.cd.setObjectName("cd")
        self.cd2 = QtWidgets.QWidget(self.cd)
        self.cd2.setGeometry(QtCore.QRect(70, 80, 341, 341))
        self.cd2.setObjectName("cd2")
        self.cd.raise_()
        self.map.raise_()
        self.menu2.raise_()
        self.bar = QtWidgets.QWidget(finale)
        self.bar.setGeometry(QtCore.QRect(1480, -40, 491, 101))
        self.bar.setStyleSheet("QFrame#rightframe{font: 75 10pt \"MS Shell Dlg 2\";\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"border: none;\n"
"background-color:qlineargradient(spread:pad, x1:0.526, y1:1, x2:1, y2:0, stop:0 rgba(179, 179, 179, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"}\n"
"\n"
"QLabel#north{\n"
"border:none;\n"
"}\n"
"\n"
"\n"
"QLabel#south{\n"
"border:none;\n"
"}\n"
"\n"
"\n"
"QLabel#east{\n"
"border:none;\n"
"}\n"
"\n"
"\n"
"QLabel#west{\n"
"border:none;\n"
"}\n"
"\n"
"QLabel#pointer{\n"
"border:none;\n"
"}\n"
"QProgressBar#pbfuel{\n"
"border:2px solid black;\n"
"}\n"
"\n"
"\n"
"QProgressBar#barleft{\n"
"border:2px solid black;\n"
"}\n"
"\n"
"QProgressBar#barright{\n"
"border:2px solid black;\n"
"}\n"
"\n"
"QLabel#speed{\n"
"border:2px solid black;\n"
"}\n"
"QLabel{\n"
"border:2px solid black;\n"
"}\n"
"\n"
"\n"
"Line#point{\n"
"\n"
"background-color: red;\n"
"}\n"
"QPushButton{\n"
"border:2px solid black;\n"
"}\n"
"\n"
"QSlider{\n"
"border:2px solid black;\n"
"}")
        self.bar.setObjectName("bar")
        self.cross = QtWidgets.QPushButton(self.bar)
        self.cross.setGeometry(QtCore.QRect(340, 60, 41, 27))
        self.cross.setObjectName("cross")
        self.back.raise_()
        self.menu.raise_()
        self.bar.raise_()
        self.rightframe.raise_()

        self.retranslateUi(finale)
        self.menu.toggled['bool'].connect(self.rightframe.setHidden) # type: ignore
        self.menu2.toggled['bool'].connect(self.cd.setVisible) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(finale)

    def retranslateUi(self, finale):
        _translate = QtCore.QCoreApplication.translate
        finale.setWindowTitle(_translate("finale", "Form"))
        self.monitor.setText(_translate("finale", "Monitor"))
        self.control.setText(_translate("finale", "Control"))
        self.speed.setText(_translate("finale", "SPEED"))
        self.start.setText(_translate("finale", "START"))
        self.overrideleft.setText(_translate("finale", "1st stage"))
        self.altitude.setText(_translate("finale", "Altitude"))
        self.ovl4.setText(_translate("finale", "<html><head/><body><p>0</p></body></html>"))
        self.ruler_2.setText(_translate("finale", "<html><head/><body><p> ═══════════════</p><p> ═══════════════</p><p>═══════════════</p><p> ═══════════════</p><p> ═══════════════</p><p> ═══════════════</p><p> ═══════════════</p><p><br/></p><p><br/></p></body></html>"))
        self.ruler_3.setText(_translate("finale", "<html><head/><body><p> ═══════════════</p><p> ═══════════════</p><p>═══════════════</p><p> ═══════════════</p><p> ═══════════════</p><p> ═══════════════</p><p> ═══════════════</p><p><br/></p><p><br/></p></body></html>"))
        self.speed1.setText(_translate("finale", "50.2"))
        self.msl.setText(_translate("finale", "MSL"))
        self.speed_3.setText(_translate("finale", "3300"))
        self.gs.setText(_translate("finale", "GS"))
        self.ws.setText(_translate("finale", "WS"))
        self.gs1.setText(_translate("finale", "50"))
        self.climb.setText(_translate("finale", "Climb"))
        self.ws1.setText(_translate("finale", "50"))
        self.temp.setText(_translate("finale", "Air Temp"))
        self.gps.setText(_translate("finale", "GPS"))
        self.agl.setText(_translate("finale", "AGL"))
        self.climb1.setText(_translate("finale", "0ft"))
        self.temp1.setText(_translate("finale", "29.9 C"))
        self.north.setText(_translate("finale", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">N</span></p></body></html>"))
        self.south.setText(_translate("finale", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">S</span></p></body></html>"))
        self.west.setText(_translate("finale", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">W</span></p></body></html>"))
        self.east.setText(_translate("finale", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">E</span></p></body></html>"))
        self.d1.setText(_translate("finale", "Longitude"))
        self.ov1.setText(_translate("finale", "<html><head/><body><p>0</p></body></html>"))
        self.overrideleft_2.setText(_translate("finale", "2nd stage"))
        self.d2.setText(_translate("finale", "Latitude"))
        self.raw.setText(_translate("finale", "RAW DATA"))
        self.menu.setText(_translate("finale", "🔺"))
        self.menu2.setText(_translate("finale", "🔺"))
        self.cross.setText(_translate("finale", "🆇"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    finale = QtWidgets.QWidget()
    ui = Ui_finale()
    ui.setupUi(finale)
    finale.show()
    sys.exit(app.exec_())
