import pytest
from pages.login_page import LoginPage
from utils.data_reader import read_test_data
from utils.result_writer import write_test_result

FILE_PATH = "test_data/test_data.xlsx"
URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

@pytest.mark.usefixtures("setup")
class TestLogin:
    @pytest.mark.parametrize("test_id, username, password, date, time, tester_name", read_test_data(FILE_PATH))
    def test_login(self, test_id, username, password, date, time, tester_name):
        self.driver.get(URL)
        login_page = LoginPage(self.driver)

        login_page.enter_username(username)
        login_page.enter_password(password)
        login_page.click_login()

        if login_page.is_login_successful():
            write_test_result(FILE_PATH, test_id, "Test Passed")
            assert True
        else:
            write_test_result(FILE_PATH, test_id, "Test Failed")
            assert False
