import requests
from config.conf import *
from robot.libraries.BuiltIn import BuiltIn

# 每个请求都加上self.token
# def outter(func):
#     def inner(*args, **kwargs):
#         self.token = get_self.token(*args, **kwargs)
#         res = func(self.token)
#         return res
#     return inner

def get_token(username="xxx", psd="123456", access=1,idName = None):
    new_url = url_dev + "/api/v1/token/"
    # print(new_url)
    header = {"Content-Type": "application/json"}
    body = {"username": username, "password": psd}
    res = requests.post(new_url, json=body, headers=header, verify=False)
    if access == 1 :
        if idName:
            BuiltIn().set_global_variable("${%s}" % idName, res.json()["data"]["access"])
        return res.json()["data"]["access"]
    return res.json()


if __name__ == '__main__':
    f1 = get_token(idName=12)
    print(f1)
    pass
