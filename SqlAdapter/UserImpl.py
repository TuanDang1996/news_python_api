from SqlAdapter.SqlBaseClass import SqlBaseClass

class UserImpl(SqlBaseClass):

    def getHistoryByUserId(self, userId):
        query = ("SELECT history "
                 "FROM user "
                 "WHERE user.id = %s")
        data = (userId)
        result = self.executeSqlQuery(query, data)
        historyString = result[0]["history"][1:-1]
        return [int(x) for x  in historyString.split(", ")]