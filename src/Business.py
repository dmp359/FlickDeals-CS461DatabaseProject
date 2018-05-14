import pandas as pd

class Business:
    # Constructor
    def __init__(self, bid=None, name=None, img_url=None, homepage=None,
                 pnum=None, rid=None, num_visits=None,
                 num_favorited_deals=None):
        self._bid = bid
        self._name = name
        self._img_url = img_url
        self._homepage = homepage
        self._pnum = pnum
        self._rid = rid
        self._num_visits = num_visits
        self._num_favorited_deals = num_favorited_deals

    #  @return did
    def getBid(self):
        return self._bid
    
    def getImageUrl(self):
        return self._img_url

    def getName(self):
        return self._name
    
    def getHomepageUrl(self):
        return self._homepage
    
    def getPhoneNum(self):
        return self._pnum

    def getRid(self):
        return self._rid
    
    def getNumVisits(self):
        return self._num_visits
    
    def getNumFavorites(self):
        return self._num_favorited_deals

    def setNumVisits(self, visit):
        _num_visits = visit

    def setNumFavorites(self, fav):
        _num_favorited_deals = fav

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