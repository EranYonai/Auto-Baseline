import sys
import qdarkstyle
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
import sqlite3

class MainWindow(QtWidgets.QMainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		loadUi("inventory.ui", self)
		self.resize(1050, 1070)
		self.loaddata()
		self.actionRefresh.triggered.connect(self.refresh)
		self.actionUpload.triggered.connect(self.upload)
		self.search_button.clicked.connect(self.search)
		self.editMode_button.clicked.connect(self.editMode_button_function)

	def create_tabs_tuples(self):
		ws_db_fields = ["service_tag", "dsp_version", "image_version", "configuration", "model", "graphics_card", "approved", "used"]
		system_db_fields = ["system_number", "piu_configuration", "lp_number", "patch_unit", "monitor_1", "monitor_2", "ecg_phantom", "aquarium_number", "aquarium_maximo", "approved", "used"]
		us_db_fields = ["serial_number", "machine", "software_version", "application_version", "video_cable", "ethernet_cable", "approved", "used"]
		stockert_db_fields = ["software_version", "serial_number", "epio_box_sn", "epio_connection_cable", "epio_interface_cable", "epushuttle_piu", "global_port", "ablation_adaptor_cable", "gen_to_ws_cable", "patch_elect_cable", "footpedal", "approved", "used"]
		workstation = ("workstations", self.ws_table, 8, ws_db_fields)
		system = ("systems", self.system_table, 11, system_db_fields)
		ultrasound = ("ultrasounds", self.us_table, 7, us_db_fields)
		stockert = ("stockerts", self.stockert_table, 13, stockert_db_fields)
		return [system, workstation, ultrasound, stockert]

	def loaddata(self):
		connection = sqlite3.connect("equipment.db")
		cur = connection.cursor()
		# constructs tuples for each db, [0] is the db name, [1] is the table object, [2] is the number of columns in db
		tabs = self.create_tabs_tuples()
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
		connection.close()

	def refresh(self):
		# refreshes all tables by removing all rows -> adding new - blank rows -> calling loadata().
		self.stop_edit_listener()  # stops listener before refreshing lists.
		self.editMode_button.setChecked(False)  # exits edit mode
		#  maybe pop notification here?
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

	def search(self):
		pass

	def upload(self):
		pass

	def editMode_button_function(self):
		if (self.editMode_button.isChecked()):
			print("editModeEnabled")
			self.start_edit_listener()
		else:
			print("editModeDisabled")
			self.stop_edit_listener()

	def start_edit_listener(self):
		tabs = self.create_tabs_tuples()
		for tab in tabs:
			tab[1].blockSignals(False)  # enable signals from the specific widget
			tab[1].cellChanged.connect(self.onItemChange)

	def stop_edit_listener(self):
		tabs = self.create_tabs_tuples()
		for tab in tabs:
			tab[1].blockSignals(True)  # disable signals from the specific widget

	def onItemChange(self):
		#  self.machines.currentIndex() - 0 systems, 1 workstations, 3 ultrasounds..
		whichTable = self.machines.currentIndex()
		print("signal from " + str(whichTable))
		tabs = self.create_tabs_tuples()
		try:
			item = tabs[whichTable][1].item(tabs[whichTable][1].currentRow(), tabs[whichTable][1].currentColumn())  # gets the item = QTableWidgetItem
			itemKey = tabs[whichTable][1].item(tabs[whichTable][1].currentRow(), 0)
			self.updateItemSQL(item, itemKey.text(), whichTable)
		except Exception as e:
			print(e)

	def update_sql_get_string(self, col, text, key, whichTable):
		tabs = self.create_tabs_tuples()
		query = """UPDATE %s SET %s = '%s' WHERE %s = '%s'; """ % (tabs[whichTable][0], tabs[whichTable][3][col], text, tabs[whichTable][3][0], key)
		return query

	def updateItemSQL(self, item, itemKey, whichTable):
		print("itemAt: %s/%s, text: %s, primarykey: %s" % (item.row(), item.column(), item.text(), itemKey))
		try:
			connection = sqlite3.connect("equipment.db")
			cur = connection.cursor()
			sqlquery = self.update_sql_get_string(item.column(), item.text(), itemKey, whichTable)
			cur.execute(sqlquery)
			print(sqlquery)
			cur.close()
			connection.commit()
			connection.close()
			print("Update command was sent to DB! DB should've updated!")
		except Exception as e:
			print("Exception at updateItemSQL:")
			print(e)


if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
	win = MainWindow()
	win.show()
	win.setFocus()
	sys.exit(app.exec_())