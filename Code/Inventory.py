import sys, sqlite3, time, os
import qdarkstyle
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets


# experimentalWarning is a function that takes (self, kind) as arguments.
# Pops the appropriate error or notification
# :param kind - 'table_refreshed' will print an "Database changed!" notification.
# :param kind - 'admin_wrong' will print an "Admin Password is wrong" warning.
def experimental_warning(kind):
    if kind == "table_refreshed":
        warning = QtWidgets.QMessageBox()
        warning.setText("Database changed!")
        warning.setIcon(1)  # Set Icon enums: 0::noIcon, 1::Info, 2::Warning, 3::Critical, 4::Question
        warning.setWindowTitle("Noticication")
        warning.exec_()
    if kind == "admin_wrong":
        warning = QtWidgets.QMessageBox()
        warning.setText("Admin password is wrong.")
        warning.setIcon(2)  # Set Icon enums: 0::noIcon, 1::Info, 2::Warning, 3::Critical, 4::Question
        warning.setWindowTitle("Warning")
        warning.exec_()


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("inventory.ui", self)
        self.resize(1050, 1070)

        # Global attributes:
        self.db_current = "db\\equipment.db"  # default db
        self.db_location = "C:\\Users\\eyonai\\OneDrive - JNJ\\Documents\\GitHub\\Baseliner\\Code\\db"
        self.action_db = self.menuActions.addMenu('Databases')
        # Triggeres and connections:
        self.load_data()
        self.search_button.clicked.connect(self.search)
        self.editMode_button.clicked.connect(self.editmode_button_function)
        self.refresh_button.clicked.connect(self.refresh)
        self.action_db.triggered.connect(self.choose_database)
        self.actionCreateDB.triggered.connect(self.create_database)
        # Function calls:
        self.find_database()

    def create_tabs_tuples(self):
        ws_db_fields = ["service_tag", "dsp_version", "image_version", "configuration", "model", "graphics_card",
                        "approved", "used"]
        system_db_fields = ["system_number", "piu_configuration", "lp_number", "patch_unit", "monitor_1", "monitor_2",
                            "ecg_phantom", "aquarium_number", "aquarium_maximo", "approved", "used"]
        us_db_fields = ["serial_number", "machine", "software_version", "application_version", "video_cable",
                        "ethernet_cable", "approved", "used"]
        stockert_db_fields = ["software_version", "serial_number", "epio_box_sn", "epio_connection_cable",
                              "epio_interface_cable", "epushuttle_piu", "global_port", "ablation_adaptor_cable",
                              "gen_to_ws_cable", "patch_elect_cable", "footpedal", "approved", "used"]
        workstation = ("workstations", self.ws_table, 8, ws_db_fields)
        system = ("systems", self.system_table, 11, system_db_fields)
        ultrasound = ("ultrasounds", self.us_table, 8, us_db_fields)
        stockert = ("stockerts", self.stockert_table, 13, stockert_db_fields)
        return [system, workstation, ultrasound, stockert]

    def load_data(self):
        connection = sqlite3.connect(self.db_current)
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
        tabs = self.create_tabs_tuples()
        for tab in tabs:
            tab[1].setRowCount(0)
            tab[1].setRowCount(rows)
        self.load_data()
        print("Tables refreshed!")

    # def auto_refresh(self):
    # 	while True:
    # 		for i in range(0, 10):
    # 			self.refresh_button.setText("Refresh " + str(i))
    # 			time.sleep(1)
    # 			self.refresh()
    # 		#  https://stackoverflow.com/questions/49886313/how-to-run-a-while-loop-with-pyqt5

    def search(self):
        pass

    def create_database(self):
        # Starts by asking for password, not everyone can create a new db. Password: 'dbManager'
        pressed_ok = False
        input_password, pressed_ok = QtWidgets.QInputDialog.getText(self, 'Admin Password', 'Enter Admin password:')
        if pressed_ok and input_password == "dbManager":
            print("ADMIN! can create dbs!")
        else:
            experimental_warning('admin_wrong')

    def find_database(self):
        db_list = os.listdir(self.db_location)
        # db_list = ['V7', 'V8', 'Test']  # Test, ^uncomment above line for real usage.
        for db in db_list:
            action = self.action_db.addAction(db[:-3])  # db[:-3] removes the .db from the file name
            # action = self.action_db.addAction(db)  # Test, ^uncomment above line for real usage.
            action.setCheckable(True)

    def choose_database(self, action):
        database_name = action.text()
        database_bool = action.isChecked()
        if database_bool:  # If true, turn all other menus to false
            for action in self.action_db.actions():
                if action.text() != database_name:
                    action.setChecked(False)
        self.db_current = 'db\\' + database_name + '.db'  # changes db_current to the selected db and runs refresh function
        self.refresh()
        experimental_warning('table_refreshed')

    def editmode_button_function(self):
        if self.editMode_button.isChecked():
            print("editModeEnabled")
            self.start_edit_listener()
        else:
            print("editModeDisabled")
            self.stop_edit_listener()

    def start_edit_listener(self):
        tabs = self.create_tabs_tuples()
        for tab in tabs:
            tab[1].blockSignals(False)  # enable signals from the specific widget
            tab[1].cellChanged.connect(self.on_item_change)

    def stop_edit_listener(self):
        tabs = self.create_tabs_tuples()
        for tab in tabs:
            tab[1].blockSignals(True)  # disable signals from the specific widget

    def on_item_change(self):
        #  self.machines.currentIndex() - 0 systems, 1 workstations, 3 ultrasounds..
        whichTable = self.machines.currentIndex()
        tabs = self.create_tabs_tuples()
        try:
            item = tabs[whichTable][1].item(tabs[whichTable][1].currentRow(),
                                            tabs[whichTable][1].currentColumn())  # gets the item = QTableWidgetItem
            itemKey = tabs[whichTable][1].item(tabs[whichTable][1].currentRow(), 0)
            self.update_sql_item(item, itemKey.text(), whichTable)
        except Exception as e:
            print("Exception at on_item_change: " + str(e))

    def update_sql_get_string(self, col, text, key, whichTable):
        tabs = self.create_tabs_tuples()
        query = f"""UPDATE {tabs[whichTable][0]} SET {tabs[whichTable][3][col]} = '{text}' WHERE {tabs[whichTable][3][0]} = '{key}'; """
        return query

    def update_sql_item(self, item, itemKey, whichTable):
        try:
            connection = sqlite3.connect(self.db_current)
            cur = connection.cursor()
            sqlquery = self.update_sql_get_string(item.column(), item.text(), itemKey, whichTable)
            cur.execute(sqlquery)
            cur.close()
            connection.commit()
            connection.close()
            print(sqlquery)
        except Exception as e:
            print("Exception at update_sql_item: " + str(e))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    win = MainWindow()
    win.show()
    win.setFocus()
    sys.exit(app.exec_())

#  need to create a special function and button from the top menu (file menu) that creates a new db
#  need to choose on statup which db to use
#  need to change position of refresh button - maybe think of a better logic? every x sec?
#  intersting articles:
#  https://www.programmersought.com/article/35244519297/
#  https://forum.qt.io/topic/87141/while-retrieving-data-from-qtablewidget-the-type-appears-to-be-unicode-how-can-i-convert-it-to-number/5
#  https://stackoverflow.com/questions/40188267/how-to-update-qtableview-when-database-updated
#  https://realpython.com/python-pyqt-qthread/
