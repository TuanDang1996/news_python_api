from CrawlerAdapter.ND_Crawler import ND_crawler

class Crawler:
    def __init__(self):
        self.nd_crawler = ND_crawler()

    def setJsonAndLink(self, json, link, topicCode):
        self.jsonObject = json
        self.link = link
        self.topicCode = topicCode

    def getDetailElement(self, item, nameElement):
        htmlPage = self.nd_crawler
        element = self.jsonObject[nameElement]
        #kiem tra xem thanh phan nay co phai lay tat ca noi dung text ben trong hay khong
        if 'getAll' not in element:
            if('attribute' not in element):
                if type(element['index']) is int:
                    # kiểm tra chuỗi cần lấy có nằm bên trong các tag con của tag hiện tại hay không
                    if ('parentElement' in element) and ('className' in element):
                        result =  htmlPage.Re_Contents(item, element['tagName'],
                                                        element['index'],element['className'], element['parentElement'])
                    elif ('parentElement' not in element) and ('className' in element):
                        result = htmlPage.Re_Contents(item, element['tagName'], element['index'], className=element['className'])
                    elif ('parentElement' in element) and ('className' not in element):
                        result = htmlPage.Re_Contents(item, tagName=element['tagName'], index=element['index'],
                                                       parentElement=element['parentElement'])
                    else:
                        result = htmlPage.Re_Contents(item, element['tagName'], element['index'])
                else:
                    # kiểm tra chuỗi cần lấy có nằm bên trong các tag con của tag hiện tại hay không
                    if ('parentElement' in element) and ('className' in element):
                        result = htmlPage.Re_Find_All_Content(item, element['tagName']
                                                              , parentElement=element['parentElement'], className=element['className'])
                    elif ('parentElement' not in element) and ('className' in element):
                        result = htmlPage.Re_Find_All_Content(item, element['tagName'],
                                                      className=element['className'])
                    elif ('parentElement' in element) and ('className' not in element):
                        result = htmlPage.Re_Find_All_Content(item, element['tagName'],
                                                      parentElement=element['parentElement'])
                    else:
                        result = htmlPage.Re_Find_All_Content(item, element['tagName'])
            else:
                if type(element['index']) is int:
                    #lấy giá trị cua thuộc tính
                    if(('parentElement' in element) and ('className' in element)):
                        result =  htmlPage.Re_Find_Attribute(item, element['tagName'], element['attribute'], element['index'],
                                                             element['parentElement'], element['className'])
                    elif(('parentElement' in element) and ('className' not in element)):
                        result = htmlPage.Re_Find_Attribute(item, element['tagName'], element['attribute'],
                                                             element['index'], element['parentElement'])
                    elif('parentElement' not in element) and ('className' in element):
                        result = htmlPage.Re_Find_Attribute(item, element['tagName'], className=element['className'], index=element['index'],
                                                                 attribute=element['attribute'])
                    else:
                        result = htmlPage.Re_Find_Attribute(item, element['tagName'], element['attribute'],element['index'])
                else:
                    # lấy giá trị cua thuộc tính
                    if (('parentElement' in element) and ('className' in element)):
                        result = htmlPage.Re_Find_All_Attribute(item, element['tagName'], element['attribute'],
                                                                     element['parentElement'], element['className'])
                    elif (('parentElement' in element) and ('className' not in element)):
                        result = htmlPage.Re_Find_All_Attribute(item, element['tagName'], element['attribute'], element['parentElement'])
                    elif ('parentElement' not in element) and ('className' in element):
                        result = htmlPage.Re_Find_All_Attribute(item, element['tagName'],
                                                                     className=element['className'],
                                                                     attribute=element['attribute'])
                    else:
                        result = htmlPage.Re_Find_All_Attribute(item, element['tagName'], element['attribute'])
        else:
            if ('className' in element) and ('parentElement' in element):
                result = htmlPage.Re_Find_All_Text(item, element['tagName'], element['className'], element['parentElement'])
            elif ('className' not in element) and ('parentElement' in element):
                result =  htmlPage.Re_Find_All_Text(item, tagContentName=element['tagName'],
                                                            parentElement=element['parentElement'])
            elif ('className' in element) and ('parentElement' not in element):
                result = htmlPage.Re_Find_All_Text(item, tagContentName=element['tagName'], className=element['className'])
            else:
                result = htmlPage.Re_Find_All_Text(item,  element['tagName'])

        return result

    def crawl(self): raise NotImplemented

    def getSourceArticle(self, link):
        article = self.jsonObject['article']

        if 'className' in article:
            return self.nd_crawler.Get_Page_Data(link, article['htmlTag'], article['className'])
        else:
            return self.nd_crawler.Get_Page_Data(link, article['htmlTag'])

    def stopCrawler(self):
        self.nd_crawler.driver.close()