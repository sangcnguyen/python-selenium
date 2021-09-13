import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from pages.result import ResultPage
from pages.search import SearchPage


@pytest.fixture
def browser():
    # Initialize ChromeDriver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    # Wait implicitly for elements to be ready before attempting interactions
    driver.implicitly_wait(10)

    # Return the driver object at the end of setup
    yield driver

    # For cleanup, quit the driver
    driver.quit()


def test_basic_duckduckgo_search(browser):
    # Set up test case data
    PHRASE = 'panda'
    # Search for the phrase
    search_page = SearchPage(browser)
    search_page.load()
    search_page.search(PHRASE)
    # Verify that results appear
    result_page = ResultPage(browser)
    assert result_page.link_div_count() > 0
    assert result_page.phrase_result_count(PHRASE) > 0
    assert result_page.search_input_value() == PHRASE
