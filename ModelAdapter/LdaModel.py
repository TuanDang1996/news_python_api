from ModelAdapter.UnderSeaObject import UnderSea
from CommonFiles.common_function import common_function
import gensim
from gensim import corpora


class LdaModel:

    def __init__(self, modelInfor):
        self.vi_stop = common_function.getStopWords()
        self.tokenizer = UnderSea()
        self.linkLoad = modelInfor["linkLoad"]
        self.linkSave = modelInfor["linkSave"]
        self.num_topic = modelInfor["num_topic"]
        self.model = None
        self.data = []

    def createModel(self):
        texts = self.data
        # turn our tokenized documents into a id <-> term dictionary
        dictionary = corpora.Dictionary(texts)

        # convert tokenized documents into a document-term matrix
        corpus = [dictionary.doc2bow(text) for text in texts]

        # generate LDA model
        self.model = gensim.models.ldamodel.LdaModel(corpus, num_topics=self.num_topic, id2word=dictionary, passes=20)
        self.saveModel()

    def prepareData(self, doc_set):
        texts = []

        # loop through document list
        for i in doc_set:
            tokens = self.tokenizer.tokenize(i)
            # remove stop words from tokens
            stopped_tokens = [i for i in tokens if not i in self.vi_stop]
            # add tokens to list
            texts.append(stopped_tokens)

        self.data = texts

    def updateModel(self):
        texts = self.data
        # turn our tokenized documents into a id <-> term dictionary
        dictionary = corpora.Dictionary(texts)
        other_corpus = [dictionary.doc2bow(text) for text in texts]
        self.model.update(other_corpus)
        self.saveModel()


    def findTopic(self, content):
        tokens = self.tokenizer.tokenize(content)
        stopped_tokens = [i for i in tokens if not i in self.vi_stop]
        ques_vec = self.model.id2word.doc2bow(stopped_tokens)
        result = max(self.model[ques_vec], key=lambda item: item[1])
        return result

    def loadModel(self):
        linkLoad = self.linkLoad
        self.model = gensim.models.ldamodel.LdaModel.load(linkLoad)

    def saveModel(self):
        linkSave = self.linkSave
        self.model.save(linkSave)

