from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from fig.pages.google import BasePage

class HomePage(BasePage):

    @property
    def search_box(self) -> "WebElement":
        return self._driver.find_element(By.ID, "APjFqb")


    @property
    def google_search_button(self) -> "WebElement":
        return self._driver.find_element(By.CLASS_NAME, "gNO89b")
    

    def visit(self) -> "HomePage":
        self._driver.get("https://google.com")
        return self


    def search(self, query: str) -> "HomePage":
        self.search_box.send_keys(query)
        self.google_search_button.click()
        return self
    
