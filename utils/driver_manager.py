import os
import yaml
from appium import webdriver
from appium.options.android import UiAutomator2Options  # 导入 Appium 的 Options 类

# 配置文件路径
current_dir = os.path.dirname(os.path.abspath(__file__))
app_config_path = os.path.join(current_dir, '../configs/app_config.yaml')
devices_config_path = os.path.join(current_dir, '../configs/devices.yaml')

# 加载配置文件
with open(app_config_path, 'r', encoding='utf-8') as f:
    app_config = yaml.safe_load(f)

with open(devices_config_path, 'r', encoding='utf-8') as f:
    devices = yaml.safe_load(f)


class DriverManager:
    _instance = None  # 单例实例

    @classmethod
    def get_driver(cls, device_name="O10", app_name="mi_personal_assistant"):
        if cls._instance is None:
            # 合并设备和应用配置
            combined_caps = {
                **devices['devices'][device_name],
                **app_config['apps'][app_name]
            }

            # 创建 Appium Options 对象（替代 desired_capabilities）
            options = UiAutomator2Options().load_capabilities(combined_caps)

            # 初始化驱动
            cls._instance = webdriver.Remote(
                command_executor='http://localhost:4723/wd/hub',
                options=options  # 使用 options 参数
            )
        return cls._instance

    @classmethod
    def quit_driver(cls):
        if cls._instance is not None:
            cls._instance.quit()
            cls._instance = None


# 暴露模块级函数
get_driver = DriverManager.get_driver
quit_driver = DriverManager.quit_driver