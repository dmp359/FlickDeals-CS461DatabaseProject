import pandas as pd #show data as tables

# An implementation of the Student class.
class Student:

    # Constructor
    # @param id
    # @param name
    # @param gpa
    def __init__(self, name, sid=None, gpa=None):
        self._name = name
        self._id = sid
        self._gpa = gpa

    # Get the name of the student.
    #  @return name
    def getName(self):
        return self._name

    # Get the id of the student.
    #  @return id
    def getId(self):
        return self._id

    # Get the GPA of the student.
    #  @return GPA
    def getGPA(self):
        return self._gpa

    # Set the student's name.
    # @param name
    def setName(self, name):
        self._name = name

    # Set the student's id.
    # @param id
    def setId(self, id):
        self._id = id

    # Set the student's gpa.
    # @param gpa
    def setGPA(self, gpa):
        self._gpa = gpa

    # Generate a string representation of the student.
    # @return string representation
    def __str__(self):
        return str(self._id) +" "+ str(self._name) +" "+ str(self._gpa)


    # Show a list of students as panda table.
    # @return panda dataframe
    @staticmethod
    def showAsTable(rows):
        df = pd.DataFrame(columns=["sid","name","gpa"])
        for i in rows:
            df.loc[df.shape[0]] = i
        return df
