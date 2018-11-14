from CrawlerAdapter.Crawler import Crawler

class ListPage(Crawler):
    def crawl(self):
        listArticle = []
        listAttribute = self.jsonObject["listAttribute"]
        formatLink = self.link
        quantity = self.jsonObject["Quantity"]

        for i in range(1, quantity + 3, 1):
            # format link
            link = formatLink.format(i.__str__())
            print("Crawler menu page from " + link + "....")
            # lay danh sach bai viet
            listSourceArticle = self.getSourceArticle(link)
            for article in listSourceArticle:
                jsonArticle = {}
                for attr in listAttribute:
                    result = self.getDetailElement(article, attr)
                    # kiem tra ket qua tra ve
                    print(attr + ":" + result)
                    jsonArticle[attr] = result
                listArticle.append(jsonArticle)
        return listArticle
