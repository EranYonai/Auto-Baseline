import PyQt5
import qdarkstyle
import sys
from selenium import webdriver
import xml.etree.ElementTree as ET
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtWidgets import QListWidget
from Forms.MainWindowBig import Ui_MainWindow
from Forms.system_dialog import Ui_system_dialog
from Forms.ultrasound_dialog import Ui_Dialog as Ui_ultrasound_Dialog
from Forms.workstation_dialog import Ui_workstation_Dialog
from Forms.licenses_dialog import Ui_licenses_Dialog
from Forms.catheters_Dialog import Ui_Dialog as catheters_Ui
from Forms.stockert_dialog import Ui_Dialog as stockert_Ui
from Forms.smartablate_dialog import Ui_Dialog as smartablate_Ui
from Forms.ngen_dialog import Ui_Dialog as ngen_Ui
from Forms.nmarq_dialog import Ui_Dialog as nmarq_Ui
from Forms.pacer_dialog import Ui_Dialog as pacer_Ui
from Forms.qdotdongle_dialog import Ui_Dialog as qdotdongle_Ui
from Forms.epu_dialog import Ui_Dialog as epu_Ui
from Forms.demo_dialog import Ui_Dialog as demo_Ui
from Forms.printer_dialog import Ui_Dialog as printer_Ui
from Forms.CatalogHelper_details import Ui_Dialog as cathelp_detUi
from Forms.CatalogHelper_main import Ui_Dialog as cathelp_mainUi
from Forms.spu_dialog import Ui_Dialog as spu_Ui

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__(parent=None)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.reset_allFields()
        self.filePath_configured = False #In order to know if filePath was already choosen, and won't open everytime
        self.hideThings() #A function that hides all of the buttons and progress bars. 
        self.catheterList_info = [] #List that stores Catheters. DIDN'T USE it so far. Because it'll be easier from export function to loop through the current items of catheter List.
        self.wsList = self.createWindowsLists("ws") # Saves instances of Workstation_Dialog() in a list
        self.sysList = self.createWindowsLists("sys") # Saves instances of System_Dialog() in a list
        self.ultraList = self.createWindowsLists("ultra") # Saves instances of Ultrasound_Dialog() in a list
        self.stockertList = self.createWindowsLists("stockert")
        self.smartablateList = self.createWindowsLists("smartablate")
        self.ngenList = self.createWindowsLists("ngen")
        self.nmarqList = self.createWindowsLists("nmarq")
        self.pacerList = self.createWindowsLists("pacer")
        self.qdotdongleList = self.createWindowsLists("qdotdongle")
        self.printerList = self.createWindowsLists("printer")
        self.epuList = self.createWindowsLists("epu")
        self.demoList = self.createWindowsLists("demo")
        self.bardList = self.createWindowsLists('bard')
        self.spuList = self.createWindowsLists("spu")
        self.ui.actionWork_Station.triggered.connect(lambda: self.showThings("workstation")) #Calls function "showThings" that shows the sent item
        self.ui.actionRF_Generator_Stockert.triggered.connect(lambda: self.showThings("stockert")) #Calls function "showThings" that shows the sent item
        self.ui.actionRF_Generator_Smart_Ablate.triggered.connect(lambda: self.showThings("smartablate")) #Calls function "showThings" that shows the sent item
        self.ui.actionRF_Generator_nGen.triggered.connect(lambda: self.showThings("ngen")) #Calls function "showThings" that shows the sent item
        self.ui.actionRF_Generator_nMARQ.triggered.connect(lambda: self.showThings("nmark")) #Calls function "showThings" that shows the sent item
        self.ui.actionUltraSound.triggered.connect(lambda: self.showThings("ultra")) #Calls function "showThings" that shows the sent item
        self.ui.actionPacer.triggered.connect(lambda: self.showThings("pacer")) #Calls function "showThings" that shows the sent item
        self.ui.actionSystem.triggered.connect(lambda: self.showThings("system")) #Calls function "showThings" that shows the sent item
        self.ui.actionPrinter.triggered.connect(lambda: self.showThings("printer")) #Calls function "showThings" that shows the sent item
        self.ui.actionQDOT_Dongle.triggered.connect(lambda: self.showThings("qdotdongle")) #Calls function "showThings" that shows the sent item
        self.ui.actionDemo_Laptop.triggered.connect(lambda: self.showThings("demo")) #Calls function "showThings" that shows the sent item
        self.ui.actionEPU_Device.triggered.connect(lambda: self.showThings("epu")) #Calls function "showThings" that shows the sent item
        self.ui.actionCatalog_Helper.triggered.connect(self.catalogHelp)
        self.ui.workstation_win_1.clicked.connect(lambda: self.open_workstationDialog(0)) #For each WS number there's a specific workstation dialog
        self.ui.workstation_win_2.clicked.connect(lambda: self.open_workstationDialog(1))
        self.ui.workstation_win_3.clicked.connect(lambda: self.open_workstationDialog(2))
        self.ui.workstation_win_4.clicked.connect(lambda: self.open_workstationDialog(3))
        self.ui.workstation_win_5.clicked.connect(lambda: self.open_workstationDialog(4))
        self.ui.workstation_win_6.clicked.connect(lambda: self.open_workstationDialog(5))
        self.ui.workstation_win_7.clicked.connect(lambda: self.open_workstationDialog(6))
        self.ui.workstation_win_8.clicked.connect(lambda: self.open_workstationDialog(7))
        self.ui.system_win_1.clicked.connect(lambda: self.open_systemDialog(0)) #For each System number there's a specific system dialog
        self.ui.system_win_2.clicked.connect(lambda: self.open_systemDialog(1))
        self.ui.system_win_3.clicked.connect(lambda: self.open_systemDialog(2))
        self.ui.system_win_4.clicked.connect(lambda: self.open_systemDialog(3))
        self.ui.system_win_5.clicked.connect(lambda: self.open_systemDialog(4))
        self.ui.system_win_6.clicked.connect(lambda: self.open_systemDialog(5))
        self.ui.system_win_7.clicked.connect(lambda: self.open_systemDialog(6))
        self.ui.system_win_8.clicked.connect(lambda: self.open_systemDialog(7))
        self.ui.ultra_win_1.clicked.connect(lambda: self.open_ultrasoundDialog(0)) #For each U/S system number there's a spcific ultrasound dialog
        self.ui.ultra_win_2.clicked.connect(lambda: self.open_ultrasoundDialog(1))
        self.ui.ultra_win_3.clicked.connect(lambda: self.open_ultrasoundDialog(2))
        self.ui.ultra_win_4.clicked.connect(lambda: self.open_ultrasoundDialog(3))
        self.ui.ultra_win_5.clicked.connect(lambda: self.open_ultrasoundDialog(4))
        self.ui.ultra_win_6.clicked.connect(lambda: self.open_ultrasoundDialog(5))
        self.ui.ultra_win_7.clicked.connect(lambda: self.open_ultrasoundDialog(6))
        self.ui.ultra_win_8.clicked.connect(lambda: self.open_ultrasoundDialog(7))
        self.ui.catheter_1.clicked.connect(lambda: self.open_cathetersDialog(0)) #Upon pressing add catheter -> opening Catheter dialog. User inserts MFG and family of such
        self.ui.catheter_2.clicked.connect(lambda: self.remove_catheter(0)) #Upon pressing remove catheter -> deletes the selected item. Can store the item if wanted.
        self.ui.extender_b.clicked.connect(lambda: self.open_cathetersDialog(1))
        self.ui.remove_extender_b.clicked.connect(lambda: self.remove_catheter(1))
        self.ui.stockert_win_1.clicked.connect(lambda: self.open_stockertDialog(0))#For each System number there's a specific stockert dialog
        self.ui.stockert_win_2.clicked.connect(lambda: self.open_stockertDialog(1))
        self.ui.smartablate_win_1.clicked.connect(lambda: self.open_smartablateDialog(0))#For each System number there's a specific smartablate dialog
        self.ui.smartablate_win_2.clicked.connect(lambda: self.open_smartablateDialog(1))
        self.ui.smartablate_win_3.clicked.connect(lambda: self.open_smartablateDialog(2))
        self.ui.ngen_win_1.clicked.connect(lambda: self.open_ngenDialog(0))#For each System number there's a specific ngen dialog
        self.ui.ngen_win_2.clicked.connect(lambda: self.open_ngenDialog(1))
        self.ui.ngen_win_3.clicked.connect(lambda: self.open_ngenDialog(2))
        self.ui.nmark_win_1.clicked.connect(lambda: self.open_nmarqDialog(0))#For each System number there's a specific nmarq dialog
        self.ui.nmark_win_2.clicked.connect(lambda: self.open_nmarqDialog(1))
        self.ui.pacer_win.clicked.connect(lambda: self.open_pacerDialog(0))#For each System number there's a specific pacer dialog
        self.ui.qdot_win.clicked.connect(lambda: self.open_qdotdongleDialog(0))#For each System number there's a specific qdotdongle dialog
        self.ui.epu_win.clicked.connect(lambda: self.open_epuDialog(0))#For each System number there's a specific epu dialog
        self.ui.printer_win.clicked.connect(lambda: self.open_printerDialog(0))#For each System number there's a specific printer dialog
        self.ui.demo_win.clicked.connect(lambda: self.open_demoDialog(0))#For each System number there's a specific demo dialog
        self.ui.demo_win_2.clicked.connect(lambda: self.open_demoDialog(1))
        self.ui.demo_win_3.clicked.connect(lambda: self.open_demoDialog(2))
        self.ui.actionBard.triggered.connect(lambda: self.experimentalWarning("notimp"))
        self.ui.actionSPU.triggered.connect(lambda: self.showThings("spu"))
        self.ui.spu_win.clicked.connect(lambda: self.open_SPUDialog(0))
        self.ui.export_button.clicked.connect(self.exportTXT) #Upon pressing "export" the program will append it's current content to a .txt file
        self.ui.import_button.clicked.connect(self.importButton) #This is the next step of the program, upon importing txt file
        self.experimentalWarning("beta")
    def hideThings(self):
        self.ui.workstation_win_1.hide()
        self.ui.work_bar_1.hide()
        self.ui.workstation_win_2.hide()
        self.ui.work_bar_2.hide()
        self.ui.workstation_win_3.hide()
        self.ui.work_bar_3.hide()
        self.ui.workstation_win_4.hide()
        self.ui.work_bar_4.hide()
        self.ui.workstation_win_5.hide()
        self.ui.work_bar_5.hide()
        self.ui.workstation_win_6.hide()
        self.ui.work_bar_6.hide()
        self.ui.workstation_win_7.hide()
        self.ui.work_bar_7.hide()
        self.ui.workstation_win_8.hide()
        self.ui.work_bar_8.hide()
        self.ui.system_win_1.hide()
        self.ui.system_bar_1.hide()
        self.ui.system_win_2.hide()
        self.ui.system_bar_2.hide()
        self.ui.system_win_3.hide()
        self.ui.system_bar_3.hide()
        self.ui.system_win_4.hide()
        self.ui.system_bar_4.hide()
        self.ui.system_win_5.hide()
        self.ui.system_bar_5.hide()
        self.ui.system_win_6.hide()
        self.ui.system_bar_6.hide()
        self.ui.system_win_7.hide()
        self.ui.system_bar_7.hide()
        self.ui.system_win_8.hide()
        self.ui.system_bar_8.hide()
        self.ui.ultra_win_1.hide()
        self.ui.ultra_bar_1.hide()
        self.ui.ultra_win_2.hide()
        self.ui.ultra_bar_2.hide()
        self.ui.ultra_win_3.hide()
        self.ui.ultra_bar_3.hide()
        self.ui.ultra_win_4.hide()
        self.ui.ultra_bar_4.hide()
        self.ui.ultra_win_5.hide()
        self.ui.ultra_bar_5.hide()
        self.ui.ultra_win_6.hide()
        self.ui.ultra_bar_6.hide()
        self.ui.ultra_win_7.hide()
        self.ui.ultra_bar_7.hide()
        self.ui.ultra_win_8.hide()
        self.ui.ultra_bar_8.hide()
        self.ui.stockert_win_1.hide()
        self.ui.stockert_bar_1.hide()
        self.ui.stockert_win_2.hide()
        self.ui.stockert_bar_2.hide()
        self.ui.smartablate_win_1.hide()
        self.ui.smartablate_bar_1.hide()
        self.ui.smartablate_win_2.hide()
        self.ui.smartablate_bar_2.hide()
        self.ui.smartablate_win_3.hide()
        self.ui.smartablate_bar_3.hide()
        self.ui.ngen_win_1.hide()
        self.ui.ngen_bar_1.hide()
        self.ui.ngen_win_2.hide()
        self.ui.ngen_bar_2.hide()
        self.ui.ngen_win_3.hide()
        self.ui.ngen_bar_3.hide()
        self.ui.nmark_win_1.hide()
        self.ui.nmark_bar_1.hide()
        self.ui.nmark_win_2.hide()
        self.ui.nmark_bar_2.hide()
        self.ui.pacer_win.hide()
        self.ui.pacer_bar.hide()
        self.ui.qdot_win.hide()
        self.ui.qdot_bar.hide()
        self.ui.printer_win.hide()
        self.ui.printer_bar.hide()
        self.ui.epu_win.hide()
        self.ui.epu_bar.hide()
        self.ui.demo_win.hide()
        self.ui.demo_bar.hide()
        self.ui.demo_win_2.hide()
        self.ui.demo_bar_2.hide()
        self.ui.demo_win_3.hide()
        self.ui.demo_bar_3.hide()
        self.ui.bar_win.hide()
        self.ui.bard_bar.hide()
        self.ui.spu_bar.hide()
        self.ui.spu_win.hide()
    def createWindowsLists(self, kind):
        if (kind == "ws"):
            wsList = [Workstation_Dialog(),Workstation_Dialog(),Workstation_Dialog(),Workstation_Dialog(),Workstation_Dialog(),Workstation_Dialog(),Workstation_Dialog(),Workstation_Dialog()]
            return wsList
        if (kind == "sys"):
            sysList = [System_Dialog(),System_Dialog(),System_Dialog(),System_Dialog(),System_Dialog(),System_Dialog(),System_Dialog(),System_Dialog()]
            return sysList
        if (kind == "stockert"):
            stockertList = [Stockert_Dialog(),Stockert_Dialog()]
            return stockertList
        if (kind == "ultra"):
            ultraList = [Ultrasound_Dialog(),Ultrasound_Dialog(),Ultrasound_Dialog(),Ultrasound_Dialog(),Ultrasound_Dialog(),Ultrasound_Dialog(),Ultrasound_Dialog(),Ultrasound_Dialog()]
            return ultraList
        if (kind == "smartablate"):
            smartablateList = [SmartAblate_Dialog(),SmartAblate_Dialog(),SmartAblate_Dialog()]
            return smartablateList
        if (kind == "ngen"):
            ngenList = [nGEN_Dialog(),nGEN_Dialog(),nGEN_Dialog()]
            return ngenList
        if (kind == "nmarq"):
            nmarqList = [nMARQ_Dialog(),nMARQ_Dialog()]
            return nmarqList
        if (kind == "pacer"):
            pacerList = [Pacer_Dialog()]
            return pacerList
        if (kind == "qdotdongle"):
            qdotdongleList = [qDotDongle_Dialog()]
            return qdotdongleList
        if (kind == "printer"):
            printerList = [Printer_Dialog()]
            return printerList
        if (kind == "epu"):
            epuList = [epu_Dialog()]
            return epuList
        if (kind == "demo"):
            demoList = [Demo_Dialog(),Demo_Dialog(),Demo_Dialog()]
            return demoList
        if (kind == 'bard'):
            bardList = [Bard_Dialog()]
            return bardList
        if (kind == 'spu'):
            spuList = [SPU_Dialog()]
            return spuList
        if (kind == "all"):
            self.wsList = [Workstation_Dialog(),Workstation_Dialog(),Workstation_Dialog(),Workstation_Dialog(),Workstation_Dialog(),Workstation_Dialog(),Workstation_Dialog(),Workstation_Dialog()]
            self.sysList = [System_Dialog(),System_Dialog(),System_Dialog(),System_Dialog(),System_Dialog(),System_Dialog(),System_Dialog(),System_Dialog()]
            self.ultraList =  [Ultrasound_Dialog(),Ultrasound_Dialog(),Ultrasound_Dialog(),Ultrasound_Dialog(),Ultrasound_Dialog(),Ultrasound_Dialog(),Ultrasound_Dialog(),Ultrasound_Dialog()]
            self.stockertList = [Stockert_Dialog(),Stockert_Dialog()]
            self.smartablateList = [SmartAblate_Dialog(),SmartAblate_Dialog(),SmartAblate_Dialog()]
            self.ngenList = [nGEN_Dialog(),nGEN_Dialog(),nGEN_Dialog()]
            self.nmarqList = [nMARQ_Dialog(),nMARQ_Dialog()]
            self.pacerList = [Pacer_Dialog()]
            self.qdotdongleList = [qDotDongle_Dialog()]
            self.printerList = [Printer_Dialog()]
            self.epuList = [epu_Dialog()]
            self.demoList = [Demo_Dialog(),Demo_Dialog(),Demo_Dialog()]
            self.bardList = [Bard_Dialog()]
            self.spuList = [SPU_Dialog()]
    def reset_allFields(self):
        self.workCount, self.stockertCount, self.smartablateCount, self.ngenCount, self.nmarqCount, self.ultraCount, self.systemCount, self.demoCount, self.pacerCount, self.qdotdongleCount, self.printerCount, self.epuCount, self.spuCount, self.bardCount  = 0,0,0,0,0,0,0,0,0,0,0,0,0,0 #Declare counts in order to know how much of each.
        self.workstationOpened = [False,False,False,False,False,False,False,False] # List of bool values in order to know if window was opened before.
        self.systemOpened = [False,False,False,False,False,False,False,False] # List of bool values in order to know if window was opened before.
        self.ultrasoundOpened = [False,False,False,False,False,False,False,False] # List of bool values in order to know if window was opened before.
        self.stockertOpened = [False, False]
        self.smartablateOpened = [False, False, False]
        self.ngenOpened = [False, False, False]
        self.nmarqOpened = [False, False]
        self.pacerOpened = [False]
        self.qdotdongleOpened = [False]
        self.printerOpened = [False]
        self.epuOpened = [False]
        self.demoOpened = [False,False,False]
        self.bardOpened = [False]
        self.spuOpened = [False]
        self.wsList_info = [[],[],[],[],[],[],[],[],[]] #List stores WS info
        self.ultraList_info = [[],[],[],[],[],[],[],[]] #List stores Ultrasound info
        self.sysList_info = [[],[],[],[],[],[],[],[]] #List stores System info
        self.smartablate_info = [[],[],[]]
        self.stockertList_info = [[],[]]
        self.ngenlist_info = [[],[],[]]
        self.nmarqlist_info = [[],[]]
        self.pacerlist_info = [[]]
        self.qdotdonglelist_info = [[]]
        self.printerlist_info = [[]]
        self.epulist_info = [[]]
        self.demolist_info = [[],[],[]]
        self.spuList_info = [[]]
        self.bardList_info = [[]]
        self.header = ""
        self.ui.catheter_list.clear()
        self.ui.extender_list_2.clear()
    def reset_progressbars(self):
        self.ui.work_bar_1.setValue(0)
        self.ui.work_bar_2.setValue(0)
        self.ui.work_bar_3.setValue(0)
        self.ui.work_bar_4.setValue(0)
        self.ui.work_bar_5.setValue(0)
        self.ui.work_bar_6.setValue(0)
        self.ui.work_bar_7.setValue(0)
        self.ui.work_bar_8.setValue(0)
        self.ui.system_bar_1.setValue(0)
        self.ui.system_bar_2.setValue(0)
        self.ui.system_bar_3.setValue(0)
        self.ui.system_bar_4.setValue(0)
        self.ui.system_bar_5.setValue(0)
        self.ui.system_bar_6.setValue(0)
        self.ui.system_bar_7.setValue(0)
        self.ui.system_bar_8.setValue(0)
        self.ui.ultra_bar_1.setValue(0)
        self.ui.ultra_bar_2.setValue(0)
        self.ui.ultra_bar_3.setValue(0)
        self.ui.ultra_bar_4.setValue(0)
        self.ui.ultra_bar_5.setValue(0)
        self.ui.ultra_bar_6.setValue(0)
        self.ui.ultra_bar_7.setValue(0)
        self.ui.ultra_bar_8.setValue(0)
        self.ui.stockert_bar_1.setValue(0)
        self.ui.stockert_bar_2.setValue(0)
        self.ui.smartablate_bar_1.setValue(0)
        self.ui.smartablate_bar_2.setValue(0)
        self.ui.smartablate_bar_3.setValue(0)
        self.ui.ngen_bar_1.setValue(0)
        self.ui.ngen_bar_2.setValue(0)
        self.ui.ngen_bar_3.setValue(0)
        self.ui.nmark_bar_1.setValue(0)
        self.ui.nmark_bar_2.setValue(0)
        self.ui.pacer_bar.setValue(0)
        self.ui.qdot_bar.setValue(0)
        self.ui.printer_bar.setValue(0)
        self.ui.epu_bar.setValue(0)
        self.ui.demo_bar.setValue(0)
        self.ui.demo_bar_2.setValue(0)
        self.ui.demo_bar_3.setValue(0)
    def check_progressbars(self):
        #I can also check if for each xxxOpened the progress bars.value is > 0
        state = True
        for ws in self.workstationOpened:
            if ws:
                state = False
        for sys in self.systemOpened:
            if sys:
                state = False
        for ult in self.ultrasoundOpened:
            if ult:
                state = False
        for sto in self.stockertOpened:
            if sto:
                state = False
        for sma in self.smartablateOpened:
            if sma:
                state = False
        for ngen in self.ngenOpened:
            if ngen:
                state = False
        for nmarq in self.nmarqOpened:
            if nmarq:
                state = False
        for pac in self.pacerOpened:
            if pac:
                state = False
        for qdot in self.qdotdongleOpened:
            if qdot:
                state = False
        for pri in self.printerOpened:
            if pri:
                state = False
        for epu in self.epuOpened:
            if epu:
                state = False
        for dem in self.demoOpened:
            if dem:
                state = False
        for spu in self.spuOpened:
            if spu:
                state = False
        for bard in self.bardOpened:
            if bard:
                state = False
        return state #if any window opened return False, if not, return True.
    def catalogHelp(self):
        self.experimentalWarning("experimental")
        catWin = CatalogHelper_Dialog(self) #Inheritance -> Passing MainWindow (self) as an argument
        catWin.exec_()
    def showThings(self, show):
        if show == "workstation":
            self.ui.additional_tabs.setCurrentIndex(1)
            self.workCount += 1
            if self.workCount == 1:
                self.ui.workstation_win_1.show()
                self.ui.work_bar_1.show()
            if self.workCount == 2:
                self.ui.workstation_win_2.show()
                self.ui.work_bar_2.show()
            if self.workCount == 3:
                self.ui.workstation_win_3.show()
                self.ui.work_bar_3.show()
            if self.workCount == 4:
                self.ui.workstation_win_4.show()
                self.ui.work_bar_4.show()
            if self.workCount == 5:
                self.ui.workstation_win_5.show()
                self.ui.work_bar_5.show()
            if self.workCount == 6:
                self.ui.workstation_win_6.show()
                self.ui.work_bar_6.show()
            if self.workCount == 7:
                self.ui.workstation_win_7.show()
                self.ui.work_bar_7.show()
            if self.workCount == 8:
                self.ui.workstation_win_8.show()
                self.ui.work_bar_8.show()
            if self.workCount > 8:
                notimplemented = QtWidgets.QMessageBox()
                notimplemented.setText(
                    "You've reached maximum number of Workstations")
                notimplemented.setWindowTitle("Work in Progress")
                notimplemented.exec_()
                self.workCount = 8
        if show == "stockert":
            self.ui.additional_tabs.setCurrentIndex(2)
            self.stockertCount += 1
            if self.stockertCount == 1:
                self.ui.stockert_win_1.show()
                self.ui.stockert_bar_1.show()
            if self.stockertCount == 2:
                self.ui.stockert_win_2.show()
                self.ui.stockert_bar_2.show()
            if self.stockertCount > 2:
                notimplemented = QtWidgets.QMessageBox()
                notimplemented.setText(
                    "You've reached maximum number of Stockert")
                notimplemented.setWindowTitle("Work in Progress")
                notimplemented.exec_()
                self.stockertCount = 2
        if show == "smartablate":
            self.ui.additional_tabs.setCurrentIndex(2)
            self.smartablateCount += 1
            if self.smartablateCount == 1:
                self.ui.smartablate_win_1.show()
                self.ui.smartablate_bar_1.show()
            if self.smartablateCount == 2:
                self.ui.smartablate_win_2.show()
                self.ui.smartablate_bar_2.show()
            if self.smartablateCount == 3:
                self.ui.smartablate_win_3.show()
                self.ui.smartablate_bar_3.show()
            if self.smartablateCount > 3:
                notimplemented = QtWidgets.QMessageBox()
                notimplemented.setText(
                    "You've reached maximum number of SmartAblate")
                notimplemented.setWindowTitle("Work in Progress")
                notimplemented.exec_()
                self.smartablateCount = 3
        if show == "ngen":
            self.ui.additional_tabs.setCurrentIndex(2)
            self.ngenCount += 1
            if self.ngenCount == 1:
                self.ui.ngen_win_1.show()
                self.ui.ngen_bar_1.show()
            if self.ngenCount == 2:
                self.ui.ngen_win_2.show()
                self.ui.ngen_bar_2.show()
            if self.ngenCount == 3:
                self.ui.ngen_win_3.show()
                self.ui.ngen_bar_3.show()
            if self.ngenCount > 3:
                notimplemented = QtWidgets.QMessageBox()
                notimplemented.setText(
                    "You've reached maximum number of nGENs")
                notimplemented.setWindowTitle("Work in Progress")
                notimplemented.exec_()
                self.ngenCount = 3
        if show == "nmark":
            self.ui.additional_tabs.setCurrentIndex(2)
            self.nmarqCount += 1
            if self.nmarqCount == 1:
                self.ui.nmark_win_1.show()
                self.ui.nmark_bar_1.show()
            if self.nmarqCount == 2:
                self.ui.nmark_win_2.show()
                self.ui.nmark_bar_2.show()
            if self.nmarqCount > 2:
                notimplemented = QtWidgets.QMessageBox()
                notimplemented.setText(
                    "You've reached maximum number of nMARQs")
                notimplemented.setWindowTitle("Work in Progress")
                notimplemented.exec_()
                self.nmarqCount = 2
        if show == "ultra":
            self.ui.additional_tabs.setCurrentIndex(3)
            self.ultraCount += 1
            if self.ultraCount == 1:
                self.ui.ultra_win_1.show()
                self.ui.ultra_bar_1.show()
            if self.ultraCount == 2:
                self.ui.ultra_win_2.show()
                self.ui.ultra_bar_2.show()
            if self.ultraCount == 3:
                self.ui.ultra_win_3.show()
                self.ui.ultra_bar_3.show()
            if self.ultraCount == 4:
                self.ui.ultra_win_4.show()
                self.ui.ultra_bar_4.show()
            if self.ultraCount == 5:
                self.ui.ultra_win_5.show()
                self.ui.ultra_bar_5.show()
            if self.ultraCount == 6:
                self.ui.ultra_win_6.show()
                self.ui.ultra_bar_6.show()
            if self.ultraCount == 7:
                self.ui.ultra_win_7.show()
                self.ui.ultra_bar_7.show()
            if self.ultraCount == 8:
                self.ui.ultra_win_8.show()
                self.ui.ultra_bar_8.show()
            if self.ultraCount > 8:
                notimplemented = QtWidgets.QMessageBox()
                notimplemented.setText(
                    "You've reached maximum number of Ultrasounds")
                notimplemented.setWindowTitle("Work in Progress")
                notimplemented.exec_()
                self.ultraCount = 8
        if show == "pacer":
            self.pacerCount +=1
            self.ui.additional_tabs.setCurrentIndex(5)
            if self.pacerCount == 1:
                self.ui.pacer_win.show()
                self.ui.pacer_bar.show()
            if self.pacerCount > 1:
                notimplemented = QtWidgets.QMessageBox()
                notimplemented.setText(
                    "You've reached maximum number of Pacers")
                notimplemented.setWindowTitle("Work in Progress")
                notimplemented.exec_()
                self.pacerCount = 1
        if show == "system":
            self.ui.additional_tabs.setCurrentIndex(0)
            self.systemCount +=1
            if self.systemCount == 1:
                self.ui.system_win_1.show()
                self.ui.system_bar_1.show()
            if self.systemCount == 2:
                self.ui.system_win_2.show()
                self.ui.system_bar_2.show()
            if self.systemCount == 3:
                self.ui.system_win_3.show()
                self.ui.system_bar_3.show()
            if self.systemCount == 4:
                self.ui.system_win_4.show()
                self.ui.system_bar_4.show()
            if self.systemCount == 5:
                self.ui.system_win_5.show()
                self.ui.system_bar_5.show()
            if self.systemCount == 6:
                self.ui.system_win_6.show()
                self.ui.system_bar_6.show()
            if self.systemCount == 7:
                self.ui.system_win_7.show()
                self.ui.system_bar_7.show()
            if self.systemCount == 8:
                self.ui.system_win_8.show()
                self.ui.system_bar_8.show()
            if self.systemCount > 8:
                notimplemented = QtWidgets.QMessageBox()
                notimplemented.setText(
                    "You've reached maximum number of Systems")
                notimplemented.setWindowTitle("Work in Progress")
                notimplemented.exec_()
                self.systemCount = 8
        if show == "qdotdongle":
            self.qdotdongleCount += 1
            self.ui.additional_tabs.setCurrentIndex(5)
            if self.qdotdongleCount == 1:
                self.ui.qdot_win.show()
                self.ui.qdot_bar.show()
            if self.qdotdongleCount > 1:
                notimplemented = QtWidgets.QMessageBox()
                notimplemented.setText(
                    "You've reached maximum number of QDOT Dongles")
                notimplemented.setWindowTitle("Work in Progress")
                notimplemented.exec_()
                self.qdotdongleCount = 1
        if show == "printer":
            self.printerCount += 1
            self.ui.additional_tabs.setCurrentIndex(5)
            if self.printerCount == 1:
                self.ui.printer_win.show()
                self.ui.printer_bar.show()
            if self.printerCount > 1:
                notimplemented = QtWidgets.QMessageBox()
                notimplemented.setText(
                    "You've reached maximum number of Printers")
                notimplemented.setWindowTitle("Work in Progress")
                notimplemented.exec_()
                self.printerCount =1
        if show == "epu":
            self.epuCount += 1
            self.ui.additional_tabs.setCurrentIndex(5)
            if self.epuCount == 1:
                self.ui.epu_win.show()
                self.ui.epu_bar.show()
            if self.epuCount > 1:
                notimplemented = QtWidgets.QMessageBox()
                notimplemented.setText(
                    "You've reached maximum number of EPUs")
                notimplemented.setWindowTitle("Work in Progress")
                notimplemented.exec_()
                self.epuCount = 1
        if show == "spu":
            self.spuCount += 1
            self.ui.additional_tabs.setCurrentIndex(5)
            if self.spuCount == 1:
                self.ui.spu_win.show()
                self.ui.spu_bar.show()
            if self.spuCount > 1:
                notimplemented = QtWidgets.QMessageBox()
                notimplemented.setText(
                    "You've reached maximum number of SPUs")
                notimplemented.setWindowTitle("Work in Progress")
                notimplemented.exec_()
                self.spuCount = 1
        if show == "demo":
            self.ui.additional_tabs.setCurrentIndex(5)
            self.demoCount +=1
            if self.demoCount == 1:
                self.ui.demo_win.show()
                self.ui.demo_bar.show()
            if self.demoCount == 2:
                self.ui.demo_win_2.show()
                self.ui.demo_bar_2.show()
            if self.demoCount == 3:
                self.ui.demo_bar_3.show()
                self.ui.demo_win_3.show()
            if self.demoCount > 3:
                notimplemented = QtWidgets.QMessageBox()
                notimplemented.setText(
                    "You've reached maximum number of Laptops")
                notimplemented.setWindowTitle("Work in Progress")
                notimplemented.exec()
                self.demoCount = 3
    def updateProgressbars(self, type, number):
        #This function gets type of window and the number of the window (in order to extract info from typeList_info)
        #And iterates through the values if > 0 adds to count and update the matching progress bar
        if (type == "ws"):
            count = 0
            for x in self.wsList_info[number]:
                if len(x) != 0:
                    count += 1
            count -= 2 #Minus value of solios check and Performance
            if number == 0:
                self.ui.work_bar_1.setValue(count)
            if number == 1:
                self.ui.work_bar_2.setValue(count)
            if number == 2:
                self.ui.work_bar_3.setValue(count)
            if number == 3:
                self.ui.work_bar_4.setValue(count)
            if number == 4:
                self.ui.work_bar_5.setValue(count)
            if number == 5:
                self.ui.work_bar_6.setValue(count)
            if number == 6:
                self.ui.work_bar_7.setValue(count)
            if number == 7:
                 self.ui.work_bar_8.setValue(count)
        if (type == "us"):
            count = 0
            for x in self.ultraList_info[number]:
                if len(x) != 0:
                    count += 1
            if number == 0:
                self.ui.ultra_bar_1.setValue(count)
            if number == 1:
                self.ui.ultra_bar_2.setValue(count)
            if number == 2:
                self.ui.ultra_bar_3.setValue(count)
            if number == 3:
                self.ui.ultra_bar_4.setValue(count)
            if number == 4:
                self.ui.ultra_bar_5.setValue(count)
            if number == 5:
                self.ui.ultra_bar_6.setValue(count)
            if number == 6:
                self.ui.ultra_bar_7.setValue(count)
            if number == 7:
                self.ui.ultra_bar_8.setValue(count)
        if (type == "sys"):
            count = 0
            for x in self.sysList_info[number]:
                if len(x) != 0:
                    count += 1
            if number == 0:
                self.ui.system_bar_1.setValue(count)
            if number == 1:
                self.ui.system_bar_2.setValue(count)
            if number == 2:
                self.ui.system_bar_3.setValue(count)
            if number == 3:
                self.ui.system_bar_4.setValue(count)
            if number == 4:
                self.ui.system_bar_5.setValue(count)
            if number == 5:
                self.ui.system_bar_6.setValue(count)
            if number == 6:
                self.ui.system_bar_7.setValue(count)
            if number == 7:
                self.ui.system_bar_8.setValue(count)
        if (type == "stockert"):
            count = 0
            for x in self.stockertList_info[number]:
                if len(x) != 0:
                    count += 1
            if number == 0:
                self.ui.stockert_bar_1.setValue(count)
            if number == 1:
                self.ui.stockert_bar_2.setValue(count)
        if (type == "smartablate"):
            count = 0
            for x in self.smartablate_info[number]:
                if len(x) != 0:
                    count+=1
            if number == 0:
                self.ui.smartablate_bar_1.setValue(count)
            if number == 1:
                self.ui.smartablate_bar_2.setValue(count)
            if number == 2:
                self.ui.smartablate_bar_3.setValue(count)
        if (type == "ngen"):
            count = 0
            for x in self.ngenlist_info[number]:
                if len(x) != 0:
                    count+=1
            if number == 0:
                self.ui.ngen_bar_1.setValue(count)
            if number == 1:
                self.ui.ngen_bar_2.setValue(count)
            if number == 2:
                self.ui.ngen_bar_3.setValue(count)
        if (type == "nmarq"):
            count = 0
            for x in self.nmarqlist_info[number]:
                if len(x) != 0:
                    count+=1
            if number == 0:
                self.ui.nmark_bar_1.setValue(count)
            if number == 1:
                self.ui.nmark_bar_2.setValue(count)
        if (type == "pacer"):
            count = 0
            for x in self.pacerlist_info[number]:
                if len(x) != 0:
                    count+=1
            if number == 0:
                self.ui.pacer_bar.setValue(count)
        if (type == "qdotdongle"):
            count = 0
            for x in self.qdotdonglelist_info[number]:
                if len(x) != 0:
                    count+=1
            if number == 0:
                self.ui.qdot_bar.setValue(count)
        if (type == "printer"):
            count = 0 
            for x in self.printerlist_info[number]:
                if len(x) != 0:
                    count+=1
            if number == 0:
                self.ui.printer_bar.setValue(count)
        if (type == "epu"):
            count = 0
            for x in self.epulist_info[number]:
                if len(x) != 0:
                    count+=1
            if number == 0:
                self.ui.epu_bar.setValue(count)
        if (type == "spu"):
            count = 0
            for x in self.spuList_info[number]:
                if len(x) != 0:
                    count+=1
            if number == 0:
                self.ui.spu_bar.setValue(count)
        if (type == "demo"):
            count = 0
            for x in self.demolist_info[number]:
                if len(x) != 0:
                    count+=1
            count-=1
            if number == 0:
                self.ui.demo_bar.setValue(count)
            if number == 1:
                self.ui.demo_bar_2.setValue(count)
            if number == 2:
                self.ui.demo_bar_3.setValue(count)
    def open_ultrasoundDialog(self, position):
        if self.ultrasoundOpened[position]:
            self.ultraList[position].fillFields(self.ultraList_info[position])
        self.ultraList[position].exec_()
        self.ultraList_info[position] = [self.ultraList[position].ultrasystem, self.ultraList[position].SWversion, self.ultraList[position].SLnumber,
                           self.ultraList[position].appVer, self.ultraList[position].Videocable, self.ultraList[position].Ethcable]
        self.updateProgressbars("us", position)
        self.ultrasoundOpened[position] = True
    def open_systemDialog(self, position):
        if self.systemOpened[position]:
            self.sysList[position].fillFields(self.sysList_info[position])
        self.sysList[position].exec_()
        self.sysList_info[position] = [self.sysList[position].Systemnumber, self.sysList[position].PIUconf, self.sysList[position].Lposition, self.sysList[position].PUnumber,
                            self.sysList[position].Monitormodel, self.sysList[position].ECGnumber, self.sysList[position].Aquanumber, self.sysList[position].Aquamax]
        self.updateProgressbars("sys", position)
        self.systemOpened[position] = True
    def open_bardDialog(self, position):
        pass
    def open_SPUDialog(self, position):
        if self.spuOpened[position]:
            self.spuList[position].fillFields(self.spuList_info[position])
        self.spuList[position].exec_()
        self.spuList_info[position] = [self.spuList[position].mainfwver, self.spuList[position].swver, self.spuList[position].pn, self.spuList[position].secfwver, self.spuList[position].sn, self.spuList[position].frontloc, self.spuList[position].frontloc_rev, self.spuList[position].ledbo, self.spuList[position].ledbo_rev, self.spuList[position].motherbo, self.spuList[position].motherbo_rev, self.spuList[position].powerb, self.spuList[position].powerb_rev, self.spuList[position].backbo, self.spuList[position].backbo_rev, self.spuList[position].upbo, self.spuList[position].upbo_rev, self.spuList[position].tpibo, self.spuList[position].tpibo_rev, self.spuList[position].pacingbo, self.spuList[position].pacingbo_rev, self.spuList[position].digibo, self.spuList[position].digibo_rev, self.spuList[position].ecgbo, self.spuList[position].ecgbo_rev, self.spuList[position].spuprobo, self.spuList[position].spuprobo_rev]
        self.updateProgressbars("spu", position)
        self.spuOpened[position] = True
    def open_workstationDialog(self, position):
        if self.workstationOpened[position]:
            self.wsList[position].fillFields(self.wsList_info[position])
        self.wsList[position].exec_()
        self.wsList_info[position] = [self.wsList[position].softwarever, self.wsList[position].upgradefrom, self.wsList[position].dspver,self.wsList[position].imagever, self.wsList[position].servicetag, self.wsList[position].wsconf, self.wsList[position].wsmodel, str(self.wsList[position].solios), str(self.wsList[position].performance), self.wsList[position].gpu]
        self.workstationOpened[position] = True
        self.updateProgressbars("ws",position)
        #self.WSlist_info in place of WS if true add licenses = self.wsList[position].Licenses
    def open_cathetersDialog(self, cat_ext):
        cathetersDialog = Catheters_Dialog()
        cathetersDialog.exec_()
        cathetersClip = [cathetersDialog.Catfamily, cathetersDialog.CatMFG]
        item = cathetersClip[0]+": "+cathetersClip[1]
        #In order to get catheters list for export just run for loop for each item in widgetlist
        if len(item) > 2: 
            if (cat_ext == 0):
                self.ui.catheter_list.addItem(item)
            if (cat_ext == 1):
                self.ui.extender_list_2.addItem(item)
    def get_catheterList(self, cat_ext):
        if (cat_ext == 0):
            if (self.ui.catheter_list.count() > 0):
                catheterList = [str(self.ui.catheter_list.item(i).text())for i in range(self.ui.catheter_list.count())]
                return catheterList
            else:
                return []
        if (cat_ext == 1):
            if (self.ui.extender_list_2.count() > 0):
                extenderList = [str(self.ui.extender_list_2.item(i).text())for i in range(self.ui.extender_list_2.count())]
                return extenderList
            else:
                return []
    def open_stockertDialog(self, position):
        if self.stockertOpened[position]:
            self.stockertList[position].fillFields(self.stockertList_info[position])
        self.stockertList[position].exec_()
        self.stockertList_info[position] = self.stockertList[position].infoList
        self.updateProgressbars("stockert", position)
        self.stockertOpened[position] = True
    def open_smartablateDialog(self, position):
        if self.smartablateOpened[position]:
            self.smartablateList[position].fillFields(self.smartablate_info[position])
        self.smartablateList[position].exec_()
        self.smartablate_info[position] = self.smartablateList[position].infoList
        self.updateProgressbars("smartablate", position)
        self.smartablateOpened[position] = True
    def open_ngenDialog(self, position):
        if self.ngenOpened[position]:
            self.ngenList[position].fillFields(self.ngenlist_info[position])
        self.ngenList[position].exec_()
        self.ngenlist_info[position] = self.ngenList[position].infoList
        self.updateProgressbars("ngen", position)
        self.ngenOpened[position] = True
    def open_nmarqDialog(self, position):
        if self.nmarqOpened[position]:
            self.nmarqList[position].fillFields(self.nmarqlist_info[position])
        self.nmarqList[position].exec_()
        self.nmarqlist_info[position] = self.nmarqList[position].infoList
        self.updateProgressbars("nmarq", position)
        self.nmarqOpened[position] = True
    def open_pacerDialog(self, position):
        if self.pacerOpened[position]:
            self.pacerList[position].fillFields(self.pacerlist_info[position])
        self.pacerList[position].exec_()
        self.pacerlist_info[position] = self.pacerList[position].infoList
        self.updateProgressbars("pacer", position)
        self.pacerOpened[position] = True
    def open_qdotdongleDialog(self, position):
        if self.qdotdongleOpened[position]:
            self.qdotdongleList[position].fillFields(self.qdotdonglelist_info[position])
        self.qdotdongleList[position].exec_()
        self.qdotdonglelist_info[position] = self.qdotdongleList[position].infoList
        self.updateProgressbars("qdotdongle", position)
        self.qdotdongleOpened[position] = True
    def open_printerDialog(self, position):
        if self.printerOpened[position]:
            self.printerList[position].fillFields(self.printerlist_info[position])
        self.printerList[position].exec_()
        self.printerlist_info[position] = self.printerList[position].infoList
        self.updateProgressbars("printer", position)
        self.printerOpened[position] = True
    def open_epuDialog(self, position):
        if self.epuOpened[position]:
            self.epuList[position].fillFields(self.epulist_info[position])
        self.epuList[position].exec_()
        self.epulist_info[position] = self.epuList[position].infoList
        self.updateProgressbars("epu", position)
        self.epuOpened[position] = True
    def open_demoDialog(self, position):
        if self.demoOpened[position]:
            self.demoList[position].fillFields(self.demolist_info[position])
        self.demoList[position].exec_()
        self.demolist_info[position] = self.demoList[position].infoList
        self.updateProgressbars("demo", position)
        self.demoOpened[position] = True
    def remove_catheter(self, cat_ext):
        if (cat_ext == 0):
            item = self.ui.catheter_list.takeItem(self.ui.catheter_list.currentRow())
            item = None
        if (cat_ext == 1):
            item = self.ui.extender_list_2.takeItem(self.ui.extender_list_2.currentRow())
            item = None
    def exportTXT(self):
        error_list = ""
        self.experimentalWarning("wslicenses")
        if not self.filePath_configured:
            self.exportfilelocation = QtWidgets.QFileDialog.getSaveFileName(None, "Save File", '/',"Text Files (*.txt)")[0]
            self.filePath_configured = True
        if (self.filePath_configured and len(self.exportfilelocation) > 1):
            toText = []
            for a in range (len(self.systemOpened)):
                if self.systemOpened[a]:
                    if self.ui.system_bar_1.value() > 1 and a == 0:
                        toText.append(self.format("system",0))
                    if self.ui.system_bar_2.value() > 1 and a == 1:
                        toText.append(self.format("system",1))
                    if self.ui.system_bar_3.value() > 1 and a == 2:
                        toText.append(self.format("system",2))
                    if self.ui.system_bar_4.value() > 1 and a == 3:
                        toText.append(self.format("system",3))
                    if self.ui.system_bar_5.value() > 1 and a == 4:
                        toText.append(self.format("system",4))
                    if self.ui.system_bar_6.value() > 1 and a == 5:
                        toText.append(self.format("system",5))
                    if self.ui.system_bar_7.value() > 1 and a == 6:
                        toText.append(self.format("system",6))
                    if self.ui.system_bar_8.value() > 1 and a == 7:
                        toText.append(self.format("system",7))
            for a in range (len(self.ultrasoundOpened)):
                if self.ultrasoundOpened[a]:
                    if self.ui.ultra_bar_1.value() > 1 and a == 0:
                        toText.append(self.format("ultra",0))
                    if self.ui.ultra_bar_2.value() > 1 and a == 1:
                        toText.append(self.format("ultra",1))
                    if self.ui.ultra_bar_3.value() > 1 and a == 2:
                        toText.append(self.format("ultra",2))
                    if self.ui.ultra_bar_4.value() > 1 and a == 3:
                        toText.append(self.format("ultra",3))
                    if self.ui.ultra_bar_5.value() > 1 and a == 4:
                        toText.append(self.format("ultra",4))
                    if self.ui.ultra_bar_6.value() > 1 and a == 5:
                        toText.append(self.format("ultra",5))
                    if self.ui.ultra_bar_7.value() > 1 and a == 6:
                        toText.append(self.format("ultra",6))
                    if self.ui.ultra_bar_8.value() > 1 and a == 7:
                        toText.append(self.format("ultra",7))
            for a in range (len(self.workstationOpened)):
                if self.workstationOpened[a]:
                    if self.ui.work_bar_1.value() > 1 and a == 0:
                        toText.append(self.format("ws",0))
                    if self.ui.work_bar_2.value() > 1 and a == 1:
                        toText.append(self.format("ws",1))
                    if self.ui.work_bar_3.value() > 1 and a == 2:
                        toText.append(self.format("ws",2))
                    if self.ui.work_bar_4.value() > 1 and a == 3:
                        toText.append(self.format("ws",3))
                    if self.ui.work_bar_5.value() > 1 and a == 4:
                        toText.append(self.format("ws",4))
                    if self.ui.work_bar_6.value() > 1 and a == 5:
                        toText.append(self.format("ws",5))
                    if self.ui.work_bar_7.value() > 1 and a == 6:
                        toText.append(self.format("ws",6))
                    if self.ui.work_bar_8.value() > 1 and a == 7:
                        toText.append(self.format("ws",7))
            for a in range (len(self.stockertOpened)):
                if self.stockertOpened[a]:
                    if self.ui.stockert_bar_1.value() > 1 and a == 0:
                        toText.append(self.format("stockert", 0))
                    if self.ui.stockert_bar_2.value() > 1 and a == 1:
                        toText.append(self.format("stockert", 1))
            for a in range (len(self.smartablateOpened)):
                if self.smartablateOpened[a]:
                    if self.ui.smartablate_bar_1.value() > 1 and a == 0:
                        toText.append(self.format("smartablate", 0))
                    if self.ui.smartablate_bar_2.value() > 1 and a == 1:
                        toText.append(self.format("smartablate", 1))
                    if self.ui.smartablate_bar_3.value() > 1 and a == 2:
                        toText.append(self.format("smartablate", 2))
            for a in range (len(self.ngenOpened)):
                if self.ngenOpened[a]:
                    if self.ui.ngen_bar_1.value() > 1 and a == 0:
                        toText.append(self.format("ngen", 0))
                    if self.ui.ngen_bar_2.value() > 1 and a == 1:
                        toText.append(self.format("ngen", 1))
                    if self.ui.ngen_bar_3.value() > 1 and a == 2:
                        toText.append(self.format("ngen", 2))
            for a in range (len(self.nmarqOpened)):
                if self.nmarqOpened[a]:
                    if self.ui.nmark_bar_1.value() > 1 and a == 0:
                        toText.append(self.format("nmarq", 0))
                    if self.ui.nmark_bar_2.value() > 1 and a == 1:
                        toText.append(self.format("nmarq", 1))
            for a in range (len(self.demoOpened)):
                if self.demoOpened[a]:
                    if self.ui.demo_bar.value() > 1 and a == 0:
                        toText.append(self.format("demo", 0))
                    if self.ui.demo_bar_2.value() > 1 and a == 1:
                        toText.append(self.format("demo", 1))
                    if self.ui.demo_bar_3.value() > 1 and a == 2:
                        toText.append(self.format("demo", 2))
            for a in range (len(self.pacerOpened)):
                if self.pacerOpened[a]:
                    if self.ui.pacer_bar.value() > 1 and a == 0:
                        toText.append(self.format("pacer", 0))
            for a in range (len(self.printerOpened)):
                if self.printerOpened[a]:
                    if self.ui.printer_bar.value() > 1 and a == 0:
                        toText.append(self.format("printer", 0))
            for a in range (len(self.epuOpened)):
                if self.epuOpened[a]:
                    if self.ui.epu_bar.value() > 1 and a == 0:
                        toText.append(self.format("epu", 0))
            for a in range (len(self.qdotdongleOpened)):
                if self.qdotdongleOpened[a]:
                    if self.ui.qdot_bar.value() > 1 and a == 0:
                        toText.append(self.format("qdot", 0))
            for a in range (len(self.spuOpened)):
                if self.spuOpened[a]:
                    if self.ui.spu_bar.value() > 1 and a == 0:
                        toText.append(self.format("spu", 0))
            toText.append(self.format('catheters', None))
            toText.append(self.format('extenders', None))
            export_file = open(self.exportfilelocation, 'a')
            for i in range (len(toText)):
                export_file.write(toText[i])
            export_file.close()
            self.exportXML(self.exportfilelocation)
            self.filePath_configured = False # This way the user can save as many times as he wants, without appending toText again to the same file.
    def exportXML(self, fileLocation):
        try:
            fileLocation = fileLocation[:-4]
            fileLocation += '_config.xml'
            root = ET.Element("Baseline_data") #Root tag -> <Baseline_data>
            comment = ET.Comment("Import data for Baseline Tool") #Creating a tag to the root tag and appending it the next line
            root.append(comment)
            #Header
            #Start of WS export
            countOpenWin = 0
            count_ = 0 
            for tf in (self.workstationOpened):
                if tf:
                    countOpenWin += 1
            title_ws = ET.SubElement(root, "Workstations", {"count":str(countOpenWin)}) #Sub element - "Workstations" count: workcount
            fieldsofWS = ['SoftwareVer', 'Upgradefrom', 'DSPver','Imagever', 'ServiceTag', 'WsConf', 'WsModel', 'Solios', 'Performance', 'GraphicsCard'] #in order to print a good looking xml
            for x in range (self.workCount): #for each opened workcount window because if he opened the first and the third
                if (self.workstationOpened[x]): #If workstation window was really opened and not just shown
                    child_ws = ET.SubElement(title_ws, "Workstation_"+str(count_)) #Creating a child <Workstation_x> 
                    for y in range(len(fieldsofWS)):
                        child_field = ET.SubElement(child_ws, fieldsofWS[y]) #Creating a child to <Workstation_x> called the field name e.g. <SoftwareVer>
                        child_field.text = self.wsList_info[x][y] #adding text to the field 
                    LicensesWS = self.wsList[x].licensesToImport
                    LicensesSPWS = self.wsList[x].licensesSPtoImport
                    for i in range(len(LicensesWS)):
                        LicensesWS[i][0] = LicensesWS[i][0].replace('®','1')
                        LicensesWS[i][0] = LicensesWS[i][0].replace('™','2')
                        LicensesWS[i][0] = LicensesWS[i][0].replace(' ','_')
                    for i in range(len(LicensesWS)):
                        child_license = ET.SubElement(child_ws, LicensesWS[i][0])
                        child_license.text = str(LicensesWS[i][1])
                    for i in range(len(LicensesSPWS)):
                        child_license = ET.SubElement(child_ws, LicensesSPWS[i][0])
                        child_license.text = str(LicensesSPWS[i][1])
                    count_ += 1
            #End of WS  export
            #Start of SYS export
            countOpenWin = 0
            count_ = 0 
            for tf in (self.systemOpened):
                if tf:
                    countOpenWin += 1
            title_sys = ET.SubElement(root, "Systems", {"count":str(countOpenWin)})
            fieldofSys = ['SystemNumber', 'PIUconf', 'LocationpadNumber','PatchUnitNumber', 'Monitors', 'ECGphantom', 'AquaNumber', 'AquaMaximu']
            for x in range (self.systemCount):
                if (self.systemOpened[x]):
                    child_sys = ET.SubElement(title_sys, "System_"+str(count_))
                    for y in range(len(fieldofSys)):
                        child_field = ET.SubElement(child_sys, fieldofSys[y])
                        child_field.text = self.sysList_info[x][y]
                    count_ += 1
            #End of SYS export
            #Start of US export
            countOpenWin = 0
            count_ = 0 
            for tf in (self.ultrasoundOpened):
                if tf:
                    countOpenWin += 1
            title_us = ET.SubElement(root, "Ultrasounds", {"count":str(countOpenWin)})
            fieldofUS = ['UltrasoundSystem', 'SoftwareV', 'SerialNumber','SwiftLink', 'VideoCable', 'EthernetCable']
            for x in range (self.ultraCount):
                if (self.ultrasoundOpened[x]):
                    child_us = ET.SubElement(title_us, "Ultrasound_"+str(count_))
                    for y in range(len(fieldofUS)):
                        child_field = ET.SubElement(child_us, fieldofUS[y])
                        child_field.text = self.ultraList_info[x][y]
                    count_ += 1
            #End of US export
            #Start of stockert export
            countOpenWin = 0
            count_ = 0 
            for tf in (self.stockertOpened):
                if tf:
                    countOpenWin += 1
            title_sto = ET.SubElement(root, "Stockerts", {"count":str(countOpenWin)})
            fieldofSto = ['SystemSoftware', 'SerialNumber', 'EPIOinterfaceCable','AbaAdaCable', 'EPIOboxSN', 'EPIOConnectionCable']
            for x in range (self.stockertCount):
                if (self.stockertOpened[x]):
                    child_sto = ET.SubElement(title_sto, "Stockert_"+str(count_))
                    for y in range(len(fieldofSto)):
                        child_field = ET.SubElement(child_sto, fieldofSto[y])
                        child_field.text = self.stockertList_info[x][y]
                    count_ += 1
            #End of stockert export
            #Start of SmartAblate export
            countOpenWin = 0
            count_ = 0 
            for tf in (self.smartablateOpened):
                if tf:
                    countOpenWin += 1
            title_sma = ET.SubElement(root, "SmartAblates", {"count":str(countOpenWin)})
            fieldofSMA = ['SystemSW', 'SerialNumber', 'Cables']
            for x in range (self.smartablateCount):
                if (self.smartablateOpened[x]):
                    child_sma = ET.SubElement(title_sma, "SmartAblate_"+str(count_))
                    for y in range(len(fieldofSMA)):
                        child_field = ET.SubElement(child_sma, fieldofSMA[y])
                        child_field.text = self.smartablate_info[x][y]
                    count_ += 1
            #End of SmartAblate export
            #Start of nGEN export
            countOpenWin = 0
            count_ = 0 
            for tf in (self.ngenOpened):
                if tf:
                    countOpenWin += 1
            title_ngen = ET.SubElement(root, "nGENs", {"count":str(countOpenWin)})
            fieldofNgen = ['ConsoleSN', 'ConsolePN', 'ConsoleVer','psuSN', 'psuPN', 'psuCable','GentoPiuCable','Monitor1SN','Monitor1PN','Monitor1Ver','Monitor1HubSN','Monitor1HubPN','Monitor1PsuSN','Monitor1PsuPN','Monitor2SN','Monitor2PN','Monitor2Ver','Monitor2HubSN','Monitor2HubPN','Monitor2PsuSN','Monitor2PsuPN','PumpSN','PumpPN','PumpVersion','PumptoConsoleCable']
            for x in range (self.ngenCount):
                if (self.ngenOpened[x]):
                    child_ngen = ET.SubElement(title_ngen, "nGEN_"+str(count_))
                    for y in range(len(fieldofNgen)):
                        child_field = ET.SubElement(child_ngen, fieldofNgen[y])
                        child_field.text = self.ngenlist_info[x][y]
                    count_ += 1
            #End of nGEN export
            #Start of nMARQ export
            countOpenWin = 0
            count_ = 0 
            for tf in (self.nmarqOpened):
                if tf:
                    countOpenWin += 1
            title_nmarq = ET.SubElement(root, "nMARQs", {"count":str(countOpenWin)})
            fieldofnmarq = ['SystemSW', 'SerialNumber', 'GentoCartoCable','EthernetCable', 'GentopumpCable', 'GentoMonitor','PumpSN','PumpModel','footPadel']
            for x in range (self.nmarqCount):
                if (self.nmarqOpened[x]):
                    child_nmarq = ET.SubElement(title_nmarq, "nMARQ_"+str(count_))
                    for y in range(len(fieldofnmarq)):
                        child_field = ET.SubElement(child_nmarq, fieldofnmarq[y])
                        child_field.text = self.nmarqlist_info[x][y]
                    count_ += 1
            #End of nMARQ export
            #Start of Pacer export
            countOpenWin = 0
            count_ = 0 
            for tf in (self.pacerOpened):
                if tf:
                    countOpenWin += 1
            title_pacer = ET.SubElement(root, "Pacers", {"count":str(countOpenWin)})
            fieldofPacer = ['PacerType', 'SerialNumber']
            for x in range (self.pacerCount):
                if (self.pacerOpened[x]):
                    child_pac = ET.SubElement(title_pacer, "Pacer_"+str(count_))
                    for y in range(len(fieldofPacer)):
                        child_field = ET.SubElement(child_pac, fieldofPacer[y])
                        child_field.text = self.pacerlist_info[x][y]
                    count_ += 1
            #End of Pacer export
            #Start of qDOTdongle export
            countOpenWin = 0
            count_ = 0 
            for tf in (self.qdotdongleOpened):
                if tf:
                    countOpenWin += 1
            title_qdot = ET.SubElement(root, "QdotDongles", {"count":str(countOpenWin)})
            fieldofQDOT = ['DongleSN', 'DongleSW', 'DongleHW']
            for x in range (self.qdotdongleCount):
                if (self.qdotdongleOpened[x]):
                    child_qdot = ET.SubElement(title_qdot, "QDOT_"+str(count_))
                    for y in range(len(fieldofQDOT)):
                        child_field = ET.SubElement(child_qdot, fieldofQDOT[y])
                        child_field.text = self.qdotdonglelist_info[x][y]
                    count_ += 1
            #End of qDOTdongle export
            #Start of Printer export
            countOpenWin = 0
            count_ = 0 
            for tf in (self.printerOpened):
                if tf:
                    countOpenWin += 1
            title_printer = ET.SubElement(root, "Printers", {"count":str(countOpenWin)})
            fieldofPrinter = ['PrinterModel', 'PrinterSN']
            for x in range (self.printerCount):
                if (self.printerOpened[x]):
                    child_printer = ET.SubElement(title_printer, "Ultrasound_"+str(count_))
                    for y in range(len(fieldofPrinter)):
                        child_field = ET.SubElement(child_printer, fieldofPrinter[y])
                        child_field.text = self.printerlist_info[x][y]
                    count_ += 1
            #End of Printer export
            #Start of EPU export
            countOpenWin = 0
            count_ = 0 
            for tf in (self.epuOpened):
                if tf:
                    countOpenWin += 1
            title_epu = ET.SubElement(root, "EPUs", {"count":str(countOpenWin)})
            fieldofEPU = ['UnitSN', 'UnitVersion']
            for x in range (self.epuCount):
                if (self.epuOpened[x]):
                    child_epu = ET.SubElement(title_epu, "EPU_"+str(count_))
                    for y in range(len(fieldofEPU)):
                        child_field = ET.SubElement(child_epu, fieldofEPU[y])
                        child_field.text = self.epulist_info[x][y]
                    count_ += 1
            #End of EPU export
            #Start of SPU export
            countOpenWin = 0
            count_ = 0 
            for tf in (self.spuOpened):
                if tf:
                    countOpenWin += 1
            title_spu = ET.SubElement(root, "SPUs", {"count":str(countOpenWin)})
            fieldofSPU = ['MainfwVer', 'swVer', 'PN', 'SecFwVer', 'SN','frontloc','frontloc_rev','ledbo','ledbo_rev','motherbo', 'motherbo_rev','powerb', 'powerb_rev','backbo','backbo_rev','upbo','upbo_rev','tpibo','tpibo_rev','pacingbo','pacingbo_rev','digibo','digibo_rev','ecgbo','ecgbo_rev','spuprobo','spuprobo_rev']
            for x in range (self.spuCount):
                if (self.spuOpened[x]):
                    child_spu = ET.SubElement(title_spu, "SPU_"+str(count_))
                    for y in range(len(fieldofSPU)):
                        child_field = ET.SubElement(child_spu, fieldofSPU[y])
                        child_field.text = self.spuList_info[x][y]
                    count_ += 1
            #End of SPU export
            #Start of Demo export
            countOpenWin = 0
            count_ = 0 
            for tf in (self.demoOpened):
                if tf:
                    countOpenWin += 1
            title_demo = ET.SubElement(root, "DemoLaptops", {"count":str(countOpenWin)})
            fieldofdemo = ['WSType', 'SWVer', 'DSPVer','ImageVer', 'ServiceTag', 'Surpoint']
            for x in range (self.demoCount):
                if (self.demoOpened[x]):
                    child_demo = ET.SubElement(title_demo, "DemoLaptop_"+str(count_))
                    for y in range(len(fieldofdemo)):
                        child_field = ET.SubElement(child_demo, fieldofdemo[y])
                        child_field.text = self.demolist_info[x][y]
                    count_ += 1
            #End of Demo export
            #Start of Catheters export
            catheterlist = self.get_catheterList(0)
            title_catheters = ET.SubElement(root, "Catheters", {"count":str(len(catheterlist))})
            if (len(catheterlist) > 0):
                for item in range(len(catheterlist)):
                    field = ET.SubElement(title_catheters, ("catheter_"+str(item)))
                    field.text = catheterlist[item]
            #End of Catheters export
            #Start of Catheters export
            extenderslist = self.get_catheterList(1)
            title_extenders = ET.SubElement(root, "Extenders", {"count":str(len(extenderslist))})
            if (len(extenderslist) > 0):
                for item in range(len(extenderslist)):
                    field = ET.SubElement(title_extenders, ("extender_"+str(item)))
                    field.text = extenderslist[item]
            #End of Catheters export
            b_xml = ET.tostring(root) # parse to bytes
            with open(fileLocation, "wb") as f: #might want to to apply the xml insted of rewriting.
                f.write(b_xml)
            notimplemented = QtWidgets.QMessageBox()
            notimplemented.setText("Exported succssfully, save _config file in order to import in the future")
            notimplemented.setWindowTitle("Exported Succssfully!")
            notimplemented.exec_()
        except Exception as e:
            notimplemented = QtWidgets.QMessageBox()
            notimplemented.setText("Error while exporting")
            notimplemented.setWindowTitle("Error while exporting")
            notimplemented.exec_()
            print (e)
    # format is a function that takes (self,type,position) as arguments.
    # self being the pyqt5 inheritance - this function is being called by self.format(type,position)
    def format(self, type, position):
        if type == 'system':
            return 'System #%d: \nSystem Number:\t\t%s\nPIU Configuration:\t%s\nLocation Pad:\t\t%s\nPatch Unit:\t\t%s\nMonitor Model:\t\t%s\nECG Phantom:\t\t%s\nAquarium Number:\t%s\nAquarium Maximo:\t%s\n-------------------\n' % (position + 1, self.sysList_info[position][0], self.sysList_info[position][1], self.sysList_info[position][2], self.sysList_info[position][3], self.sysList_info[position][4], self.sysList_info[position][5], self.sysList_info[position][6], self.sysList_info[position][7])
        if type == 'ultra':
            return 'Ultrasound #%d: \nUltrasound System:\t%s\nSoftware Version:\t%s\nSerial Number:\t\t%s\nApplication Version:\t%s\nVideo Cable:\t\t%s\nEthernet Cable:\t\t%s\n-------------------\n' %(position + 1, self.ultraList_info[position][0], self.ultraList_info[position][1], self.ultraList_info[position][2], self.ultraList_info[position][3], self.ultraList_info[position][4], self.ultraList_info[position][5])
        if type == 'ws':
            if (self.wsList_info[position][7] == "True"):
                soliosState = "Yes"
            else:
                soliosState = "No"
            if (self.wsList_info[position][8] == "True"):
                performance = "Yes"
            else:
                performance = "No"
            if (len(self.wsList_info[position][1]) > 1):
                toReturn = 'Workstation #%d:\nSW Version:\t\t%s Upgraded from %s\nDSP Version:\t\t%s\nImage Version:\t\t%s\nWS Service Tag:\t\t%s\nWS Configuration:\t%s\nWS Type:\t\t%s\nSolios:\t\t\t%s\nPerformance Tool:\t%s\nGraphics Card:\t\t%s\nLicenses:\t\t%s\nService Packs:\t\t%s\n-------------------\n'%(position + 1,self.wsList_info[position][0], self.wsList_info[position][1], self.wsList_info[position][2], self.wsList_info[position][3], self.wsList_info[position][4], self.wsList_info[position][5], self.wsList_info[position][6], soliosState,performance, self.wsList_info[position][9], self.wsList[position].licensesToExport, self.wsList[position].spToExport)
            else:
                toReturn = 'Workstation #%d:\nSW Version:\t\t%s\nDSP Version:\t\t%s\nImage Version:\t\t%s\nWS Service Tag:\t\t%s\nWS Configuration:\t%s\nWS Type:\t\t%s\nSolios:\t\t\t%s\nPerformance Tool:\t%s\nGraphics Card:\t\t%s\nLicenses:\t\t%s\nService Packs:\t\t%s\n-------------------\n'%(position + 1,self.wsList_info[position][0], self.wsList_info[position][2], self.wsList_info[position][3], self.wsList_info[position][4], self.wsList_info[position][5], self.wsList_info[position][6], soliosState,performance, self.wsList_info[position][9], self.wsList[position].licensesToExport, self.wsList[position].spToExport)
            return toReturn
        if type == 'catheters': #Loops for items in list, assign to [] and loop through it printings. Might want to add Cables:
            items = []
            catToReturn = "Catheters: \n"
            for i in range (self.ui.catheter_list.count()):
                items.append(self.ui.catheter_list.item(i))
            for x in range(len(items)):
                catToReturn += '%s\n' % (items[x].text())
            return catToReturn
        if type == 'extenders': #Loops for items in list, assign to [] and loop through it printings. Might want to add Cables:
            items = []
            extToReturn = "Extenders: \n"
            for i in range (self.ui.extender_list_2.count()):
                items.append(self.ui.extender_list_2.item(i))
            for x in range(len(items)):
                extToReturn += '%s\n' % (items[x].text())
            return extToReturn
        if type == "stockert":
            return 'Stockert GmbH SMARTABLATE System RF Generator #%d:\nSoftware Version:\t%s\nSerial Number:\t\t%s\nEP I/O Sys to Carto:\t%s\nAblation adaptor Cable:\t%s\nEP I/O Box SN:\t\t%s\n-------------------\n' %(position+1,self.stockertList_info[position][0],self.stockertList_info[position][1],self.stockertList_info[position][2],self.stockertList_info[position][3],self.stockertList_info[position][4])
        if type == "smartablate":
            return 'SMARTABLATE RF Generator #%d:\nSystem Software:\t%s\nSerial Number:\t\t%s\nCables:\t\t\t%s\n-------------------\n' % (position+1,self.smartablate_info[position][0],self.smartablate_info[position][1],self.smartablate_info[position][2])
        if type == "ngen":
            return 'nGEN RF Generator #%d:\nnGEN Console S.N:\t\t%s\nnGEN Console P.N:\t\t%s\nnGEN Console Version:\t\t%s\nnGEN PSU S.N:\t\t\t%s\nnGEN PSU P.N:\t\t\t%s\nnGEN PSU Cable:\t\t\t%s\nRF Generator to PIU Cable:\t%s\nnGEN Monitor #1 S.N:\t\t%s\nnGEN Monitor #1 P.N:\t\t%s\nnGEN Monitor  #1 Version:\t%s\nnGEN Monitor Hub #1 S.N:\t%s\nnGEN Monitor Hub #1 P.N:\t%s\nnGEN Monitor PSU #1 S.N:\t%s\nnGEN Monitor PSU #1 P.N:\t%s\nnGEN Monitor #2 S.N:\t\t%s\nnGEN Monitor #2 P.N:\t\t%s\nnGEN Monitor #2 Version:\t%s\nnGEN Monitor Hub #2 S.N:\t%s\nnGEN Monitor Hub #2 P.N:\t%s\nnGEN Monitor PSU #2 S.N:\t%s\nnGEN Monitor PSU #2 P.N:\t%s\nnGEN Pump S.N:\t\t\t%s\nnGEN Pump P.N:\t\t\t%s\nnGEN Pump Version:\t\t%s\nnGEN Pump to Console cable:\t%s\n-------------------\n' % (position+1,self.ngenlist_info[position][0],self.ngenlist_info[position][1],self.ngenlist_info[position][2],self.ngenlist_info[position][3],self.ngenlist_info[position][4],self.ngenlist_info[position][5],self.ngenlist_info[position][6],self.ngenlist_info[position][7],self.ngenlist_info[position][8],self.ngenlist_info[position][9],self.ngenlist_info[position][10],self.ngenlist_info[position][11],self.ngenlist_info[position][12],self.ngenlist_info[position][13],self.ngenlist_info[position][14],self.ngenlist_info[position][15],self.ngenlist_info[position][16],self.ngenlist_info[position][17],self.ngenlist_info[position][18],self.ngenlist_info[position][19],self.ngenlist_info[position][20],self.ngenlist_info[position][21],self.ngenlist_info[position][22],self.ngenlist_info[position][23],self.ngenlist_info[position][24])
        if type == "nmarq":
            return 'nMARQ Multi Channel RF Generator #%d:\nSW Version:\t\t\t%s\nSerial Number:\t\t\t%s\nnMARQ to CARTO Cable:\t\t%s\nEthernet cable:\t\t\t%s\nnMARQ to COOLFLOW Pump Cable:\t%s\nGenerator to Monitor:\t\t%s\nCOOLFLOW pump S.N:\t\t%s\nCOOLFLOW pump Model:\t\t%s\nFoot Pedal:\t\t\t%s\n-------------------\n' % (position+1,self.nmarqlist_info[position][0],self.nmarqlist_info[position][1],self.nmarqlist_info[position][2],self.nmarqlist_info[position][3],self.nmarqlist_info[position][4],self.nmarqlist_info[position][5],self.nmarqlist_info[position][6],self.nmarqlist_info[position][7],self.nmarqlist_info[position][8])
        if type == "demo":
            if (self.demolist_info[position][5] == "True"):
                soliosState = "Yes"
            else:
                soliosState = "No"
            return 'Demo Laptop #%d:\nWS Type:\t\t%s\nSoftware Version:\t%s\nDSP Version:\t\t%s\nImage Version:\t\t%s\nService Tag:\t\t%s\nAll licenses are activated by default but:\nVisitag Surpoint:\t%s\n-------------------\n' % (position + 1,self.demolist_info[position][0],self.demolist_info[position][1],self.demolist_info[position][2],self.demolist_info[position][3],self.demolist_info[position][4], soliosState)
        if type == "pacer":
            return 'Pacer:\nPacer Type:\t\t%s\nSerial Number:\t\t%s\n-------------------\n' % (self.pacerlist_info[position][0],self.pacerlist_info[position][1])
        if type == "printer":
            return 'Printer:\nPrinter Model:\t\t%s\nSerial Number:\t\t%s\n-------------------\n' % (self.printerlist_info[position][0],self.printerlist_info[position][1])
        if type == "epu":
            return 'EPU Device:\nUnit Serial Number:\t%s\nUnit Version:\t\t%s\n-------------------\n' % (self.epulist_info[position][0],self.epulist_info[position][1])
        if type == "qdot":
            return 'qDOT Dongle:\nSerial Number:\t\t%s\nSoftware Version:\t%s\nHardware Version:\t%s\n-------------------\n' % (self.qdotdonglelist_info[position][0],self.qdotdonglelist_info[position][1],self.qdotdonglelist_info[position][2])
        if type == "spu":
            return 'SPU:\nS/N: \t\t%s\nP/N:\t\t%s\nSW Version:\t%s\nMain FW Version:\t%s\nSecondary FW Ver:\t%s\n   Board\t| P/N\t    |Revision\nFront Location\t|%s|%s\nLed Board\t|%s|%s\nMother Board\t|%s|%s\nBack Board\t|%s|%s\nPower Board\t|%s|%s\nUpper Board\t|%s|%s\nPacing Board\t|%s|%s\nTPI Board\t|%s|%s\nDigital Board\t|%s|%s\nECG Board\t|%s|%s\nSPU Prototypes\t|%s|%s\n-------------------\n' % (self.spuList_info[position][4], self.spuList_info[position][2], self.spuList_info[position][1], self.spuList_info[position][0], self.spuList_info[position][3], self.spuList_info[position][5], self.spuList_info[position][6], self.spuList_info[position][7], self.spuList_info[position][8], self.spuList_info[position][9], self.spuList_info[position][10], self.spuList_info[position][13], self.spuList_info[position][14], self.spuList_info[position][11], self.spuList_info[position][12], self.spuList_info[position][15], self.spuList_info[position][16], self.spuList_info[position][19],self.spuList_info[position][20], self.spuList_info[position][17],self.spuList_info[position][18], self.spuList_info[position][21], self.spuList_info[position][22], self.spuList_info[position][23], self.spuList_info[position][24], self.spuList_info[position][25],self.spuList_info[position][26])
    # experimentalWarning is a function that takes (self, kind) as arguments.
    # self being the pyqt5 inheritance - this function is being called by self.experimentalWarning(kind)
    # :param kind - 'experimental' will print an experimental feature messageBox.
    # :param kind - 'beta' will print a beta messageBox.
    # :param kind - 'wslicenses' will print licenses upon error bug description messageBox.
    # :param kind - 'notimp' will print not yet implemented warning messageBox.
    def experimentalWarning(self, kind):
        if (kind == "experimental"):
            warning = QtWidgets.QMessageBox()
            warning.setText("This is an experimental feature\nPlease accept firewall dialog if it's the first time of running.")
            warning.setWindowTitle("Warning")
            warning.exec_()
        if (kind == "beta"):
            warning = QtWidgets.QMessageBox()
            warning.setText("This program is in beta, please use in care.\nIf you see an issue please contact Eran.")
            warning.setWindowTitle("Warning")
            warning.exec_()
        if (kind =="wslicenses"):
            warning = QtWidgets.QMessageBox()
            warning.setText("Upon export of data, each WS licenses are deleted.\nIt is a known bug please wait for next version for a fix.\nMake sure to save the .txt file.")
            warning.setWindowTitle("Warning")
            warning.exec_()
        if (kind == "notimp"):
            warning = QtWidgets.QMessageBox()
            warning.setText("Not yet implemented")
            warning.setWindowTitle("Warning")
            warning.exec_()
    def importButton(self):
        try:
            state = self.check_progressbars()
            if state:
                filename = QtWidgets.QFileDialog.getOpenFileName(None, "Open File", '/',"XML Files (*.xml)")[0]
                #imported_xml = ET.Element(filename)
                self.importBase(filename)
            else:
                #some windows were opened, notify the loss of data and
                windowsOpened_alert = QtWidgets.QMessageBox()
                windowsOpened_alert.setText("Some windows were opened, import now will result in the loss of data. \nDo you want to continue?")
                windowsOpened_alert.setWindowTitle("Confirmation Window")
                windowsOpened_alert.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
                button_okCancel = windowsOpened_alert.exec_() #if pressed okay -> 1024 if pressed cancel -> 4194304
                if (button_okCancel == 1024):
                    self.hideThings()
                    self.reset_allFields() #reset all fields
                    self.reset_progressbars()
                    self.createWindowsLists("all") #Resets all windows dialogs.
                    filename = QtWidgets.QFileDialog.getOpenFileName(None, "Open File", '/',"XML Files (*.xml)")[0]
                    self.importBase(filename)
                if (button_okCancel == 4194304):
                    pass #well, cancel
        except Exception as e:
            notimplemented = QtWidgets.QMessageBox()
            notimplemented.setIcon(QtWidgets.QMessageBox.Critical)
            notimplemented.setText('Error in importing')
            notimplemented.setWindowTitle("Error")
            notimplemented.exec_()
            print (e)
    def importBase(self, filelocation):
        imported_xml = ET.parse(filelocation)
        importedroot = imported_xml.getroot()
        for child in importedroot:
            if (child.tag != 'Catheters' and child.tag != 'Extenders' and child.tag != 'Workstations'):
                for childx2 in child: #Ultrasound_0
                    listofValues = []
                    for childx3 in childx2:
                        if childx3.text == None: #Crash when Object is None. (because somewhere it tries to len() it)
                            listofValues.append("") 
                        else:
                            listofValues.append(childx3.text)
                    self.importaddtoInfoCount(child.tag, listofValues)
            elif child.tag == 'Catheters':
                for childx2 in child:
                    self.importaddtoInfoCount(child.tag, childx2.text)
            elif (child.tag == 'Extenders'):
                for childx2 in child:
                    self.importaddtoInfoCount(child.tag, childx2.text)
            elif (child.tag == 'Workstations'):
                for childx2 in child: #Workstation_0
                    listofValues = []
                    for childx3 in childx2:
                        if childx3.text == None: #Crash when Object is None. (because somewhere it tries to len() it)
                            listofValues.append("") 
                        else:
                            listofValues.append([childx3.tag,childx3.text])
                    self.importaddtoInfoCount(child.tag, listofValues)
    def importaddtoInfoCount(self, type, listValues):
        #This function gets type (child.tag) e.g. "Workstations" and listValues which is the list of all the values of the children texts(childx3.text)
        #importaddtoInfoCount starts by self.showThings
        if (type == "Workstations"):
            costumValue = []
            listLicenses = []
            listSP = []
            if len(listValues)  == 10:
                self.showThings("workstation")
                self.workstationOpened[self.workCount-1] = True
                toSend = []
                for i in listValues:
                    toSend.append(i[1])
                self.wsList_info[self.workCount-1] = toSend
                self.updateProgressbars("ws", self.workCount-1)
            else:
                listforWS = listValues[:10]
                listValues = listValues[10:]
                if len(listValues) == 36: #That means the user added custom license
                    listLicenses = listValues[:31]
                    costumValue = listValues[31]
                    listSP = listValues[32:]
                else:
                    listLicenses =listValues[:31]
                    listSP = listValues[31:]
                    costumValue = None
                self.showThings("workstation")
                self.workstationOpened[self.workCount-1] = True
                listforWStoSend = []
                for i in listforWS:
                    if (i != ''):
                        listforWStoSend.append(i[1])
                    if (i == ''):
                        listforWStoSend.append('')
                self.wsList_info[self.workCount-1] = listforWStoSend
                self.wsList[self.workCount-1].importedLicenses = listLicenses
                self.wsList[self.workCount-1].importedSP = listSP
                self.wsList[self.workCount-1].importedManual = costumValue
                self.updateProgressbars("ws", self.workCount-1)
        if (type == "Systems"):
            self.showThings("system")
            self.systemOpened[self.systemCount-1] = True
            self.sysList_info[self.systemCount-1] = listValues
            self.updateProgressbars("sys", self.systemCount-1)
        if (type == "Ultrasounds"):
            self.showThings("ultra")
            self.ultrasoundOpened[self.ultraCount-1] = True
            self.ultraList_info[self.ultraCount-1] = listValues
            self.updateProgressbars("us", self.ultraCount-1)
        if (type == "Stockerts"):
            self.showThings("stockert")
            self.stockertOpened[self.stockertCount-1] = True
            self.stockertList_info[self.stockertCount-1] = listValues
            self.updateProgressbars("stockert", self.stockertCount-1)
        if (type =="SmartAblates"):
            self.showThings("smartablate")
            self.smartablateOpened[self.smartablateCount-1] = True
            self.smartablate_info[self.smartablateCount-1] = listValues
            self.updateProgressbars("smartablate", self.smartablateCount-1)
        if (type == "nGENs"):
            self.showThings("ngen")
            self.ngenOpened[self.ngenCount-1] = True
            self.ngenlist_info[self.ngenCount-1] = listValues
            self.updateProgressbars("ngen", self.ngenCount-1)
        if (type =="nMARQs"):
            self.showThings("nmark")
            self.nmarqOpened[self.nmarqCount-1] = True
            self.nmarqlist_info[self.nmarqCount-1] = listValues
            self.updateProgressbars("nmarq", self.nmarqCount-1)
        if (type == "Pacers"):
            self.showThings("pacer")
            self.pacerOpened[self.pacerCount-1] = True
            self.pacerlist_info[self.pacerCount-1] = listValues
            self.updateProgressbars("pacer", self.pacerCount-1)
        if (type == "QdotDongles"):
            self.showThings("qdotdongle")
            self.qdotdongleOpened[self.qdotdongleCount-1] = True
            self.qdotdonglelist_info[self.qdotdongleCount-1] = listValues
            self.updateProgressbars("qdotdongle", self.qdotdongleCount-1)
        if (type == "Printers"):
            self.showThings("printer")
            self.printerOpened[self.printerCount-1] = True
            self.printerlist_info[self.printerCount-1] = listValues
            self.updateProgressbars("printer", self.printerCount-1)
        if (type == "EPUs"):
            self.showThings("epu")
            self.epuOpened[self.epuCount-1] = True
            self.epulist_info[self.epuCount-1] = listValues
            self.updateProgressbars("epu", self.epuCount-1)
        if (type == "SPUs"):
            self.showThings("spu")
            self.spuOpened[self.spuCount-1] = True
            self.spuList_info[self.spuCount-1] = listValues
            self.updateProgressbars("spu",self.spuCount-1)
        if (type == "DemoLaptops"):
            self.showThings("demo")
            self.demoOpened[self.demoCount-1] = True
            self.demolist_info[self.demoCount-1] = listValues
            self.updateProgressbars("demo", self.demoCount-1)
        if (type == "Catheters"):
            self.ui.catheter_list.addItem(listValues)
        if (type == "Extenders"):
            self.ui.extender_list_2.addItem(listValues)
