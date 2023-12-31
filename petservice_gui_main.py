import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import  QListWidgetItem, QAbstractItemView, QInputDialog, QMessageBox
from datetime import datetime
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
        self.setPrevPetSelection()
        self.gui_pet.serviceList.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        
        self.gui_pet.addAppButton.clicked.connect(self.add_appointment_button_clicked)
        self.gui_pet.deleteAppButton.clicked.connect(self.delete_appointment_row)
        self.gui_pet.searchAppButton.clicked.connect(self.search_appointment_button_clicked)
        self.gui_pet.searchInputApp.returnPressed.connect(self.search_appointment_button_clicked)
        self.gui_pet.historyTable.doubleClicked.connect(self.history_table_cell_edit)
        
        #INFORMATION TAB
        self.gui_pet.deletePetButton.clicked.connect(self.delete_pet_row)
        self.gui_pet.deleteOwnerButton.clicked.connect(self.delete_owner_row)
        self.gui_pet.searchPetButton.clicked.connect(self.search_pet_button_clicked)
        self.gui_pet.searchInputPet.returnPressed.connect(self.search_pet_button_clicked)
        self.gui_pet.searchOwnerButton.clicked.connect(self.search_owner_button_clicked)
        self.gui_pet.searchInputOwner.returnPressed.connect(self.search_owner_button_clicked)
        self.gui_pet.petTable.doubleClicked.connect(self.pet_table_cell_edit)
        self.gui_pet.ownerTable.doubleClicked.connect(self.owner_table_cell_edit)
        
    
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
                if col_id in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
                    item.setEditable(False)
                if col_id in [0, 1, 2, 3, 4, 5, 6, 7 , 8]:
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                else:
                    item.setTextAlignment(QtCore.Qt.AlignLeft)
                model.setItem(row_id, col_id, item)
        return model
    
    def adjustTableColumns(self, table):
        header = table.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.Interactive)
        if table == self.gui_pet.serviceTable: 
                header.resizeSection(0, 0)  
                header.resizeSection(1, 500)  
                header.resizeSection(2, 300)  
        elif table == self.gui_pet.historyTable:
                header.resizeSection(0, 100)  
                header.resizeSection(1, 120)
                header.resizeSection(2, 100)
                header.resizeSection(3, 120)
                header.resizeSection(4, 140)
                header.resizeSection(5, 160)
                header.resizeSection(6, 199)
                header.resizeSection(7, 0)
                header.resizeSection(8, 200)
                
        elif table == self.gui_pet.petTable:
                header.resizeSection(0, 0)  
                header.resizeSection(1, 100)
                header.resizeSection(2, 70)
                header.resizeSection(3, 100)
                header.resizeSection(4, 100)
        elif table == self.gui_pet.ownerTable:
                header.resizeSection(0, 0)  
                header.resizeSection(1, 218)
                header.resizeSection(2, 150)


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
        
    def setPrevPetSelection(self):
        self.gui_pet.choosePrevPets.clear()
        self.gui_pet.choosePrevPets.addItems(self.petObject.returnPetName()) 
        self.gui_pet.choosePrevPets.currentIndexChanged.connect(self.populatePetData)

    def populatePetData(self, selected_pet):
        selected_pet = self.gui_pet.choosePrevPets.currentText()
        pet_data = self.petObject.getPetDataFromSelectedPet(selected_pet)
        print(selected_pet)
        if pet_data:
            pet_name = pet_data[0]
            pet_species = pet_data[1]
            pet_breed = pet_data[2]
            owner_name = pet_data[3]
            owner_number = pet_data[4]

            # Populate the QLineEdits with the retrieved data
            self.gui_pet.enterPName.setText(pet_name)
            self.gui_pet.enterSpecies.setText(pet_species)
            self.gui_pet.enterBreed.setText(pet_breed)
            self.gui_pet.enterOName.setText(owner_name)
            self.gui_pet.enterOName_2.setText(owner_number)


      
    #SERVICE PAGE ---------------------------------------------------------------------------------------- 
    def add_service_button_clicked(self):
        service_name = self.gui_pet.enterSName.text()
        service_cost = self.gui_pet.enterCost.text()
        self.servObject.addService(service_name, service_cost)
        
        self.setStandardItemModel()
        self.gui_pet.serviceTable.model().layoutChanged.emit()
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

        self.serviceModel = self.setSModel(self.servObject.returnServiceData(), self.serviceModel)
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
        service_names = (item.text() for item in self.gui_pet.serviceList.selectedItems() if item.text())
        
        if not (pet_name and pet_species and pet_breed and owner_name and owner_number and app_date and app_time and app_availtype and app_status and service_names):
            QMessageBox.warning(self, "Missing Information", "Please fill in all fields.")
            return
        self.appObject.addAppointment(pet_name, pet_species, pet_breed, owner_name, owner_number, app_date, app_time, app_availtype, app_status, service_names)
        
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
        
        
        # done
    def search_appointment_button_clicked(self):
        search_appointment = self.gui_pet.searchInputApp.text()
        SResults = self.appObject.searchAppointment(search_appointment)
        if SResults:
            self.clearModel(self.historyModel)
            self.historyModel = self.setSModel(SResults, self.historyModel)
            self.historyModel.setHorizontalHeaderLabels(self.appObject.columns)
            self.gui_pet.historyTable.setModel(self.historyModel)
            self.adjustTableColumns(self.gui_pet.historyTable)
            self.gui_pet.historyTable.model().layoutChanged.emit()
        else:
            QtWidgets.QMessageBox.information(self, "No Results", f"No results found for appointment'{search_appointment}'.")
            
    def history_table_cell_edit(self, index):
        row = index.row()
        column = index.column()
        columnName = self.historyModel.horizontalHeaderItem(column).text()
        item = self.gui_pet.historyTable.model().item(row, column)
        current_value = item.text()
        unique_key = self.gui_pet.historyTable.model().item(row, 0).text()
        
        availType = ["Reservation", "Walk-in"]
        status = ["Pending", "Canceled", "Completed"]
        
        if column in [0, 5, 6, 8]:
            QtWidgets.QMessageBox.warning(self, "Non-editable column", "This column is non-editable.")
            return
        
        elif column in [1]:  # Date column
            new_value, ok = QtWidgets.QInputDialog.getText(self, "Update Appointment", "Enter new date (YYYY-MM-DD):", text=current_value)
            
            if ok and new_value:
                try:
                    # Parse the new date value and convert it to the desired format
                    new_date = datetime.strptime(new_value, "%Y-%m-%d").strftime("%Y-%m-%d")
                    self.appObject.updateAppointment(unique_key, columnName, new_date)
                    self.setStandardItemModel()
                    self.gui_pet.historyTable.model().layoutChanged.emit()
                except ValueError:
                    QtWidgets.QMessageBox.warning(self, "Invalid date format", "Please enter the date in the format YYYY-MM-DD.")
        
        elif column in [2]:  # Time column
            new_value, ok = QtWidgets.QInputDialog.getText(self, "Update Appointment", "Enter new time (HH:MM):", text=current_value)
            
            if ok and new_value:
                try:
                    # Parse the new time value and convert it to the desired format
                    new_time = datetime.strptime(new_value, "%H:%M").strftime("%H:%M")
                    self.appObject.updateAppointment(unique_key, columnName, new_time)
                    self.setStandardItemModel()
                    self.gui_pet.historyTable.model().layoutChanged.emit()
                except ValueError:
                    QtWidgets.QMessageBox.warning(self, "Invalid time format", "Please enter the time in the format HH:MM.")
    
        elif column in [3, 4, 8]:
            if column == 3:
                current_index = availType.index(current_value) if current_value in availType else 0
                new_value, ok = QInputDialog.getItem(self, "Update Appointment", "Select avail type:", availType, current=current_index)
            if column == 4:
                current_index = status.index(current_value) if current_value in status else 0
                new_value, ok = QInputDialog.getItem(self, "Update Appointment", "Select status:", status, current=current_index)
            elif column == 8:
                serv_names = self.servObject.returnServiceNames()
                current_index = serv_names.index(current_value) if current_value in serv_names else 0
                new_value, ok = QtWidgets.QInputDialog.getItem(self, "Update Appointment", "Select Service:", serv_names, current=current_index)
            
            if ok and new_value and new_value != current_value:
                reply = QMessageBox.question(self, "Save Changes", "Do you want to save the changes?", 
                                            QMessageBox.Yes | QMessageBox.No)
                if reply == QMessageBox.Yes:
                    self.appObject.updateAppointment(unique_key, columnName, new_value)
                    self.setStandardItemModel()
                    self.gui_pet.historyTable.model().layoutChanged.emit()
                else:
                    pass
                
        else: 
            new_value, ok = QInputDialog.getText(self, "Update Appointment", "Enter new text:", text=current_value)

            if ok and new_value and new_value != current_value:
                reply = QMessageBox.question(self, "Save Changes", "Do you want to save the changes?", 
                                            QMessageBox.Yes | QMessageBox.No)
                if reply == QMessageBox.Yes:
                        self.appObject.updateAppointment(unique_key, columnName, new_value)
                        self.setStandardItemModel()
                        self.gui_pet.historyTable.model().layoutChanged.emit()
            else:
                pass


    #INFORMATION TAB --------------------------------------------------------------------------------
    def delete_pet_row(self):
        selected_rows = self.gui_pet.petTable.currentIndex().row()
        column_index = 0
        pet = self.gui_pet.petTable.model().index(selected_rows, column_index).data()
        reply = QtWidgets.QMessageBox.question(self, "Delete Confirmation", "Are you sure you want to delete this pet?",
                                 QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            self.petObject.deletePet(pet)

        self.setPrevPetSelection()
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
       
    #fixed 
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
                if column == 4:
                    if self.ownerObject.checkOwnerExists(new_value) == False:
                        QtWidgets.QMessageBox.warning(self, "Owner Unavailable", "Owner does not exist.")
                    else:
                        self.petObject.updatePet(unique_key, columnName, new_value)
                        self.setStandardItemModel()
                        self.gui_pet.petTable.model().layoutChanged.emit()
                else:
                    self.petObject.updatePet(unique_key, columnName, new_value)
                    self.setStandardItemModel()
                    self.gui_pet.petTable.model().layoutChanged.emit()
            else:
                pass
            
        self.setPrevPetSelection()
    
    #wip
    def owner_table_cell_edit(self, index):
        row = index.row()
        column = index.column()
        columnName = self.ownerModel.horizontalHeaderItem(column).text()
        item = self.gui_pet.ownerTable.model().item(row, column)
        current_value = item.text()
        unique_key = self.gui_pet.ownerTable.model().item(row, 0).text()
        new_value, ok = QtWidgets.QInputDialog.getText(self, "Update Owner Information", "Enter new text:", text=current_value)

        if ok and new_value and new_value != current_value:
            reply = QtWidgets.QMessageBox.question(self, "Save Changes", "Do you want to save the changes?", 
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            if reply == QtWidgets.QMessageBox.Yes:
                if column == 2:
                    self.ownerObject.updateOwner(unique_key, "phoneNumber", new_value)
                    self.setStandardItemModel()
                    self.gui_pet.ownerTable.model().layoutChanged.emit()
                else:
                    self.ownerObject.updateOwner(unique_key, columnName, new_value)
                    self.setStandardItemModel()
                    self.gui_pet.ownerTable.model().layoutChanged.emit()
            else:
                pass





if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    window = MainWindow(ui)
    window.show()
    sys.exit(app.exec_())
