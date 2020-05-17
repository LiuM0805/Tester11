import json


class BaseApi:

    @classmethod  # 修饰符对应的函数不需要实例化了
    def _json_format(cls, jq):
        print(json.dumps(jq.json(), indent=2, ensure_ascii=False))
