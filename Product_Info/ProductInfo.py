import selenium.webdriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class ProductInfo:
    """
    Base Class For retrieving information from websites
    """

    def __init__(self, url: str):
        self.url = url
        options = selenium.webdriver.FirefoxOptions()
        options.headless = True
        # TODO: Firefox läuft auf Fehler
        self.driver = selenium.webdriver.Firefox(GeckoDriverManager().install(), options=options)
        # self.driver = selenium.webdriver.Edge(EdgeChromiumDriverManager().install())
        self.refresh()

    def refresh(self):
        self.driver.get(self.url)

    def quit(self):
        self.driver.quit()

class AmazonInfo(ProductInfo):
    """erbt von ProductInfo"""
    def __init__(self, url: str):
        super().__init__(url)
        self.titleXPath = '//*[@id="productTitle"]'
        self.priceXPath = '//*[@id="priceblock_ourprice"]'

    def getTitle(self):
        """Returns the title of the product (product name)."""
        title = self.driver.find_element_by_xpath(self.titleXPath)
        return title.text

    def getPrice(self):
        """Returns the price of the product."""
        priceElem = self.driver.find_element_by_xpath(self.priceXPath)
        price = priceElem.text.replace("€", "").replace(" ", "").replace(",", ".")
        return float(price)