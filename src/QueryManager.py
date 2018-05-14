import psycopg2

from DBUtils import DBUtils
from Users import User
from Deal import Deal
from Business import Business

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


class QueryManager:

    def __init__(self):
        self._conn = None
        self._bundle = None


   # Open a database connection.
   #
   # @param boundle address
   # @return connection
    def openDBConnectionWithBundle(self, bundle):
        prop = getBundle(bundle)
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

    # Deals -----------------------------------------------------------------------------------
    def getAllDeals(self):
        query = '''SELECT Deals.title, Deals.description, Deals.avgRating, Deals.imageURL,
                   Deals.startDate, Deals.endDate, Business.name, Business.phoneNum, Business.businessId, Deals.dealId
                   FROM Deals
                   INNER JOIN Business ON Deals.bid=Business.businessId
                   ORDER BY Business.name
                '''
        return DBUtils.getAllRows(self._conn, query)
    
    def getTopNDeals(self, n):
        query = '''SELECT Deals.title, Deals.description, Deals.avgRating, Deals.imageURL,
            Deals.startDate, Deals.endDate, Business.name, Business.phoneNum, Business.businessId, Deals.dealId
            FROM Deals
            INNER JOIN Business ON Deals.bid=Business.businessId
            ORDER BY Deals.avgRating desc
            limit {n}
        '''.format(n=n)
        return DBUtils.getAllRows(self._conn, query)

    def searchForDeal(self, deal_name):
        # TODO: Maybe also UNION with 'FROM Deals where description matches deal name
        query = '''SELECT Deals.title, Deals.description, Deals.avgRating, Deals.imageURL,
                   Deals.startDate, Deals.endDate, Business.name, Business.phoneNum, Business.businessId, Deals.dealId
                    FROM Deals
                    INNER JOIN Business ON Deals.bid=Business.businessId
                    where title LIKE \'%{deal_name}%\'
                    ORDER BY Deals.avgrating DESC;
                    '''.format(deal_name=deal_name)
        return DBUtils.getAllRows(self._conn, query)
    
    def updateFavorite_user(self, business, did, cid):
        return
        #INSERT into Favorites values ('%s', '%s');

    
    def updateFavorite_business(self, business, did, cid):
        try :
            query='''
            UPDATE Business SET numFavouritedDeals = numFavouritedDeals + 1 WHERE businessId = '%s'
            '''
            DBUtils.executeUpdate(self._conn, query, business.getBid())
            business.setNumFavorites(1 + business.getNumFavorites())
        except psycopg2.Error as e:
                print (e)

        return business



    # Businesses -----------------------------------------------------------------------------------
    def getAllRetailers(self):
        # TODO: Sort by "reputation"
        query = 'SELECT name, imageURL, homepageURL FROM Business'
        return DBUtils.getAllRows(self._conn, query)

'''

TOOD: QUERIES
/*Someone visited a deal*/
UPDATE Business SET numVisited = numVisited + 1 WHERE businessId = 'b1';

/*Added a deal to favorite list*/
/* Need the business, dealid, and user id
UPDATE Business SET numFavouritedDeals = numFavouritedDeals + 1 WHERE businessId = 'b1';
INSERT into Favorites values ('customerId', 'DealId1');

/*Someone removed deal from their favorite list*/
UPDATE Business SET numFavouritedDeals = numFavouritedDeals - 1 WHERE businessId = 'b1';

/*Searching for Deals. Returns deals details + business name + business phone number */
SELECT Deals.title, Deals.description, Deals.avgRating, Deals.imageURL, Deals.startDate, Deals.endDate, Business.name, Business.phoneNum
FROM Deals
INNER JOIN Business ON Deals.bid=Business.businessId
where title like '%izza%'
ORDER BY Deals.avgrating;

/* Customer's favorites */
SELECT title, description, avgRating, imageURL, startDate, endDate
FROM Deals
INNER JOIN Favorites ON Favorites.did=Deals.dealId
where Favorites.cid='C1';


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
'''

   # Update the student's GPA in the database.
   # @param sid
   # @param gpa
   # @return
'''
    def setGPA(self, sid, gpa):
        student = None;
        try:
            # Check if they exist
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
    def getAccounts(self):
        query = "select fname, lname, email from Users"
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
'''
