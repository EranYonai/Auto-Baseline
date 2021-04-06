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
    if kind == "exited_edit_mode":
        warning = QtWidgets.QMessageBox()
        warning.setText("Exited edit mode!")
        warning.setIcon(2)  # Set Icon enums: 0::noIcon, 1::Info, 2::Warning, 3::Critical, 4::Question
        warning.setWindowTitle("Notification")
        warning.exec_()


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("inventory.ui", self)
        self.resize(1050, 1070)

        # Global attributes:
        self.db_current = "db\\V8.db"  # default db
        self.db_location = "C:\\Users\\eyonai\\OneDrive - JNJ\\Documents\\GitHub\\Baseliner\\Code\\db"
        self.action_db = self.menuActions.addMenu('Databases')
        # Triggeres and connections:
        self.search_button.clicked.connect(self.search)
        self.editMode_button.clicked.connect(self.editmode_button_function)
        self.refresh_button.clicked.connect(self.refresh)
        self.action_db.triggered.connect(self.choose_database)
        self.actionCreateDB.triggered.connect(self.manage_database)
        # Function calls:
        self.load_db_menu()
        self.load_data()  # First load of data - current_db is the default

    def create_tabs_tuples(self):
        ws_db_fields = [["service_tag", "STRING PRIMARY KEY"], ["dsp_version", "STRING"], ["image_version", "STRING"],
                        ["configuration", "STRING"], ["model", "STRING"], ["graphics_card", "STRING"],
                        ["approved", "BOOLEAN"], ["used", "INTEGER"]]
        system_db_fields = [["system_number", "STRING PRIMARY KEY"], ["piu_configuration", "STRING"],
                            ["lp_number", "STRING"], ["patch_unit", "STRING"], ["monitor_1", "STRING"],
                            ["monitor_2", "STRING"], ["ecg_phantom", "STRING"], ["aquarium_number", "STRING"],
                            ["aquarium_maximo", "STRING"], ["approved", "BOOLEAN"], ["used", "INTEGER"]]
        us_db_fields = [["serial_number", "STRING PRIMARY KEY"], ["machine", "STRING"], ["software_version", "STRING"],
                        ["application_version", "STRING"], ["video_cable", "STRING"],
                        ["ethernet_cable", "STRING"], ["approved", "BOOLEAN"], ["used", "INTEGER"]]
        stockert_db_fields = [["software_version", "STRING PRIMARY KEY"], ["serial_number", "STRING"],
                              ["epio_box_sn", "STRING"], ["epio_connection_cable", "STRING"],
                              ["epio_interface_cable", "STRING"], ["epushuttle_piu", "STRING"],
                              ["global_port", "STRING"],
                              ["ablation_adaptor_cable", "STRING"], ["gen_to_ws_cable", "STRING"],
                              ["patch_elect_cable", "STRING"], ["footpedal", "STRING"], ["approved", "BOOLEAN"],
                              ["used", "INTEGER"]]
        ngen_db_fields = [["console_sn", "STRING PRIMARY KEY"], ["console_pn", "STRING"],
                          ["console_version", "STRING"], ["psu_sn", "STRING"],
                          ["psu_pn", "STRING"], ["psu_cable", "STRING"],
                          ["gen_to_piu", "STRING"], ["monitor1_sn", "STRING"], ["monitor1_pn", "STRING"],
                          ["monitor1_ver", "STRING"], ["monitor1_hubsn", "STRING"], ["monitor1_hubpn", "STRING"],
                          ["monitor1_psusn", "STRING"],
                          ["monitor1_psupn", "STRING"], ["monitor2_sn", "STRING"],
                          ["monitor2_pn", "STRING"], ["monitor2_version", "STRING"], ["monitor2_hubsn", "STRING"],
                          ["monitor2_hubpn", "STRING"], ["monitor2_psusn", "STRING"], ["monitor2_psupn", "STRING"],
                          ["pump_sn", "STRING"], ["pump_pn", "STRING"], ["pump_version", "STRING"],
                          ["pump_to_console", "STRING"], ["foot_pedal", "STRING"], ["approved", "BOOLEAN"],
                          ["used", "INTEGER"]]
        nmarq_db_fields = [["serial_number", "STRING PRIMARY KEY"], ["software_version", "STRING"],
                           ["gen_to_carto", "STRING"], ["ethernet", "STRING"],
                           ["gen_to_pump", "STRING"], ["gen_to_monitor", "STRING"],
                           ["pump_sn", "STRING"],
                           ["pump_model", "STRING"], ["foot_pedal", "STRING"], ["approved", "BOOLEAN"],
                           ["used", "INTEGER"]]
        smartablate_db_fields = [["serial_number", "STRING PRIMARY KEY"], ["software_version", "STRING"],
                                 ["gen_to_piu", "STRING"], ["gen_to_ws", "STRING"],
                                 ["foot_pedal", "STRING"], ["approved", "BOOLEAN"],
                                 ["used", "INTEGER"]]
        pacer_db_fields = [["serial_number", "STRING PRIMARY KEY"], ["type", "STRING"], ["approved", "BOOLEAN"],
                           ["used", "INTEGER"]]
        dongle_db_fields = [["serial_number", "STRING PRIMARY KEY"], ["software_version", "STRING"],
                            ["hardware_version", "STRING"], ["approved", "BOOLEAN"],
                            ["used", "INTEGER"]]
        epu_db_fields = [["serial_number", "STRING PRIMARY KEY"], ["version", "STRING"], ["approved", "BOOLEAN"],
                         ["used", "INTEGER"]]
        printer_db_fields = [["serial_number", "STRING PRIMARY KEY"], ["model", "STRING"], ["approved", "BOOLEAN"],
                             ["used", "INTEGER"]]
        spu_db_fields = [["serial_number", "STRING PRIMARY KEY"], ["pn", "STRING"],
                         ["software_version", "STRING"], ["main_fw_version", "STRING"],
                         ["secondary_fw_version", "STRING"], ["front_board_location", "STRING"],
                         ["front_board_location_rev", "STRING"],
                         ["led_board", "STRING"], ["led_board_rev", "STRING"], ["mother_board", "STRING"],
                         ["mother_board_rev", "STRING"],
                         ["back_board", "STRING"], ["back_board_rev", "STRING"], ["power_board", "STRING"],
                         ["power_board_rev", "STRING"],
                         ["upper_board", "STRING"], ["upper_board_rev", "STRING"], ["pacing_board", "STRING"],
                         ["pacing_board_rev", "STRING"],
                         ["tpi_board", "STRING"], ["tpi_board_rev", "STRING"], ["digital_board", "STRING"],
                         ["digital_board_rev", "STRING"],
                         ["ecg_board", "STRING"], ["ecg_board_rev", "STRING"], ["spu_pro", "STRING"],
                         ["spu_pro_rev", "STRING"], ["approved", "BOOLEAN"],
                         ["used", "INTEGER"]]
        demo_db_fields = [["service_tag", "STRING PRIMARY KEY"], ["ws_type", "STRING"],
                          ["sw_version", "STRING"], ["dsp_version", "STRING"],
                          ["image_version", "STRING"], ["approved", "BOOLEAN"],
                          ["used", "INTEGER"]]
        workstation = ("workstations", self.ws_table, 8, ws_db_fields)
        system = ("systems", self.system_table, 11, system_db_fields)
        ultrasound = ("ultrasounds", self.us_table, 8, us_db_fields)
        stockert = ("stockerts", self.stockert_table, 13, stockert_db_fields)
        ngen = ("ngens", self.ngen_table, 27, ngen_db_fields)
        nmarq = ("nmarqs", self.nmarq_table, 11, nmarq_db_fields)
        smartablate = ("smartablates", self.smartablate_table, 7, smartablate_db_fields)
        pacer = ("pacers", self.pacer_table, 4, pacer_db_fields)
        dongle = ("dongles", self.dongles_table, 5, dongle_db_fields)
        epu = ("epus", self.epu_table, 4, epu_db_fields)
        printer = ("printers", self.printer_table, 4, printer_db_fields)
        spu = ("spus", self.spu_table, 29, spu_db_fields)
        demo = ("demos", self.demo_table, 7, demo_db_fields)
        return [system, workstation, ultrasound, stockert, ngen, nmarq, smartablate, pacer, dongle, epu, printer, spu,
                demo]

    def load_data(self):
        try:
            connection = sqlite3.connect(self.db_current)
            cur = connection.cursor()
            # tuples for each db, [0] is the db name, [1] is the table object, [2] is the number of columns in db
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
        except Exception as e:
            print("Exception at load_data: " + str(e))

    def refresh(self):
        # refreshes all tables by removing all rows -> adding new - blank rows -> calling loadata().
        self.stop_edit_listener()  # stops listener before refreshing lists.
        self.editMode_button.setChecked(False)  # exits edit mode
        experimental_warning("exited_edit_mode")
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
    #       #  https://realpython.com/python-pyqt-qthread/

    def search(self):
        pass

    def manage_database(self):
        # Starts by asking for password, not everyone can create a new db. Password: 'dbManager'
        pressed_ok = False
        input_password, pressed_ok = QtWidgets.QInputDialog.getText(self, 'Admin Password', 'Enter Admin password:')
        if pressed_ok and input_password == "dbManager":
            self.create_database()
        else:
            experimental_warning('admin_wrong')

    def create_database(self):
        db_path = self.db_location
        # Solution for db name will be a popup window for now:
        db_name, pressed_ok = QtWidgets.QInputDialog.getText(self, 'Database Name', 'Enter database name:')
        if not pressed_ok:
            db_name = ""
        if db_name != "" and len(db_name) < 10:  # Some verification for db name value.
            connection = sqlite3.connect('db\\' + db_name + '.db')
            cur = connection.cursor()  # Opens connection to db (creates a new db file)
            equipment_tuple = self.create_tabs_tuples()
            for machine in equipment_tuple:  # for each element in equipment tuple
                sql_command = f"CREATE TABLE {machine[0]} ("
                for column in machine[3]:
                    sql_command += f"[{column[0]}] {column[1]}, "
                sql_command = sql_command[:-2] + ')'  # Removes the ', ' at the end and adds ')'
                cur.execute(sql_command)  # Executes the command
            connection.commit()  # Commits the changes
            connection.close()  # Closes connection to db.
            self.load_db_menu()  # Refreshes the menu

    def load_db_menu(self):
        db_list = os.listdir(self.db_location)
        # db_list = ['V7', 'V8', 'Test']  # Test, ^uncomment above line for real usage.
        # Need to remove all actions first::
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
            print("edit_mode: Enabled")
            self.start_edit_listener()
        else:
            print("edit_mode: Disabled")
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
            if itemKey is not None:  # If itemKey is none, it means the user tried to change empty row, do nothing.
                self.update_sql_item(item, itemKey.text(), whichTable)
            else:  # For debug purposes, delete this else on release.
                print("User is editing empty row.")
        except Exception as e:
            print("Exception at on_item_change: " + str(e))

    def update_sql_get_string(self, col, text, key, whichTable):
        tabs = self.create_tabs_tuples()
        query = f"UPDATE {tabs[whichTable][0]} " \
                f"SET {tabs[whichTable][3][col][0]} = '{text}' " \
                f"WHERE {tabs[whichTable][3][0][0]} = '{key}'; "
        return query

    def update_sql_item(self, item, itemKey, whichTable):
        try:
            connection = sqlite3.connect(self.db_current)
            cur = connection.cursor()
            sql_query = self.update_sql_get_string(item.column(), item.text(), itemKey, whichTable)
            cur.execute(sql_query)
            cur.close()
            connection.commit()
            connection.close()
            print(sql_query)
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
#  interesting articles:
#  https://www.programmersought.com/article/35244519297/
#  https://forum.qt.io/topic/87141/while-retrieving-data-from-qtablewidget-the-type-appears-to-be-unicode-how-can-i-convert-it-to-number/5
#  https://stackoverflow.com/questions/40188267/how-to-update-qtableview-when-database-updated
#  https://realpython.com/python-pyqt-qthread/
