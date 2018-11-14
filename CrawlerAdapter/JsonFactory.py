from CommonFiles.app_config import app_config
import json

class JsonFactory:
    def __init__(self):
        self.magazines = app_config.Magazines
        self.JsonLink = {}
        self.AllLink = {
            "VnExpress" : app_config.VnExpressJsonLink,
            "TuoiTre": app_config.TuoiTreJsonLink
        }
        self.loadJSON()

    def loadJSON(self):
        for mg in self.magazines:
            print("Load " + mg + " JSON...")
            listJson = []
            links = self.AllLink[mg]
            for link in links:
                elm = {}
                MenuPageLink = link + app_config.MenuPageFileName
                DetailPageLink = link + app_config.DetailPaeFileName
                elm["MenuJson"] = self.Read_Text_File(MenuPageLink)
                elm["DetailJson"] = self.Read_Text_File(DetailPageLink)
                listJson.append(elm)
            self.JsonLink[mg] = listJson

    def getListJsonByMagazineName(self, magazineName):
        return self.JsonLink[magazineName]

    def getJsonTopicByTopicCode(self, magazineName, topicCode):
        jsonMagazine = self.getListJsonByMagazineName(magazineName)
        for elm in jsonMagazine:
            menuJson = elm["MenuJson"]
            if menuJson["code"] == topicCode:
                return elm

    def getAllJson(self):
        return self.JsonLink

    def Read_Text_File(self, link):
        with open(link) as myfile:
            return json.load(myfile)