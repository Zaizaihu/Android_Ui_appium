import pytest
from utils.driver_manager import get_driver, quit_driver

@pytest.fixture(scope="session", autouse=True)
def driver():
    driver = get_driver()
    yield driver
    quit_driver()