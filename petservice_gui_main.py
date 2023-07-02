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
                header.resizeSection(0, 180)  
                header.resizeSection(1, 350)  
                header.resizeSection(2, 200)  
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

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    window = MainWindow(ui)
    window.show()
    sys.exit(app.exec_())
