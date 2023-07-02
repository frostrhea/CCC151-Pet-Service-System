import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from petservice import Ui_MainWindow
#import codefile as classObject  #set file here

class MainWindow(QtWidgets.QMainWindow):
    
    
    def __init__(self, ui):
        super().__init__()
        
        self.gui_pet = ui
        self.gui_pet.setupUi(self)     
        
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
    
    
    
    

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    window = MainWindow(ui)
    window.show()
    sys.exit(app.exec_())