class Ultrasound_Dialog(QtWidgets.QDialog):
    def __init__(self):
        super(Ultrasound_Dialog, self).__init__()
        self.udialog = Ui_ultrasound_Dialog()
        self.udialog.setupUi(self)
        self.udialog.confirm_button.clicked.connect(self.confirmPressed)
        self.udialog.check_button.clicked.connect(self.verification)
        self.infoBox() #By adding self.infoBox() when ending __init__, it puts "" inside infobox fields thus making the app not crash when pressing X or esc
        # dict_of_values = {
        # "system": "",
        # "swversion": "",
        # "slnumber":"",
        # "swlcable":"",
        # "videocable":"",
        # "ethcable":""}
    def infoBox(self):
        # self.dict_of_values["system"] = self.udialog.ultrasound_combo.currentText()
        # self.dict_of_values["swversion"] = self.udialog.softwarever_text.text()
        # self.dict_of_values["slnumber"] = self.udialog.serialnum_text.text()
        # self.dict_of_values["swlcable"] = self.udialog.swiftlink_text.text()
        # self.dict_of_values["videocable"] = self.udialog.videocable_text.text()
        # self.dict_of_values["ethcable"] = self.udialog.ethernet_text.text()
        self.ultrasystem = self.udialog.ultrasound_combo.currentText()
        self.SWversion = self.udialog.softwarever_text.text()
        self.SLnumber = self.udialog.serialnum_text.text()
        self.appVer = self.udialog.applicationver_text.text()
        self.Videocable = self.udialog.videocable_text.text()
        self.Ethcable = self.udialog.ethernet_text.text()
    def confirmPressed(self):
        self.infoBox()
        self.close()
    def verification(self):
        notimplemented = QtWidgets.QMessageBox()
        notimplemented.setIcon(QtWidgets.QMessageBox.Critical)
        notimplemented.setText('To be implemented...')
        notimplemented.setWindowTitle("Work in Progress")
        notimplemented.exec_()
    def fillFields(self, clip):
        index = self.udialog.ultrasound_combo.findText(
            clip[0], QtCore.Qt.MatchFixedString)
        if index >= 0:
            self.udialog.ultrasound_combo.setCurrentIndex(index)
        self.udialog.softwarever_text.setText(clip[1])
        self.udialog.serialnum_text.setText(clip[2])
        self.udialog.applicationver_text.setText(clip[3])
        self.udialog.videocable_text.setText(clip[4])
        self.udialog.ethernet_text.setText(clip[5])
        self.infoBox() #After filling fields also apply values to self.values.
