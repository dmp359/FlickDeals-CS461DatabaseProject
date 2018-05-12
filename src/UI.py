#Import libraries
from ipywidgets import *
from IPython.display import display

from Users import User
from Registrar import Registrar

#Define Widgets.
'''
studentName = widgets.Textarea(
    value='',
    placeholder='Enter Student Name',
    description='Name:',
    disabled=False
)

studentGPA = widgets.Textarea(
    value='',
    placeholder='Enter Student GPA',
    description='GPA:',
    disabled=False
)
'''

# This list will be created programatically eventually
# Filled in with title/description and clickable image from db
deal_HTML_items = [
    '<div class="grid-item">Deal description 1</div>',
    '<div class="grid-item">Deal description 2</div>',
    '<div class="grid-item">Deal description 3</div>',
    '<div class="grid-item">Deal description 4</div>',
    '<div class="grid-item">Deal description 5</div>',
    '<div class="grid-item">Deal description 6</div>',
]

gridItems = ''.join(deal_HTML_items)
welcomeHTML = '''
    <link rel="stylesheet" href="styles.css">
    Hi and welcome to <b>Flick Deals</b>
    <img src="http://images.clipartpanda.com/money-clipart-money-pics-free.png" height=50 width = 50>
    <h1> Check out today's hottest deals! </h1>
        <div class="grid-container">
            {gridItems}
        </div>
     '''.format(gridItems=gridItems)

welcomeBanner = widgets.HTML(
    value=welcomeHTML,
)

def printHello():
    display(welcomeBanner)
   

#Click Function
def run_queries(sender):
    reg = Registrar()
    response = reg.openDBConnectionWithBundle("PgBundle.properties")
    print (response)
    
    '''
    newStudent = Student(studentName.value)
    newStudent = reg.registerStudent(newStudent);
    print("Registered a new student: " + str(newStudent));

    newStudent = reg.setGPA(newStudent.getId(), float(studentGPA.value));
    print("Updated GPA for student: " + str(newStudent));

    roster = reg.getRoster();
    reg.closeConnection();
    table=Student.showAsTable(roster)
    display(table)

def add_one_student():
    button = widgets.Button(description="Run")
    
    #Display Widgets
    display(studentName)
    display(studentGPA)
    display(button)

    #Click Handlers
    button.on_click(run_queries)
'''

