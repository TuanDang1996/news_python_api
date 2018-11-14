from SqlAdapter.SqlBaseClass import SqlBaseClass
from SqlAdapter.CategoryImpl import CategoryImpl
from datetime import date, datetime, timedelta

class ArticleImpl(SqlBaseClass):
    def __init__(self):
        self.categoryImpl = CategoryImpl()

    def importArticleToDatabase(self, article, categoryCode):
        if ('Content' in article) and (article['Content'].__len__ != 0):
            now = datetime.now()
            categoryId = self.categoryImpl.getCategoryIdByCode(categoryCode)
            #prepare query and data
            query = ("INSERT INTO article "
                     "(title, sapo, content, author, categoryId, picture, date, view, link, megazine) "
                     "VALUES (%(Title)s, %(Sapo)s, %(Content)s, %(Author)s, %(categoryId)s, %(picture)s, %(date)s, %(view)s, %(link)s, %(megazine)s)")
            data = {
                "Title": article["Title"],
                "Sapo": article["Sapo"],
                "Content": article["Content"],
                "Author": article["Author"],
                "categoryId": categoryId,
                "picture": article["smallPicture"],
                "date": date(now.year, now.month, now.day),
                "view": 0,
                "link": article['Link'],
                "megazine": article["Magazine"]
            }

            self.insertRecord(query, data)

    def getNewestArticleId(self):
        query = ("SELECT MAX(id) as maxId "
                 "FROM article")
        result = self.executeSqlQuery(query, ())
        return result[0]['maxId']

    def getArticleById(self, articleId):
        query = ("SELECT * "
                 "FROM article "
                 "WHERE article.id = %s")
        data = (articleId)
        result = self.executeSqlQuery(query, data)
        return result[0]

    def getAllArticleContentByCategoryCode(self, code):
        query = ("SELECT a.content "
                 "FROM article a "
                 "JOIN category c on c.id = a.categoryId "
                 "WHERE c.code = %s "
                 "LIMIT 1000")
        data = (code)
        list = self.executeSqlQuery(query, data)
        result = [ct["content"] for ct in list]
        return result

    def getArticlesforTwoDates(self, code):
        start_date = datetime.now() + timedelta(-3)
        now = datetime.now()
        query = ("SELECT a.sapo "
                 "FROM (select * from article where date BETWEEN %s AND %s) a "
                 "JOIN category c on c.id = a.categoryId "
                 "WHERE c.code = %s")
        data = (date(start_date.year, start_date.month, start_date.day), date(now.year, now.month, now.day), code)
        list = self.executeSqlQuery(query, data)
        result = [ct["sapo"] for ct in list]
        return result

    def getArticlesRelateWithParticularArticle(self, articleId, startIndex):
        query = ("select a2.id, a2.sapo, a2.title, a2.categoryId, a2.picture "
                 "from (select categoryId from article where id = %s)  a1 "
                 "join article a2 on a2.categoryId = a1.categoryId "
                 "where a2.id != %s "
                 "and a2.id < %s "
                 "order by a2.id desc "
                 "LIMIT 1000")
        data = (articleId, articleId, startIndex)
        list = self.executeSqlQuery(query, data)
        return list
