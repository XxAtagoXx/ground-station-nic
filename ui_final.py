# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'final.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_finale(object):
    def setupUi(self, finale):
        if not finale.objectName():
            finale.setObjectName(u"finale")
        finale.resize(1991, 1141)
        finale.setStyleSheet(u"QPushButton#cross{\n"
"background-color:red;\n"
"}")
        self.rightframe = QFrame(finale)
        self.rightframe.setObjectName(u"rightframe")
        self.rightframe.setGeometry(QRect(1310, 100, 601, 961))
        self.rightframe.setStyleSheet(u"QFrame#rightframe{font: 75 10pt \"MS Shell Dlg 2\";\n"
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
"QLabel#ov1{\n"
"\n"
"font: 20pt \"MS Shell Dlg 2\";\n"
"color: green;\n"
"font: bold;\n"
""
                        "}\n"
"\n"
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
"\n"
"")
        self.monitor = QPushButton(self.rightframe)
        self.monitor.setObjectName(u"monitor")
        self.monitor.setGeometry(QRect(0, 10, 71, 31))
        self.monitor.setCheckable(True)
        self.control = QPushButton(self.rightframe)
        self.control.setObjectName(u"control")
        self.control.setGeometry(QRect(70, 10, 71, 31))
        self.control.setCheckable(True)
        self.speed = QLabel(self.rightframe)
        self.speed.setObjectName(u"speed")
        self.speed.setGeometry(QRect(0, 60, 71, 31))
        self.speed.setStyleSheet(u"")
        self.speed.setTextFormat(Qt.PlainText)
        self.speed.setWordWrap(False)
        self.start = QPushButton(self.rightframe)
        self.start.setObjectName(u"start")
        self.start.setGeometry(QRect(100, 760, 89, 81))
        self.start.setLayoutDirection(Qt.LeftToRight)
        self.start.setAutoFillBackground(False)
        self.start.setStyleSheet(u"")
        self.meter = QDial(self.rightframe)
        self.meter.setObjectName(u"meter")
        self.meter.setGeometry(QRect(230, 730, 161, 131))
        self.slideleft = QSlider(self.rightframe)
        self.slideleft.setObjectName(u"slideleft")
        self.slideleft.setGeometry(QRect(40, 150, 22, 251))
        self.slideleft.setOrientation(Qt.Vertical)
        self.slideright = QSlider(self.rightframe)
        self.slideright.setObjectName(u"slideright")
        self.slideright.setGeometry(QRect(430, 150, 22, 251))
        self.slideright.setOrientation(Qt.Vertical)
        self.battery = QProgressBar(self.rightframe)
        self.battery.setObjectName(u"battery")
        self.battery.setGeometry(QRect(430, 670, 51, 161))
        self.battery.setLayoutDirection(Qt.LeftToRight)
        self.battery.setValue(24)
        self.battery.setOrientation(Qt.Vertical)
        self.battery.setTextDirection(QProgressBar.TopToBottom)
        self.barright = QProgressBar(self.rightframe)
        self.barright.setObjectName(u"barright")
        self.barright.setGeometry(QRect(490, 670, 51, 161))
        self.barright.setLayoutDirection(Qt.LeftToRight)
        self.barright.setValue(24)
        self.barright.setOrientation(Qt.Vertical)
        self.barright.setTextDirection(QProgressBar.TopToBottom)
        self.overrideleft = QLabel(self.rightframe)
        self.overrideleft.setObjectName(u"overrideleft")
        self.overrideleft.setGeometry(QRect(0, 110, 101, 31))
        self.overrideleft.setStyleSheet(u"")
        self.overrideleft.setTextFormat(Qt.PlainText)
        self.overrideleft.setWordWrap(False)
        self.altitude = QLabel(self.rightframe)
        self.altitude.setObjectName(u"altitude")
        self.altitude.setGeometry(QRect(400, 110, 111, 31))
        self.altitude.setStyleSheet(u"")
        self.altitude.setTextFormat(Qt.PlainText)
        self.altitude.setWordWrap(False)
        self.lcdNumber = QLCDNumber(self.rightframe)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setGeometry(QRect(280, 780, 64, 23))
        self.ovl4 = QLabel(self.rightframe)
        self.ovl4.setObjectName(u"ovl4")
        self.ovl4.setGeometry(QRect(70, 150, 131, 251))
        self.ovl4.setWordWrap(False)
        self.ruler_2 = QLabel(self.rightframe)
        self.ruler_2.setObjectName(u"ruler_2")
        self.ruler_2.setGeometry(QRect(400, 150, 21, 251))
        self.ruler_2.setWordWrap(False)
        self.ruler_3 = QLabel(self.rightframe)
        self.ruler_3.setObjectName(u"ruler_3")
        self.ruler_3.setGeometry(QRect(10, 150, 21, 251))
        self.ruler_3.setWordWrap(False)
        self.speed1 = QLabel(self.rightframe)
        self.speed1.setObjectName(u"speed1")
        self.speed1.setGeometry(QRect(70, 60, 71, 31))
        self.speed1.setStyleSheet(u"")
        self.speed1.setTextFormat(Qt.PlainText)
        self.speed1.setWordWrap(False)
        self.msl = QLabel(self.rightframe)
        self.msl.setObjectName(u"msl")
        self.msl.setGeometry(QRect(450, 50, 61, 31))
        self.msl.setStyleSheet(u"")
        self.msl.setTextFormat(Qt.PlainText)
        self.msl.setWordWrap(False)
        self.speed_3 = QLabel(self.rightframe)
        self.speed_3.setObjectName(u"speed_3")
        self.speed_3.setGeometry(QRect(510, 50, 61, 31))
        self.speed_3.setStyleSheet(u"")
        self.speed_3.setTextFormat(Qt.PlainText)
        self.speed_3.setWordWrap(False)
        self.gs = QLabel(self.rightframe)
        self.gs.setObjectName(u"gs")
        self.gs.setGeometry(QRect(0, 550, 41, 31))
        self.gs.setStyleSheet(u"")
        self.gs.setTextFormat(Qt.PlainText)
        self.gs.setWordWrap(False)
        self.ws = QLabel(self.rightframe)
        self.ws.setObjectName(u"ws")
        self.ws.setGeometry(QRect(0, 590, 41, 31))
        self.ws.setStyleSheet(u"")
        self.ws.setTextFormat(Qt.PlainText)
        self.ws.setWordWrap(False)
        self.gs1 = QLabel(self.rightframe)
        self.gs1.setObjectName(u"gs1")
        self.gs1.setGeometry(QRect(40, 550, 31, 31))
        self.gs1.setStyleSheet(u"")
        self.gs1.setTextFormat(Qt.PlainText)
        self.gs1.setWordWrap(False)
        self.climb = QLabel(self.rightframe)
        self.climb.setObjectName(u"climb")
        self.climb.setGeometry(QRect(80, 550, 61, 31))
        self.climb.setStyleSheet(u"")
        self.climb.setTextFormat(Qt.PlainText)
        self.climb.setWordWrap(False)
        self.ws1 = QLabel(self.rightframe)
        self.ws1.setObjectName(u"ws1")
        self.ws1.setGeometry(QRect(40, 590, 31, 31))
        self.ws1.setStyleSheet(u"")
        self.ws1.setTextFormat(Qt.PlainText)
        self.ws1.setWordWrap(False)
        self.temp = QLabel(self.rightframe)
        self.temp.setObjectName(u"temp")
        self.temp.setGeometry(QRect(80, 590, 91, 31))
        self.temp.setStyleSheet(u"")
        self.temp.setTextFormat(Qt.PlainText)
        self.temp.setWordWrap(False)
        self.gps = QLabel(self.rightframe)
        self.gps.setObjectName(u"gps")
        self.gps.setGeometry(QRect(400, 550, 71, 31))
        self.gps.setStyleSheet(u"")
        self.gps.setTextFormat(Qt.PlainText)
        self.gps.setWordWrap(False)
        self.agl = QLabel(self.rightframe)
        self.agl.setObjectName(u"agl")
        self.agl.setGeometry(QRect(400, 590, 71, 31))
        self.agl.setStyleSheet(u"")
        self.agl.setTextFormat(Qt.PlainText)
        self.agl.setWordWrap(False)
        self.climb1 = QLabel(self.rightframe)
        self.climb1.setObjectName(u"climb1")
        self.climb1.setGeometry(QRect(140, 550, 61, 31))
        self.climb1.setStyleSheet(u"")
        self.climb1.setTextFormat(Qt.PlainText)
        self.climb1.setWordWrap(False)
        self.temp1 = QLabel(self.rightframe)
        self.temp1.setObjectName(u"temp1")
        self.temp1.setGeometry(QRect(170, 590, 71, 31))
        self.temp1.setStyleSheet(u"")
        self.temp1.setTextFormat(Qt.PlainText)
        self.temp1.setWordWrap(False)
        self.compass = QWidget(self.rightframe)
        self.compass.setObjectName(u"compass")
        self.compass.setGeometry(QRect(200, 120, 191, 191))
        self.compass.setStyleSheet(u"")
        self.north = QLabel(self.compass)
        self.north.setObjectName(u"north")
        self.north.setGeometry(QRect(69, 10, 61, 41))
        self.north.setWordWrap(False)
        self.south = QLabel(self.compass)
        self.south.setObjectName(u"south")
        self.south.setGeometry(QRect(80, 150, 41, 31))
        self.south.setWordWrap(False)
        self.west = QLabel(self.compass)
        self.west.setObjectName(u"west")
        self.west.setGeometry(QRect(20, 80, 31, 31))
        self.west.setWordWrap(False)
        self.east = QLabel(self.compass)
        self.east.setObjectName(u"east")
        self.east.setGeometry(QRect(150, 80, 31, 31))
        self.east.setWordWrap(False)
        self.direction = QLabel(self.rightframe)
        self.direction.setObjectName(u"direction")
        self.direction.setGeometry(QRect(160, 460, 61, 31))
        self.direction.setStyleSheet(u"")
        self.direction.setTextFormat(Qt.PlainText)
        self.direction.setWordWrap(False)
        self.direction1 = QLabel(self.rightframe)
        self.direction1.setObjectName(u"direction1")
        self.direction1.setGeometry(QRect(250, 460, 151, 31))
        self.direction1.setStyleSheet(u"")
        self.direction1.setTextFormat(Qt.PlainText)
        self.direction1.setWordWrap(False)
        self.gps1 = QLabel(self.rightframe)
        self.gps1.setObjectName(u"gps1")
        self.gps1.setGeometry(QRect(480, 550, 91, 31))
        self.gps1.setStyleSheet(u"")
        self.gps1.setTextFormat(Qt.PlainText)
        self.gps1.setWordWrap(False)
        self.agl1 = QLabel(self.rightframe)
        self.agl1.setObjectName(u"agl1")
        self.agl1.setGeometry(QRect(480, 590, 91, 31))
        self.agl1.setStyleSheet(u"")
        self.agl1.setTextFormat(Qt.PlainText)
        self.agl1.setWordWrap(False)
        self.point_2 = QFrame(self.rightframe)
        self.point_2.setObjectName(u"point_2")
        self.point_2.setGeometry(QRect(50, 530, 491, 16))
        self.point_2.setFrameShape(QFrame.HLine)
        self.point_2.setFrameShadow(QFrame.Sunken)
        self.point_4 = QFrame(self.rightframe)
        self.point_4.setObjectName(u"point_4")
        self.point_4.setGeometry(QRect(50, 90, 491, 16))
        self.point_4.setFrameShape(QFrame.HLine)
        self.point_4.setFrameShadow(QFrame.Sunken)
        self.ov1 = QLabel(self.rightframe)
        self.ov1.setObjectName(u"ov1")
        self.ov1.setGeometry(QRect(460, 150, 131, 251))
        self.ov1.setWordWrap(False)
        self.menu = QPushButton(finale)
        self.menu.setObjectName(u"menu")
        self.menu.setGeometry(QRect(1800, 70, 89, 27))
        self.menu.setStyleSheet(u"")
        self.menu.setCheckable(True)
        self.back = QWidget(finale)
        self.back.setObjectName(u"back")
        self.back.setGeometry(QRect(-30, 0, 2001, 1161))
        self.back.setStyleSheet(u"QWidget{\n"
"background-color:qlineargradient(spread:pad, x1:0.675, y1:1, x2:1, y2:0, stop:1 rgba(24, 24, 24, 233));\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color:white;\n"
"}")
        self.map = QWidget(self.back)
        self.map.setObjectName(u"map")
        self.map.setGeometry(QRect(50, 90, 1281, 971))
        self.menu2 = QPushButton(self.back)
        self.menu2.setObjectName(u"menu2")
        self.menu2.setGeometry(QRect(1730, 70, 89, 27))
        self.menu2.setStyleSheet(u"")
        self.menu2.setCheckable(True)
        self.cd = QWidget(self.back)
        self.cd.setObjectName(u"cd")
        self.cd.setGeometry(QRect(1449, 580, 481, 481))
        self.cd2 = QWidget(self.cd)
        self.cd2.setObjectName(u"cd2")
        self.cd2.setGeometry(QRect(70, 80, 341, 341))
        self.cd.raise_()
        self.map.raise_()
        self.menu2.raise_()
        self.bar = QWidget(finale)
        self.bar.setObjectName(u"bar")
        self.bar.setGeometry(QRect(1480, -40, 491, 101))
        self.bar.setStyleSheet(u"QFrame#rightframe{font: 75 10pt \"MS Shell Dlg 2\";\n"
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
        self.cross = QPushButton(self.bar)
        self.cross.setObjectName(u"cross")
        self.cross.setGeometry(QRect(340, 60, 41, 27))
        self.back.raise_()
        self.menu.raise_()
        self.bar.raise_()
        self.rightframe.raise_()

        self.retranslateUi(finale)
        self.menu.toggled.connect(self.rightframe.setHidden)
        self.menu2.toggled.connect(self.cd.setVisible)

        QMetaObject.connectSlotsByName(finale)
    # setupUi

    def retranslateUi(self, finale):
        finale.setWindowTitle(QCoreApplication.translate("finale", u"Form", None))
        self.monitor.setText(QCoreApplication.translate("finale", u"Monitor", None))
        self.control.setText(QCoreApplication.translate("finale", u"Control", None))
        self.speed.setText(QCoreApplication.translate("finale", u"SPEED", None))
        self.start.setText(QCoreApplication.translate("finale", u"START", None))
        self.overrideleft.setText(QCoreApplication.translate("finale", u"OVERRIDE", None))
        self.altitude.setText(QCoreApplication.translate("finale", u"Altitude", None))
        self.ovl4.setText(QCoreApplication.translate("finale", u"<html><head/><body><p>0</p></body></html>", None))
        self.ruler_2.setText(QCoreApplication.translate("finale", u"<html><head/><body><p> \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550</p><p> \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550</p><p>\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550</p><p> \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550</p><p> \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550</p><p> \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550</p><p> \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550</p><p><br/></p><p><br/></p></body></html>", None))
        self.ruler_3.setText(QCoreApplication.translate("finale", u"<html><head/><body><p> \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550</p><p> \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550</p><p>\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550</p><p> \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550</p><p> \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550</p><p> \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550</p><p> \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550</p><p><br/></p><p><br/></p></body></html>", None))
        self.speed1.setText(QCoreApplication.translate("finale", u"50.2", None))
        self.msl.setText(QCoreApplication.translate("finale", u"MSL", None))
        self.speed_3.setText(QCoreApplication.translate("finale", u"3300", None))
        self.gs.setText(QCoreApplication.translate("finale", u"GS", None))
        self.ws.setText(QCoreApplication.translate("finale", u"WS", None))
        self.gs1.setText(QCoreApplication.translate("finale", u"50", None))
        self.climb.setText(QCoreApplication.translate("finale", u"Climb", None))
        self.ws1.setText(QCoreApplication.translate("finale", u"50", None))
        self.temp.setText(QCoreApplication.translate("finale", u"Air Temp", None))
        self.gps.setText(QCoreApplication.translate("finale", u"GPS", None))
        self.agl.setText(QCoreApplication.translate("finale", u"AGL", None))
        self.climb1.setText(QCoreApplication.translate("finale", u"0ft", None))
        self.temp1.setText(QCoreApplication.translate("finale", u"29.9 C", None))
        self.north.setText(QCoreApplication.translate("finale", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">N</span></p></body></html>", None))
        self.south.setText(QCoreApplication.translate("finale", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">S</span></p></body></html>", None))
        self.west.setText(QCoreApplication.translate("finale", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">W</span></p></body></html>", None))
        self.east.setText(QCoreApplication.translate("finale", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">E</span></p></body></html>", None))
        self.direction.setText(QCoreApplication.translate("finale", u"Direction", None))
        self.direction1.setText("")
        self.gps1.setText("")
        self.agl1.setText("")
        self.ov1.setText(QCoreApplication.translate("finale", u"<html><head/><body><p>0</p></body></html>", None))
        self.menu.setText(QCoreApplication.translate("finale", u"\ud83d\udd3a", None))
        self.menu2.setText(QCoreApplication.translate("finale", u"\ud83d\udd3a", None))
        self.cross.setText(QCoreApplication.translate("finale", u"\ud83c\udd87", None))
    # retranslateUi

