from CommonFiles.app_config import app_config

class common_function:
    @staticmethod
    def mapTopicIdForCode(topicId):
        switcher = {
            0: "xe",
            1: "thoisu",
            2: "giaoduc",
            3: "congdong",
            4: "kinhdoanh",
            5: "thethao",
            6: "thegioi",
            7: "giadinh",
            8: "phapluat",
            9: "khoahoc",
            10: "sohoa",
            11: "dulich",
            12: "tamsu",
            13: "giaitri"
        }

        return switcher.get(topicId)

    @staticmethod
    def getStopWords():
        with open(app_config.StopWords,'r') as my_file:
            stopwords = {word.replace('_', ' ').strip() for word in my_file.read().split('\n')}
        return stopwords

    @staticmethod
    def getIgnorePicture(megazine):
        switcher = {
            "VnExpress": app_config.VNExpressIgnorePicture,
            "TuoiTre": app_config.TuoiTreIgnorePicture
        }
        return switcher.get(megazine)