class CatalogHelper_Dialog(QtWidgets.QDialog):
    def __init__(self, mainWin):
        """Here is a good example of inheritance between pyqt5 objects - which works differently then normal python inheritance.
        Here, I need to pass in the __init__ function the parent self. - which means, when i'm using this class in the parent class, i'll need to send it
        self as a variable, and here, at the child class, enter it into an object. This way I can call parent functions as variable from the child."""
        super(CatalogHelper_Dialog, self).__init__()
        self.ui = cathelp_mainUi()
        self.ui.setupUi(self)
        self.ui.getCatalog_B.clicked.connect(self.oneCatalog)
        self.mainWin = mainWin
    def getMFG_selenium(self, part):
        try:
            #This function uses selenium to open Chrome -> go to catheter catalog, enter 'part' into the search bar
            #Presses search and returns list of mfgpart, description, family, catalog in this order if it doesn't find, returns False
            driver = webdriver.Chrome() #driver is a webdriver (chromedriver.exe at root folder)
            driver.get('http://itsusrawsp10939.jnj.com/partnolookup/Default.aspx') #Sents to web address
            searchbox = driver.find_element_by_xpath('//*[@id="txtPartNo"]') #searches for the element xpath of searchbox
            searchbox.send_keys(part) #Enters the input it gets to the search bar
            searchButton = driver.find_element_by_xpath('//*[@id="btnLookup"]') #looks and finds the search button
            searchButton.click() #Clicks on it
            mfg_part_number = driver.find_element_by_xpath('//*[@id="grdResults"]/tbody/tr[2]/td[4]') #Looks for the xpath of the mfg field
            description = driver.find_element_by_xpath('//*[@id="grdResults"]/tbody/tr[2]/td[8]')
            family = driver.find_element_by_xpath('//*[@id="grdResults"]/tbody/tr[2]/td[9]')
            catalog = driver.find_element_by_xpath('//*[@id="grdResults"]/tbody/tr[2]/td[3]')
            result = [mfg_part_number.text, description.text, family.text, catalog.text]
            driver.close()
            driver.quit()
            return result
        except:
            driver.close()
            return False
    def oneCatalog(self):
        cat = self.getMFG_selenium(self.ui.signelCatalog_Text.text())
        if (cat != False):
            singleCat = SingleCatheter(cat,self)
            singleCat.exec_()
        else:
            notimplemented = QtWidgets.QMessageBox()
            notimplemented.setText("Couldn't find item in catalog")
            notimplemented.setWindowTitle("Error")
            notimplemented.exec_()
