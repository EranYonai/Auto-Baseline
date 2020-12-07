# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ultrasound_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(383, 399)
        self.softwarever_text = QtWidgets.QLineEdit(Dialog)
        self.softwarever_text.setGeometry(QtCore.QRect(170, 125, 191, 22))
        self.softwarever_text.setObjectName("softwarever_text")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(20, 295, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.check_button = QtWidgets.QPushButton(Dialog)
        self.check_button.setGeometry(QtCore.QRect(60, 350, 93, 28))
        self.check_button.setObjectName("check_button")
        self.applicationver_text = QtWidgets.QLineEdit(Dialog)
        self.applicationver_text.setGeometry(QtCore.QRect(170, 205, 191, 22))
        self.applicationver_text.setObjectName("applicationver_text")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 165, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 205, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.serialnum_text = QtWidgets.QLineEdit(Dialog)
        self.serialnum_text.setGeometry(QtCore.QRect(170, 165, 191, 22))
        self.serialnum_text.setObjectName("serialnum_text")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 80, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.videocable_text = QtWidgets.QLineEdit(Dialog)
        self.videocable_text.setGeometry(QtCore.QRect(170, 250, 191, 22))
        self.videocable_text.setObjectName("videocable_text")
        self.ethernet_text = QtWidgets.QLineEdit(Dialog)
        self.ethernet_text.setGeometry(QtCore.QRect(170, 295, 191, 22))
        self.ethernet_text.setObjectName("ethernet_text")
        self.title = QtWidgets.QLabel(Dialog)
        self.title.setGeometry(QtCore.QRect(130, 21, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(20)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 250, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 125, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.confirm_button = QtWidgets.QPushButton(Dialog)
        self.confirm_button.setGeometry(QtCore.QRect(220, 350, 93, 28))
        self.confirm_button.setObjectName("confirm_button")
        self.ultrasound_combo = QtWidgets.QComboBox(Dialog)
        self.ultrasound_combo.setGeometry(QtCore.QRect(170, 80, 191, 22))
        self.ultrasound_combo.setObjectName("ultrasound_combo")
        self.ultrasound_combo.addItem("")
        self.ultrasound_combo.addItem("")
        self.ultrasound_combo.addItem("")
        self.ultrasound_combo.addItem("")
        self.ultrasound_combo.addItem("")
        self.ultrasound_combo.addItem("")
        self.ultrasound_combo.addItem("")
        self.ultrasound_combo.addItem("")
        self.ultrasound_combo.addItem("")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.ultrasound_combo, self.softwarever_text)
        Dialog.setTabOrder(self.softwarever_text, self.serialnum_text)
        Dialog.setTabOrder(self.serialnum_text, self.applicationver_text)
        Dialog.setTabOrder(self.applicationver_text, self.videocable_text)
        Dialog.setTabOrder(self.videocable_text, self.ethernet_text)
        Dialog.setTabOrder(self.ethernet_text, self.check_button)
        Dialog.setTabOrder(self.check_button, self.confirm_button)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_6.setText(_translate("Dialog", "Ethernet Cable:"))
        self.check_button.setText(_translate("Dialog", "Verify"))
        self.label_3.setText(_translate("Dialog", "Serial Number:"))
        self.label_4.setText(_translate("Dialog", "Application Version:"))
        self.label.setText(_translate("Dialog", "UltraSound System:"))
        self.title.setText(_translate("Dialog", "UltraSound"))
        self.label_5.setText(_translate("Dialog", "Video Cable:"))
        self.label_2.setText(_translate("Dialog", "Software Version:"))
        self.confirm_button.setText(_translate("Dialog", "Confirm"))
        self.ultrasound_combo.setItemText(0, _translate("Dialog", "Vivid (i or q)"))
        self.ultrasound_combo.setItemText(1, _translate("Dialog", "Vivid IQ"))
        self.ultrasound_combo.setItemText(2, _translate("Dialog", "Vivid S-70"))
        self.ultrasound_combo.setItemText(3, _translate("Dialog", "X300 PE"))
        self.ultrasound_combo.setItemText(4, _translate("Dialog", "X700"))
        self.ultrasound_combo.setItemText(5, _translate("Dialog", "SC200 System"))
        self.ultrasound_combo.setItemText(6, _translate("Dialog", "Sequoia System (PAL)"))
        self.ultrasound_combo.setItemText(7, _translate("Dialog", "Sequoia System (NTSC)"))
        self.ultrasound_combo.setItemText(8, _translate("Dialog", "P500"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
