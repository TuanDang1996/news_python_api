from underthesea import word_sent, ner

class UnderSea:
    def tokenize(self, str):
        sentence = str
        doc_bow = word_sent(sentence)
        result = []
        for i in doc_bow:
            result.append(i.lower())
        return result