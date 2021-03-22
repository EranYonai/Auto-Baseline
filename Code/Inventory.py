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


	def loaddata(self):
		connection = sqlite3.connect("equipment.db")
		cur = connection.cursor()
		sqlquery = "SELECT * FROM workstations"
		cur.execute(sqlquery)
		tablerow = 0
		for row in cur.execute(sqlquery):
			print(row)
			print(QtWidgets.QTableWidgetItem(row[0]).text())
			self.ws_table.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
			self.ws_table.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
			self.ws_table.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
			self.ws_table.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))
			self.ws_table.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row[4]))
			self.ws_table.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(row[5]))
			self.ws_table.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(row[6]))
			self.ws_table.setItem(tablerow, 7, QtWidgets.QTableWidgetItem(row[7]))
			tablerow += 1


if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
	win = MainWindow()
	win.show()
	win.setFocus()
	sys.exit(app.exec_())