import pytest
from base_api.my_api import BaseAPI
import const

@pytest.fixture(scope="session") # 因为实际运行中发现，每次运行测试用例都会调用这个fixture，所以这里需要设置为session级别
def get_token():
    api = BaseAPI()
    # 调用封装好的get_token方法，获取token
    api.get_token(url=const.token_url, corpid=const.corpid, corpsecret=const.corpsecret)
    return api