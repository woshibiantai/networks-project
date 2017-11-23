# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyqt_networks_ui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *
import sys
import json
import os
os.environ["QT_SCALE_FACTOR"] = "1.5"

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
    	return QApplication.translate(context, text, disambig)

class Ui_Dialog(QWidget):
	def __init__(self):
		QWidget.__init__(self)
		self.setupUi(self)
	def setupUi(self, Dialog):
		Dialog.setObjectName(_fromUtf8("Dialog"))
		Dialog.resize(500, 500)
		Dialog.setMinimumSize(QtCore.QSize(500, 500))
		Dialog.setMaximumSize(QtCore.QSize(500, 500))
		Dialog.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		Dialog.setMouseTracking(False)
		Dialog.setAcceptDrops(False)
		Dialog.setWindowOpacity(1.0)
		Dialog.setAutoFillBackground(False)
		Dialog.setStyleSheet(_fromUtf8("font: 8pt \"MS PGothic\";\n"
			"border-color: rgb(0, 0, 0);\n"
			"selection-color: rgb(255, 170, 255);\n"
			""))
		Dialog.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
		self.reset_btn = QPushButton(Dialog)
		self.reset_btn.setGeometry(QtCore.QRect(215, 420, 70, 23))
		self.reset_btn.setStyleSheet(_fromUtf8("background-color: rgb(0, 98, 255);\n"
			"color: rgb(255, 255, 255);"))
		self.reset_btn.setObjectName(_fromUtf8("reset_btn"))
		self.apply_btn = QPushButton(Dialog)
		self.apply_btn.setGeometry(QtCore.QRect(215, 450, 70, 23))
		self.apply_btn.setStyleSheet(_fromUtf8("background-color: rgb(0, 98, 255);\n"
			"color: rgb(255, 255, 255);"))
		self.apply_btn.setObjectName(_fromUtf8("apply_btn"))
		self.blacklisted_sites_list = QListWidget(Dialog)
		self.blacklisted_sites_list.setGeometry(QtCore.QRect(30, 50, 431, 141))
		self.blacklisted_sites_list.setObjectName(_fromUtf8("blacklisted_sites_list"))
		self.blacklisted_sites_label = QLabel(Dialog)
		self.blacklisted_sites_label.setGeometry(QtCore.QRect(30, 20, 131, 16))
		font = QtGui.QFont()
		font.setFamily(_fromUtf8("MS PGothic 12"))
		font.setPointSize(12)
		font.setBold(False)
		font.setItalic(False)
		font.setWeight(9)
		self.blacklisted_sites_label.setFont(font)
		self.blacklisted_sites_label.setStyleSheet(_fromUtf8("font: 75 12pt \"MS PGothic\" bold;"))
		self.blacklisted_sites_label.setObjectName(_fromUtf8("blacklisted_sites_label"))
		self.blacklisted_sites_editfield = QLineEdit(Dialog)
		self.blacklisted_sites_editfield.setGeometry(QtCore.QRect(30, 200, 361, 20))
		self.blacklisted_sites_editfield.setObjectName(_fromUtf8("blacklisted_sites_editfield"))
		self.add_blacklisted_sites_btn = QPushButton(Dialog)
		self.add_blacklisted_sites_btn.setGeometry(QtCore.QRect(410, 200, 16, 16))
		self.add_blacklisted_sites_btn.setStyleSheet(_fromUtf8("background-color: rgb(0, 98, 255);\n"
			"color: rgb(255, 255, 255);"))
		self.add_blacklisted_sites_btn.setObjectName(_fromUtf8("add_blacklisted_sites_btn"))
		self.remove_blacklisted_sites_btn = QPushButton(Dialog)
		self.remove_blacklisted_sites_btn.setGeometry(QtCore.QRect(440, 200, 16, 16))
		self.remove_blacklisted_sites_btn.setStyleSheet(_fromUtf8("background-color: rgb(0, 98, 255);\n"
			"color: rgb(255, 255, 255);"))
		self.remove_blacklisted_sites_btn.setObjectName(_fromUtf8("remove_blacklisted_sites_btn"))
		self.strings_to_modify_label = QLabel(Dialog)
		self.strings_to_modify_label.setGeometry(QtCore.QRect(30, 240, 161, 21))
		font = QtGui.QFont()
		font.setFamily(_fromUtf8("MS PGothic 12"))
		font.setPointSize(12)
		font.setBold(False)
		font.setItalic(False)
		font.setWeight(9)
		self.strings_to_modify_label.setFont(font)
		self.strings_to_modify_label.setStyleSheet(_fromUtf8("font: 75 12pt \"MS PGothic\" bold;"))
		self.strings_to_modify_label.setObjectName(_fromUtf8("strings_to_modify_label"))
		self.strings_to_modify_editfield = QLineEdit(Dialog)
		self.strings_to_modify_editfield.setGeometry(QtCore.QRect(30, 380, 201, 20))
		self.strings_to_modify_editfield.setText(_fromUtf8(""))
		self.strings_to_modify_editfield.setFrame(False)
		self.strings_to_modify_editfield.setEchoMode(QLineEdit.Normal)
		self.strings_to_modify_editfield.setObjectName(_fromUtf8("strings_to_modify_editfield"))
		self.strings_modified_editfield = QLineEdit(Dialog)
		self.strings_modified_editfield.setGeometry(QtCore.QRect(260, 380, 131, 20))
		self.strings_modified_editfield.setText(_fromUtf8(""))
		self.strings_modified_editfield.setFrame(False)
		self.strings_modified_editfield.setEchoMode(QLineEdit.Normal)
		self.strings_modified_editfield.setObjectName(_fromUtf8("strings_modified_editfield"))
		self.remove_strings_to_modify_btn = QPushButton(Dialog)
		self.remove_strings_to_modify_btn.setGeometry(QtCore.QRect(440, 380, 16, 16))
		self.remove_strings_to_modify_btn.setStyleSheet(_fromUtf8("background-color: rgb(0, 98, 255);\n"
			"color: rgb(255, 255, 255);"))
		self.remove_strings_to_modify_btn.setObjectName(_fromUtf8("remove_strings_to_modify_btn"))
		self.add_strings_to_modify_btn = QPushButton(Dialog)
		self.add_strings_to_modify_btn.setGeometry(QtCore.QRect(410, 380, 16, 16))
		self.add_strings_to_modify_btn.setStyleSheet(_fromUtf8("background-color: rgb(0, 98, 255);\n"
			"color: rgb(255, 255, 255);"))
		self.add_strings_to_modify_btn.setObjectName(_fromUtf8("add_strings_to_modify_btn"))
		self.strings_to_modify_list = QListWidget(Dialog)
		self.strings_to_modify_list.setGeometry(QtCore.QRect(30, 270, 201, 101))
		self.strings_to_modify_list.setObjectName(_fromUtf8("strings_to_modify_list"))
		self.strings_modified_list = QListWidget(Dialog)
		self.strings_modified_list.setGeometry(QtCore.QRect(260, 270, 201, 101))
		self.strings_modified_list.setObjectName(_fromUtf8("strings_modified_list"))
		self.label = QLabel(Dialog)
		self.label.setGeometry(QtCore.QRect(240, 310, 21, 21))
		self.label.setStyleSheet(_fromUtf8("font: 75 12pt \"MS PGothic\";"))
		self.label.setObjectName(_fromUtf8("label"))

		self.retranslateUi(Dialog)
		QtCore.QMetaObject.connectSlotsByName(Dialog)

	def retranslateUi(self, Dialog):
		Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
		self.reset_btn.setText(_translate("Dialog", "Reset", None))
		self.apply_btn.setText(_translate("Dialog", "Apply", None))
		self.blacklisted_sites_label.setText(_translate("Dialog", "Blacklisted Sites", None))
		self.add_blacklisted_sites_btn.setText(_translate("Dialog", "+", None))
		self.remove_blacklisted_sites_btn.setText(_translate("Dialog", "-", None))
		self.strings_to_modify_label.setText(_translate("Dialog", "Strings to modify", None))
		self.strings_to_modify_editfield.setPlaceholderText(_translate("Dialog", "enter new word", None))
		self.strings_modified_editfield.setPlaceholderText(_translate("Dialog", "enter changed word", None))
		self.remove_strings_to_modify_btn.setText(_translate("Dialog", "-", None))
		self.add_strings_to_modify_btn.setText(_translate("Dialog", "+", None))
		self.label.setText(_translate("Dialog", "to", None))

        #openthefile
		existingJson = open('prefs.json')
		data = json.load(existingJson)
		existing_word_pair= data['Wordlist']
		for key,value in existing_word_pair.items():
			self.strings_to_modify_list.addItem(key)
			self.strings_modified_list.addItem(value)

		existing_blacklisted_sites= data['Blacklisted_sites']
		for getSites in existing_blacklisted_sites:
			self.blacklisted_sites_list.addItem(getSites)

		self.add_blacklisted_sites_btn.clicked.connect(self.add_blacklisted_sites)
		self.remove_blacklisted_sites_btn.clicked.connect(self.remove_blacklisted_sites)

		self.add_strings_to_modify_btn.clicked.connect(self.add_strings_to_modify)
		self.remove_strings_to_modify_btn.clicked.connect(self.remove_strings_to_modify)
		self.reset_btn.clicked.connect(self.reset_all)
		self.apply_btn.clicked.connect(self.apply_all)


	def add_blacklisted_sites(self):
		#blacklisted_sites_editfield --> QLineEdit
		getSites = self.blacklisted_sites_editfield.text()
		self.blacklisted_sites_editfield.clear() #clear the linefield after every addition
		self.blacklisted_sites_list.addItem(getSites) #add Item to the listviewwidget


	def remove_blacklisted_sites(self):
		for SelectedItem in self.blacklisted_sites_list.selectedItems():
			self.blacklisted_sites_list.takeItem(self.blacklisted_sites_list.row(SelectedItem))

	def add_strings_to_modify(self):
		getFirstStrings= self.strings_to_modify_editfield.text()
		getSecondStrings= self.strings_modified_editfield.text()
		if getFirstStrings=="" or getSecondStrings=="":
			pass
		else:
			print(getFirstStrings, getSecondStrings)
			self.strings_to_modify_list.addItem(getFirstStrings)
			self.strings_modified_list.addItem(getSecondStrings)
			self.strings_to_modify_editfield.clear()
			self.strings_modified_editfield.clear()

	def remove_strings_to_modify(self):
		for SelectedItem in self.strings_to_modify_list.selectedItems():
			for SelectedItem2 in self.strings_modified_list.selectedItems():
				if self.strings_to_modify_list.isItemSelected(SelectedItem)==False or self.strings_modified_list.isItemSelected(SelectedItem2)==False:
					pass
				else:
					self.strings_to_modify_list.takeItem(self.strings_to_modify_list.row(SelectedItem))
					self.strings_modified_list.takeItem(self.strings_modified_list.row(SelectedItem2))

	def reset_all(self):
		self.blacklisted_sites_list.clear()
		self.strings_to_modify_list.clear()
		self.strings_modified_list.clear()

	def apply_all(self):
		wordlist_dict = {}
		i=0
		while i< self.strings_to_modify_list.count():
			item = self.strings_to_modify_list.item(i)
			paireditem = self.strings_modified_list.item(i)
			i+=1
			wordlist_dict[str(item.text())] = str(paireditem.text())

		blacklisted_dict = {}
		for index in range(self.blacklisted_sites_list.count()):
			blacklisted_dict[str(self.blacklisted_sites_list.item(index).text())] = ""
			print(self.blacklisted_sites_list.item(index).text())

		with open('prefs.json','w') as f:
			f.write(json.dumps({'Wordlist': wordlist_dict, 'Blacklisted_sites':blacklisted_dict}))
			f.close()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = Ui_Dialog()
	ex.show()
	sys.exit(app.exec_())
