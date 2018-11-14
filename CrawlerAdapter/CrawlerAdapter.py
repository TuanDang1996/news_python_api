from CrawlerAdapter.ListPage import ListPage
from CrawlerAdapter.DetailPage import DetailPage
from CrawlerAdapter.JsonFactory import JsonFactory
from CommonFiles.app_config import app_config

class CrawlerAdapter:

    def __init__(self):
        self.magazines = app_config.Magazines
        self.listPage = ListPage()
        self.detailPage = DetailPage()
        self.jsonFactory = JsonFactory()
        self.listArticle = {}

    def crawlArticle(self):
        listArticle = {}
        for mg in self.magazines:
            print("Crawl articles of " + mg)
            jsonMagazine = self.jsonFactory.getListJsonByMagazineName(mg)
            for js in jsonMagazine:
                #prepare data
                menuJson = js["MenuJson"]
                detailJson = js["DetailJson"]
                topicCode = menuJson["Code"]

                if topicCode not in listArticle:
                    listArticle[topicCode] = []

                #crawl list page
                menuPageLink = menuJson["FormatLink"]
                self.listPage.setJsonAndLink(menuJson, menuPageLink, topicCode)
                listPageCrawled = self.listPage.crawl()

                #crawl detail page
                for at in listPageCrawled:
                    link = at["Link"]
                    self.detailPage.setJsonAndLink(detailJson, link, topicCode)
                    article = self.detailPage.crawl()
                    article['smallPicture'] = at['Image']
                    article['Magazine'] = mg
                    article['Link'] = at['Link']
                    listArticle[topicCode].append(article)
        self.listPage.stopCrawler()
        self.detailPage.stopCrawler()
        return listArticle