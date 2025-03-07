import pytest
from pages.subLine1.login_page import LoginPage
from utils.driver_manager import get_driver
from utils.logger import setup_logger

logger = setup_logger()

class TestLogin:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = get_driver()
        self.login_page = LoginPage(self.driver)

    def test_valid_login(self):
        self.login_page.login("admin", "password123")
        # 断言登录成功（示例）
        assert "Welcome" in self.driver.page_source

    def test_invalid_login(self):
        self.login_page.login("wrong_user", "wrong_pass")
        # 断言错误提示
        assert "Invalid credentials" in self.driver.page_source

    def test_login(setup_test_case):
        try:
            logger.info("Starting login test...")
            driver, test_data = setup_test_case
            login_page = LoginPage()

            username = test_data.get('username')
            password = test_data.get('password')

            login_page.enter_username(username)
            login_page.enter_password(password)
            login_page.click_login_button()

            logger.info("Login test completed successfully.")
        except Exception as e:
            logger.error(f"Login test failed: {e}")
            raise