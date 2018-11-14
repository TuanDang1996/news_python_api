from CrawlerAdapter.Crawler import Crawler
from CommonFiles.app_config import app_config

class DetailPage(Crawler):
    def crawl(self):
        jsonDetail = self.jsonObject
        link = self.link
        print("Crawler detail page from " + link + "....")
        # lay chi tiet tung bai
        try:
            mainArticle = self.getSourceArticle(link)[0]
            # gia tri sau khi crawler ve
            result = {}
            # lay gia tri cua tung attribute
            listAttribute = jsonDetail["listAttribute"]
            for attr in listAttribute:
                if (not self.topicCode in app_config.IgnorePicture) or  (attr != "Picture"):
                    result[attr] = self.getDetailElement(mainArticle, attr)
                    if type(result[attr]) is str:
                        print(attr + " : " + result[attr])
                    elif type(result[attr]) is list:
                        print(attr + " : " + str(len(result[attr])))
            # tra du lieu ra
            return result
        except Exception as e:
            print("Getting error when cralw detail page: " + str(e))
            return {}
