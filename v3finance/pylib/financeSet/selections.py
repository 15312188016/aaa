# import requests
# from config.conf import *
from pylib.getToken import *
import time
import datetime
from pprint import pprint


# self.token = get_token()

class BaseSelectios():
    def __init__(self, get_token):
        self.token = get_token

    # 收费方案-收费项筛选
    def selections_center_items(self, grade_id="", is_auto_generate=0, template_id=""):
        new_url = url_dev + f"/api/v1/selections/center_items/?grade_id={grade_id}&" \
                            f"is_auto_generate={is_auto_generate}&template_id={template_id}"
        header = {"Content-Type": "application/json",
                  "Authorization": "Bearer" + " " + self.token}
        res = requests.get(new_url, headers=header, verify=False)
        return res.json()

    #    #收费方案-学生身份筛选
    def selections_student_tags(self):
        new_url = url_dev + "/api/v1/selections/student_tags/"
        header = {"Content-Type": "application/json",
                  "Authorization": "Bearer" + " " + self.token}
        res = requests.get(new_url, headers=header, verify=False)
        return res.json()

    #收费方案-筛选折扣
    def selections_discounts(self,grade_id="",student_tag=""):
        new_url = url_dev + "/api/v1/selections/center_discounts/"
        header = {"Content-Type": "application/json",
                  "Authorization": "Bearer" + " " + self.token}
        par = {"grade_id":grade_id,"student_tag":student_tag}
        res = requests.get(new_url, headers=header, params=par,verify=False)
        return res.json()







if __name__ == '__main__':
    t1 = BaseSelectios(get_token(username="kh_test", psd="123456", access=1, idName=None))
    # pprint(t1.selections_center_items())
    pprint(t1.selections_discounts())
