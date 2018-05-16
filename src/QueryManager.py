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
        try:
            query = """
                SELECT *
                FROM Customers
                LIMIT 1;
            """
        except psycopg2.Error as e:
            print (e)
        return DBUtils.getAllRows(self._conn, query)


    # Deals -----------------------------------------------------------------------------------
    def getAllDeals(self):
        try:
            query = """SELECT Deals.title, Deals.description, Deals.avgRating, Deals.imageURL,
                    Deals.startDate, Deals.endDate, Business.name, Business.phoneNum, Business.businessId, Deals.dealId
                    FROM Deals
                    INNER JOIN Business ON Deals.bid=Business.businessId
                    ORDER BY Business.name
                    """
        except psycopg2.Error as e:
            print (e)
        return DBUtils.getAllRows(self._conn, query)

    def getFavoritedDeals(self, customer):
        try:
            query = """
                SELECT Deals.title, Deals.description, Deals.avgRating, Deals.imageURL,
                    Deals.startDate, Deals.endDate, Business.name, Business.phoneNum,
                    Business.businessId, Deals.dealId
                FROM Deals
                INNER JOIN Favorites ON Favorites.did=Deals.dealId
                INNER JOIN Business ON Deals.bid=Business.businessId
                WHERE Favorites.cid='{cid}'
                """.format(cid=customer.getCid())
        except psycopg2.Error as e:
            print (e)
        return DBUtils.getAllRows(self._conn, query)

    def getTopNDeals(self, n):
        # Return the top n best deals (best as in highest average rating)
        try:
            query = """
                SELECT Deals.title, Deals.description, Deals.avgRating, Deals.imageURL,
                    Deals.startDate, Deals.endDate, Business.name, Business.phoneNum,
                    Business.businessId, Deals.dealId
                FROM Deals
                INNER JOIN Business ON Deals.bid=Business.businessId
                WHERE Deals.avgRating IS NOT NULL
                ORDER BY Deals.avgRating desc
                LIMIT {n}
            """.format(n=n)
        except psycopg2.Error as e:
            print (e)
        return DBUtils.getAllRows(self._conn, query)

    def searchForDeal(self, deal_name):
        try:
            # Get deal info where name or description contains a substring of the passed
            # in deal_name search string
            query = """
                    SELECT Deals.title, Deals.description, Deals.avgRating, Deals.imageURL,
                        Deals.startDate, Deals.endDate, Business.name,
                        Business.phoneNum, Business.businessId, Deals.dealId
                    FROM Deals
                    INNER JOIN Business ON Deals.bid=Business.businessId
                    where title LIKE \'%{deal_name}%\' or description LIKE \'%{deal_name}%\'
                    ORDER BY Deals.avgrating DESC
                        """.format(deal_name=deal_name)
        except psycopg2.Error as e:
            print (e)
        return DBUtils.getAllRows(self._conn, query)


    def favoriteDeal(self, deal, customer):
        try:
            # Check if the customer has already favorited this deal (select from Favorites).
            query = """SELECT count(*) FROM Favorites 
                    WHERE cid='{cid}' and did='{did}'""".format(cid=customer.getCid(), did=deal.getDid())
            result = DBUtils.getVar(self._conn, query)

            # If so, return. You can only favorite once per deal
            if (result > 0):
                print("{name} has already favorited this deal".format(name=customer.getFName()))
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
        except psycopg2.Error as e:
            print (e)
        
        
    def getUserRating(self, deal, customer):
        try:
            # Find what a user rated a value, i.e. you rated this deal x out of 5
            # First check if the value exists
            query = """
                SELECT COUNT(*) FROM Ratings
                WHERE cid='{cid}' and did='{did}'
                """.format(cid=customer.getCid(), did=deal.getDid())
            result = DBUtils.getVar(self._conn, query)
            if result < 1:
                return None
            
            query = """
                SELECT value FROM Ratings
                WHERE cid='{cid}' and did='{did}'
                """.format(cid=customer.getCid(), did=deal.getDid())
            result = DBUtils.getVar(self._conn, query)
        except psycopg2.Error as e:
            print (e)
        return result
        

    def rateDeal(self, deal, customer, value):
        try:
            # Check if the customer has already rated this deal (select from Ratings)
            query = """SELECT count(*) FROM Ratings 
                    WHERE cid='{cid}' and did='{did}'
                    """.format(cid=customer.getCid(), did=deal.getDid())
            result = DBUtils.getVar(self._conn, query)
            # If so, the rating should be updated
            if result > 0:
                print("You have already rated this deal")
                return
                
            # User rating is new and has to be added
            query = """INSERT INTO Ratings VALUES (%s, %s, %s)"""
            DBUtils.executeUpdate(self._conn, query, (customer.getCid(), deal.getDid(), value))

            # Update deal's average rating
            # 1) Count the number of ratings this now deal has
            query = """SELECT count(*) FROM Ratings 
                    WHERE did='{did}'""".format(did=deal.getDid())
            num_ratings = DBUtils.getVar(self._conn, query) # (At least one at this point since new rating was added)

            # 2) Get previous average rating
            query = """SELECT avgRating FROM Deals 
                    WHERE dealId='{did}'""".format(did=deal.getDid())
            previous_avg = DBUtils.getVar(self._conn, query)

            if previous_avg is not None:
                # 3a) Calculate updated average.
                new_avg = (previous_avg + value) / (num_ratings)
            else:
                # 3b) Set average.
                new_avg = value

            # 4) Update deal's average rating     
            query = """UPDATE Deals SET avgRating = {new_avg}
                    WHERE dealId='{did}'
                    """.format(did=deal.getDid(), new_avg=new_avg)

            DBUtils.executeUpdate(self._conn, query)
            print("Deal rated!")
        except psycopg2.Error as e:
            print (e)

        
    # Businesses -----------------------------------------------------------------------------------
    def getAllRetailers(self):
        try:
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
        except psycopg2.Error as e:
            print (e)
        return DBUtils.getAllRows(self._conn, query)
