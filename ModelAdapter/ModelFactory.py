from ModelAdapter.LdaModel import LdaModel
from CommonFiles.app_config import app_config
from SqlAdapter.ArticleImpl import ArticleImpl
from CommonFiles.common_function import common_function


class ModelFactory:

    def __init__(self):
        self.rootModel = None
        self.childModels = []
        #build model
        self.createRootModel()
        self.createChildModels()

    def getRootModel(self):
        return self.rootModel

    def getAllChildModel(self):
        return [i[1] for i in self.childModels]

    def getChildModelByTopicCode(self, code):
        for topic in self.childModels:
            topicCode = common_function.mapTopicIdForCode(topic[0])
            if code == topicCode:
                return topic[1]

    def getChildModelByTopicId(self, id):
        for topic in self.childModels:
            if id == topic[0]:
                return topic[1]

    def createChildModels(self):
        articleDAO = ArticleImpl()
        for i in range(0, 14, 1):
            # make model
            #prepare data
            modelInfor = {
                "linkLoad": app_config.ChildLevelLoad[i],
                "linkSave": app_config.ChildLevelSave[i],
                "num_topic": 10
            }
            categoryCode = common_function.mapTopicIdForCode(i)
            data = articleDAO.getAllArticleContentByCategoryCode(categoryCode)
            #make model
            ldaModel = LdaModel(modelInfor)
            try:
                print("Loading " + categoryCode + " model...")
                ldaModel.loadModel()
            except:
                print("Creating " + categoryCode + " model...")
                ldaModel.prepareData(data)
                ldaModel.createModel()
            #put a model into array
            self.childModels.append((i, ldaModel))

    def createRootModel(self):
        # make model
        #prepare data
        modelInfor = {
            "linkLoad": app_config.RootLevelLoad,
            "linkSave": app_config.RootLevelSave,
            "num_topic": 14
        }
        #make model
        print("Lodaing Root model...")
        ldaModel = LdaModel(modelInfor)
        ldaModel.loadModel()
        #save model
        self.rootModel = ldaModel
