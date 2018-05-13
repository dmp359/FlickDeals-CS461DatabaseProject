import pandas as pd

class Business:
    # Constructor
    def __init__(self, bid, url, title,
                 desc, avg_rating, img, start_date,
                 end_date, dur_id,bid):
        self._did = did
        self._date_submitted = date_submitted
        self._title = title
        self._desc = desc
        self._avg_rating = avg_rating
        self._img = img
        self._start_date = start_date
        self._end_date = end_date
        self._dur_id = dur_id
        self._bid = bid

    #  @return did
    def getDid(self):
        return self._did
    
    def getTitle(self):
        return self._title
    
    def getDescription(self):
        return self._desc
    
    def getImage(self):
        return self._img

    # @return string representation
    def __str__(self):
        return str(self._title) +" "+ str(self._desc) +" "+ str(self._img)


    # @return panda dataframe
    @staticmethod
    def showAsTable(rows):
        df = pd.DataFrame(columns=["name","rating"])
        for i in rows:
            df.loc[df.shape[0]] = i
        return df