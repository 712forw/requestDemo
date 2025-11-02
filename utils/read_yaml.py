import yaml
from utils.my_logger import logger

def read_yaml(filename, keyword=None):
    # 这里添加keyword参数，用于指定读取的yaml文件中的某个key的值
    # 比如说我只想读取"添加部门"的数据，那么就传入这个keyword；如果没有传入，那么默认读取整个yaml文件
    logger.info(f"读取测试数据，文件为：{filename}")
    with open(filename, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    if keyword is not None:
        new_data = []
        for a in data:
            if data.get("keyword") == keyword:
                new_data.append(a)
        return new_data
    else:
        return data