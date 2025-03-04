from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

# 配置日志记录
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class ElementFinder:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, by, value, timeout=10):
        """
        通用的元素查找函数，使用显式等待
        :param by: 定位方式，如 AppiumBy.ID, AppiumBy.XPATH 等
        :param value: 定位值
        :param timeout: 等待超时时间，默认为 10 秒
        :return: 找到的元素，如果未找到则返回 None
        """
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((by, value))
            )
            logger.info(f"成功找到元素，定位方式: {by}，定位值: {value}")
            return element
        except Exception as e:
            logger.error(f"元素查找失败，定位方式: {by}，定位值: {value}，错误信息: {e}")
            return None

    def find_elements(self, by, value, timeout=10):
        """
        通用的多个元素查找函数，使用显式等待
        :param by: 定位方式，如 AppiumBy.ID, AppiumBy.XPATH 等
        :param value: 定位值
        :param timeout: 等待超时时间，默认为 10 秒
        :return: 找到的元素列表，如果未找到则返回空列表
        """
        try:
            elements = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located((by, value))
            )
            logger.info(f"成功找到 {len(elements)} 个元素，定位方式: {by}，定位值: {value}")
            return elements
        except Exception as e:
            logger.error(f"元素查找失败，定位方式: {by}，定位值: {value}，错误信息: {e}")
            return []