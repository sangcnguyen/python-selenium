from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    URL = "https://the-internet.herokuapp.com/login"
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#login > button")
    FLASH_MESSAGE = (By.CSS_SELECTOR,".flash")

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

    def wait_for_element(self, element):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(element))

    def login(self, username, password):
        self.wait_for_element(self.USERNAME_INPUT)
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)
        self.wait_for_element(self.PASSWORD_INPUT)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def get_flash_message(self):
      return  self.driver.find_element(*self.FLASH_MESSAGE).text.split('\n')[0].strip()