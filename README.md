# Baseliner
An auto baseline generator project
	• 0.1
	First viable version without import
	• 0.2 
	1. Added import and export to XML
	2. Organize and divided some functions to better suit the needs of the code
	• 0.3
	1. Fixed bug of nGEN import order (Monitor 1 and Monitor 2 are flipped)
	- The problem was in nGEN's class fillFields function, it first inserted into fields of monitor2 the information from the clip of monitor1. Fixed by fixing the order of the text insertion
	2. Fixed bug when export Ultrasound to XML wouldn't work
	- There was a typo in function importaddtoInfoCount()
	3. Change WS licenses window to better support lower resolution screens.
	- Solved it by changing the Dialog layout to be wider.
	4. Continue simplifying functions
	- Changed each open_dialog second var to be called "position"
	- Changed typo nmark all across the code, left only from MainWindowBig.ui
	5. Fix crash when pressing the X button of sub dialogs.
	- Solved it by adding infoBox() in the end of each __init__ in dialog class.
	Adding infoBox() in the end of each fillFields() in dialog class.
	The logic is - the crash happened when the open_dialog caller function filled the list while the textboxes were not initialized, adding infoBox() at the end of init solved the issue because the fields will be an empty string and that’s okay. 
	Also, I encountered another bug when fixing this one, when importing and pressing the X the dialog and progress bar were restarted with empty fields. I solved it by adding infoBox() at the end of fillFields(). Thus making the actual values (each dialog has its own array of vars) that holds the textboxes.text() the values of the list that was sent to fillFields(). 
	6. Fix bug when after import pressing X on demo laptop resets the dialog's fields.
	- Fixed by adding self.infoBox() at the end of fillFields functions inside Demo_Dialog class.
	7. Fixed crash when pressing X on Export file location dialog
	- Solved it by adding len(self.exportfilelocation) > 1 to the if that starts exporting.
	8. Change checkbox in txt from True\False to Yes\No
	-Added an if in format() function for WS (solios) and for Demo (Surpoint)
	9. Added Tools tab -> Catalog Helper.
	Includes call in __init__ when triggering menu and two classes - CatalogHelper_Dialog and SingleCatheter
	Added import selenium
	https://stackoverflow.com/questions/47690548/running-pyinstaller-another-pc-with-chromedriver
	Read about pyinstaller with selenium
	Need to put chromedriver in the dist folder in order to not crash when using selenium.
	10. Change .txt format to "Catheter & Extenders" from "Catheters"
	11. Added experimentalWarning(self, kind) def to main class to raise warnings when certain parts of the program need user care.
	• 0.4 
	1. Added Header for txt file - think on how to add it to XML
	e.g. "Baseline V&V 16/06/2020
		Upgrade STD Baseline After V7 Phase 2 HOTFIX-
		Preformed by: Eran Yonai"
		Need to add it to DB, another Menu button that pops a dialog with the text in it.
	2. Continue simplifying functions
	- Added comments to: 
	3. Add SPU dialog under "extras"
	4. Add Recording System dialog under "extras"
	5. Add WS licenses to XML
	• 1 - Release
	6. Add verification
	7. Add Checkboxes to import, e.g. if you want to import only nGEN from an existing database.
	8. Add Catheter Catalog shortcut
