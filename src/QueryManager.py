import psycopg2

from DBUtils import DBUtils
from Customer import Customer
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

    # Users -----------------------------------------------------------------------------------
    def getFirstUser(self):
        query = """
            SELECT *
            FROM Customers
            LIMIT 1;
        """
        return DBUtils.getAllRows(self._conn, query)

    # Deals -----------------------------------------------------------------------------------
    def getAllDeals(self):
        query = """SELECT Deals.title, Deals.description, Deals.avgRating, Deals.imageURL,
                   Deals.startDate, Deals.endDate, Business.name, Business.phoneNum, Business.businessId, Deals.dealId
                   FROM Deals
                   INNER JOIN Business ON Deals.bid=Business.businessId
                   ORDER BY Business.name
                """
        return DBUtils.getAllRows(self._conn, query)

    def getFavoritedDeals(self, customer):
        query = """
            SELECT Deals.title, Deals.description, Deals.avgRating, Deals.imageURL,
                   Deals.startDate, Deals.endDate, Business.name, Business.phoneNum,
                   Business.businessId, Deals.dealId
            FROM Deals
            INNER JOIN Favorites ON Favorites.did=Deals.dealId
            INNER JOIN Business ON Deals.bid=Business.businessId
            WHERE Favorites.cid='{cid}'
            """.format(cid=customer.getCid())
        return DBUtils.getAllRows(self._conn, query)

    def getTopNDeals(self, n):
        query = """
            SELECT Deals.title, Deals.description, Deals.avgRating, Deals.imageURL,
                   Deals.startDate, Deals.endDate, Business.name, Business.phoneNum,
                   Business.businessId, Deals.dealId
            FROM Deals
            INNER JOIN Business ON Deals.bid=Business.businessId
            ORDER BY Deals.avgRating desc
            LIMIT {n}
        """.format(n=n)
        return DBUtils.getAllRows(self._conn, query)

    def searchForDeal(self, deal_name):
        # TODO: Maybe also UNION with 'FROM Deals where description matches deal name
        query = """SELECT Deals.title, Deals.description, Deals.avgRating, Deals.imageURL,
                   Deals.startDate, Deals.endDate, Business.name, Business.phoneNum, Business.businessId, Deals.dealId
                    FROM Deals
                    INNER JOIN Business ON Deals.bid=Business.businessId
                    where title LIKE \'%{deal_name}%\'
                    ORDER BY Deals.avgrating DESC;
                    """.format(deal_name=deal_name)
        return DBUtils.getAllRows(self._conn, query)


    
    def favoriteDeal(self, business, deal, customer):
        try :
            query=""" This is just (step 3)
            UPDATE Business SET numFavouritedDeals = numFavouritedDeals + 1 WHERE businessId = '%s'
            """
            DBUtils.executeUpdate(self._conn, query, business.getBid())
            business.setNumFavorites(1 + business.getNumFavorites())
        except psycopg2.Error as e:
                print (e)

        return business # Return both deal and business like: [deal, business] so I can update UI

    def favoriteDeal(self, deal, customer):
        # Check if the customer has already favorited this deal (select in Favorites).
        query = """SELECT count(*) FROM Favorites 
                WHERE cid='{cid}' and did='{did}'""".format(cid=customer.getCid(), did=deal.getDid())
        result = DBUtils.getVar(self._conn, query)

        # If so, return. You can only favorite once
        if (result > 0):
            print("Deal already exists in favorites")
            return

        # Add favorite to favorite table, (linking customer and the deal)
        query = """INSERT INTO Favorites VALUES (%s, %s)"""
        DBUtils.executeUpdate(self._conn, query, (customer.getCid(), deal.getDid()))
        
        # Get the business associated with the deal
        query = """
            SELECT bid from Deals where dealId='{did}'
            """.format(did=deal.getDid()) 
        busID = DBUtils.getVar(self._conn, query)

        # Update business's num favorites
        query = """UPDATE Business SET numFavouritedDeals = numFavouritedDeals + 1
                   WHERE businessId='{bid}'
                """.format(bid=busID)
        DBUtils.executeUpdate(self._conn, query)
        print("Deal favorited! Check your profile.")
        return False # did not exist until now
        
    # Businesses -----------------------------------------------------------------------------------
    def getAllRetailers(self):
        # Businesses sorted by "reputation", which is num_visits + num_favorites * 2
        query = """
            Select name, imageURL, homePageURL, categoryName
            FROM Business
            INNER JOIN (SELECT * from Belongs_To group by cid, bid) belongTo
            on belongTo.bid=Business.businessId
            INNER JOIN Category
            on belongTo.cid=Category.categoryId
            order by (numvisited + numFavouritedDeals*2) desc
        """
        return DBUtils.getAllRows(self._conn, query)


