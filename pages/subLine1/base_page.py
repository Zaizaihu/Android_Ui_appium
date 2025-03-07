from utils.element_finder import ElementFinder
import os
from utils.logger import setup_logger

logger = setup_logger()

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.element_finder = ElementFinder(driver)

    def click_element(self, by, value):
        """
        点击元素
        :param by: 定位方式
        :param value: 定位值
        """
        element = self.element_finder.find_element(by, value)
        if element:
            element.click()

    def input_text(self, by, value, text):
        """
        在元素中输入文本
        :param by: 定位方式
        :param value: 定位值
        :param text: 要输入的文本
        """
        element = self.element_finder.find_element(by, value)
        if element:
            element.clear()
            element.send_keys(text)

    def swipe_up(self, duration=800):
        """
        向上滑动屏幕
        :param duration: 滑动持续时间，单位为毫秒
        """
        size = self.driver.get_window_size()
        start_x = size['width'] * 0.5
        start_y = size['height'] * 0.8
        end_y = size['height'] * 0.2
        self.driver.swipe(start_x, start_y, start_x, end_y, duration)

    def swipe_down(self, duration=800):
        """
        向下滑动屏幕
        :param duration: 滑动持续时间，单位为毫秒
        """
        size = self.driver.get_window_size()
        start_x = size['width'] * 0.5
        start_y = size['height'] * 0.2
        end_y = size['height'] * 0.8
        self.driver.swipe(start_x, start_y, start_x, end_y, duration)

    def swipe_left(self, duration=800):
        """
        向左滑动屏幕
        :param duration: 滑动持续时间，单位为毫秒
        """
        size = self.driver.get_window_size()
        start_x = size['width'] * 0.8
        start_y = size['height'] * 0.5
        end_x = size['width'] * 0.2
        self.driver.swipe(start_x, start_y, end_x, start_y, duration)

    def swipe_right(self, duration=800):
        """
        向右滑动屏幕
        :param duration: 滑动持续时间，单位为毫秒
        """
        size = self.driver.get_window_size()
        start_x = size['width'] * 0.2
        start_y = size['height'] * 0.5
        end_x = size['width'] * 0.8
        self.driver.swipe(start_x, start_y, end_x, start_y, duration)

    def assert_element_displayed(self, by, value):
        """
        断言元素是否显示
        :param by: 定位方式
        :param value: 定位值
        :return: 如果元素显示返回 True，否则返回 False
        """
        element = self.element_finder.find_element(by, value)
        if element:
            return element.is_displayed()
        return False

    def take_screenshot(self, file_name):
        screenshot_dir = 'logs/screenshots'
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)
        file_path = os.path.join(screenshot_dir, file_name)
        try:
            self.driver.save_screenshot(file_path)
            logger.info(f"Screenshot saved to {file_path}")
        except Exception as e:
            logger.error(f"Failed to take screenshot: {e}")