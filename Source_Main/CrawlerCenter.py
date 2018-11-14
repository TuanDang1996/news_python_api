from CrawlerAdapter.CrawlerAdapter import CrawlerAdapter
from SqlAdapter.ArticleImpl import ArticleImpl
from CommonFiles.app_config import app_config
from SqlAdapter.PictureImpl import PictureDAO
from CommonFiles.common_function import common_function

class CrawlerCenter:
    def __init__(self, modelAdapter):
        self.modelAdapter = modelAdapter
        self.crawlerAdapter = CrawlerAdapter()
        self.articleDAO = ArticleImpl()
        self.pictureDAO = PictureDAO()



    def crawler(self):
        listArticle = self.crawlerAdapter.crawlArticle()
        listTopic = app_config.TopicCodes

        for tp in listTopic:
            listArticleCrawled = listArticle[tp]
            articles1 = self.removeExistArticle(listArticleCrawled, tp)
            articlesAfterRemove = self.removeSameArticle(articles1, tp)
            if len(articlesAfterRemove) > 0:
                self.updateModel(articlesAfterRemove, tp)
                self.insertArticles(articlesAfterRemove, tp)


    def removeSameArticle(self, listArticle, topicCode):
        detectedTopics = []
        result = []
        for at in listArticle:
            topic = self.modelAdapter.findTopicFromChildModel(at["Sapo"], topicCode)
            if (len(at["Sapo"]) != 0) and (topic[0] not in detectedTopics):
                detectedTopics.append(topic[0])
                result.append(at)
        return result

    def removeExistArticle(self, listArticle, topicCode):
        detectedTopics = []
        result = []
        list2dates = self.articleDAO.getArticlesforTwoDates(topicCode)

        for at in list2dates:
            topic = self.modelAdapter.findTopicFromChildModel(at, topicCode)
            detectedTopics.append(topic[0])

        for at in listArticle:
            if ("Sapo" in at) and (len(at["Sapo"]) != 0):
                topic = self.modelAdapter.findTopicFromChildModel(at["Sapo"], topicCode)
                if topic[0] not in detectedTopics:
                    result.append(at)
        return result

    def updateModel(self, listArticle, topicCode):
        listContent = [at["Content"] for at in listArticle]
        self.modelAdapter.updateRootModel(listContent)
        self.modelAdapter.updateChildeModelByCategoryCocde(listContent, topicCode)

    def insertArticles(self, listArticle, topicCode):
        for at in listArticle:
            self.articleDAO.importArticleToDatabase(at, topicCode)
            articleId= self.articleDAO.getNewestArticleId()
            pictures = at['Picture'] if 'Picture' in at else []
            descriptionPictures = at['ImageDescription'] if 'ImageDescription' in at else []
            desLength = len(descriptionPictures)
            ignorePicture = common_function.getIgnorePicture(at['Magazine']) if 'Magazine' in at else []
            ignoredCount = 0
            for index in range(0, len(pictures), 1):
                pic = pictures[index]
                des = descriptionPictures[index - ignoredCount] if (index - ignoredCount >= 0) and (index - ignoredCount < desLength) else ""
                check = 0
                for ig in ignorePicture:
                    if pic.find(ig) > -1:
                        check += 1
                        ignoredCount += 1
                        break
                if check == 0:
                    self.pictureDAO.addPicture(articleId, des, pic)


    def crawlerAll(self):
        listArticle = self.crawlerAdapter.crawlArticle()
        listTopic = app_config.TopicCodes

        for tp in listTopic:
            try:
                listArticleCrawled = listArticle[tp]
                if len(listArticleCrawled) > 0:
                    self.insertArticles(listArticleCrawled, tp)
            except Exception as er:
                print("Getting error when pu article into db: " + str(er))