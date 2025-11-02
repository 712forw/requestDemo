import requests
from utils.my_logger import logger

class BaseAPI:
    def my_request(self, method, url, **kwargs):
        """
        企业微信接口请求封装
        :param method:
        :param url:
        :param json:
        :param params:
        :return:
        """
        logger.info(f"开始请求接口：{url}，请求方式：{method}，请求参数：{kwargs}")
        try:
            # 判断token是否存在，存在则添加到请求参数中
            if hasattr(self, "token"):
                self.response = requests.request(method=method, url=url, params={"access_token": self.token}, **kwargs)
            else:
                self.response = requests.request(method=method, url=url, **kwargs)
            logger.info(f"请求接口成功，响应信息为：{self.response.text}")
        except:
            logger.warning("请求接口失败，请检查请求信息！")
            raise Exception("请求接口失败") # raise 语句用于手动引发异常


    def get_token(self, url, corpid, corpsecret): # get请求，这里method我们不写也可以
        params = {
            "corpid": corpid,
            "corpsecret": corpsecret
        }
        logger.info("请求接口，获取token")
        self.my_request(method="GET", url=url, params=params)
        try:
            self.token = self.response.json()["token"].get("access_token")
            logger.info(f"获取token成功，token值为：{self.token}")
        except:
            logger.warning(f"获取token失败，请检查请求信息：{self.response.text}")
            raise Exception("获取token失败")