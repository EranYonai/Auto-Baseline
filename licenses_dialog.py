# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'licenses_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_licenses_Dialog(object):
    def setupUi(self, licenses_Dialog):
        licenses_Dialog.setObjectName("licenses_Dialog")
        licenses_Dialog.resize(468, 652)
        self.title = QtWidgets.QLabel(licenses_Dialog)
        self.title.setGeometry(QtCore.QRect(130, 15, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(20)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.comboBox = QtWidgets.QComboBox(licenses_Dialog)
        self.comboBox.setGeometry(QtCore.QRect(220, 65, 101, 22))
        self.comboBox.setToolTipDuration(-1)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(licenses_Dialog)
        self.label.setGeometry(QtCore.QRect(100, 65, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.merge = QtWidgets.QCheckBox(licenses_Dialog)
        self.merge.setGeometry(QtCore.QRect(10, 95, 171, 20))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(9)
        self.merge.setFont(font)
        self.merge.setObjectName("merge")
        self.sound = QtWidgets.QCheckBox(licenses_Dialog)
        self.sound.setGeometry(QtCore.QRect(10, 125, 171, 20))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(9)
        self.sound.setFont(font)
        self.sound.setObjectName("sound")
        self.paso = QtWidgets.QCheckBox(licenses_Dialog)
        self.paso.setGeometry(QtCore.QRect(10, 155, 171, 20))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(9)
        self.paso.setFont(font)
        self.paso.setObjectName("paso")
        self.nivu = QtWidgets.QCheckBox(licenses_Dialog)
        self.nivu.setGeometry(QtCore.QRect(10, 265, 171, 20))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(9)
        self.nivu.setFont(font)
        self.nivu.setObjectName("nivu")
        self.rmt = QtWidgets.QCheckBox(licenses_Dialog)
        self.rmt.setGeometry(QtCore.QRect(10, 205, 171, 20))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(9)
        self.rmt.setFont(font)
        self.rmt.setObjectName("rmt")
        self.smarttouch = QtWidgets.QCheckBox(licenses_Dialog)
        self.smarttouch.setGeometry(QtCore.QRect(10, 235, 171, 20))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(9)
        self.smarttouch.setFont(font)
        self.smarttouch.setObjectName("smarttouch")
        self.dualmonitor = QtWidgets.QCheckBox(licenses_Dialog)
        self.dualmonitor.setGeometry(QtCore.QRect(10, 415, 171, 20))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(9)
        self.dualmonitor.setFont(font)
        self.dualmonitor.setObjectName("dualmonitor")
        self.visitag = QtWidgets.QCheckBox(licenses_Dialog)
        self.visitag.setGeometry(QtCore.QRect(10, 295, 171, 20))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(9)
        self.visitag.setFont(font)
        self.visitag.setObjectName("visitag")
        self.segct = QtWidgets.QCheckBox(licenses_Dialog)
        self.segct.setGeometry(QtCore.QRect(10, 355, 211, 20))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(9)
        self.segct.setFont(font)
        self.segct.setObjectName("segct")
        self.activation3 = QtWidgets.QCheckBox(licenses_Dialog)
        self.activation3.setGeometry(QtCore.QRect(10, 325, 171, 20))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(9)
        self.activation3.setFont(font)
        self.activation3.setObjectName("activation3")
        self.confidense = QtWidgets.QCheckBox(licenses_Dialog)
        self.confidense.setGeometry(QtCore.QRect(10, 445, 191, 20))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(9)
        self.confidense.setFont(font)
        self.confidense.setObjectName("confidense")
        self.segmr = QtWidgets.QCheckBox(licenses_Dialog)
        self.segmr.setGeometry(QtCore.QRect(10, 385, 211, 20))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(9)
        self.segmr.setFont(font)
        self.segmr.setObjectName("segmr")
        self.famdx = QtWidgets.QCheckBox(licenses_Dialog)
        self.famdx.setGeometry(QtCore.QRect(230, 155, 171, 20))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(9)
        self.famdx.setFont(font)
        self.famdx.setObjectName("famdx")
        self.finder = QtWidgets.QCheckBox(licenses_Dialog)
        self.finder.setGeometry(QtCore.QRect(10, 475, 171, 20))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(9)
        self.finder.setFont(font)
        self.finder.setObjectName("finder")
        self.replay = QtWidgets.QCheckBox(licenses_Dialog)
        self.replay.setGeometry(QtCore.QRect(230, 95, 171, 20))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(9)
        self.replay.setFont(font)
        self.replay.setObjectName("replay")
        self.visitagsur = QtWidgets.QCheckBox(licenses_Dialog)
        self.visitagsur.setGeometry(QtCore.QRect(10, 505, 171, 20))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(9)
        self.visitagsur.setFont(font)
        self.visitagsur.setObjectName("visitagsur")
        self.qdotmicro = QtWidgets.QCheckBox(licenses_Dialog)
        self.qdotmicro.setGeometry(QtCore.QRect(230, 185, 171, 20))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(9)
        self.qdotmicro.setFont(font)
        self.qdotmicro.setObjectName("qdotmicro")
        self.ripple = QtWidgets.QCheckBox(licenses_Dialog)
        self.ripple.setGeometry(QtCore.QRect(230, 125, 171, 20))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(9)
        self.ripple.setFont(font)
        self.ripple.setObjectName("ripple")
        self.visitagepu = QtWidgets.QCheckBox(licenses_Dialog)
        self.visitagepu.setGeometry(QtCore.QRect(230, 215, 201, 20))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(9)
        self.visitagepu.setFont(font)
        self.visitagepu.setObjectName("visitagepu")
        self.complex = QtWidgets.QCheckBox(licenses_Dialog)
        self.complex.setGeometry(QtCore.QRect(230, 275, 171, 20))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(9)
        self.complex.setFont(font)
        self.complex.setObjectName("complex")
        self.sia = QtWidgets.QCheckBox(licenses_Dialog)
        self.sia.setGeometry(QtCore.QRect(230, 245, 171, 20))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(9)
        self.sia.setFont(font)
        self.sia.setObjectName("sia")
        self.prime = QtWidgets.QCheckBox(licenses_Dialog)
        self.prime.setGeometry(QtCore.QRect(230, 335, 231, 20))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(9)
        self.prime.setFont(font)
        self.prime.setObjectName("prime")
        self.hdcolor = QtWidgets.QCheckBox(licenses_Dialog)
        self.hdcolor.setGeometry(QtCore.QRect(230, 305, 171, 20))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(9)
        self.hdcolor.setFont(font)
        self.hdcolor.setObjectName("hdcolor")
        self.activationv8 = QtWidgets.QCheckBox(licenses_Dialog)
        self.activationv8.setGeometry(QtCore.QRect(230, 455, 191, 20))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(9)
        self.activationv8.setFont(font)
        self.activationv8.setObjectName("activationv8")
        self.helios = QtWidgets.QCheckBox(licenses_Dialog)
        self.helios.setGeometry(QtCore.QRect(230, 365, 171, 20))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(9)
        self.helios.setFont(font)
        self.helios.setObjectName("helios")
        self.baloon = QtWidgets.QCheckBox(licenses_Dialog)
        self.baloon.setGeometry(QtCore.QRect(230, 395, 171, 20))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(9)
        self.baloon.setFont(font)
        self.baloon.setObjectName("baloon")
        self.soundfam = QtWidgets.QCheckBox(licenses_Dialog)
        self.soundfam.setGeometry(QtCore.QRect(230, 485, 171, 20))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(9)
        self.soundfam.setFont(font)
        self.soundfam.setObjectName("soundfam")
        self.activationv7p3 = QtWidgets.QCheckBox(licenses_Dialog)
        self.activationv7p3.setGeometry(QtCore.QRect(230, 515, 241, 20))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(9)
        self.activationv7p3.setFont(font)
        self.activationv7p3.setObjectName("activationv7p3")
        self.activationv7 = QtWidgets.QCheckBox(licenses_Dialog)
        self.activationv7.setGeometry(QtCore.QRect(230, 425, 191, 20))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(9)
        self.activationv7.setFont(font)
        self.activationv7.setObjectName("activationv7")
        self.activationv7sp2 = QtWidgets.QCheckBox(licenses_Dialog)
        self.activationv7sp2.setGeometry(QtCore.QRect(10, 535, 251, 20))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(9)
        self.activationv7sp2.setFont(font)
        self.activationv7sp2.setObjectName("activationv7sp2")
        self.ManualLine = QtWidgets.QLineEdit(licenses_Dialog)
        self.ManualLine.setGeometry(QtCore.QRect(215, 575, 113, 22))
        self.ManualLine.setObjectName("ManualLine")
        self.label_2 = QtWidgets.QLabel(licenses_Dialog)
        self.label_2.setGeometry(QtCore.QRect(115, 580, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.confirm_button = QtWidgets.QPushButton(licenses_Dialog)
        self.confirm_button.setGeometry(QtCore.QRect(180, 605, 93, 28))
        self.confirm_button.setObjectName("confirm_button")
        self.cafe_2 = QtWidgets.QCheckBox(licenses_Dialog)
        self.cafe_2.setGeometry(QtCore.QRect(10, 180, 171, 20))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(9)
        self.cafe_2.setFont(font)
        self.cafe_2.setObjectName("cafe_2")

        self.retranslateUi(licenses_Dialog)
        self.comboBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(licenses_Dialog)

    def retranslateUi(self, licenses_Dialog):
        _translate = QtCore.QCoreApplication.translate
        licenses_Dialog.setWindowTitle(_translate("licenses_Dialog", "Dialog"))
        self.title.setText(_translate("licenses_Dialog", "Licenses"))
        self.comboBox.setItemText(0, _translate("licenses_Dialog", "None"))
        self.comboBox.setItemText(1, _translate("licenses_Dialog", "Select All"))
        self.label.setText(_translate("licenses_Dialog", "Presets"))
        self.merge.setText(_translate("licenses_Dialog", "CARTOMERGE® PLUS"))
        self.sound.setText(_translate("licenses_Dialog", "CARTOSOUND®"))
        self.paso.setText(_translate("licenses_Dialog", "PASO™"))
        self.nivu.setText(_translate("licenses_Dialog", "CARTOUNIVU™"))
        self.rmt.setText(_translate("licenses_Dialog", "RMT"))
        self.smarttouch.setText(_translate("licenses_Dialog", "SMARTTOUCH™"))
        self.dualmonitor.setText(_translate("licenses_Dialog", "Dual-Monitor"))
        self.visitag.setText(_translate("licenses_Dialog", "VISITAG™"))
        self.segct.setText(_translate("licenses_Dialog", "CARTOSEG™ Extended CT"))
        self.activation3.setText(_translate("licenses_Dialog", "CARTO 3® Activation"))
        self.confidense.setText(_translate("licenses_Dialog", "CONFIDENSE™ Mapping"))
        self.segmr.setText(_translate("licenses_Dialog", "CARTOSEG™ Extended MR"))
        self.famdx.setText(_translate("licenses_Dialog", "FAM Dx"))
        self.finder.setText(_translate("licenses_Dialog", "CARTOFINDER™"))
        self.replay.setText(_translate("licenses_Dialog", "CARTOREPLAY™"))
        self.visitagsur.setText(_translate("licenses_Dialog", "VISITAG SURPOINT™"))
        self.qdotmicro.setText(_translate("licenses_Dialog", "CARTO QDOT MICRO™"))
        self.ripple.setText(_translate("licenses_Dialog", "Ripple Mapping"))
        self.visitagepu.setText(_translate("licenses_Dialog", "VISITAG SURPOINT™ EPU"))
        self.complex.setText(_translate("licenses_Dialog", "Complex Point"))
        self.sia.setText(_translate("licenses_Dialog", "SIA"))
        self.prime.setText(_translate("licenses_Dialog", "CARTO PRIME™ "))
        self.hdcolor.setText(_translate("licenses_Dialog", "HD Coloring"))
        self.activationv8.setText(_translate("licenses_Dialog", "CARTO 3 V8 Activation"))
        self.helios.setText(_translate("licenses_Dialog", "HELIOSTAR™"))
        self.baloon.setText(_translate("licenses_Dialog", "RF BALLOON"))
        self.soundfam.setText(_translate("licenses_Dialog", "SOUNDFAM™"))
        self.activationv7p3.setText(_translate("licenses_Dialog", "CARTO 3 V7 Phase 3 Activation"))
        self.activationv7.setText(_translate("licenses_Dialog", "CARTO 3 V7 Activation"))
        self.activationv7sp2.setText(_translate("licenses_Dialog", "CARTO 3 V7 Phase 2 SP Activation"))
        self.label_2.setText(_translate("licenses_Dialog", "Manually add:"))
        self.confirm_button.setText(_translate("licenses_Dialog", "Confirm"))
        self.cafe_2.setText(_translate("licenses_Dialog", "CAFE"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    licenses_Dialog = QtWidgets.QDialog()
    ui = Ui_licenses_Dialog()
    ui.setupUi(licenses_Dialog)
    licenses_Dialog.show()
    sys.exit(app.exec_())
