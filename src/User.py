import pandas as pd #show data as tables

# An implementation of the User class.
class User:

    # Constructor
    def __init__(self, cid=None, age=None, fname=None, lname=None, gender=None, aid=None, pnum=None, email=None, password=None):
        self._cid = cid
        self._age = age
        self._fname = fname
        self._lname = lname
        self._gender = gender
        self._aid = aid
        self._pnum = pnum
        self._email = email
        self._password = password

    #  @return cid
    def getCid(self):
        return self._cid
    
    def getfName(self):
        return self._fname
    
    def getEmail(self):
        return self._email
    
    def setEmail(self, email):
        self._email = email

    # @return string representation
    def __str__(self):
        return str(self.fname) +" "+ str(self.lname) +" "+ str(self.email)

    # Show a list of students as panda table.
    # @return panda dataframe
    @staticmethod
    def showAsTable(rows):
        df = pd.DataFrame(columns=["fname","lname","email"])
        for i in rows:
            df.loc[df.shape[0]] = i
        return df
