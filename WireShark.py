# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Networks4_Widget--ddd.ui'
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
        #self.trigger = pyqtSignal()
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        #self.connect(self.Ok_btn,QtCore.SIGNAL('trigger'), self.incrementRow)
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(829, 583)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 230, 51, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.Select_btn = QtGui.QPushButton(Form)
        self.Select_btn.setGeometry(QtCore.QRect(340, 330, 75, 23))
        self.Select_btn.setObjectName(_fromUtf8("Select_btn"))
        self.count_label = QtGui.QLabel(Form)
        self.count_label.setGeometry(QtCore.QRect(20, 140, 46, 13))
        self.count_label.setObjectName(_fromUtf8("count_label"))
        self.Index_txt = QtGui.QLineEdit(Form)
        self.Index_txt.setGeometry(QtCore.QRect(110, 330, 131, 20))
        self.Index_txt.setObjectName(_fromUtf8("Index_txt"))
        self.count_edit = QtGui.QLineEdit(Form)
        self.count_edit.setGeometry(QtCore.QRect(110, 140, 131, 20))
        self.count_edit.setObjectName(_fromUtf8("count_edit"))
        self.details_edit = QtGui.QTextEdit(Form)
        self.details_edit.setGeometry(QtCore.QRect(110, 370, 701, 91))
        self.details_edit.setObjectName(_fromUtf8("details_edit"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 330, 71, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.details__label = QtGui.QLabel(Form)
        self.details__label.setGeometry(QtCore.QRect(20, 400, 46, 13))
        self.details__label.setObjectName(_fromUtf8("details__label"))
        self.Content_edit = QtGui.QTextEdit(Form)
        self.Content_edit.setGeometry(QtCore.QRect(100, 490, 711, 81))
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
        self.Ok_btn.setGeometry(QtCore.QRect(470, 30, 75, 21))
        self.Ok_btn.setObjectName(_fromUtf8("Ok_btn"))
        self.filter_edit = QtGui.QLineEdit(Form)
        self.filter_edit.setGeometry(QtCore.QRect(110, 80, 131, 21))
        self.filter_edit.setObjectName(_fromUtf8("filter_edit"))
        self.interface_combo = QtGui.QComboBox(Form)
        self.interface_combo.setGeometry(QtCore.QRect(108, 30, 301, 22))
        self.interface_combo.setObjectName(_fromUtf8("interface_combo"))
        self.load_btn = QtGui.QPushButton(Form)
        self.load_btn.setGeometry(QtCore.QRect(690, 130, 75, 23))
        self.load_btn.setObjectName(_fromUtf8("load_btn"))
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(430, 80, 46, 13))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.save_edit = QtGui.QLineEdit(Form)
        self.save_edit.setGeometry(QtCore.QRect(500, 80, 113, 20))
        self.save_edit.setObjectName(_fromUtf8("save_edit"))
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(430, 130, 61, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.load_edit = QtGui.QLineEdit(Form)
        self.load_edit.setGeometry(QtCore.QRect(500, 130, 113, 20))
        self.load_edit.setObjectName(_fromUtf8("load_edit"))
        self.tableWidget = QtGui.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(110, 180, 701, 131))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels(["Time","Source","Destination","Protocol","Length","ID","Checksum"])#.split(";"))
        header = self.tableWidget.horizontalHeader()
        header.setResizeMode(0,  QtGui.QHeaderView.ResizeToContents)
        header.setResizeMode(1,  QtGui.QHeaderView.ResizeToContents)
        header.setResizeMode(2,  QtGui.QHeaderView.ResizeToContents)
        header.setResizeMode(3,  QtGui.QHeaderView.ResizeToContents)
        header.setResizeMode(4,  QtGui.QHeaderView.ResizeToContents)
        header.setResizeMode(5,  QtGui.QHeaderView.ResizeToContents)
        header.setResizeMode(6,  QtGui.QHeaderView.ResizeToContents)
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
        self.load_btn.setText(_translate("Form", "Load", None))
        self.count_edit.setText(_translate("Form","10",None))
        self.filter_edit.setText(_translate("Form","None",None))
        self.save_edit.setText(_translate("Form","pkts.pcap",None))
        self.Ok_btn.clicked.connect (self.Ok)
        self.Select_btn.clicked.connect (self.Select)
        self.load_btn.clicked.connect (self.Load)
        self.label_4.setText(_translate("Form", "Save to", None))
        self.label_5.setText(_translate("Form", "Load from", None))
        self.interface_combo.clear()
		
        for i in range(len(get_windows_if_list())):
            #print(get_windows_if_list()[i]["name"])
            self.interface_combo.addItem(get_windows_if_list()[i]["name"])	
	
    def Ok(self):
        global l
        global rowNo
        rowNo = 0
        filter_val = self.filter_edit.text()
        if(filter_val == "None"):
            filter_val = None
        elif(filter_val == "http"):
            filter_val = "tcp port 80"
        elif("ip.addr" in filter_val):
            filter_val = "host " + filter_val.split("=",1)[1]
            print(filter_val)
        count_val = self.count_edit.text()
        self.tableWidget.setRowCount(int(count_val))
        iface_name = str(self.interface_combo.currentText())
        #pktdump = PcapWriter("packets.txt", append=True, sync=True)
        l = sniff(iface = iface_name, count = int(count_val), filter = filter_val)
        for i in range(len(l)):
            #self.tableWidget.setItem(i,0,QtGui.QTableWidgetItem(l[i].sprintf("Time: %IP.time% Source: %IP.src% Destination:  %IP.dst% Protocol: %IP.proto% Length:  %IP.len% ID: %IP.id% Checksum: %IP.chksum%","\n")))
            self.tableWidget.setItem(i,0,QtGui.QTableWidgetItem(l[i].sprintf("%IP.time%" ,"\n")))
            self.tableWidget.setItem(i,1,QtGui.QTableWidgetItem(l[i].sprintf("%IP.src% ","\n")))
            self.tableWidget.setItem(i,2,QtGui.QTableWidgetItem(l[i].sprintf("%IP.dst% ","\n")))
            self.tableWidget.setItem(i,3,QtGui.QTableWidgetItem(l[i].sprintf("%IP.proto% ","\n")))
            self.tableWidget.setItem(i,4,QtGui.QTableWidgetItem(l[i].sprintf("%IP.len% ","\n")))
            self.tableWidget.setItem(i,5,QtGui.QTableWidgetItem(l[i].sprintf("%IP.id% ","\n")))
            self.tableWidget.setItem(i,6,QtGui.QTableWidgetItem(l[i].sprintf("%IP.chksum%","\n")))
            #print(l[i].sprintf("Time: %IP.time% Source: %IP.src% Destination:  %IP.dst% Protocol: %IP.proto% Length:  %IP.len% ID: %IP.id% Checksum: %IP.chksum%","\n"))
        #pktdump.write(l)
        
        #wrpcap("pkts.pcap",l)
        save_val = self.save_edit.text()
        wrpcap(save_val,l)
		
		#self.Packets.append(x.sprintf("Time: %IP.time% Source: %IP.src% Destination:  %IP.dst% Protocol %IP.proto% Length:  %IP.len% ID: %IP.id% Checksum: %IP.chksum%","\n")),count = int(count_val), filter = filter_val)
        return b""
    	
    def Select(self):
        ind = self.Index_txt.text()
        index= int (ind)
        #print (index)
        r=[]
        r.append(l[index])
        #print(r)
        self.details_edit.setText(str(r))
        
        p = sniff(count=3)
        #p.show()
        #x=[]
        #x.append (hexdump(b'l[index]'*16))
        #hex = hexdump(l[index],dump = True)
        #print(hex)
        print (str(hexdump(b'l[index]'*16)))
        self.Content_edit.append(str(bytes((l[index]))))
        #self.Content_edit.append(hex)
    
    def Load(self):
        load_val = self.load_edit.text()
        packets = rdpcap(load_val)
        for i in range(len(packets)):
            self.tableWidget.setItem(i,0,QtGui.QTableWidgetItem(packets[i].sprintf("%IP.time%" ,"\n")))
            self.tableWidget.setItem(i,1,QtGui.QTableWidgetItem(packets[i].sprintf("%IP.src% ","\n")))
            self.tableWidget.setItem(i,2,QtGui.QTableWidgetItem(packets[i].sprintf("%IP.dst% ","\n")))
            self.tableWidget.setItem(i,3,QtGui.QTableWidgetItem(packets[i].sprintf("%IP.proto% ","\n")))
            self.tableWidget.setItem(i,4,QtGui.QTableWidgetItem(packets[i].sprintf("%IP.len% ","\n")))
            self.tableWidget.setItem(i,5,QtGui.QTableWidgetItem(packets[i].sprintf("%IP.id% ","\n")))
            self.tableWidget.setItem(i,6,QtGui.QTableWidgetItem(packets[i].sprintf("%IP.chksum%","\n")))

if __name__ == '__main__':
    app= QtGui.QApplication(sys.argv)
    ex = Ui_Form()
    ex.show()
    sys.exit(app.exec_())