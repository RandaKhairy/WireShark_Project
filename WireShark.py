# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Networks1_Widget.ui'
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
        Form.resize(400, 300)
        self.Label = QtGui.QLabel(Form)
        self.Label.setGeometry(QtCore.QRect(30, 60, 45, 31))
        self.Label.setObjectName(_fromUtf8("Label"))
        self.Packets = QtGui.QTextEdit(Form)
        self.Packets.setGeometry(QtCore.QRect(110, 130, 221, 81))
        self.Packets.setObjectName(_fromUtf8("Packets"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 160, 51, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.Interface_edit = QtGui.QLineEdit(Form)
        self.Interface_edit.setGeometry(QtCore.QRect(110, 70, 133, 21))
        self.Interface_edit.setObjectName(_fromUtf8("Interface_edit"))
        self.Ok_btn = QtGui.QPushButton(Form)
        self.Ok_btn.setGeometry(QtCore.QRect(260, 70, 75, 21))
        self.Ok_btn.setObjectName(_fromUtf8("Ok_btn"))
        

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Networks", None))
        self.Label.setText(_translate("Form", "Interface", None))
        self.label.setText(_translate("Form", "Packets", None))
        self.Ok_btn.setText(_translate("Form", "Ok", None))
        self.Ok_btn.clicked.connect (self.Ok)

    
    

    def Ok(self):
        text = self.Interface_edit.text()
        if (text=="Ethernet"):
            iface_name= "VirtualBox Host-Only Ethernet Adapter"
        elif (text=="Bluetooth"):
            iface_name= "Bluetooth Device (Personal Area Network)"
        elif (text=="Wi-Fi"):
            iface_name= "Qualcomm QCA61x4A 802.11ac Wireless Adapter"

        l= sniff(iface=iface_name ,prn = lambda x:\
        self.Packets.append(x.sprintf("Time: %IP.time% Source: %IP.src% Distination:  %IP.dst% Protocol %IP.proto% Length:  %IP.len% ID: %IP.id% Checksum: %IP.chksum%","\n")),count=50, timeout=100)
            
        #r=[]
        #p= sniff(iface="Realtek RTL8723BE Wireless LAN 802.11n PCI-E NIC",prn = lambda x:\
        #x.sprintf("Time: %IP.time% Source: %IP.src% Distination:  %IP.dst% Protocol %IP.proto% Length:  %IP.len% ID: %IP.id% Checksum: %IP.chksum%","\n"),count=10, timeout=100)
        #self.Packets.append('spam: spam spam spam spam')
        #p.show()
        #for i in range(10000):
            #r.append (p[i].summary())
        #self.Packets.setText(str(r))
        #print(r)

   # def readOutput(self):
     #   l= sniff(iface="Realtek RTL8723BE Wireless LAN 802.11n PCI-E NIC",prn = lambda x:\
     #   self.Packets.append(x.sprintf("Time: %IP.time% Source: %IP.src% Distination:  %IP.dst% Protocol %IP.proto% Length:  %IP.len% ID: %IP.id% Checksum: %IP.chksum%","\n")),count=50, timeout=100)
        
        



 
  

if __name__ == '__main__':
    app= QtGui.QApplication(sys.argv)
    ex = Ui_Form()
    ex.show()
    sys.exit(app.exec_())
