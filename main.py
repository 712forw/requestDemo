import pytest
from utils.my_logger import logger
import os

project_path = os.path.dirname(__file__)

if __name__ == '__main__':
    logger.info("开始执行接口自动化测试用例".center(50, "*"))
    pytest.main()
    logger.info("接口自动化测试用例执行完毕！".center(50, "*"))
    os.system(r"allure generate ./report/resutls -o ./report/allure-report --clean")
    logger.info("测试报告生成完毕".center(50, "*"))