class SPU_Dialog(QtWidgets.QDialog):
    def __init__(self):
        super(SPU_Dialog, self).__init__()
        self.spdialog = spu_Ui()
        self.spdialog.setupUi(self)
        self.spdialog.confirm_button.clicked.connect(self.confirmPressed)
        self.spdialog.check_button.clicked.connect(self.verification)
        self.infoBox()
    def confirmPressed(self):
        self.infoBox()
        self.close()
    def verification(self):
        notimplemented = QtWidgets.QMessageBox()
        notimplemented.setIcon(QtWidgets.QMessageBox.Critical)
        notimplemented.setText('To be implemented...')
        notimplemented.setWindowTitle("Work in Progress")
        notimplemented.exec_()
    def infoBox(self):
        self.mainfwver = self.spdialog.mainfwver_text.text()
        self.swver = self.spdialog.swver_text.text()
        self.pn = self.spdialog.pn_text.text()
        self.secfwver = self.spdialog.secfwver_text.text()
        self.sn = self.spdialog.sn_text.text()
        self.frontloc = self.spdialog.frontloc_text.text()
        self.frontloc_rev = self.spdialog.frontloc_text_rev.text()
        self.ledbo = self.spdialog.ledbo_text.text()
        self.ledbo_rev = self.spdialog.ledbo_text_rev.text()
        self.motherbo = self.spdialog.motherbo_text.text()
        self.motherbo_rev = self.spdialog.motherbo_text_rev.text()
        self.powerb = self.spdialog.powerb_text.text()
        self.powerb_rev = self.spdialog.powerb_text_rev.text()
        self.backbo = self.spdialog.backbo_text.text()
        self.backbo_rev = self.spdialog.backbo_text_rev.text()
        self.upbo = self.spdialog.upbo_text.text()
        self.upbo_rev = self.spdialog.upbo_text_rev.text()
        self.backbo = self.spdialog.backbo_text.text()
        self.backbo_rev = self.spdialog.backbo_text_rev.text()
        self.tpibo = self.spdialog.tpibo_text.text()
        self.tpibo_rev = self.spdialog.tpibo_text_rev.text()
        self.pacingbo = self.spdialog.pacingbo_text.text()
        self.pacingbo_rev = self.spdialog.pacingbo_text_rev.text()
        self.digibo = self.spdialog.digibo_text.text()
        self.digibo_rev = self.spdialog.digibo_text_rev.text()
        self.ecgbo = self.spdialog.ecgbo_text.text()
        self.ecgbo_rev = self.spdialog.ecgbo_text_rev.text()
        self.spuprobo = self.spdialog.spuprobo_text.text()
        self.spuprobo_rev = self.spdialog.spuprobo_text_rev.text()
    def fillFields(self, clip):
        self.spdialog.mainfwver_text.setText(clip[0])
        self.spdialog.swver_text.setText(clip[1])
        self.spdialog.pn_text.setText(clip[2])
        self.spdialog.secfwver_text.setText(clip[3])
        self.spdialog.sn_text.setText(clip[4])
        self.spdialog.frontloc_text.setText(clip[5])
        self.spdialog.frontloc_text_rev.setText(clip[6])
        self.spdialog.ledbo_text.setText(clip[7])
        self.spdialog.ledbo_text_rev.setText(clip[8])
        self.spdialog.motherbo_text.setText(clip[9])
        self.spdialog.motherbo_text_rev.setText(clip[10])
        self.spdialog.powerb_text.setText(clip[11])
        self.spdialog.powerb_text_rev.setText(clip[12])
        self.spdialog.backbo_text.setText(clip[13])
        self.spdialog.backbo_text_rev.setText(clip[14])
        self.spdialog.upbo_text.setText(clip[15])
        self.spdialog.upbo_text_rev.setText(clip[16])
        self.spdialog.tpibo_text.setText(clip[17])
        self.spdialog.tpibo_text_rev.setText(clip[18])
        self.spdialog.pacingbo_text.setText(clip[19])
        self.spdialog.pacingbo_text_rev.setText(clip[20])
        self.spdialog.digibo_text.setText(clip[21])
        self.spdialog.digibo_text_rev.setText(clip[22])
        self.spdialog.ecgbo_text.setText(clip[23])
        self.spdialog.ecgbo_text_rev.setText(clip[24])
        self.spdialog.spuprobo_text.setText(clip[25])
        self.spdialog.spuprobo_text_rev.setText(clip[26])
        self.infoBox()
