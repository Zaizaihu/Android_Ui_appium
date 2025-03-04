import pytest
from pages.login_page import LoginPage
from utils.driver_manager import get_driver

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