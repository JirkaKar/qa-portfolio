import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    opts = Options()
    opts.add_argument("--headless=new")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=opts)
    yield driver
    driver.quit()
