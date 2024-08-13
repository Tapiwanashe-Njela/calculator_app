#Import modules
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout



#Main app,create objects and settings
app = QApplication([]) #Allows us to create and execute our app; takes in an empty list ALWAYS
main_window = QWidget() #Object to create a new form (window) that we will be editing
main_window.setWindowTitle("---") #Set the title text 
main_window.resize(250,300) #Adjusting the size of the form 



#Create all app objects(widgets)
#grids buttons textbox etc



#Adding Functionality
#add functions e.g button click() etc



#ALL DESIGN HERE; Getting all the created objects onto our screen
master_layout = QVBoxLayout() #Create a column object; #Allows us to design our layout
#use add master_layout.addWidget(created app obj( buttons etc) )

main_window.setLayout(master_layout) #We then set the master layout as the main layout to be displayed


#Events
#basically link teh events e.g
#delete_button.clicked.connect(button_click) #We link the delete button click event to the button click function



#Show and run the app
main_window.show()
app.exec_()
