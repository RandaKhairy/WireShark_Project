# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Networks4_Widget.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys
import os
import scapy
from scapy.all import*
from PyQt4.QtCore import * 
from PyQt4.QtGui import * 
from scapy.packet import *



try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(823, 569)
        self.Packets = QtGui.QTextEdit(Form)
        self.Packets.setGeometry(QtCore.QRect(100, 210, 601, 81))
        self.Packets.setObjectName(_fromUtf8("Packets"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 230, 51, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.Select_btn = QtGui.QPushButton(Form)
        self.Select_btn.setGeometry(QtCore.QRect(320, 320, 75, 23))
        self.Select_btn.setObjectName(_fromUtf8("Select_btn"))
        self.Interface_edit = QtGui.QLineEdit(Form)
        self.Interface_edit.setGeometry(QtCore.QRect(110, 30, 133, 21))
        self.Interface_edit.setObjectName(_fromUtf8("Interface_edit"))
        self.count_label = QtGui.QLabel(Form)
        self.count_label.setGeometry(QtCore.QRect(20, 140, 46, 13))
        self.count_label.setObjectName(_fromUtf8("count_label"))
        self.Index_txt = QtGui.QLineEdit(Form)
        self.Index_txt.setGeometry(QtCore.QRect(110, 320, 131, 20))
        self.Index_txt.setObjectName(_fromUtf8("Index_txt"))
        self.count_edit = QtGui.QLineEdit(Form)
        self.count_edit.setGeometry(QtCore.QRect(110, 140, 131, 20))
        self.count_edit.setObjectName(_fromUtf8("count_edit"))
        self.details_edit = QtGui.QTextEdit(Form)
        self.details_edit.setGeometry(QtCore.QRect(100, 370, 601, 91))
        self.details_edit.setObjectName(_fromUtf8("details_edit"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 320, 71, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.details__label = QtGui.QLabel(Form)
        self.details__label.setGeometry(QtCore.QRect(20, 400, 46, 13))
        self.details__label.setObjectName(_fromUtf8("details__label"))
        self.Content_edit = QtGui.QTextEdit(Form)
        self.Content_edit.setGeometry(QtCore.QRect(100, 490, 591, 71))
        self.Content_edit.setObjectName(_fromUtf8("Content_edit"))
        self.Label = QtGui.QLabel(Form)
        self.Label.setGeometry(QtCore.QRect(20, 20, 50, 30))
        self.Label.setObjectName(_fromUtf8("Label"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 510, 46, 13))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.filter_label = QtGui.QLabel(Form)
        self.filter_label.setGeometry(QtCore.QRect(20, 80, 46, 13))
        self.filter_label.setObjectName(_fromUtf8("filter_label"))
        self.Ok_btn = QtGui.QPushButton(Form)
        self.Ok_btn.setGeometry(QtCore.QRect(320, 140, 75, 21))
        self.Ok_btn.setObjectName(_fromUtf8("Ok_btn"))
        self.filter_edit = QtGui.QLineEdit(Form)
        self.filter_edit.setGeometry(QtCore.QRect(110, 80, 131, 21))
        self.filter_edit.setObjectName(_fromUtf8("filter_edit"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Networks", None))
        self.label.setText(_translate("Form", "Packets", None))
        self.Select_btn.setText(_translate("Form", "Select", None))
        self.count_label.setText(_translate("Form", "Count", None))
        self.label_2.setText(_translate("Form", "Packet Index", None))
        self.details__label.setText(_translate("Form", "Details", None))
        self.Label.setText(_translate("Form", "Interface", None))
        self.label_3.setText(_translate("Form", "Content", None))
        self.filter_label.setText(_translate("Form", "Filter", None))
        self.Ok_btn.setText(_translate("Form", "Start", None))
        self.Ok_btn.clicked.connect (self.Ok)
        self.Select_btn.clicked.connect (self.Select)

    def Ok(self):
        global l
        text = self.Interface_edit.text()
        if (text=="Ethernet"):
            iface_name= "VirtualBox Host-Only Ethernet Adapter"
        elif (text=="Bluetooth"):
            iface_name= "Bluetooth Device (Personal Area Network)"
        elif (text=="Wi-Fi"):
            iface_name= "Realtek RTL8723BE Wireless LAN 802.11n PCI-E NIC"

        l= sniff(iface=iface_name ,prn = lambda x:\
        self.Packets.append(x.sprintf("Time: %IP.time% Source: %IP.src% Distination:  %IP.dst% Protocol %IP.proto% Length:  %IP.len% ID: %IP.id% Checksum: %IP.chksum%","\n")),count=20, timeout=100)
        return b""

    

    def Select(self):
        ind = self.Index_txt.text()
        index= int (ind)
        print (index)
        r=[]
        r.append(l[index])
        print(r)
        self.details_edit.setText(str(r))
        
        p= sniff(count=3)
        p.show()
        self.Content_edit.append(str(bytes((l[index]))))

if __name__ == '__main__':
    app= QtGui.QApplication(sys.argv)
    ex = Ui_Form()
    ex.show()
    sys.exit(app.exec_())