import psycopg2

from DBUtils import DBUtils
from Student import Student

# Read the java properties file.
#
# @param boundle address
# @return a dictionary containing the connection information
def getBundle(filepath, sep='=', comment_char='#'):
    props = {}
    with open(filepath, "rt") as f:
        for line in f:
            l = line.strip()
            if l and not l.startswith(comment_char):
                key_value = l.split(sep)
                key = key_value[0].strip()
                value = sep.join(key_value[1:]).strip().strip('"')
                props[key] = value
    return props


# An implementation of the Registrar
class Registrar:

    def __init__(self):
        self._conn = None
        self._bundle = None


   # Open a database connection.
   #
   # @param boundle address
   # @return connection
    def  openDBConnectionWithBundle(self, bundle):
        prop =getBundle(bundle)
        return self.openDBConnection(prop['dbUser'],prop['dbPass'],prop['dbSID'],prop['dbHost'],prop['dbPort'])

   # Open the database connection.
   # @param dbUser
   # @param dbPass
   # @param dbSID
   # @param dbHost
   # @return
    def openDBConnection(self, dbUser,dbPass,dbSID,dbHost,port):
        if (self._conn != None):
            self.closeDBConnection()
        try:
            self._conn = DBUtils.openDBConnection(dbUser, dbPass, dbSID, dbHost, port)
            res = DBUtils.testConnection(self._conn)
        except psycopg2.Error as e:
            print (e)
        return res


   # Close the database connection.
    def closeConnection(self):
        try:
            DBUtils.closeConnection(self._conn)
        except psycopg2.Error as e:
            print (e)


   # Register a new student in the database.
   # @param newStudent
   # @return
    def registerStudent(self, newStudent):
        try :
            sid = 1 + DBUtils.getVar(self._conn, "select max(sid) from Students");
            newStudent.setId(sid);
            query = """
                insert into Students (sid, name) values (%s,%s)
            """
            DBUtils.executeUpdate(self._conn, query,(newStudent.getId(),newStudent.getName()));
        except psycopg2.Error as e:
                print (e)

        return newStudent;


   # Update the student's GPA in the database.
   # @param sid
   # @param gpa
   # @return
    def setGPA(self, sid, gpa):
        student = None;
        try:
            cnt = DBUtils.getVar(self._conn, "select count(*) from Students where sid = " + str(sid))
            if (cnt == 0):
                return student

            query = "update Students set gpa = " + str(gpa) + " where sid = " + str(sid)
            DBUtils.executeUpdate(self._conn, query)
            query = "select name, gpa from Students where sid =  " + str(sid)
            row = DBUtils.getRow(self._conn, query)
            student = Student(sid=sid, name=row[0], gpa=row[1])
        except psycopg2.Error as e:
            print (e)
        return student

   # Get the complete roster of students.
   # @return
    def getRoster(self):
        query = "select sid, name, gpa from Students"
        return DBUtils.getAllRows(self._conn,query)



    def addTermsDynamicSQL(self, terms):
        for i in range(len(terms)):
            term = terms[i]
        try:
            query = "insert into Terms values ('" + term + "')";
            DBUtils.executeUpdate(_conn, query);
        except psycopg2.Error as e:
            print (e)

    def addTermsPreparedStatement(self, terms):
        raise Exception("Not Supported in psycopg2")
