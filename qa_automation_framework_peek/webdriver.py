from selenium import webdriver


class Driver:

    def __init__(self):
        self.instance = webdriver.Chrome("/Users/romanrychagivskyi/Downloads/chromedriver-7")

    def navigate(self, url):
        if isinstance(url, str):
            self.instance.get(url)
        else:
            raise TypeError("URL must be a string.")