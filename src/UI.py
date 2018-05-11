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
welcomeBanner = widgets.HTML(
    value='Hello and welcome to <b>Flick Deals</b><br><img src="http://images.clipartpanda.com/money-clipart-money-pics-free.png" height=50 width = 50>',
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

