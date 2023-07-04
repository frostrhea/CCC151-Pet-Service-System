import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import  QListWidgetItem, QAbstractItemView
from petservice import Ui_MainWindow
import systemClasses as classObject  #set file here

class MainWindow(QtWidgets.QMainWindow):
    
    
    def __init__(self, ui):
        super().__init__()
        self.servObject = classObject.servObject
        self.appObject = classObject.appObject
        self.petObject = classObject.petObject
        self.ownerObject = classObject.ownerObject
        
        self.gui_pet = ui
        self.gui_pet.setupUi(self)     
        self.setStandardItemModel()
        #self.selected_column = None
        # switching pages
        self.gui_pet.historyButton.clicked.connect(self.history_button_clicked)
        self.gui_pet.ServicesButton.clicked.connect(self.service_button_clicked)
        self.gui_pet.backPetServiceButton.clicked.connect(self.back_button_clicked)
        self.gui_pet.backPetServiceButton_2.clicked.connect(self.back_button_clicked)
        
        #SERVICE PAGE
        self.gui_pet.addServiceButton.clicked.connect(self.add_service_button_clicked)
        self.gui_pet.deleteServButton.clicked.connect(self.delete_service_row)
        self.gui_pet.searchServiceButton.clicked.connect(self.search_service_button_clicked)
        self.gui_pet.searchInputService.returnPressed.connect(self.search_service_button_clicked)
        self.gui_pet.serviceTable.doubleClicked.connect(self.service_table_cell_edit)
        
        #APPOINTMENT PAGE
        self.setAvailTypeSelection()
        self.setStatusSelection()
        self.setServiceSelection()
        self.gui_pet.serviceList.setSelectionMode(QAbstractItemView.ExtendedSelection)
        
        self.gui_pet.addAppButton.clicked.connect(self.add_appointment_button_clicked)
        self.gui_pet.deleteAppButton.clicked.connect(self.delete_appointment_row)
        
        #INFORMATION TAB
        self.gui_pet.deletePetButton.clicked.connect(self.delete_pet_row)
        self.gui_pet.deleteOwnerButton.clicked.connect(self.delete_owner_row)
        self.gui_pet.searchPetButton.clicked.connect(self.search_pet_button_clicked)
        self.gui_pet.searchOwnerButton.clicked.connect(self.search_owner_button_clicked)
        self.gui_pet.petTable.doubleClicked.connect(self.pet_table_cell_edit)
        
    
    def history_button_clicked(self):
        self.gui_pet.stackedWidget.setCurrentIndex(0)
        
    def service_button_clicked(self):
        self.gui_pet.stackedWidget.setCurrentIndex(1)
    
    def back_button_clicked(self):
        self.gui_pet.stackedWidget.setCurrentIndex(2)
    
    
    def setSModel(self, data, model):
        #rows = cursor.fetchall()
        for row_id, row in enumerate(data):
            for col_id, value in enumerate(row):
                text = str(value)
                item = QtGui.QStandardItem(text)
                model.setItem(row_id, col_id, item)
                #print(f"text: {text}")
                if col_id in [0, 1, 2, 3, 4]:
                    item.setEditable(False)
                if col_id in [0, 1, 2, 3, 4, 5, 6]:
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                else:
                    item.setTextAlignment(QtCore.Qt.AlignLeft)
                model.setItem(row_id, col_id, item)
        return model
    
    def adjustTableColumns(self, table):
        header = table.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.Interactive)
        if table == self.gui_pet.serviceTable: 
                header.resizeSection(0, 190)  
                header.resizeSection(1, 390)  
                header.resizeSection(2, 220)  
        elif table == self.gui_pet.historyTable:
                header.resizeSection(0, 100)  
                header.resizeSection(1, 120)
                header.resizeSection(2, 100)
                header.resizeSection(3, 120)
                header.resizeSection(4, 120)
                header.resizeSection(5, 150)
                header.resizeSection(6, 150)
                
        elif table == self.gui_pet.petTable:
                header.resizeSection(0, 0)  
                header.resizeSection(1, 100)
                header.resizeSection(2, 70)
                header.resizeSection(3, 100)
                header.resizeSection(4, 100)
        elif table == self.gui_pet.ownerTable:
                header.resizeSection(0, 70)  
                header.resizeSection(1, 180)
                header.resizeSection(2, 120)


    def clearModel(self, model, rows=0, cols=0):
        model.clear()
        model.setRowCount(rows)
        model.setColumnCount(cols)
        
    def setStandardItemModel(self): #change all
        #SERVICE
        self.serviceModel = QtGui.QStandardItemModel()
        self.serviceModel.setHorizontalHeaderLabels(self.servObject.columns) 
        self.gui_pet.serviceTable.setModel(self.serviceModel)
        self.serviceModel = self.setSModel(self.servObject.returnServiceData(), self.serviceModel)
        
        #HISTORY
        self.historyModel = QtGui.QStandardItemModel()
        self.historyModel.setHorizontalHeaderLabels(self.appObject.columns)
        self.gui_pet.historyTable.setModel(self.historyModel)
        self.historyModel = self.setSModel(self.appObject.returnAppointmentData(), self.historyModel)
        
        #PET
        self.petModel = QtGui.QStandardItemModel()
        self.petModel.setHorizontalHeaderLabels(self.petObject.columns)
        self.gui_pet.petTable.setModel(self.petModel)
        self.petModel = self.setSModel(self.petObject.returnPetData(), self.petModel)
        
        #OWNER
        self.ownerModel = QtGui.QStandardItemModel()
        self.ownerModel.setHorizontalHeaderLabels(self.ownerObject.columns) 
        self.gui_pet.ownerTable.setModel(self.ownerModel)
        self.ownerModel = self.setSModel(self.ownerObject.returnOwnerData(), self.ownerModel)
        
        self.adjustTableColumns(self.gui_pet.serviceTable)
        self.adjustTableColumns(self.gui_pet.historyTable)
        self.adjustTableColumns(self.gui_pet.petTable)
        self.adjustTableColumns(self.gui_pet.ownerTable)
      
    #SELECTIONS 
    def setAvailTypeSelection(self):
        self.gui_pet.chooseAvailType.clear() 
        self.gui_pet.chooseAvailType.addItems(self.appObject.availType)
        
    def setStatusSelection(self):
        self.gui_pet.chooseStatus.clear()
        self.gui_pet.chooseStatus.addItems(self.appObject.status) 
    
    def setServiceSelection(self):
        self.gui_pet.serviceList.clear()
        self.gui_pet.serviceList.addItems(self.servObject.returnServiceNames()) 
        
    def handle_service_selection(self):
        selected_items = []
        for item in self.gui_pet.serviceList.selectedItems():
            selected_items.append(item.text())
      
    #SERVICE PAGE ---------------------------------------------------------------------------------------- 
    def add_service_button_clicked(self):
        service_id = self.gui_pet.enterservIDName.text()
        service_name = self.gui_pet.enterSName.text()
        service_cost = self.gui_pet.enterCost.text()
        self.servObject.addService(service_id, service_name, service_cost)
        
        self.setStandardItemModel()
        self.gui_pet.serviceTable.model().layoutChanged.emit()
        self.gui_pet.enterservIDName.clear()
        self.gui_pet.enterSName.clear()
        self.gui_pet.enterCost.clear()
        self.setServiceSelection()
        
    def delete_service_row(self):
        selected_rows = self.gui_pet.serviceTable.currentIndex().row()
        column_index = 0
        service = self.gui_pet.serviceTable.model().index(selected_rows, column_index).data()
        reply = QtWidgets.QMessageBox.question(self, "Delete Confirmation", "Are you sure you want to delete this service?",
                                 QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            self.servObject.deleteService(service)

        self.serviceModel = self.setSModel(self.servObject.returnService(), self.serviceModel)
        self.setStandardItemModel()
        self.gui_pet.serviceTable.model().layoutChanged.emit()

    def search_service_button_clicked(self):
        search_service = self.gui_pet.searchInputService.text()
        SResults = self.servObject.searchService(search_service)
        if SResults:
            self.clearModel(self.serviceModel)
            self.serviceModel = self.setSModel(SResults, self.serviceModel)
            self.serviceModel.setHorizontalHeaderLabels(self.servObject.columns)
            self.gui_pet.serviceTable.setModel(self.serviceModel)
            self.adjustTableColumns(self.gui_pet.serviceTable)
            self.gui_pet.serviceTable.model().layoutChanged.emit()
        else:
            QtWidgets.QMessageBox.information(self, "No Results", f"No results found for service '{search_service}'.")

    def service_table_cell_edit(self, index):
        row = index.row()
        column = index.column()
        columnName = self.serviceModel.horizontalHeaderItem(column).text()
        item = self.gui_pet.serviceTable.model().item(row, column)
        current_value = item.text()
        unique_key = self.gui_pet.serviceTable.model().item(row, 0).text() 
        new_value, ok = QtWidgets.QInputDialog.getText(self, "Update Service", "Enter new text:", text=current_value)
        
        if ok and new_value and new_value != current_value:
            reply = QtWidgets.QMessageBox.question(self, "Save Changes", "Do you want to save the changes?", 
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            if reply == QtWidgets.QMessageBox.Yes:
                if column in [0,1,2]:
                    self.servObject.updateService(unique_key, columnName, new_value)
                    self.setStandardItemModel()
                    self.gui_pet.serviceTable.model().layoutChanged.emit()
            else:
                pass

    #APPOINTMENT PAGE ---------------------------------------------------------------------------------------- 
    def add_appointment_button_clicked(self):
        pet_name = self.gui_pet.enterPName.text()
        pet_species = self.gui_pet.enterSpecies.text()
        pet_breed = self.gui_pet.enterBreed.text()
        
        owner_name = self.gui_pet.enterOName.text()
        owner_number = self.gui_pet.enterOName_2.text()
        
        app_date = self.gui_pet.dateEdit.text()
        app_time = self.gui_pet.timeEdit.text()
        app_availtype = self.gui_pet.chooseAvailType.currentText()
        app_status = self.gui_pet.chooseStatus.currentText()
        
         # Get the selected service names
        service_names = []
        selected_items = self.gui_pet.serviceList.selectedItems()
        for item in selected_items:
            service_names.append(item.text())
        #self.appObject.addAppointment(pet_name, pet_species, pet_breed, owner_name, owner_number, app_date, app_time, app_availtype, app_status, service_names, selected_items)
        self.appObject.addAppointment(pet_name, pet_species, pet_breed, owner_name, owner_number, app_date, app_time, app_availtype, app_status)
        
        self.setStandardItemModel()
        self.gui_pet.historyTable.model().layoutChanged.emit()
        self.gui_pet.ownerTable.model().layoutChanged.emit()
        self.gui_pet.petTable.model().layoutChanged.emit()
        self.gui_pet.enterPName.clear()
        self.gui_pet.enterSpecies.clear()
        self.gui_pet.enterBreed.clear()
        self.gui_pet.enterOName.clear()
        self.gui_pet.enterOName_2.clear()
      
    def delete_appointment_row(self):
        selected_rows = self.gui_pet.historyTable.currentIndex().row()
        column_index = 0
        appointment = self.gui_pet.historyTable.model().index(selected_rows, column_index).data()
        reply = QtWidgets.QMessageBox.question(self, "Delete Confirmation", "Are you sure you want to delete this appointment?",
                                 QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            self.appObject.deleteAppointment(appointment)

        self.historyModel = self.setSModel(self.appObject.returnAppointmentData(), self.historyModel)
        self.setStandardItemModel()
        self.gui_pet.historyTable.model().layoutChanged.emit()  
        
        
        # not done
    def search_appointment_button_clicked(self):
        search_appointment = self.gui_pet.searchInputApp.text()
        SResults = self.servObject.searchAppointment(search_appointment)
        if SResults:
            self.clearModel(self.appModel)
            self.appModel = self.setSModel(SResults, self.appModel)
            self.appModel.setHorizontalHeaderLabels(self.appObject.columns)
            self.gui_pet.historyTable.setModel(self.appModel)
            self.adjustTableColumns(self.gui_pet.historyTable)
            self.gui_pet.historyTable.model().layoutChanged.emit()
        else:
            QtWidgets.QMessageBox.information(self, "No Results", f"No results found for appointment'{search_appointment}'.")


    #INFORMATION TAB --------------------------------------------------------------------------------
    def delete_pet_row(self):
        selected_rows = self.gui_pet.petTable.currentIndex().row()
        column_index = 0
        pet = self.gui_pet.petTable.model().index(selected_rows, column_index).data()
        reply = QtWidgets.QMessageBox.question(self, "Delete Confirmation", "Are you sure you want to delete this pet?",
                                 QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            self.petObject.deletePet(pet)

        self.historyModel = self.setSModel(self.petObject.returnPetData(), self.petModel)
        self.setStandardItemModel()
        self.gui_pet.petTable.model().layoutChanged.emit()  

    def delete_owner_row(self):
        selected_rows = self.gui_pet.ownerTable.currentIndex().row()
        column_index = 0
        owner = self.gui_pet.ownerTable.model().index(selected_rows, column_index).data()
        reply = QtWidgets.QMessageBox.question(self, "Delete Confirmation", "Are you sure you want to delete this pet owner?",
                                 QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            self.ownerObject.deleteOwner(owner)

        self.ownerModel = self.setSModel(self.ownerObject.returnOwnerData(), self.ownerModel)
        self.setStandardItemModel()
        self.gui_pet.ownerTable.model().layoutChanged.emit()  

    def search_pet_button_clicked(self):
        search_pet = self.gui_pet.searchInputPet.text()
        SResults = self.petObject.searchPet(search_pet)
        if SResults:
            self.clearModel(self.petModel)
            self.petModel = self.setSModel(SResults, self.petModel)
            self.petModel.setHorizontalHeaderLabels(self.petObject.columns)
            self.gui_pet.petTable.setModel(self.petModel)
            self.adjustTableColumns(self.gui_pet.petTable)
            self.gui_pet.petTable.model().layoutChanged.emit()
        else:
            QtWidgets.QMessageBox.information(self, "No Results", f"No results found for pet'{search_pet}'.")

    def search_owner_button_clicked(self):
        search_owner = self.gui_pet.searchInputOwner.text()
        SResults = self.ownerObject.searchOwner(search_owner)
        if SResults:
            self.clearModel(self.ownerModel)
            self.ownerModel = self.setSModel(SResults, self.ownerModel)
            self.ownerModel.setHorizontalHeaderLabels(self.ownerObject.columns)
            self.gui_pet.ownerTable.setModel(self.ownerModel)
            self.adjustTableColumns(self.gui_pet.ownerTable)
            self.gui_pet.ownerTable.model().layoutChanged.emit()
        else:
            QtWidgets.QMessageBox.information(self, "No Results", f"No results found for pet'{search_owner}'.")
       
    #unique key is set at column 0 but since giremove man from table, nagkaproblem sya     
    def pet_table_cell_edit(self, index):
        row = index.row()
        column = index.column()
        columnName = self.petModel.horizontalHeaderItem(column).text()
        item = self.gui_pet.petTable.model().item(row, column)
        current_value = item.text()
        unique_key = self.gui_pet.petTable.model().item(row, 0).text()
        new_value, ok = QtWidgets.QInputDialog.getText(self, "Update Pet", "Enter new text:", text=current_value)

        if ok and new_value and new_value != current_value:
            reply = QtWidgets.QMessageBox.question(self, "Save Changes", "Do you want to save the changes?", 
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            if reply == QtWidgets.QMessageBox.Yes:
                self.petObject.updatePet(unique_key, columnName, new_value)
                self.setStandardItemModel()
                self.gui_pet.petTable.model().layoutChanged.emit()
            else:
                pass





if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    window = MainWindow(ui)
    window.show()
    sys.exit(app.exec_())