class Bard_Dialog(QtWidgets.QDialog):
    pass
class SingleCatheter(QtWidgets.QDialog):
    def __init__(self, listValues, parent_win):
        super(SingleCatheter, self).__init__()
        self.dialog = cathelp_detUi()
        self.dialog.setupUi(self)
        self.parent_win = parent_win
        self.dialog.pushButton.clicked.connect(self.sendExtenders)
        self.dialog.pushButton_2.clicked.connect(self.sendCatheters)
        self.dialog.catalog_text.setText(listValues[3])
        self.dialog.mfg_text.setText(listValues[0])
        self.dialog.description_text.setText(listValues[1])
        self.dialog.family_text.setText(listValues[2])
    def sendExtenders(self):
        item = self.dialog.description_text.text()+': '+self.dialog.mfg_text.text()
        self.parent_win.mainWin.ui.extender_list_2.addItem(item)
        self.close()
    def sendCatheters(self):
        item = self.dialog.description_text.text()+': '+self.dialog.mfg_text.text()
        self.parent_win.mainWin.ui.catheter_list.addItem(item)
        self.close()
class System_Dialog(QtWidgets.QDialog):
    def __init__(self):
        super(System_Dialog, self).__init__()
        self.sdialog = Ui_system_dialog()
        self.sdialog.setupUi(self)
        self.sdialog.confirm_button.clicked.connect(self.confirmPressed)
        self.sdialog.check_button.clicked.connect(self.verification)
        self.infoBox() #By adding self.infoBox() when ending __init__, it puts "" inside infobox fields thus making the app not crash when pressing X or esc
    def confirmPressed(self):
        self.infoBox()
        self.close()
    def verification(self):
        notimplemented = QtWidgets.QMessageBox()
        notimplemented.setIcon(QtWidgets.QMessageBox.Critical)
        notimplemented.setText('To be implemented...')
        notimplemented.setWindowTitle("Work in Progress")
        notimplemented.exec_()
    def infoBox(self):
        self.Systemnumber = self.sdialog.system_text.text()
        self.PIUconf = self.sdialog.piu_text.text()
        self.Lposition = self.sdialog.lp_text.text()
        self.PUnumber = self.sdialog.patchunit_text.text()
        self.Monitormodel = self.sdialog.mm_text.text()
        self.ECGnumber = self.sdialog.ecg_text.text()
        self.Aquanumber = self.sdialog.aquanum_text.text()
        self.Aquamax = self.sdialog.aquamax_text.text()
    def fillFields(self, clip):
        self.sdialog.system_text.setText(clip[0])
        self.sdialog.piu_text.setText(clip[1])
        self.sdialog.lp_text.setText(clip[2])
        self.sdialog.patchunit_text.setText(clip[3])
        self.sdialog.mm_text.setText(clip[4])
        self.sdialog.ecg_text.setText(clip[5])
        self.sdialog.aquanum_text.setText(clip[6])
        self.sdialog.aquamax_text.setText(clip[7])
        self.infoBox() #After filling fields also apply values to self.values.
