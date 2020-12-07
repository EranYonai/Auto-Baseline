# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CatalogHelper_details.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(342, 229)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 30, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.description_text = QtWidgets.QLineEdit(Dialog)
        self.description_text.setGeometry(QtCore.QRect(110, 110, 221, 22))
        self.description_text.setObjectName("description_text")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 110, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.mfg_text = QtWidgets.QLineEdit(Dialog)
        self.mfg_text.setGeometry(QtCore.QRect(110, 70, 221, 22))
        self.mfg_text.setObjectName("mfg_text")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 145, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.catalog_text = QtWidgets.QLineEdit(Dialog)
        self.catalog_text.setGeometry(QtCore.QRect(110, 30, 221, 22))
        self.catalog_text.setObjectName("catalog_text")
        self.family_text = QtWidgets.QLineEdit(Dialog)
        self.family_text.setGeometry(QtCore.QRect(110, 145, 221, 22))
        self.family_text.setObjectName("family_text")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(30, 180, 131, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 180, 121, 28))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.catalog_text, self.mfg_text)
        Dialog.setTabOrder(self.mfg_text, self.description_text)
        Dialog.setTabOrder(self.description_text, self.family_text)
        Dialog.setTabOrder(self.family_text, self.pushButton)
        Dialog.setTabOrder(self.pushButton, self.pushButton_2)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Catalog:"))
        self.label_2.setText(_translate("Dialog", "MFG Part:"))
        self.label_3.setText(_translate("Dialog", "Description:"))
        self.label_4.setText(_translate("Dialog", "Family:"))
        self.pushButton.setText(_translate("Dialog", "Add to Extenders"))
        self.pushButton_2.setText(_translate("Dialog", "Add to Catheters"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
