from Source_Main.CrawlerCenter import CrawlerCenter
from Source_Main.TopicCenter import TopicCenter
from ModelAdapter.ModelAdapter import ModelAdapter

class SourceMain:
    def __init__(self):
        modelAdapter = ModelAdapter()
        self.crawlerCenter = CrawlerCenter(modelAdapter = modelAdapter)
        self.topicCenter = TopicCenter(modelAdapter = modelAdapter)

    def crawl(self):
        self.crawlerCenter.crawler()

    def findTopicByArticleId(self, articleId):
        return self.topicCenter.findTopicFromArticleId(articleId)

    def sortFavoriteTopic(self, userId):
        return self.topicCenter.sortFavoriteTopic(userId)

    def sortAllTopic(self, userId):
        return self.topicCenter.sortAllTopic(userId)

    def recomendRelatedArticles(self, articleId, quantity, startIndex):
        return self.topicCenter.getRecomendArticles(articleId, quantity, startIndex)