class Licenses_Dialog(QtWidgets.QDialog):
    def __init__(self, parentWin):
        super(Licenses_Dialog, self).__init__()
        self.ldialog = Ui_licenses_Dialog()
        self.ldialog.setupUi(self)
        self.licenseClip = []
        self.ldialog.comboBox.currentTextChanged.connect(self.presets)
        self.ldialog.confirm_button.clicked.connect(self.grabcheckboxes)
        if (len(parentWin.importedLicenses) > 1):
            self.fillFields(parentWin.importedLicenses, parentWin.importedSP, parentWin.importedManual)
    def grabcheckboxes(self):
        licensesclip = []
        spclip = []
        licensesclip.append([self.ldialog.merge.text(), self.ldialog.merge.isChecked()])
        licensesclip.append([self.ldialog.sound.text(), self.ldialog.sound.isChecked()])
        licensesclip.append([self.ldialog.paso.text(), self.ldialog.paso.isChecked()])
        licensesclip.append([self.ldialog.cafe_2.text(),self.ldialog.cafe_2.isChecked()])
        licensesclip.append([self.ldialog.rmt.text(), self.ldialog.rmt.isChecked()])
        licensesclip.append([self.ldialog.smarttouch.text(),self.ldialog.smarttouch.isChecked()])
        licensesclip.append([self.ldialog.nivu.text(), self.ldialog.nivu.isChecked()])
        licensesclip.append([self.ldialog.visitag.text(),self.ldialog.visitag.isChecked()])
        licensesclip.append([self.ldialog.activation3.text(), self.ldialog.activation3.isChecked()])
        licensesclip.append([self.ldialog.segct.text(), self.ldialog.segct.isChecked()])
        licensesclip.append([self.ldialog.segmr.text(), self.ldialog.segmr.isChecked()])
        licensesclip.append([self.ldialog.dualmonitor.text(), self.ldialog.dualmonitor.isChecked()])
        licensesclip.append([self.ldialog.confidense.text(),self.ldialog.confidense.isChecked()])
        licensesclip.append([self.ldialog.finder.text(),self.ldialog.finder.isChecked()])
        licensesclip.append([self.ldialog.visitagsur.text(),self.ldialog.visitagsur.isChecked()])
        licensesclip.append([self.ldialog.replay.text(),self.ldialog.replay.isChecked()])
        licensesclip.append([self.ldialog.ripple.text(),self.ldialog.ripple.isChecked()])
        licensesclip.append([self.ldialog.famdx.text(), self.ldialog.famdx.isChecked()])
        licensesclip.append([self.ldialog.qdotmicro.text(),self.ldialog.qdotmicro.isChecked()])
        licensesclip.append([self.ldialog.visitagepu.text(),self.ldialog.visitagepu.isChecked()])
        licensesclip.append([self.ldialog.sia.text(), self.ldialog.sia.isChecked()])
        licensesclip.append([self.ldialog.complex.text(),self.ldialog.complex.isChecked()])
        licensesclip.append([self.ldialog.hdcolor.text(),self.ldialog.hdcolor.isChecked()])
        licensesclip.append([self.ldialog.prime.text(), self.ldialog.prime.isChecked()])
        licensesclip.append([self.ldialog.helios.text(),self.ldialog.helios.isChecked()])
        licensesclip.append([self.ldialog.baloon.text(),self.ldialog.baloon.isChecked()])
        licensesclip.append([self.ldialog.activationv7.text(), self.ldialog.activationv7.isChecked()])
        licensesclip.append([self.ldialog.activationv8.text(), self.ldialog.activationv8.isChecked()])
        licensesclip.append([self.ldialog.soundfam.text(),self.ldialog.soundfam.isChecked()])
        licensesclip.append([self.ldialog.activationv7p3.text(), self.ldialog.activationv7p3.isChecked()])
        licensesclip.append([self.ldialog.activationv7sp2.text(), self.ldialog.activationv7sp2.isChecked()])
        spclip.append([self.ldialog.sp_helios.text(), self.ldialog.sp_helios.isChecked()])
        spclip.append([self.ldialog.sp_lasso.text(), self.ldialog.sp_lasso.isChecked()])
        spclip.append([self.ldialog.sp_qdot.text(), self.ldialog.sp_qdot.isChecked()])
        spclip.append([self.ldialog.sp_spu.text(), self.ldialog.sp_spu.isChecked()])
        if len(self.ldialog.ManualLine.text()) > 1:
            manualline = self.ldialog.ManualLine.text()#because those chars breaks the XML
            manualline = manualline.replace('!', '').replace('@','').replace('#','').replace('$','').replace('%','').replace('^','').replace('&','').replace('*','').replace('(','').replace(')','')
            licensesclip.append([manualline, True])
        self.licenseClip = licensesclip
        self.spClip = spclip
        self.close()
    def presets(self, index):
        if self.ldialog.comboBox.currentText() == "Select All":
            self.ldialog.merge.setChecked(True)
            self.ldialog.sound.setChecked(True)
            self.ldialog.paso.setChecked(True)
            self.ldialog.cafe_2.setChecked(True)
            self.ldialog.rmt.setChecked(True)
            self.ldialog.smarttouch.setChecked(True)
            self.ldialog.nivu.setChecked(True)
            self.ldialog.visitag.setChecked(True)
            self.ldialog.activation3.setChecked(True)
            self.ldialog.segct.setChecked(True)
            self.ldialog.segmr.setChecked(True)
            self.ldialog.dualmonitor.setChecked(True)
            self.ldialog.confidense.setChecked(True)
            self.ldialog.finder.setChecked(True)
            self.ldialog.visitagsur.setChecked(True)
            self.ldialog.replay.setChecked(True)
            self.ldialog.ripple.setChecked(True)
            self.ldialog.famdx.setChecked(True)
            self.ldialog.visitagepu.setChecked(True)
            self.ldialog.sia.setChecked(True)
            self.ldialog.complex.setChecked(True)
            self.ldialog.hdcolor.setChecked(True)
            self.ldialog.prime.setChecked(True)
            self.ldialog.activationv7.setChecked(True)
            self.ldialog.activationv8.setChecked(True)
            self.ldialog.soundfam.setChecked(True)
            self.ldialog.activationv7p3.setChecked(True)
            self.ldialog.activationv7sp2.setChecked(True)
        if self.ldialog.comboBox.currentText() == "None":
            self.ldialog.merge.setChecked(False)
            self.ldialog.sound.setChecked(False)
            self.ldialog.paso.setChecked(False)
            self.ldialog.cafe_2.setChecked(False)
            self.ldialog.rmt.setChecked(False)
            self.ldialog.smarttouch.setChecked(False)
            self.ldialog.nivu.setChecked(False)
            self.ldialog.visitag.setChecked(False)
            self.ldialog.activation3.setChecked(False)
            self.ldialog.segct.setChecked(False)
            self.ldialog.segmr.setChecked(False)
            self.ldialog.dualmonitor.setChecked(False)
            self.ldialog.confidense.setChecked(False)
            self.ldialog.finder.setChecked(False)
            self.ldialog.visitagsur.setChecked(False)
            self.ldialog.replay.setChecked(False)
            self.ldialog.ripple.setChecked(False)
            self.ldialog.famdx.setChecked(False)
            self.ldialog.qdotmicro.setChecked(False)
            self.ldialog.visitagepu.setChecked(False)
            self.ldialog.sia.setChecked(False)
            self.ldialog.complex.setChecked(False)
            self.ldialog.hdcolor.setChecked(False)
            self.ldialog.prime.setChecked(False)
            self.ldialog.helios.setChecked(False)
            self.ldialog.baloon.setChecked(False)
            self.ldialog.activationv7.setChecked(False)
            self.ldialog.activationv8.setChecked(False)
            self.ldialog.soundfam.setChecked(False)
            self.ldialog.activationv7p3.setChecked(False)
            self.ldialog.activationv7sp2.setChecked(False)
    def fillFields(self, LicenseClip, spClip, customValue):
        for i in range(len(LicenseClip)):
            if ("CARTOMERGE" in LicenseClip[i][0] and LicenseClip[i][1] == "True"):
                self.ldialog.merge.setChecked(True)
            if ("CARTOSOUND" in LicenseClip[i][0] and LicenseClip[i][1] == "True"):
                self.ldialog.sound.setChecked(True)
            if ("PASO" in LicenseClip[i][0] and LicenseClip[i][1] == "True"):
                self.ldialog.paso.setChecked(True)
            if ("CAFE" in LicenseClip[i][0] and LicenseClip[i][1] == "True"):
                self.ldialog.cafe_2.setChecked(True)
            if ("SMARTTOUCH" in LicenseClip[i][0] and LicenseClip[i][1] == "True"):
                self.ldialog.smarttouch.setChecked(True)
            if ("CARTOUNIVU" in LicenseClip[i][0] and LicenseClip[i][1] == "True"):
                self.ldialog.nivu.setChecked(True)
            if ("VISITAG2" in LicenseClip[i][0] and LicenseClip[i][1] == "True"):
                self.ldialog.visitag.setChecked(True)
            if ("RMT" in LicenseClip[i][0] and LicenseClip[i][1] == "True"):
                self.ldialog.rmt.setChecked(True)
            if ("CARTO_31_Activation" in LicenseClip[i][0] and LicenseClip[i][1] == "True"):
                self.ldialog.activation3.setChecked(True)
            if ("CARTOSEG2_Extended_CT" in LicenseClip[i][0] and LicenseClip[i][1] == "True"):
                self.ldialog.segct.setChecked(True)
            if ("CARTOSEG2_Extended_MR" in LicenseClip[i][0] and LicenseClip[i][1] == "True"):
                self.ldialog.segmr.setChecked(True)
            if ("Dual-Monitor" in LicenseClip[i][0] and LicenseClip[i][1] == "True"):
                self.ldialog.dualmonitor.setChecked(True)
            if ("CONFIDENSE" in LicenseClip[i][0] and LicenseClip[i][1] == "True"):
                self.ldialog.confidense.setChecked(True)
            if ("CARTOFINDER" in LicenseClip[i][0] and LicenseClip[i][1] == "True"):
                self.ldialog.finder.setChecked(True)
            if ("VISITAG_SURPOINT2" == LicenseClip[i][0] and LicenseClip[i][1] == "True"):
                self.ldialog.visitagsur.setChecked(True)
            if ("CARTOREPLAY2" in LicenseClip[i][0] and LicenseClip[i][1] == "True"):
                self.ldialog.replay.setChecked(True)
            if ("Ripple_Mapping" in LicenseClip[i][0] and LicenseClip[i][1] == "True"):
                self.ldialog.ripple.setChecked(True)
            if ("FAM_Dx" in LicenseClip[i][0] and LicenseClip[i][1] == "True"):
                self.ldialog.famdx.setChecked(True)
            if ("CARTO_QDOT_MICRO2" in LicenseClip[i][0] and LicenseClip[i][1] == "True"):
                self.ldialog.qdotmicro.setChecked(True)
            if ("VISITAG_SURPOINT2_EPU" == LicenseClip[i][0] and LicenseClip[i][1] == "True"):
                self.ldialog.visitagepu.setChecked(True)
            if ("SIA" in LicenseClip[i][0] and LicenseClip[i][1] == "True"):
                self.ldialog.sia.setChecked(True)
            if ("Complex_Point" in LicenseClip[i][0] and LicenseClip[i][1] == "True"):
                self.ldialog.complex.setChecked(True)
            if ("HD_Coloring" in LicenseClip[i][0] and LicenseClip[i][1] == "True"):
                self.ldialog.hdcolor.setChecked(True)
            if ("CARTO_PRIME2" in LicenseClip[i][0] and LicenseClip[i][1] == "True"):
                self.ldialog.prime.setChecked(True)
            if ("HELIOSTAR2" in LicenseClip[i][0] and LicenseClip[i][1] == "True"):
                self.ldialog.helios.setChecked(True)
            if ("RF_BALLOON" in LicenseClip[i][0] and LicenseClip[i][1] == "True"):
                self.ldialog.baloon.setChecked(True)
            if ("CARTO_3_V7_Activation" in LicenseClip[i][0] and LicenseClip[i][1] == "True"):
                self.ldialog.activationv7.setChecked(True)
            if ("CARTO_3_V8_Activation" in LicenseClip[i][0] and LicenseClip[i][1] == "True"):
                self.ldialog.activationv8.setChecked(True)
            if ("SOUNDFAM2" in LicenseClip[i][0] and LicenseClip[i][1] == "True"):
                self.ldialog.soundfam.setChecked(True)
            if ("CARTO_3_V7_Phase_3_Activation" in LicenseClip[i][0] and LicenseClip[i][1] == "True"):
                self.ldialog.activationv7p3.setChecked(True)
            if ("CARTO_3_V7_Phase_2_SP_Activation" in LicenseClip[i][0] and LicenseClip[i][1] == "True"):
                self.ldialog.activationv7sp2.setChecked(True)
        for i in range (len(spClip)):
            if ("HELIOSTAR" in spClip[i][0] and spClip[i][1] == "True"):
                self.ldialog.sp_helios.setChecked(True)
            if ("LASSOSTARNav" in spClip[i][0] and spClip[i][1] == "True"):
                self.ldialog.sp_lasso.setChecked(True)
            if ("QDOT" in spClip[i][0] and spClip[i][1] == "True"):
                self.ldialog.sp_qdot.setChecked(True)
            if ("SPU" in spClip[i][0] and spClip[i][1] == "True"):
                self.ldialog.sp_spu.setChecked(True)
        if customValue != None:
            self.ldialog.ManualLine.setText(customValue[0])
