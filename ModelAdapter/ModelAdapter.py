from ModelAdapter.ModelFactory import ModelFactory
from CommonFiles.app_config import app_config

class ModelAdapter:
    def __init__(self):
        self.modelFactory = ModelFactory()

    def updateRootModel(self, articleContent):
        print("Updating root model....")
        rootModel = self.modelFactory.getRootModel()
        rootModel.prepareData(articleContent)
        rootModel.updateModel()

    def updateChildeModelByCategoryCocde(self, articleContent, topicCode):
        print("Updating childe model has code is " + topicCode + "....")
        childModel = self.modelFactory.getChildModelByTopicCode(topicCode)
        childModel.prepareData(articleContent)
        childModel.updateModel()

    def findTopicFromRootModel(self, content):
        print("Finding topic from root model....")
        rootModel = self.modelFactory.getRootModel()
        return rootModel.findTopic(content)

    def findTopicFromChildModel(self, content, topicCode):
        print("Finding topic from " + topicCode + " model....")
        childeModel = self.modelFactory.getChildModelByTopicCode(topicCode)
        return childeModel.findTopic(content)

    def getChildModelFromTopicCode(self, topicCode):
        return self.modelFactory.getChildModelByTopicCode(topicCode)