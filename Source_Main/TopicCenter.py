from SqlAdapter.ArticleImpl import ArticleImpl
from SqlAdapter.CategoryImpl import CategoryImpl
from SqlAdapter.UserImpl import UserImpl
from CommonFiles.common_function import common_function

class TopicCenter:
    def __init__(self, modelAdapter):
        self.modelAdapter = modelAdapter
        self.articleDAO = ArticleImpl()
        self.categoryDAO = CategoryImpl()
        self.userDAO = UserImpl()

    def findTopicFromArticleId(self, articleId):
        article = self.articleDAO.getArticleById(articleId)
        topic = self.modelAdapter.findTopicFromRootModel(article["content"])
        topicCode = common_function.mapTopicIdForCode(topic[0])
        result = self.categoryDAO.getCategoryByCode(topicCode)
        return result

    def findFavorite(self, userId):
        listTopic = []
        listUnique = []
        #get user history
        history = self.userDAO.getHistoryByUserId(userId)
        listArticle = []
        for i in history:
            listArticle.append(self.articleDAO.getArticleById(i))
        #find Favorite from history
        for at in listArticle:
            topic = self.modelAdapter.findTopicFromRootModel(at['sapo'])
            listTopic.append(topic[0])
            temp = [item[0] for item in listUnique]
            if not topic[0] in temp:
                listUnique.append((topic[0], common_function.mapTopicIdForCode(topic[0]), 1))
            else:
                i = 0
                for item in listUnique:
                    if item[0] == topic[0]:
                        listUnique[i] = (topic[0], common_function.mapTopicIdForCode(topic[0]), item[2] + 1)
                        break
                    else:
                        i = i + 1

        return sorted(listUnique, key=lambda listUnique: listUnique[2], reverse=True)

    def sortTopicByHabit(self, userId, listTopic):
        historyArray = self.findFavorite(userId)
        favoriteArray = listTopic

        i = 0
        for ha in historyArray:
            for t in range(0, len(favoriteArray), 1):
                if ha[1] == favoriteArray[t]["code"]:
                    favoriteArray[t], favoriteArray[i] = favoriteArray[i], favoriteArray[t]
                    i = i + 1

        return favoriteArray

    def sortAllTopic(self, userId):
        listTopic = self.categoryDAO.getAllCategory()
        return self.sortTopicByHabit(userId, listTopic)

    def sortFavoriteTopic(self, userId):
        listTopic = self.categoryDAO.getChoosedCategoryByUserId(userId)
        return self.sortTopicByHabit(userId, listTopic)

    def getRecomendArticles(self, articleId, quantity, startIndex):
        listArticle = self.articleDAO.getArticlesRelateWithParticularArticle(articleId, startIndex if startIndex != 0 else self.articleDAO.getNewestArticleId())
        print("Getting " + str(len(listArticle)) + " articles relate")
        article = self.articleDAO.getArticleById(articleId)
        categoryCode = self.categoryDAO.getCategoryIdFromArticle(articleId)
        print("Category code: " + categoryCode)

        particularTopic = self.modelAdapter.findTopicFromChildModel(article["sapo"], categoryCode)

        result = []
        for at in listArticle:
            topicTemp = self.modelAdapter.findTopicFromChildModel(at["sapo"], categoryCode)
            if topicTemp[0] == particularTopic[0]:
                result.append(at)
                if len(result) == quantity:
                    break

        return result
