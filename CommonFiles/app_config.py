class app_config(object):
    #Link LDA Model
    RootLevelSave = "./ModelAdapter/LDA_Model/lda.model"
    RootLevelLoad = "./ModelAdapter/LDA_Model/lda.model"
    ChildLevelSave = {
        0: "./ModelAdapter/LDA_Model/child_model/xe.model",
        1: "./ModelAdapter/LDA_Model/child_model/thoisu.model",
        2: "./ModelAdapter/LDA_Model/child_model/giaoduc.model",
        3: "./ModelAdapter/LDA_Model/child_model/congdong.model",
        4: "./ModelAdapter/LDA_Model/child_model/kinhdoanh.model",
        5: "./ModelAdapter/LDA_Model/child_model/theothao.model",
        6: "./ModelAdapter/LDA_Model/child_model/thegioi.model",
        7: "./ModelAdapter/LDA_Model/child_model/giadinh.model",
        8: "./ModelAdapter/LDA_Model/child_model/phapluat.model",
        9: "./ModelAdapter/LDA_Model/child_model/khoahoc.model",
        10: "./ModelAdapter/LDA_Model/child_model/sohoa.model",
        11: "./ModelAdapter/LDA_Model/child_model/dulich.model",
        12: "./ModelAdapter/LDA_Model/child_model/tamsu.model",
        13: "./ModelAdapter/LDA_Model/child_model/giaitri.model"
    }
    ChildLevelLoad = {
        0: "./ModelAdapter/LDA_Model/child_model/xe.model",
        1: "./ModelAdapter/LDA_Model/child_model/thoisu.model",
        2: "./ModelAdapter/LDA_Model/child_model/giaoduc.model",
        3: "./ModelAdapter/LDA_Model/child_model/congdong.model",
        4: "./ModelAdapter/LDA_Model/child_model/kinhdoanh.model",
        5: "./ModelAdapter/LDA_Model/child_model/theothao.model",
        6: "./ModelAdapter/LDA_Model/child_model/thegioi.model",
        7: "./ModelAdapter/LDA_Model/child_model/giadinh.model",
        8: "./ModelAdapter/LDA_Model/child_model/phapluat.model",
        9: "./ModelAdapter/LDA_Model/child_model/khoahoc.model",
        10: "./ModelAdapter/LDA_Model/child_model/sohoa.model",
        11: "./ModelAdapter/LDA_Model/child_model/dulich.model",
        12: "./ModelAdapter/LDA_Model/child_model/tamsu.model",
        13: "./ModelAdapter/LDA_Model/child_model/giaitri.model"
    }

    #link json file
    Magazines = ["VnExpress", "TuoiTre"]
    IgnorePicture = ["congdong", "tamsu"]

    VnExpressJsonLink = [
         "./JSON/VnExpress/JSON_Input/ThoiSu/",
         "./JSON/VnExpress/JSON_Input/TheGioi/",
         "./JSON/VnExpress/JSON_Input/CongDong/",
         "./JSON/VnExpress/JSON_Input/DuLich/",
         "./JSON/VnExpress/JSON_Input/GiaDinh/",
         "./JSON/VnExpress/JSON_Input/GiaoDuc/",
         "./JSON/VnExpress/JSON_Input/KhoaHoc/",
         "./JSON/VnExpress/JSON_Input/KinhDoanh/",
         "./JSON/VnExpress/JSON_Input/PhapLuat/",
         "./JSON/VnExpress/JSON_Input/SoHoa/",
         "./JSON/VnExpress/JSON_Input/TamSu/",
         "./JSON/VnExpress/JSON_Input/TheThao/",
         "./JSON/VnExpress/JSON_Input/Xe/",
         "./JSON/VnExpress/JSON_Input/GiaiTri/"
    ]

    TuoiTreJsonLink = [
        "./JSON/TuoiTre/JSON_Input/ThoiSu/",
        "./JSON/TuoiTre/JSON_Input/TheGioi/",
        "./JSON/TuoiTre/JSON_Input/GiaDinh/",
        "./JSON/TuoiTre/JSON_Input/GiaoDuc/",
        "./JSON/TuoiTre/JSON_Input/KinhDoanh/",
        "./JSON/TuoiTre/JSON_Input/PhapLuat/",
        "./JSON/TuoiTre/JSON_Input/KhoaHoc/",
        "./JSON/TuoiTre/JSON_Input/TheThao/",
        "./JSON/TuoiTre/JSON_Input/Xe/",
        "./JSON/TuoiTre/JSON_Input/GiaiTri/"
    ]

    MenuPageFileName = "MenuPage.json"
    DetailPaeFileName = "DetailPage.json"

    #list topic
    TopicCodes = ["thoisu", "thegioi", "xe", "giaoduc", "congdong", "kinhdoanh", "thethao", "giadinh", "phapluat", "khoahoc", "sohoa", "dulich", "tamsu", "giaitri"]

    #stop words link
    StopWords = "./VNStopWords/stopwords.words"

    #ignore image
    VNExpressIgnorePicture = ['https://static.eclick.vn', 'https://img.polyad.net', 'https://s.vnecdn.net', 'https://a.vnecdn.net']

    TuoiTreIgnorePicture = ["https://cdn.tuoitre.vn/zoom/150_120"]