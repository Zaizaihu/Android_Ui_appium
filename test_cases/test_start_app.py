import pytest
from utils.driver_manager import get_driver

class TestMiAssistant:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = get_driver(device_name="O10", app_name="mi_personal_assistant")

    def test_launch_app(self):
        # 验证应用是否成功启动
        assert "shop" in self.driver.current_package

    @pytest.fixture(autouse=True)
    def teardown(self):
        yield
        self.driver.quit()