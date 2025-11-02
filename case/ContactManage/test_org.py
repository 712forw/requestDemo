import allure
import pytest
import os
from utils.my_logger import logger
from utils.read_yaml import read_yaml
from main import project_path

create_org_data = read_yaml(os.path.join(project_path, "caseData/ContactManage/create_org_data.yaml"))

@allure.epic("通讯录管理")
@allure.feature("部门管理")
class TestCreateOrg:
    @pytest.mark.parametrize("title, case_data", [(case_data.get("title"), case_data) for case_data in create_org_data])
    @allure.title("{title}")
    @allure.story("创建部门")
    def test_create_org(self, get_token, case_data):
        # 获取token，前之中已经获取了token
        logger.info(f"开始执行测试用例：{case_data.title()}")
        api = get_token
        # 请求接口
        api.my_request(method=case_data.get("method"), url = case_data.get("url"),
                       params={"access_token":api.token}, json=case_data.get("data"))
        # 断言
        assert api.response.json()["errcode"] == case_data.get("except")
