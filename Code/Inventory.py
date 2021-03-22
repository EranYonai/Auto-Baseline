import sys
import qdarkstyle
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QListWidget
import sqlite3

class MainWindow(QtWidgets.QMainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		loadUi("inventory.ui", self)
		self.loaddata()
		self.actionRefresh.triggered.connect(self.refresh)

	def loaddata(self):
		connection = sqlite3.connect("equipment.db")
		cur = connection.cursor()
		# constructs tuples for each db, [0] is the db name, [1] is the table object, [2] is the number of columns in db
		workstation = ("workstations", self.ws_table, 8) 
		system = ("systems", self.system_table, 11)
		ultrasound = ("ultrasounds", self.us_table, 7)
		stockert = ("stockerts", self.stockert_table, 13)
		tabs = [workstation, system, ultrasound, stockert]
		for tab in tabs:
			sqlquery = "SELECT * FROM " + tab[0]  # tab[0] = db name
			cur.execute(sqlquery)
			tablerow = 0
			for row in cur.execute(sqlquery):
				column = 0
				for i in range(0, tab[2]):
					tab[1].setItem(tablerow, column, QtWidgets.QTableWidgetItem(str(row[column])))
					column += 1
				tablerow += 1

	def refresh(self):
		# refreshes all tables by removing all rows -> adding new - blank rows -> calling loadata().
		rows = 300
		self.ws_table.setRowCount(0)
		self.system_table.setRowCount(0)
		self.us_table.setRowCount(0)
		self.stockert_table.setRowCount(0)
		self.ws_table.setRowCount(rows)
		self.system_table.setRowCount(rows)
		self.us_table.setRowCount(rows)
		self.stockert_table.setRowCount(rows)
		self.loaddata()

if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
	win = MainWindow()
	win.show()
	win.setFocus()
	sys.exit(app.exec_())