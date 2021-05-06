import os
import sqlite3
import sys
import time

import qdarkstyle
from PyQt5 import QtWidgets, uic

import cfg


# experimentalWarning is a function that takes (self, kind) as arguments.
# Pops the appropriate error or notification
# :param kind - 'table_refreshed' will print an "Database changed!" notification.
# :param kind - 'admin_wrong' will print an "Admin Password is wrong" warning.
def experimental_warning(kind):
    if kind == "table_refreshed":
        warning = QtWidgets.QMessageBox()
        warning.setText("Database changed!")
        warning.setIcon(1)  # Set Icon enums: 0::noIcon, 1::Info, 2::Warning, 3::Critical, 4::Question
        warning.setWindowTitle("Notification")
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
        uic.loadUi("inventory.ui", self)
        self.resize(1050, 1070)

        # Global attributes:
        self.action_db = self.menuActions.addMenu('Databases')

        # Triggers and connections:
        self.search_button.clicked.connect(self.search)
        self.editMode_button.clicked.connect(self.editmode_button_function)
        self.refresh_button.clicked.connect(self.refresh)
        self.action_db.triggered.connect(self.choose_database)
        self.actionCreateDB.triggered.connect(self.manage_database)

        # On initialization:
        self.load_db_menu()
        self.db_current = self.current_db("db\\V7.db")
        self.load_data()  # First load of data - current_db is the default
        # refresh_thread = threading.Thread(target=self.auto_refresh, args=(20, ))
        # refresh_thread.start()

    def create_tabs_tuples(self):
        workstation = (cfg.TABLE_NAMES['WORKSTATION'], self.ws_table, 8, cfg.TABLE_FIELDS['WS'])
        system = (cfg.TABLE_NAMES['SYSTEM'], self.system_table, 11, cfg.TABLE_FIELDS['SYSTEM'])
        ultrasound = (cfg.TABLE_NAMES['ULS'], self.us_table, 8, cfg.TABLE_FIELDS['ULS'])
        stockert = (cfg.TABLE_NAMES['STOCKERT'], self.stockert_table, 13, cfg.TABLE_FIELDS['STOCKERT'])
        ngen = (cfg.TABLE_NAMES['NGEN'], self.ngen_table, 27, cfg.TABLE_FIELDS['NGEN'])
        nmarq = (cfg.TABLE_NAMES['NMARQ'], self.nmarq_table, 11, cfg.TABLE_FIELDS['NMARQ'])
        smartablate = (cfg.TABLE_NAMES['SMARTABLATE'], self.smartablate_table, 7, cfg.TABLE_FIELDS['SMARTABLATE'])
        pacer = (cfg.TABLE_NAMES['PACER'], self.pacer_table, 4, cfg.TABLE_FIELDS['PACER'])
        dongle = (cfg.TABLE_NAMES['DONGLE'], self.dongles_table, 5, cfg.TABLE_FIELDS['DONGLE'])
        epu = (cfg.TABLE_NAMES['EPU'], self.epu_table, 4, cfg.TABLE_FIELDS['EPU'])
        printer = (cfg.TABLE_NAMES['PRINTER'], self.printer_table, 4, cfg.TABLE_FIELDS['PRINTER'])
        spu = (cfg.TABLE_NAMES['SPU'], self.spu_table, 29, cfg.TABLE_FIELDS['SPU'])
        demo = (cfg.TABLE_NAMES['DEMO'], self.demo_table, 7, cfg.TABLE_FIELDS['DEMO'])
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

    def current_db(self, db):
        db_name = db[3:][:-3]  # Need to remove db\\V7.db first 3 char and last 3 char to get just the name.
        for action in self.action_db.actions():
            if action.text() != db_name:
                action.setChecked(False)
            else:
                action.setChecked(True)
        return db

    def refresh(self):
        # refreshes all tables by removing all rows -> adding new - blank rows -> calling loadata().
        self.stop_edit_listener()  # stops listener before refreshing lists.
        if self.editMode_button.isChecked():
            experimental_warning("exited_edit_mode")
            self.editMode_button.setChecked(False)  # exits edit mode

        rows = 300
        tabs = self.create_tabs_tuples()
        for tab in tabs:
            tab[1].setRowCount(0)
            tab[1].setRowCount(rows)
        self.load_data()
        print("Tables refreshed!")

    def auto_refresh(self, sleep_for):
        while True:
            for i in range(sleep_for):
                self.refresh_button.setText("Refresh in:  " + str(i))
                time.sleep(1)
            self.refresh()

    # 		#  https://stackoverflow.com/questions/49886313/how-to-run-a-while-loop-with-pyqt5
    #       #  https://realpython.com/python-pyqt-qthread/

    def search(self):
        pass

    def manage_database(self):
        # Starts by asking for password, not everyone can create a new db.
        input_password, pressed_ok = QtWidgets.QInputDialog.getText(self, 'Admin Password', 'Enter Admin password:')
        if pressed_ok and input_password == cfg.PASSWORDS['DB_MANAGER']:
            self.create_database()
        if pressed_ok and input_password != cfg.PASSWORDS['DB_MANAGER']:
            experimental_warning('admin_wrong')

    def create_database(self):
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
            print("create_database: new database created! " + db_name)

    def load_db_menu(self):
        db_list = os.listdir(cfg.FILE_PATHS['DB_LOCATION'])
        # db_list = ['V7', 'V8', 'Test']  # Test, ^uncomment above line for real usage.
        # Need to remove all actions first::
        # https://stackoverflow.com/questions/51333771/removing-dynamically-created-qmenu-items
        for db in db_list:
            action = self.action_db.addAction(db[:-3])  # db[:-3] removes the .db from the file name
            # action = self.action_db.addAction(db)  # Test, ^uncomment above line for real usage.
            action.setCheckable(True)

    def choose_database(self, action):
        try:
            database_name = action.text()
            database_bool = action.isChecked()
            if database_bool:  # If true, turn all other menus to false
                for action in self.action_db.actions():
                    if action.text() != database_name:
                        action.setChecked(False)
            self.db_current = cfg.FILE_PATHS['DB_LOCATION'] + database_name + '.db'
            # changes db_current to the selected db and runs refresh function
            self.refresh()
            # experimental_warning('table_refreshed') - Annoying
        except Exception as e:
            print('Exception in choose_database: ' + str(e))

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

# TODO:
#  V need to create a special function and button from the top menu (file menu) that creates a new db
#  ----
#  need to choose on statup which db to use >> username & password, when connected, insert to a new db accounts:
#  Because I want to know how many users use/change/refresh each db to mitigate\prevent possible issues.
#  |username| |password| |currently_connected_to|
#  |EYonai  | |1234    | |'V7'                  |
#  When exiting program, remove the connected user currently_connected_to cell
#  When refreshing database, change a label to currently connected: 'x' by looping through the users and see if
#  len(currently_connected) >= 0 if yes, and if this is the current shown db, add +1 to currently connected label
#  ----
#  need to change position of refresh button - maybe think of a better logic? every x sec? maybe change times based on
#  how many users are connected to this db?
#  interesting articles:
#  https://www.programmersought.com/article/35244519297/
#  https://forum.qt.io/topic/87141/while-retrieving-data-from-qtablewidget-the-type-appears-to-be-unicode-how-can-i-convert-it-to-number/5
#  https://stackoverflow.com/questions/40188267/how-to-update-qtableview-when-database-updated
#  https://realpython.com/python-pyqt-qthread/
