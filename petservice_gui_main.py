import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from petservice import Ui_MainWindow
import appointment_copy as classObject  #set file here

class MainWindow(QtWidgets.QMainWindow):
    
    
    def __init__(self, ui):
        super().__init__()
        self.servObject = classObject.servObject
        
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
                if col_id in [0, 1, 2, 3, 4]:
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
                header.resizeSection(0, 240)  
                header.resizeSection(1, 459)  


    def clearModel(self, model, rows=0, cols=0):
        model.clear()
        model.setRowCount(rows)
        model.setColumnCount(cols)
        
    def setStandardItemModel(self): #change all
        self.serviceModel = QtGui.QStandardItemModel()
        #self.historyModel = QtGui.QStandardItemModel()
        self.serviceModel = self.setSModel(self.servObject.returnService(), self.serviceModel)
        #self.historyModel = self.setSModel(self.appObject.returnAppointment(), self.historyModel)
        
        self.serviceModel.setHorizontalHeaderLabels(self.servObject.columns) 
        self.gui_pet.serviceTable.setModel(self.serviceModel)
        #self.historyModel.setHorizontalHeaderLabels(self.appObject.columns)
        #self.gui_ssis.historyTable.setModel(self.historyModel)
        
        self.adjustTableColumns(self.gui_pet.serviceTable)
        #self.adjustTableColumns(self.gui_pet.CourseTable)
      
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

    #SERVICE PAGE ---------------------------------------------------------------------------------------- 



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    window = MainWindow(ui)
    window.show()
    sys.exit(app.exec_())
