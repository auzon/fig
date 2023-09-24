from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from fig.pages.google import BasePage

class SearchPage(BasePage):

    @property
    def result_description_list(self) -> list["WebElement"]:
        return self._driver.find_elements(By.CLASS_NAME, "VwiC3b")


    def calculate_relatedness_ratio(self, query: str):
        if not self.result_description_list:
            raise Exception("Couldn't find any result element")
        
        containing = 0
        total = 0
        for result in self.result_description_list:
            if query.lower() in result.text.lower():
                containing += 1
            total += 1
        return containing / total
            
            

