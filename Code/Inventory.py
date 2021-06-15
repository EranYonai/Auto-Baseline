import os
import sqlite3
import sys
import time
import logging
import qdarkstyle
import cfg
import shutil
import pandas  # used to export to excel
import openpyxl  # used by Pandas when working with excel
import xlsxwriter  # used by Pandas when working with excel
import os  # used to launch the excel file on the user's machine after it was created
from PyQt5 import QtWidgets, uic, QtGui


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
        logging.info("Change Database")
    if kind == "admin_wrong":
        warning = QtWidgets.QMessageBox()
        warning.setText("Admin password is wrong.")
        warning.setIcon(2)  # Set Icon enums: 0::noIcon, 1::Info, 2::Warning, 3::Critical, 4::Question
        warning.setWindowTitle("Warning")
        warning.exec_()
        logging.info("user input admin password is wrong")
    if kind == "exited_edit_mode":
        warning = QtWidgets.QMessageBox()
        warning.setText("Exited edit mode!")
        warning.setIcon(2)  # Set Icon enums: 0::noIcon, 1::Info, 2::Warning, 3::Critical, 4::Question
        warning.setWindowTitle("Notification")
        warning.exec_()
        logging.info("exited edit mode")
    if kind == "permission_error":
        warning = QtWidgets.QMessageBox()
        warning.setText(
            "We don't have premission to do that. \nTry closing all open Excel files, \nor selecting a different name.")
        warning.setIcon(2)  # Set Icon enums: 0::noIcon, 1::Info, 2::Warning, 3::Critical, 4::Question
        warning.setWindowTitle("Notification")
        warning.exec_()


def start_logger():
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)
    logging.basicConfig(filename=cfg.FILE_PATHS['INVENTORY_LOG'],
                        filemode='a',  # Change to w if you want log file to delete before start writing new logs.
                        format='%(asctime)s - %(levelname)s %(funcName)s: %(message)s',
                        datefmt='%H:%M:%S',
                        level=logging.DEBUG)
    logging.warning("-----------Start Application-----------")
    logging.debug("Logs location: " + cfg.FILE_PATHS['INVENTORY_LOG'])
    logging.debug("DB_LOCATION: " + cfg.FILE_PATHS['DB_LOCATION'])


