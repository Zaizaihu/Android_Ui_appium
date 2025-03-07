import pytest
import yaml
import json
from utils.driver_manager import DriverManager
from utils.driver_factory import DriverFactory
from utils.logger import setup_logger

logger = setup_logger()

@pytest.fixture(scope="function")
def setup_test_case():
    try:
        logger.info("Starting test case setup...")
        with open('configs/devices.yaml', 'r') as f:
            device_config = yaml.safe_load(f)
        with open('configs/app_config.yaml', 'r') as f:
            app_config = yaml.safe_load(f)

        driver_factory = DriverFactory()
        driver = driver_factory.create_driver(device_config, app_config)
        DriverManager.set_driver(driver)

        with open('test_data/subLine1/login_data.json', 'r') as f:
            test_data = json.load(f)

        logger.info("Test case setup completed successfully.")
        yield driver, test_data

        driver.quit()
        logger.info("Driver quit successfully after test case execution.")
    except Exception as e:
        logger.error(f"Error during test case setup: {e}")
        raise