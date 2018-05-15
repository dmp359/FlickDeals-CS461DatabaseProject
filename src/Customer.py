import pandas as pd #show data as tables

# An implementation of the Customer class.
class Customer:

    # Constructor
    def __init__(self, cid=None, age=None, fname=None, lname=None, gender=None, aid=None,
                 pnum=None, email=None, password=None):
        self._cid = cid
        self._age = age
        self._fname = fname
        self._lname = lname
        self._gender = gender
        self._aid = aid
        self._pnum = pnum
        self._email = email
        self._password = password

    def getCid(self):
        return self._cid

    def getAge(self):
        return self._age
    
    def getFName(self):
        return self._fname

    def getGender(self):
        return self._gender

    def getLName(self):
        return self._lname
    
    def getEmail(self):
        return self._email

    def getAid(self):
        return self._aid

    def setCid(self, age):
        self._age = age

    def setFName(self, fname):
        self._fname = fname

    def setLName(self, lname):
        self._lname = lname

    def setGender(self, gender):
        self._gender = gender

    def setPnum(self, pnum):
        self._pnum = pnum

    def setEmail(self, email):
        self._email = email

    def setPassword(self, pw):
        self._password = pw

    # @return string representation
    def __str__(self):
        return str(self.fname) +" "+ str(self.lname) +" "+ str(self.email)