class Login(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Welcome to Inventory Manager\nIn order to proceed please enter the password provided:")
        self.textPass = QtWidgets.QLineEdit(self)
        self.textPass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.buttonLogin = QtWidgets.QPushButton('Login', self)
        self.buttonLogin.clicked.connect(self.handle_login)
        self.setWindowTitle("Login")
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(self.textPass)
        layout.addWidget(self.buttonLogin)
        logging.warning("-----------Login Window-----------")

    def handle_login(self):
        if self.textPass.text() == cfg.PASSWORDS['INVENTORY_PASS']:
            logging.info("user logged in successfully with the password: " + self.textPass.text())
            self.accept()
        else:
            logging.info("login password wrong: " + self.textPass.text())
            self.textPass.setText("")


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi("inventory.ui", self)
        self.resize(1050, 1070)
        # Global attributes:
        self.action_db = self.menuActions.addMenu('Databases')

        # Triggers and connections:
        self.delete_button.clicked.connect(self.delete_row)
        self.editMode_button.clicked.connect(self.editmode_button_function)
        self.refresh_button.clicked.connect(self.refresh)
        self.action_db.triggered.connect(self.choose_database)
        self.actionCreateDB.triggered.connect(self.manage_database)
        self.local_backup.clicked.connect(self.create_local_backup)
        self.excel_export.clicked.connect(self.export_to_excel)
        # On initialization:
        start_logger()
        self.load_db_menu()
        self.db_current = None
        self.load_data()  # First load of data - current_db is the default
        # refresh_thread = threading.Thread(target=self.auto_refresh, args=(20, ))
        # refresh_thread.start()

    def closeEvent(self, event):
        logging.warning("-----------Application closeEvent-----------")
        event.accept()

    # Export the given database to an xlsx file.
    def export_to_excel(self):
        try:
            logging.info('received request to export to excel')
            database_name = self.comboBox.currentText()  # Get the name of selected database in the combobox
            db_path = cfg.FILE_PATHS['DB_LOCATION'] + database_name + '.db'  # Define the database's path
            current_db = sqlite3.connect(db_path)  # Load the selected database
            save_path = self.save_file_dialogue(database_name,
                                                "xlsx")  # Let the user select a save path and name with type of xlsx file.
            table_names = self.get_all_table_names(database_name,
                                                   current_db)  # Create a list with the names of all tables in the database
            if save_path != '':  # If the user canceled the saving, excel will not be craeted (might also prevent empty names)
                with pandas.ExcelWriter(save_path,
                                        engine="xlsxwriter") as writer:  # Call ExcelWriter which will write into excel files (required to add tabs etc.) and creates it
                    for name in table_names:  # Iterate over all the table_names
                        selectedTable = pandas.read_sql("SELECT * FROM " + name, current_db)  # Import the current table
                        selectedTable.to_excel(writer, sheet_name=name,
                                               index=False)  # Export the current table to a new tab in the excel file, named after him
                logging.info('Finished exporting')
                os.startfile(save_path)  # Open the exported xlsx file on the user's machine
        except Exception as e:  # If the user try overrwriting an open excel file:
            experimental_warning('permission_error')  # Raise a warning. (Action will not be completed)
            logging.exception("error in export_to_excel: ")

    # Returns a list of all tables in given database (to support cases it changes)
    def get_all_table_names(self, database_name, current_db):
        try:
            table_names = []  # Create an empty list for the table names
            temp_db = current_db.execute(
                "SELECT name FROM sqlite_master WHERE type = 'table';")  # Load table names from the database
            for name in temp_db:  # Iterate over the loaded database
                table_names.append(name[
                                       0])  # Add the name of the current iterated table to the list
            return table_names  # Returns a list of the tables
        except:  # In case of any error:
            logging.exception("exception in get_all_table_names: ")  # Show in log
            pass  # And ignore

    # Opens a window for selecting name and location for saved file and returns the full path selected including file name
    def save_file_dialogue(self, default_name, file_type):
        try:
            save_path, _filter = QtWidgets.QFileDialog.getSaveFileName(None, "Save File", default_name,
                                                                       "(*." + file_type + ")")  # As described. (*_Filter discards the tuple recived by default.)
            return save_path  # Return a string of the path selected
        except:  # In case of errors:
            logging.exception("Error in saving file: ")  # Show in log

    def create_local_backup(self):
        try:
            export_file_location = \
                QtWidgets.QFileDialog.getExistingDirectory(None, "Local Backup")
            logging.info('exporting to: ' + export_file_location)
            shutil.copytree(cfg.FILE_PATHS["DB_LOCATION"], export_file_location + '/', dirs_exist_ok=True)
            self.local_backup.setStyleSheet('background-color: rgba(0, 255, 30, 0.25);')
        except:
            logging.exception("Error in create_local_copy: ")

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
        if self.db_current is not None:
            try:
                connection = sqlite3.connect(self.db_current)
                cur = connection.cursor()
                # tuples for each db, [0] is the db name, [1] is the table object, [2] is the number of columns in db
                tabs = self.create_tabs_tuples()
                for tab in tabs:
                    sql_query = "SELECT * FROM " + tab[0]  # tab[0] = db name
                    cur.execute(sql_query)
                    table_row = 0
                    for row in cur.execute(sql_query):
                        column = 0
                        for i in range(0, tab[2]):
                            tab[1].setItem(table_row, column, QtWidgets.QTableWidgetItem(str(row[column])))
                            column += 1
                        table_row += 1
                connection.close()
            except:
                logging.exception("exception in load_data:")
        else:
            # What to do?
            pass

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
            # experimental_warning("exited_edit_mode") Annoying
            self.editMode_button.setChecked(False)  # exits edit mode

        rows = 300
        tabs = self.create_tabs_tuples()
        for tab in tabs:
            tab[1].setRowCount(0)
            tab[1].setRowCount(rows)
        self.load_data()

    def auto_refresh(self, sleep_for):
        while True:
            for i in range(sleep_for):
                self.refresh_button.setText("Refresh in:  " + str(i))
                time.sleep(1)
            self.refresh()

    # 		#  https://stackoverflow.com/questions/49886313/how-to-run-a-while-loop-with-pyqt5
    #       #  https://realpython.com/python-pyqt-qthread/

    def delete_row(self):
        which_table = self.machines.currentIndex()
        tabs = self.create_tabs_tuples()
        try:
            item = tabs[which_table][1].item(tabs[which_table][1].currentRow(),
                                             tabs[which_table][1].currentColumn())  # gets the item = QTableWidgetItem
            item_key = tabs[which_table][1].item(tabs[which_table][1].currentRow(), 0)
            if item_key is not None:  # If itemKey is none, it means the user tried to change empty row, do nothing.
                sql_query = self.delete_sql_get_string(item_key.text(), which_table)
                connection = sqlite3.connect(self.db_current)
                cur = connection.cursor()
                cur.execute(sql_query)
                cur.close()
                connection.commit()
                connection.close()
                logging.info("delete_row: " + sql_query)
                self.refresh()
                self.start_edit_listener()
            else:  # For debug purposes, delete this else on release.
                logging.info("user is deleting empty row.")
        except:
            logging.exception("Exception at delete_row:")

    def manage_database(self):
        # Starts by asking for password, not everyone can create a new db.
        input_password, pressed_ok = QtWidgets.QInputDialog.getText(self, 'Admin Password', 'Enter Admin password:')
        if pressed_ok and input_password == cfg.PASSWORDS['DB_MANAGER']:
            self.create_database()
        if pressed_ok and input_password != cfg.PASSWORDS['DB_MANAGER']:
            experimental_warning('admin_wrong')

    def create_database(self):
        try:
            # Solution for db name will be a popup window for now:
            db_name, pressed_ok = QtWidgets.QInputDialog.getText(self, 'Database Name', 'Enter database name:')
            if not pressed_ok:
                db_name = ""
            if db_name != "" and len(db_name) < 10:  # Some verification for db name value.
                connection = sqlite3.connect(cfg.FILE_PATHS['DB_LOCATION'] + db_name + '.db')
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
                logging.info("create_database: new database created! " + db_name)
        except:
            logging.exception("Error in create_database: ")

    def load_db_menu(self):
        try:
            db_list = os.listdir(cfg.FILE_PATHS['DB_LOCATION'])
        except:
            logging.error("db location invalid: " + cfg.FILE_PATHS['DB_LOCATION'])
        # first, clear the actions
        for action in self.action_db.actions():
            self.action_db.removeAction(action)
        # adds action for each db name in dir.
        for db in db_list:
            action = self.action_db.addAction(db[:-3])  # db[:-3] removes the .db from the file name
            action.setCheckable(True)
            self.comboBox.addItem(
                db[:-3])  # Populates the comboBox in 'Additional Features'with theavailable databases.

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
        except:
            logging.exception('Exception in choose_database:')

    def editmode_button_function(self):
        if self.editMode_button.isChecked():
            self.start_edit_listener()
        else:
            self.stop_edit_listener()

    def start_edit_listener(self):
        tabs = self.create_tabs_tuples()
        for tab in tabs:
            tab[1].blockSignals(False)  # enable signals from the specific widget
            tab[1].cellChanged.connect(self.on_item_change)
        self.delete_button.setEnabled(True)
        logging.info("edit mode is ON")

    def stop_edit_listener(self):
        tabs = self.create_tabs_tuples()
        for tab in tabs:
            tab[1].blockSignals(True)  # disable signals from the specific widget
        self.delete_button.setEnabled(False)
        logging.info("edit mode is off")

    def on_item_change(self):
        #  self.machines.currentIndex() - 0 systems, 1 workstations, 3 ultrasounds..
        which_table = self.machines.currentIndex()
        tabs = self.create_tabs_tuples()
        try:
            item = tabs[which_table][1].item(tabs[which_table][1].currentRow(),
                                             tabs[which_table][1].currentColumn())  # gets the item = QTableWidgetItem
            item_key = tabs[which_table][1].item(tabs[which_table][1].currentRow(), 0)
            if item_key is not None:  # If itemKey is none, it means the user tried to change empty row, do nothing.
                self.update_sql_item(item, item_key.text(), which_table)
            else:  # For debug purposes, delete this else on release.
                logging.info("user is editing empty row.")
        except:
            logging.exception("Exception at on_item_change:")

    def update_sql_get_string(self, col, text, key, whichTable):
        tabs = self.create_tabs_tuples()
        query = f"UPDATE {tabs[whichTable][0]} " \
                f"SET {tabs[whichTable][3][col][0]} = '{text}' " \
                f"WHERE {tabs[whichTable][3][0][0]} = '{key}'; "
        return query

    def delete_sql_get_string(self, key, table):
        tabs = self.create_tabs_tuples()
        query = f"DELETE FROM {tabs[table][0]} " \
                f"WHERE {tabs[table][3][0][0]}=\'{key}\'"
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
            logging.info("update_sql_item query: " + sql_query)
        except:
            logging.exception("Exception at update_sql_item:")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    login = Login()
    login.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    if login.exec_() == QtWidgets.QDialog.Accepted:
        app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
        win = MainWindow()
        win.show()
        win.setFocus()
        sys.exit(app.exec_())

# TODO:
#  V need to create a function and button from the top menu (file menu) that creates a new db
#   Export list of used devices with some options (export approved only, export approved only & times used > 1)
#   Reset times used for a table
#  V Delete button
#   Background green of approved rows
#  V Fix databases update actions upon adding new db (currently create duplicates)
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