class Workstation_Dialog(QtWidgets.QDialog):
    def __init__(self):
        super(Workstation_Dialog, self).__init__()
        self.wdialog = Ui_workstation_Dialog()
        self.wdialog.setupUi(self)
        self.licensesToExport = ""
        self.spToExport = ""
        self.licensesToImport = []
        self.importedLicenses = []
        self.importedSP = []
        self.importedManual = ""
        self.licensesSPtoImport = []
        self.LicensesOpened = False
        self.wdialog.confirm_button.clicked.connect(self.confirmPressed)
        self.wdialog.check_button.clicked.connect(self.verification)
        self.wdialog.licenses.clicked.connect(self.open_workstationDialog_licenses)
        self.infoBox() #By adding self.infoBox() when ending __init__, it puts "" inside infobox fields thus making the app not crash when pressing X or esc
    def confirmPressed(self):
        self.infoBox()
        self.close()
    def verification(self):
        notimplemented = QtWidgets.QMessageBox()
        notimplemented.setIcon(QtWidgets.QMessageBox.Critical)
        notimplemented.setText('To be implemented...')
        notimplemented.setWindowTitle("Work in Progress")
        notimplemented.exec_()
    def infoBox(self):
        self.softwarever = self.wdialog.softwarever_text.text()
        self.upgradefrom = self.wdialog.upgradefrom_text.text()
        self.dspver = self.wdialog.dspver_text.text()
        self.imagever = self.wdialog.imagever_text.text()
        self.servicetag = self.wdialog.servicetag_text.text()
        self.wsconf = self.wdialog.wsconf_text.text()
        self.wsmodel = self.wdialog.wsmodel_text.text()
        self.solios = self.wdialog.solios_check.isChecked()
        self.performance = self.wdialog.performance_check.isChecked()
        self.gpu = self.wdialog.gpu_text.text()
    def fillFields(self, clip):
        self.wdialog.softwarever_text.setText(clip[0])
        self.wdialog.upgradefrom_text.setText(clip[1])
        self.wdialog.dspver_text.setText(clip[2])
        self.wdialog.imagever_text.setText(clip[3])
        self.wdialog.servicetag_text.setText(clip[4])
        self.wdialog.wsconf_text.setText(clip[5])
        self.wdialog.wsmodel_text.setText(clip[6])
        self.wdialog.gpu_text.setText(clip[9])
        if clip[7] == "True":
            self.wdialog.solios_check.setChecked(True)
        else:
            self.wdialog.solios_check.setChecked(False)
        try:
            if clip[8] == "True":
                self.wdialog.performance_check.setChecked(True)
            else:
                self.wdialog.performance_check.setChecked(False)
        except:
            self.wdialog.performance_check.setChecked(False)
            warning = QtWidgets.QMessageBox()
            warning.setText("You imported an older version XML, please inspect performance and GPU fields.")
            warning.setWindowTitle("Warning")
            warning.exec_()

        self.infoBox() #After filling fields also apply values to self.values.
    def open_workstationDialog_licenses(self):
        if not self.LicensesOpened:
            self.licenseDialog = Licenses_Dialog(self)
            self.LicensesOpened = True
        self.licenseDialog.exec_()
        Licenses = self.licenseDialog.licenseClip
        self.licensesToImport = Licenses
        toExportLicenses = ""
        for i in range (len(Licenses)):
            if Licenses[i][1]:
                toExportLicenses += Licenses[i][0]+', '
        self.licensesToExport = toExportLicenses[:-2] #Deletes the , 
        toExportSP = ""
        spLicenses = self.licenseDialog.spClip
        self.licensesSPtoImport = spLicenses
        for i in range(len(spLicenses)):
            if spLicenses[i][1]:
                toExportSP += spLicenses[i][0]+', '
        self.spToExport = toExportSP[:-2]
class Catheters_Dialog(QtWidgets.QDialog):
    def __init__(self):
        super(Catheters_Dialog, self).__init__()
        self.cdialog = catheters_Ui()
        self.cdialog.setupUi(self)
        self.cdialog.confirm_button.clicked.connect(self.confirmPressed)
        self.cdialog.check_button.clicked.connect(self.verification)
        self.infoBox() #By adding self.infoBox() when ending __init__, it puts "" inside infobox fields thus making the app not crash when pressing X or esc
    def confirmPressed(self):
        self.infoBox()
        self.close()
    def verification(self):
        notimplemented = QtWidgets.QMessageBox()
        notimplemented.setIcon(QtWidgets.QMessageBox.Critical)
        notimplemented.setText('To be implemented...')
        notimplemented.setWindowTitle("Work in Progress")
        notimplemented.exec_()
    def infoBox(self):
        self.Catfamily = self.cdialog.mfg_text_2.text()
        self.CatMFG = self.cdialog.mfg_text.text()
class Stockert_Dialog(QtWidgets.QDialog):
    def __init__(self):
        super(Stockert_Dialog, self).__init__()
        self.stdialog = stockert_Ui()
        self.stdialog.setupUi(self)
        self.stdialog.confirm_button.clicked.connect(self.confirmPressed)
        self.stdialog.check_button.clicked.connect(self.verification)
        self.infoBox() #By adding self.infoBox() when ending __init__, it puts "" inside infobox fields thus making the app not crash when pressing X or esc
    def confirmPressed(self):
        self.infoBox()
        self.close()
    def verification(self):
        notimplemented = QtWidgets.QMessageBox()
        notimplemented.setIcon(QtWidgets.QMessageBox.Critical)
        notimplemented.setText('To be implemented...')
        notimplemented.setWindowTitle("Work in Progress")
        notimplemented.exec_()
    def infoBox(self):
        self.sysSW = self.stdialog.software_text.text()
        self.sn = self.stdialog.SN_text.text()
        self.epCable = self.stdialog.EPcable_text.text()
        self.abaadaCable = self.stdialog.abaadaCable_text.text()
        self.epboxSN = self.stdialog.epboxSN_text.text()
        self.epioCable = self.stdialog.epioCable_text.text()
        self.infoList = [self.sysSW, self.sn, self.epCable, self.abaadaCable, self.epboxSN, self.epioCable]
    def fillFields(self, clip):
        self.stdialog.software_text.setText(clip[0])
        self.stdialog.SN_text.setText(clip[1])
        self.stdialog.EPcable_text.setText(clip[2])
        self.stdialog.abaadaCable_text.setText(clip[3])
        self.stdialog.epboxSN_text.setText(clip[4])
        self.stdialog.epioCable_text.setText(clip[5])
        self.infoBox() #After filling fields also apply values to self.values.
