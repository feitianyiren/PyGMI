# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Experiments\PyGMI\PyGMI-release - v3.0 beta - WIP\PyGMI_files\Instruments_panels\Lakeshore340.ui'
#
# Created: Wed Mar 25 13:02:02 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Panel(object):
    def setupUi(self, Panel):
        Panel.setObjectName("Panel")
        Panel.resize(411, 189)
        self.gridLayout = QtGui.QGridLayout(Panel)
        self.gridLayout.setObjectName("gridLayout")
        self.label_72 = QtGui.QLabel(Panel)
        self.label_72.setObjectName("label_72")
        self.gridLayout.addWidget(self.label_72, 6, 0, 1, 1)
        self.pushButton_7 = QtGui.QPushButton(Panel)
        self.pushButton_7.setDefault(False)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 2, 3, 1, 1)
        self.checkTbox = QtGui.QCheckBox(Panel)
        self.checkTbox.setChecked(False)
        self.checkTbox.setObjectName("checkTbox")
        self.gridLayout.addWidget(self.checkTbox, 1, 1, 1, 1)
        self.T_display = QtGui.QLabel(Panel)
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setWeight(75)
        font.setBold(True)
        self.T_display.setFont(font)
        self.T_display.setAutoFillBackground(False)
        self.T_display.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"color: rgb(255, 255, 255);")
        self.T_display.setFrameShape(QtGui.QFrame.WinPanel)
        self.T_display.setFrameShadow(QtGui.QFrame.Sunken)
        self.T_display.setScaledContents(False)
        self.T_display.setAlignment(QtCore.Qt.AlignCenter)
        self.T_display.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.T_display.setObjectName("T_display")
        self.gridLayout.addWidget(self.T_display, 1, 0, 1, 1)
        self.temp_controller_I = QtGui.QDoubleSpinBox(Panel)
        self.temp_controller_I.setMinimumSize(QtCore.QSize(91, 0))
        self.temp_controller_I.setAlignment(QtCore.Qt.AlignCenter)
        self.temp_controller_I.setSuffix("")
        self.temp_controller_I.setDecimals(3)
        self.temp_controller_I.setMaximum(9999999.0)
        self.temp_controller_I.setSingleStep(10.0)
        self.temp_controller_I.setProperty("value", 0.0)
        self.temp_controller_I.setObjectName("temp_controller_I")
        self.gridLayout.addWidget(self.temp_controller_I, 7, 1, 1, 1)
        self.label_75 = QtGui.QLabel(Panel)
        self.label_75.setObjectName("label_75")
        self.gridLayout.addWidget(self.label_75, 6, 1, 1, 1)
        self.label_45 = QtGui.QLabel(Panel)
        self.label_45.setAlignment(QtCore.Qt.AlignCenter)
        self.label_45.setObjectName("label_45")
        self.gridLayout.addWidget(self.label_45, 2, 0, 1, 1)
        self.temp_controller_loop = QtGui.QSpinBox(Panel)
        self.temp_controller_loop.setAlignment(QtCore.Qt.AlignCenter)
        self.temp_controller_loop.setMinimum(1)
        self.temp_controller_loop.setObjectName("temp_controller_loop")
        self.gridLayout.addWidget(self.temp_controller_loop, 5, 1, 1, 1)
        self.label_24 = QtGui.QLabel(Panel)
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.gridLayout.addWidget(self.label_24, 4, 0, 1, 1)
        self.pushButton_5 = QtGui.QPushButton(Panel)
        self.pushButton_5.setDefault(False)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 2, 2, 1, 1)
        self.temp_controller_ramprate = QtGui.QDoubleSpinBox(Panel)
        self.temp_controller_ramprate.setMinimumSize(QtCore.QSize(91, 0))
        self.temp_controller_ramprate.setAlignment(QtCore.Qt.AlignCenter)
        self.temp_controller_ramprate.setDecimals(2)
        self.temp_controller_ramprate.setMaximum(200000.0)
        self.temp_controller_ramprate.setSingleStep(1.0)
        self.temp_controller_ramprate.setProperty("value", 10.0)
        self.temp_controller_ramprate.setObjectName("temp_controller_ramprate")
        self.gridLayout.addWidget(self.temp_controller_ramprate, 2, 1, 1, 1)
        self.temp_controller_setpoint = QtGui.QDoubleSpinBox(Panel)
        self.temp_controller_setpoint.setMinimumSize(QtCore.QSize(91, 0))
        self.temp_controller_setpoint.setAlignment(QtCore.Qt.AlignCenter)
        self.temp_controller_setpoint.setDecimals(3)
        self.temp_controller_setpoint.setMaximum(330.0)
        self.temp_controller_setpoint.setSingleStep(0.1)
        self.temp_controller_setpoint.setProperty("value", 2.0)
        self.temp_controller_setpoint.setObjectName("temp_controller_setpoint")
        self.gridLayout.addWidget(self.temp_controller_setpoint, 5, 2, 1, 1)
        self.pushButton_6 = QtGui.QPushButton(Panel)
        self.pushButton_6.setDefault(False)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 5, 3, 1, 1)
        self.temp_controller_P = QtGui.QDoubleSpinBox(Panel)
        self.temp_controller_P.setMinimumSize(QtCore.QSize(91, 0))
        self.temp_controller_P.setAlignment(QtCore.Qt.AlignCenter)
        self.temp_controller_P.setSuffix("")
        self.temp_controller_P.setDecimals(3)
        self.temp_controller_P.setMaximum(9999999.0)
        self.temp_controller_P.setSingleStep(0.1)
        self.temp_controller_P.setProperty("value", 0.0)
        self.temp_controller_P.setObjectName("temp_controller_P")
        self.gridLayout.addWidget(self.temp_controller_P, 7, 0, 1, 1)
        self.label_44 = QtGui.QLabel(Panel)
        self.label_44.setAlignment(QtCore.Qt.AlignCenter)
        self.label_44.setObjectName("label_44")
        self.gridLayout.addWidget(self.label_44, 4, 2, 1, 1)
        self.temp_controller_D = QtGui.QDoubleSpinBox(Panel)
        self.temp_controller_D.setMinimumSize(QtCore.QSize(91, 0))
        self.temp_controller_D.setAlignment(QtCore.Qt.AlignCenter)
        self.temp_controller_D.setSuffix("")
        self.temp_controller_D.setDecimals(3)
        self.temp_controller_D.setMaximum(9999999.0)
        self.temp_controller_D.setSingleStep(1.0)
        self.temp_controller_D.setProperty("value", 0.0)
        self.temp_controller_D.setObjectName("temp_controller_D")
        self.gridLayout.addWidget(self.temp_controller_D, 7, 2, 1, 1)
        self.label_76 = QtGui.QLabel(Panel)
        self.label_76.setObjectName("label_76")
        self.gridLayout.addWidget(self.label_76, 6, 2, 1, 1)
        self.temp_controller_channel = QtGui.QComboBox(Panel)
        self.temp_controller_channel.setObjectName("temp_controller_channel")
        self.temp_controller_channel.addItem("")
        self.temp_controller_channel.addItem("")
        self.temp_controller_channel.addItem("")
        self.temp_controller_channel.addItem("")
        self.gridLayout.addWidget(self.temp_controller_channel, 5, 0, 1, 1)
        self.label_46 = QtGui.QLabel(Panel)
        self.label_46.setAlignment(QtCore.Qt.AlignCenter)
        self.label_46.setObjectName("label_46")
        self.gridLayout.addWidget(self.label_46, 4, 1, 1, 1)
        self.spinBox = QtGui.QSpinBox(Panel)
        self.spinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox.setMaximum(5)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout.addWidget(self.spinBox, 7, 3, 1, 1)
        self.label_2 = QtGui.QLabel(Panel)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 6, 3, 1, 1)
        self.refresh_rate = QtGui.QDoubleSpinBox(Panel)
        self.refresh_rate.setMinimumSize(QtCore.QSize(91, 0))
        self.refresh_rate.setAlignment(QtCore.Qt.AlignCenter)
        self.refresh_rate.setDecimals(1)
        self.refresh_rate.setMaximum(9999999.0)
        self.refresh_rate.setSingleStep(0.5)
        self.refresh_rate.setProperty("value", 2.0)
        self.refresh_rate.setObjectName("refresh_rate")
        self.gridLayout.addWidget(self.refresh_rate, 1, 3, 1, 1)
        self.label_47 = QtGui.QLabel(Panel)
        self.label_47.setAlignment(QtCore.Qt.AlignCenter)
        self.label_47.setObjectName("label_47")
        self.gridLayout.addWidget(self.label_47, 1, 2, 1, 1)

        self.retranslateUi(Panel)
        QtCore.QObject.connect(self.pushButton_6, QtCore.SIGNAL("clicked()"), Panel.set_setpoint)
        QtCore.QObject.connect(self.pushButton_7, QtCore.SIGNAL("clicked()"), Panel.stop_ramp)
        QtCore.QObject.connect(self.pushButton_5, QtCore.SIGNAL("clicked()"), Panel.init_ramp)
        QtCore.QObject.connect(self.temp_controller_P, QtCore.SIGNAL("valueChanged(double)"), Panel.PID_P_update)
        QtCore.QObject.connect(self.temp_controller_I, QtCore.SIGNAL("valueChanged(double)"), Panel.PID_I_update)
        QtCore.QObject.connect(self.temp_controller_D, QtCore.SIGNAL("valueChanged(double)"), Panel.PID_D_update)
        QtCore.QObject.connect(self.spinBox, QtCore.SIGNAL("valueChanged(int)"), Panel.set_heater_range)
        QtCore.QObject.connect(self.refresh_rate, QtCore.SIGNAL("valueChanged(double)"), Panel.update_timer_timeout)
        QtCore.QObject.connect(self.checkTbox, QtCore.SIGNAL("clicked(bool)"), Panel.autocheckT)
        QtCore.QMetaObject.connectSlotsByName(Panel)

    def retranslateUi(self, Panel):
        Panel.setWindowTitle(QtGui.QApplication.translate("Panel", "Lakeshore - 340", None, QtGui.QApplication.UnicodeUTF8))
        self.label_72.setText(QtGui.QApplication.translate("Panel", "P", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_7.setText(QtGui.QApplication.translate("Panel", "OFF", None, QtGui.QApplication.UnicodeUTF8))
        self.checkTbox.setText(QtGui.QApplication.translate("Panel", "Monitor T", None, QtGui.QApplication.UnicodeUTF8))
        self.T_display.setText(QtGui.QApplication.translate("Panel", "--- K", None, QtGui.QApplication.UnicodeUTF8))
        self.label_75.setText(QtGui.QApplication.translate("Panel", "I", None, QtGui.QApplication.UnicodeUTF8))
        self.label_45.setText(QtGui.QApplication.translate("Panel", "Ramp Rate :", None, QtGui.QApplication.UnicodeUTF8))
        self.temp_controller_loop.setPrefix(QtGui.QApplication.translate("Panel", "loop ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_24.setText(QtGui.QApplication.translate("Panel", "Channel", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_5.setText(QtGui.QApplication.translate("Panel", "ON", None, QtGui.QApplication.UnicodeUTF8))
        self.temp_controller_ramprate.setSuffix(QtGui.QApplication.translate("Panel", " K/min", None, QtGui.QApplication.UnicodeUTF8))
        self.temp_controller_setpoint.setSuffix(QtGui.QApplication.translate("Panel", " K", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_6.setText(QtGui.QApplication.translate("Panel", "Set", None, QtGui.QApplication.UnicodeUTF8))
        self.label_44.setText(QtGui.QApplication.translate("Panel", "Setpoint", None, QtGui.QApplication.UnicodeUTF8))
        self.label_76.setText(QtGui.QApplication.translate("Panel", "D", None, QtGui.QApplication.UnicodeUTF8))
        self.temp_controller_channel.setItemText(0, QtGui.QApplication.translate("Panel", "A", None, QtGui.QApplication.UnicodeUTF8))
        self.temp_controller_channel.setItemText(1, QtGui.QApplication.translate("Panel", "B", None, QtGui.QApplication.UnicodeUTF8))
        self.temp_controller_channel.setItemText(2, QtGui.QApplication.translate("Panel", "C", None, QtGui.QApplication.UnicodeUTF8))
        self.temp_controller_channel.setItemText(3, QtGui.QApplication.translate("Panel", "D", None, QtGui.QApplication.UnicodeUTF8))
        self.label_46.setText(QtGui.QApplication.translate("Panel", "Control loop", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Panel", "Heater range", None, QtGui.QApplication.UnicodeUTF8))
        self.refresh_rate.setSuffix(QtGui.QApplication.translate("Panel", " secs", None, QtGui.QApplication.UnicodeUTF8))
        self.label_47.setText(QtGui.QApplication.translate("Panel", "Refresh rate :", None, QtGui.QApplication.UnicodeUTF8))
