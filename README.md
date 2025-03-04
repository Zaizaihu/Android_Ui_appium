android_ui_auto_project/
├── configs/                  # 配置文件
│   ├── devices.yaml          # 设备配置（多设备管理）
│   └── app_config.yaml       # 应用配置（包名、Activity等）
│
├── pages/                    # 页面对象模型（Page Object Model）
│   ├── base_page.py          # 页面基类（公共方法）
│   ├── login_page.py         # 登录页面操作封装
│   └── home_page.py          # 首页操作封装
│
├── test_cases/               # 测试用例
│   ├── test_login.py         # 登录功能测试
│   └── test_home.py          # 首页功能测试
│
├── utils/                    # 工具类
│   ├── driver_manager.py     # Appium 驱动管理（单例模式）
│   ├── element_finder.py     # 元素定位封装（显式等待、异常处理）
│   └── report_generator.py   # 测试报告生成（如 Allure 或 HTMLReport）
│   ├── driver_factory.py      # 驱动工厂（动态创建驱动）
│   └── pytest_utils.py        # Pytest 插件和 Fixtures
│
├── test_data/                # 测试数据
│   └── login_data.json       # 登录测试数据（用户名、密码）
│
├── logs/                     # 运行日志
│   └── appium_logs/          # Appium 服务器日志（可选）
│
├── reports/                  # 测试报告
│   └── html_report/          # HTML 格式测试报告
│
├── conftest.py               # Pytest 全局配置（Fixture 定义）
├── requirements.txt          # 依赖库列表
└── README.md                 # 项目说明