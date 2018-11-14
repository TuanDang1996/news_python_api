from SqlAdapter.SqlBaseClass import SqlBaseClass

class PictureDAO(SqlBaseClass):

    def addPicture(self, articleId, des, link):
        # prepare query and data
        try:
            query = ("INSERT INTO pictures "
                 "(articleId, link, description) "
                 "VALUES (%(articleId)s, %(link)s, %(description)s)")
            data = {
                "articleId": articleId,
                "link": link,
                "description": des
            }
            self.insertRecord(query, data)
        except Exception as er:
            print("Getting error when insert picture from " + str(articleId) + ": " + str(er))