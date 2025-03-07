from appium import webdriver

class DriverFactory:
    def create_driver(self, device_config, app_config):
        """
        根据设备配置和应用配置创建 Appium 驱动
        :param device_config: 设备配置信息，从 devices.yaml 加载
        :param app_config: 应用配置信息，从 app_config.yaml 加载
        :return: Appium 驱动实例
        """
        desired_caps = {
            # 设备相关配置
            'platformName': device_config.get('platformName', 'Android'),
            'platformVersion': device_config.get('platformVersion', '10'),
            'deviceName': device_config.get('deviceName', 'emulator-5554'),

            # 应用相关配置
            'appPackage': app_config.get('appPackage'),
            'appActivity': app_config.get('appActivity'),

            # 其他配置
            'automationName': 'UiAutomator2',
            'noReset': True
        }
        # 连接 Appium 服务器，创建驱动实例
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        return driver