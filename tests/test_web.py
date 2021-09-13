import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from pages.result import ResultPage
from pages.search import SearchPage


@pytest.fixture
def browser():
    # Initialize ChromeDriver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)

    yield driver

    driver.quit()


def test_basic_duckduckgo_search(browser):
    PHRASE = 'panda'
    search_page = SearchPage(browser)
    search_page.load()
    search_page.search(PHRASE)
    result_page = ResultPage(browser)
    assert result_page.link_div_count() > 0
    assert result_page.phrase_result_count(PHRASE) > 0
    assert result_page.search_input_value() == PHRASE
