from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class ND_crawler:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument('--log-level=3')
        prefs = {"profile.managed_default_content_settings.images": 0,
                 "profile.managed_default_content_settings.videos": 0,
                 'disk-cache-size': 4096}
        chrome_options.add_experimental_option("prefs", prefs)
        self.driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='//opt//local//bin//chromedriver')

    # OK
    def Get_Page_Data(self, link, g_data_tag, class_name=None):
        if class_name == None:
            self.driver.get(link)
            g_data = self.driver.find_elements_by_tag_name(g_data_tag)
        else:
            self.driver.get(link)
            g_data = self.driver.find_elements_by_css_selector(g_data_tag + '.' + class_name)
        return g_data

    # OK
    def Re_Contents(self, item, tagName, index, className=None, parentElement=None):
        result = ''
        if parentElement == None:
            try:
                if className != None:
                    element = item.find_elements_by_css_selector(tagName + '.' + className)
                else:
                    element = item.find_elements_by_tag_name(tagName)

                if element.__len__() != 0:
                    result = result + element[index].text
                else:
                    result = ''
            except Exception as er:
                print("Getting error when get content: " + str(er))
                result = ''
        else:
            try:
                if 'className' in parentElement:
                    parent = item.find_elements_by_css_selector(parentElement['tagName'] + '.' + parentElement['className'])
                else:
                    parent = item.find_elements_by_tag_name(parentElement['tagName'])

                if className != None:
                    element = parent[parentElement['index']].find_elements_by_css_selector(tagName + '.' + className)
                else:
                    element = parent[parentElement['index']].find_elements_by_tag_name(tagName)

                if element.__len__() != 0:
                    result = result + element[index].text
                else:
                    result = ''
            except Exception as er:
                print("Getting error when get content: " + str(er))
                result = ''

        return result

    # OK
    def Re_Find_All_Text(self, item, tagContentName, className = None, parentElement=None):
        result = ''
        if (parentElement == None):
            # kiem tra xem co class hay khong
            if (className == None):
                element = item.find_elements_by_tag_name(tagContentName)
            else:
                element = item.find_elements_by_css_selector(tagContentName + '.' + className)
                # kiem tra xem co element nao thao yeu cau khong
            if (element != []):
                for i in element:
                    str = i.text + "\n"
                    result = result + str
            else:
                result = ''
        else:
            # lay thanh phan cha
            if ('className' in parentElement):
                parentItem = item.find_elements_by_css_selector(
                    parentElement['tagName'] + '.' + parentElement['className'])
            else:
                parentItem = item.find_elements_by_tag_name(parentElement['tagName'])
            if (len(parentItem) != 0):
                parent = parentItem[parentElement['index']]
                # kiem tra xem co class hay khong
                if (className == None):
                    element = parent.find_elements_by_tag_name(tagContentName)
                else:
                    element = parent.find_elements_by_css_selector(tagContentName + '.' + className)
                    # kiem tra xem co element nao thao yeu cau khong
                if (len(element) != 0):
                    for i in element:
                        str = i.text + "\n"
                        result = result + str
                else:
                    result = ''
            else:
                result = ''
        return result

    # OK
    def Re_Find_Attribute(self, item, tagName, attribute, index, parentElement=None, className=None):
        result = ''
        if (parentElement == None):
            # kiem tra xem co class hay khong
            if (className == None):
                element = item.find_elements_by_tag_name(tagName)
            else:
                element = item.find_elements_by_css_selector(tagName + '.' + className)
                # kiem tra xem co element nao thao yeu cau khong
            if (element != []):
                str = element[index].get_attribute(attribute)
                result = result + str
            else:
                result = ''
        else:
            # lay thanh phan cha
            if ('className' in parentElement):
                parentItem = item.find_elements_by_css_selector(parentElement['tagName'] + '.' + parentElement['className'])
            else:
                parentItem = item.find_elements_by_tag_name(parentElement['tagName'])
            if (len(parentItem) != 0):
                parent = parentItem[parentElement['index']]
                # kiem tra xem co class hay khong
                if (className == None):
                    element = parent.find_elements_by_tag_name(tagName)
                else:
                    element = parent.find_elements_by_css_selector(tagName + '.' + className)
                    # kiem tra xem co element nao thao yeu cau khong
                if (element != []):
                    str = element[index].get_attribute(attribute)
                    result = result + str
                else:
                    result = ''
            else:
                result = ''
        return result

    def Re_Find_All_Attribute(self, item, tagName, attribute, parentElement=None, className=None):
        result = []
        if (parentElement == None):
            # kiem tra xem co class hay khong
            if (className == None):
                element = item.find_elements_by_tag_name(tagName)
            else:
                element = item.find_elements_by_css_selector(tagName + '.' + className)
                # kiem tra xem co element nao thao yeu cau khong
            if (len(element) != 0):
                for elm in element:
                    str = elm.get_attribute(attribute)
                    result.append(str)
            else:
                result = []
        else:
            # lay thanh phan cha
            if ('className' in parentElement):
                parentItem = item.find_elements_by_css_selector(
                    parentElement['tagName'] + '.' + parentElement['className'])
            else:
                parentItem = item.find_elements_by_tag_name(parentElement['tagName'])
            if (len(parentItem) != 0):
                if type(parentElement['index']) is int:
                    parent = parentItem[parentElement['index']]
                    # kiem tra xem co class hay khong
                    if (className == None):
                        element = parent.find_elements_by_tag_name(tagName)
                    else:
                        element = parent.find_elements_by_css_selector(tagName + '.' + className)
                        # kiem tra xem co element nao thao yeu cau khong
                    if (element != []):
                        for elm in element:
                            str = elm.get_attribute(attribute)
                            result.append(str)
                    else:
                        result = []
                else:
                    for par in parentItem:
                        # kiem tra xem co class hay khong
                        if (className == None):
                            element = par.find_elements_by_tag_name(tagName)
                        else:
                            element = par.find_elements_by_css_selector(tagName + '.' + className)
                            # kiem tra xem co element nao thao yeu cau khong
                        if (element != []):
                            for elm in element:
                                str = elm.get_attribute(attribute)
                                result.append(str)
                        else:
                            result = []
            else:
                result = []
        return result

    def Re_Find_All_Content(self, item, tagName, parentElement=None, className=None):
        result = []
        if (parentElement == None):
            # kiem tra xem co class hay khong
            if (className == None):
                element = item.find_elements_by_tag_name(tagName)
            else:
                element = item.find_elements_by_css_selector(tagName + '.' + className)
                # kiem tra xem co element nao thao yeu cau khong
            if (len(element) != 0):
                for elm in element:
                    str = elm.text
                    result.append(str)
            else:
                result = []
        else:
            # lay thanh phan cha
            if ('className' in parentElement):
                parentItem = item.find_elements_by_css_selector(
                    parentElement['tagName'] + '.' + parentElement['className'])
            else:
                parentItem = item.find_elements_by_tag_name(parentElement['tagName'])
            if (len(parentItem) != 0):
                if type(parentElement['index']) is int:
                    parent = parentItem[parentElement['index']]
                    # kiem tra xem co class hay khong
                    if (className == None):
                        element = parent.find_elements_by_tag_name(tagName)
                    else:
                        element = parent.find_elements_by_css_selector(tagName + '.' + className)
                        # kiem tra xem co element nao thao yeu cau khong
                    if (element != []):
                        for elm in element:
                            str = elm.text
                            result.append(str)
                    else:
                        result = []
                else:
                    for par in parentItem:
                        # kiem tra xem co class hay khong
                        if (className == None):
                            element = par.find_elements_by_tag_name(tagName)
                        else:
                            element = par.find_elements_by_css_selector(tagName + '.' + className)
                            # kiem tra xem co element nao thao yeu cau khong
                        if (element != []):
                            for elm in element:
                                str = elm.text
                                result.append(str)
                        else:
                            result = []
            else:
                result = []
        return result