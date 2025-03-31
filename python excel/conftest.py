import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()  # Use ChromeDriver
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()
