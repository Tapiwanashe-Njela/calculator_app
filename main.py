#Import modules
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout

#Main app,create objects and settings
app = QApplication([]) #Allows us to create and execute our app; takes in an empty list ALWAYS
main_window = QWidget() #Object to create a new form (window) that we will be editing
main_window.setWindowTitle("Calculator") #Set the title text 
main_window.resize(250,300) #Adjusting the size of the form 

#Create all app objects(widgets)
text_box = QLineEdit() #Create a linear text box
grid = QGridLayout() #Create a grid object

button_list = ["7", "8", "9", "/", 
               "4", "5", "6", "*", 
               "1", "2", "3", "-", 
               "0", ".", "=", "+"] #list of buttons used to create a 4x4 grid

clear_button = QPushButton("Clear")
delete_button = QPushButton("Delete")

#Adding Functionality
def button_click():
    button = app.sender() #An object that stores the identity of which button was clicked using the sender method that reads the most recent event
    text = button.text() #Get the text value of the clicked button

    #Now we use if-elif statements to determine which operation button was clicked and perform the corresponding functionality
    if text == "=":
        text_box_text = text_box.text() #We take the input in our textbox up top
        #now we try to evaluate the obtained text from the text box
        try: #The try block lets you test a block of code for errors.
            result = eval(text_box_text) #eval method evaluates the input string to make sure it is valid maths + avoid errors like divide by 0
            text_box.setText("Result: " + str(result)) #If eval passes we display the value of result in our textbox after we convert it to a string
        
        except Exception as e: #The except block lets you handle the error.; using keyword Exception means its a broad catch and we give it a name e 
            print("Error!:", e) #Print the type of error  

    elif text == "Clear":
        text_box.clear() #Clear the text in the textbox using the clear method

    elif text == "Delete":
        text_box_text = text_box.text() #We take the input in our textbox up top
        text_box.setText(str(text_box_text[:-1])) #Display the text in the textbox but remove the last position

    else: #If text on button is non of the above
        text_box_text = text_box.text() #We take the input in our textbox up top
        text_box.setText(str(text_box_text + text)) #We display it in out textbox but concat the text of the button selecte

#For loop to create the grid
row = 0 #To keep track of the number of buttons in each row
column = 0 #To keep track of the number of buttons in each column

for text in button_list:
    button = QPushButton(text) #Create a button with text = respective text in list
    button.clicked.connect(button_click) #Create a button click event for the created button that connects to a function
    grid.addWidget(button, row, column) #Add the creted button to the grid
    column += 1 #To move to the next space on the right 
    if column > 3: #If we reach the end of the column 
        row += 1 #We jump to the next row 
        column = 0 #And we start again from the first column

#ALL DESIGN HERE; Getting all the created objects onto our screen
bottom_button_row = QHBoxLayout()
master_layout = QVBoxLayout() #Create a column object; #Allows us to design our layout

master_layout.addWidget(text_box)
master_layout.addLayout(grid)
master_layout.addLayout(bottom_button_row)

bottom_button_row.addWidget(clear_button)
bottom_button_row.addWidget(delete_button)

main_window.setLayout(master_layout) #We then set the master layout as the main layout to be displayed

#Events
clear_button.clicked.connect(button_click) #We link the clear button click event to the button click function
delete_button.clicked.connect(button_click) #We link the delete button click event to the button click function

#Show and run the app
main_window.show() #Display the form
app.exec_() #Run the app