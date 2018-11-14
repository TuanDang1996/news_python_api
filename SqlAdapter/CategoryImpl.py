from SqlAdapter.SqlBaseClass import SqlBaseClass

class CategoryImpl(SqlBaseClass):

    def getCategoryIdByCode(self, categoryCode):
        query = ("SELECT id "
                 "FROM category "
                 "WHERE category.code = %s")
        data = (categoryCode)
        result = self.executeSqlQuery(query, data)
        return result[0]["id"]

    def getCategoryByCode(self, categoryCode):
        query = ("SELECT * "
                 "FROM category "
                 "WHERE category.code = %s")
        data = (categoryCode)
        result = self.executeSqlQuery(query, data)
        return result[0]

    def getChoosedCategoryByUserId(self, userId):
        query = ("SELECT c.id, c.name, c.code, c.icon, c.iconHeight, c.iconWidth "
                 "FROM favorite_category as f, category as c "
                 "WHERE f.categoryId = c.Id "
                 "AND f.accountId = %s")
        data = (userId)
        result = self.executeSqlQuery(query, data)
        return result

    def getAllCategory(self):
        query = ("SELECT * "
                 "FROM category ")
        result = self.executeSqlQuery(query, None)
        return result

    def getCategoryIdFromArticle(self, articleId):
        query = ("SELECT c.code "
                 "FROM (select categoryId from article a WHERE a.id = %s) a "
                 "join category c on c.id = a.categoryId")
        data = (articleId)
        result = self.executeSqlQuery(query, data)
        return result[0]["code"]