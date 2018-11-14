from Source_Main.CrawlerCenter import CrawlerCenter
from ModelAdapter.ModelAdapter import ModelAdapter

if __name__ == '__main__':
    modelAdapter = ModelAdapter()
    crawlerCenter = CrawlerCenter(modelAdapter)
    crawlerCenter.crawlerAll()