class SmartAblate_Dialog(QtWidgets.QDialog):
    def __init__(self):
        super(SmartAblate_Dialog, self).__init__()
        self.sadialog = smartablate_Ui()
        self.sadialog.setupUi(self)
        self.sadialog.confirm_button.clicked.connect(self.confirmPressed)
        self.sadialog.check_button.clicked.connect(self.verification)
        self.infoBox() #By adding self.infoBox() when ending __init__, it puts "" inside infobox fields thus making the app not crash when pressing X or esc
    def confirmPressed(self):
        self.infoBox()
        self.close()
    def verification(self):
        notimplemented = QtWidgets.QMessageBox()
        notimplemented.setIcon(QtWidgets.QMessageBox.Critical)
        notimplemented.setText('To be implemented...')
        notimplemented.setWindowTitle("Work in Progress")
        notimplemented.exec_()
    def infoBox(self):
        self.sysSW = self.sadialog.software_text.text()
        self.sn = self.sadialog.SN_text.text()
        self.cables = self.sadialog.cables_text.text()
        self.infoList = [self.sysSW, self.sn, self.cables]
    def fillFields(self, clip):
        self.sadialog.software_text.setText(clip[0])
        self.sadialog.SN_text.setText(clip[1])
        self.sadialog.cables_text.setText(clip[2])
        self.infoBox() #After filling fields also apply values to self.values.
class nGEN_Dialog(QtWidgets.QDialog):
    def __init__(self):
        super(nGEN_Dialog, self).__init__()
        self.ngdialog = ngen_Ui()
        self.ngdialog.setupUi(self)
        self.ngdialog.confirm_button.clicked.connect(self.confirmPressed)
        self.ngdialog.check_button.clicked.connect(self.verification)
        self.infoBox() #By adding self.infoBox() when ending __init__, it puts "" inside infobox fields thus making the app not crash when pressing X or esc
    def confirmPressed(self):
        self.infoBox()
        self.close()
    def verification(self):
        notimplemented = QtWidgets.QMessageBox()
        notimplemented.setIcon(QtWidgets.QMessageBox.Critical)
        notimplemented.setText('To be implemented...')
        notimplemented.setWindowTitle("Work in Progress")
        notimplemented.exec_()
    def infoBox(self):
        self.consoleSN = self.ngdialog.consoleSN_text.text()
        self.consolePN = self.ngdialog.consolePN_text.text()
        self.consoleV = self.ngdialog.consoleV_text.text()
        self.psuSN = self.ngdialog.psuSN_text.text()
        self.psuPN = self.ngdialog.psuPN_text.text()
        self.psuCable = self.ngdialog.psuCable_text.text()
        self.genToPiu = self.ngdialog.genToPiu_text.text()
        self.monitor2SN = self.ngdialog.monitor2SN_text.text()
        self.monitor2PN = self.ngdialog.monitor2PN_text.text()
        self.monitor2V = self.ngdialog.monitor2V_text.text()
        self.monitor2HubSN = self.ngdialog.monitor2HubSN_text.text()
        self.monitor2HubPN = self.ngdialog.monitor2HubPN_text.text()
        self.monitor2PsuSN = self.ngdialog.monitor2PsuSN_text.text()
        self.monitor2PsuPN = self.ngdialog.monitor2PsuPN_text.text()
        self.monitor1SN = self.ngdialog.monitor1SN_text.text()
        self.monitor1PN = self.ngdialog.monitor1PN_text.text()
        self.monitor1V = self.ngdialog.monitor1V_text.text()
        self.monitor1HubSN = self.ngdialog.monitor1HubSN_text.text()
        self.monitor1HubPN = self.ngdialog.monitor1HubPN_text.text()
        self.monitor1PsuSN = self.ngdialog.monitor1PsuSN_text.text()
        self.monitor1PsuPN = self.ngdialog.monitor1PsuPN_text.text()
        self.ngenPumpSN = self.ngdialog.ngenPumpSN_text.text()
        self.ngenPumpPN = self.ngdialog.ngenPumpPN_text.text()
        self.ngenPumpV = self.ngdialog.ngenPumpV_text.text()
        self.pumptoConsoleCable = self.ngdialog.pumptoConsoleCable_text.text()
        self.infoList = [self.consoleSN,self.consolePN,self.consoleV,self.psuSN,self.psuPN,self.psuCable,self.genToPiu,self.monitor1SN,self.monitor1PN,self.monitor1V,self.monitor1HubSN,self.monitor1HubPN,self.monitor1PsuSN,self.monitor1PsuPN,self.monitor2SN,self.monitor2PN,self.monitor2V,self.monitor2HubSN,self.monitor2HubPN,self.monitor2PsuSN,self.monitor2PsuPN,self.ngenPumpSN,self.ngenPumpPN,self.ngenPumpV,self.pumptoConsoleCable]
    def fillFields(self, clip):
        self.ngdialog.consoleSN_text.setText(clip[0])
        self.ngdialog.consolePN_text.setText(clip[1])
        self.ngdialog.consoleV_text.setText(clip[2])
        self.ngdialog.psuSN_text.setText(clip[3])
        self.ngdialog.psuPN_text.setText(clip[4])
        self.ngdialog.psuCable_text.setText(clip[5])
        self.ngdialog.genToPiu_text.setText(clip[6])
        self.ngdialog.monitor1SN_text.setText(clip[7])
        self.ngdialog.monitor1PN_text.setText(clip[8])
        self.ngdialog.monitor1V_text.setText(clip[9])
        self.ngdialog.monitor1HubSN_text.setText(clip[10])
        self.ngdialog.monitor1HubPN_text.setText(clip[11])
        self.ngdialog.monitor1PsuSN_text.setText(clip[12])
        self.ngdialog.monitor1PsuPN_text.setText(clip[13])
        self.ngdialog.monitor2SN_text.setText(clip[14])
        self.ngdialog.monitor2PN_text.setText(clip[15])
        self.ngdialog.monitor2V_text.setText(clip[16])
        self.ngdialog.monitor2HubSN_text.setText(clip[17])
        self.ngdialog.monitor2HubPN_text.setText(clip[18])
        self.ngdialog.monitor2PsuSN_text.setText(clip[19])
        self.ngdialog.monitor2PsuPN_text.setText(clip[20])
        self.ngdialog.ngenPumpSN_text.setText(clip[21])
        self.ngdialog.ngenPumpPN_text.setText(clip[22])
        self.ngdialog.ngenPumpV_text.setText(clip[23])
        self.ngdialog.pumptoConsoleCable_text.setText(clip[24])
        self.infoBox() #After filling fields also apply values to self.values.
class nMARQ_Dialog(QtWidgets.QDialog):
    def __init__(self):
        super(nMARQ_Dialog, self).__init__()
        self.nmdialog = nmarq_Ui()
        self.nmdialog.setupUi(self)
        self.nmdialog.confirm_button.clicked.connect(self.confirmPressed)
        self.nmdialog.check_button.clicked.connect(self.verification)
        self.infoBox() #By adding self.infoBox() when ending __init__, it puts "" inside infobox fields thus making the app not crash when pressing X or esc
    def confirmPressed(self):
        self.infoBox()
        self.close()
    def verification(self):
        notimplemented = QtWidgets.QMessageBox()
        notimplemented.setIcon(QtWidgets.QMessageBox.Critical)
        notimplemented.setText('To be implemented...')
        notimplemented.setWindowTitle("Work in Progress")
        notimplemented.exec_()
    def infoBox(self):
        self.software = self.nmdialog.software_text.text()
        self.SN = self.nmdialog.SN_text.text()
        self.GtoCable = self.nmdialog.GtoCable_text.text()
        self.ethernetCable = self.nmdialog.ethernetCable_text.text()
        self.gToPumpCable = self.nmdialog.gToPumpCable_text.text()
        self.gToM = self.nmdialog.gToM_text.text()
        self.pumpSN = self.nmdialog.pumpSN_text.text()
        self.pumpModel = self.nmdialog.pumpModel_text.text()
        self.footPadel = self.nmdialog.footPadel_text.text()
        self.infoList = [self.software,self.SN,self.GtoCable,self.ethernetCable,self.gToPumpCable, self.gToM,self.pumpSN,self.pumpModel,self.footPadel]
    def fillFields(self, clip):
        self.nmdialog.software_text.setText(clip[0])
        self.nmdialog.SN_text.setText(clip[1])
        self.nmdialog.GtoCable_text.setText(clip[2])
        self.nmdialog.ethernetCable_text.setText(clip[3])
        self.nmdialog.gToPumpCable_text.setText(clip[4])
        self.nmdialog.gToM_text.setText(clip[5])
        self.nmdialog.pumpSN_text.setText(clip[6])
        self.nmdialog.pumpModel_text.setText(clip[7])
        self.nmdialog.footPadel_text.setText(clip[8])
        self.infoBox() #After filling fields also apply values to self.values.
class Pacer_Dialog(QtWidgets.QDialog):
    def __init__(self):
        super(Pacer_Dialog, self).__init__()
        self.pdialog = pacer_Ui()
        self.pdialog.setupUi(self)
        self.pdialog.confirm_button.clicked.connect(self.confirmPressed)
        self.pdialog.check_button.clicked.connect(self.verification)
        self.infoBox() #By adding self.infoBox() when ending __init__, it puts "" inside infobox fields thus making the app not crash when pressing X or esc
    def confirmPressed(self):
        self.infoBox()
        self.close()
    def verification(self):
        notimplemented = QtWidgets.QMessageBox()
        notimplemented.setIcon(QtWidgets.QMessageBox.Critical)
        notimplemented.setText('To be implemented...')
        notimplemented.setWindowTitle("Work in Progress")
        notimplemented.exec_()
    def infoBox(self):
        self.unitSN = self.pdialog.unitSN_text.text()
        self.unitV = self.pdialog.unitV_text.text()
        self.infoList = [self.unitSN, self.unitV]
    def fillFields(self, clip):
        self.pdialog.unitSN_text.setText(clip[0])
        self.pdialog.unitV_text.setText(clip[1])
        self.infoBox() #After filling fields also apply values to self.values.
class Printer_Dialog(QtWidgets.QDialog):
    def __init__(self):
        super(Printer_Dialog, self).__init__()
        self.pdialog = printer_Ui()
        self.pdialog.setupUi(self)
        self.pdialog.confirm_button.clicked.connect(self.confirmPressed)
        self.pdialog.check_button.clicked.connect(self.verification)
        self.infoBox() #By adding self.infoBox() when ending __init__, it puts "" inside infobox fields thus making the app not crash when pressing X or esc
    def confirmPressed(self):
        self.infoBox()
        self.close()
    def verification(self):
        notimplemented = QtWidgets.QMessageBox()
        notimplemented.setIcon(QtWidgets.QMessageBox.Critical)
        notimplemented.setText('To be implemented...')
        notimplemented.setWindowTitle("Work in Progress")
        notimplemented.exec_()
    def infoBox(self):
        self.unitSN = self.pdialog.unitSN_text.text()
        self.unitV = self.pdialog.unitV_text.text()
        self.infoList = [self.unitSN, self.unitV]
    def fillFields(self, clip):
        self.pdialog.unitSN_text.setText(clip[0])
        self.pdialog.unitV_text.setText(clip[1])
        self.infoBox() #After filling fields also apply values to self.values.
class qDotDongle_Dialog(QtWidgets.QDialog):
    def __init__(self):
        super(qDotDongle_Dialog, self).__init__()
        self.qddialog = qdotdongle_Ui()
        self.qddialog.setupUi(self)
        self.qddialog.confirm_button.clicked.connect(self.confirmPressed)
        self.qddialog.check_button.clicked.connect(self.verification)
        self.infoBox() #By adding self.infoBox() when ending __init__, it puts "" inside infobox fields thus making the app not crash when pressing X or esc
    def confirmPressed(self):
        self.infoBox()
        self.close()
    def verification(self):
        notimplemented = QtWidgets.QMessageBox()
        notimplemented.setIcon(QtWidgets.QMessageBox.Critical)
        notimplemented.setText('To be implemented...')
        notimplemented.setWindowTitle("Work in Progress")
        notimplemented.exec_()
    def infoBox(self):
        self.software = self.qddialog.software_text.text()
        self.SN = self.qddialog.SN_text.text()
        self.EPcable = self.qddialog.EPcable_text.text()
        self.infoList = [self.software, self.SN, self.EPcable]
    def fillFields(self, clip):
        self.qddialog.software_text.setText(clip[0])
        self.qddialog.SN_text.setText(clip[1])
        self.qddialog.EPcable_text.setText(clip[2])
        self.infoBox() #After filling fields also apply values to self.values.
class epu_Dialog(QtWidgets.QDialog):
    def __init__(self):
        super(epu_Dialog, self).__init__()
        self.epdialog = epu_Ui()
        self.epdialog.setupUi(self)
        self.epdialog.confirm_button.clicked.connect(self.confirmPressed)
        self.epdialog.check_button.clicked.connect(self.verification)
        self.infoBox() #By adding self.infoBox() when ending __init__, it puts "" inside infobox fields thus making the app not crash when pressing X or esc
    def confirmPressed(self):
        self.infoBox()
        self.close()
    def verification(self):
        notimplemented = QtWidgets.QMessageBox()
        notimplemented.setIcon(QtWidgets.QMessageBox.Critical)
        notimplemented.setText('To be implemented...')
        notimplemented.setWindowTitle("Work in Progress")
        notimplemented.exec_()
    def infoBox(self):
        self.unitSN = self.epdialog.unitSN_text.text()
        self.unitV = self.epdialog.unitV_text.text()
        self.infoList = [self.unitSN, self.unitV]
    def fillFields(self, clip):
        self.epdialog.unitSN_text.setText(clip[0])
        self.epdialog.unitV_text.setText(clip[1])
        self.infoBox() #After filling fields also apply values to self.values.
class Demo_Dialog(QtWidgets.QDialog):
    def __init__(self):
        super(Demo_Dialog, self).__init__()
        self.pdialog = demo_Ui()
        self.pdialog.setupUi(self)
        self.pdialog.confirm_button.clicked.connect(self.confirmPressed)
        self.pdialog.check_button.clicked.connect(self.verification)
        self.infoBox() #By adding self.infoBox() when ending __init__, it puts "" inside infobox fields thus making the app not crash when pressing X or esc
    def confirmPressed(self):
        self.infoBox()
        self.close()
    def verification(self):
        notimplemented = QtWidgets.QMessageBox()
        notimplemented.setIcon(QtWidgets.QMessageBox.Critical)
        notimplemented.setText('To be implemented...')
        notimplemented.setWindowTitle("Work in Progress")
        notimplemented.exec_()
    def infoBox(self):
        self.wsType = self.pdialog.wsType_text.text()
        self.SW = self.pdialog.SW_text.text()
        self.dsp = self.pdialog.dsp_text.text()
        self.imageV = self.pdialog.imageV_text.text()
        self.serviceTag = self.pdialog.serviceTag_text.text()
        self.surpoint = self.pdialog.surpoint_checkbox.isChecked()
        self.infoList = [self.wsType, self.SW,self.dsp,self.imageV,self.serviceTag,str(self.surpoint)]
        self.infoListwithoutSurpoint = [self.wsType, self.SW,self.dsp,self.imageV,self.serviceTag]
    def fillFields(self, clip):
        self.pdialog.wsType_text.setText(clip[0])
        self.pdialog.SW_text.setText(clip[1])
        self.pdialog.dsp_text.setText(clip[2])
        self.pdialog.imageV_text.setText(clip[3])
        self.pdialog.serviceTag_text.setText(clip[4])
        if clip[5] == "True":
            self.pdialog.surpoint_checkbox.setChecked(True)
        else:
           self.pdialog.surpoint_checkbox.setChecked(False)
        self.infoBox() #After filling fields also apply values to self.values.
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    win = MainWindow()
    win.show()
    win.setFocus()
    sys.exit(app.exec_())