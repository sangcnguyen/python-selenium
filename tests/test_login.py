import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.login_page import LoginPage


@pytest.fixture
def browser():
  driver = webdriver.Chrome(
      service=ChromeService(ChromeDriverManager().install()))
  driver.implicitly_wait(10)
  yield driver
  driver.quit()


def test_login_valid_credentials(browser):
  login_page = LoginPage(browser)
  login_page.load()
  login_page.login("tomsmith", "SuperSecretPassword!")
  assert login_page.get_flash_message() == "You logged into a secure area!"
