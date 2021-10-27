# import requests
# from config.conf import *
from pylib.getToken import *
import time
import datetime
from pprint import pprint
from config.body_dict import *


# self.token = get_token()

class BaseSet():
    def __init__(self, get_token):
        self.token = get_token

    # 基础设置查看界面
    # @outter  # base_set_get = outter(base_set)
    def base_set_get(self):
        new_url = url_dev + "/api/v1/finance/settings/basic/"
        header = {"Content-Type": "application/json",
                  "Authorization": "Bearer" + " " + self.token}
        res = requests.get(new_url, headers=header, verify=False)
        return res.json()

    # 基础设置提交
    def base_set_post(self, desc="apitest附件信息", day_before_due="5", default_overdue_days="3", reminder_every_few_day=10,
                      special_offset=True, auto_offset_credit=True, calculate_discount_in_sequence=False):
        """
        desc:附件信息
        day_before_due:付款提醒-催缴
        special_offset: 专费专用
        auto_offset_credit：生成账单时自动使用备用金抵扣账单金额
        offset_credit_type：备用金自动抵扣类型
        default_overdue_days：付款期限
        reminder_every_few_day：重复催缴
        calculate_discount_in_sequence：多重折扣设置
        """
        new_url = url_dev + "/api/v1/finance/settings/basic/"
        header = {"Content-Type": "application/json",
                  "Authorization": "Bearer" + " " + self.token}
        body = {"data": {"desc": desc,
                         "day_before_due": day_before_due,
                         "special_offset": special_offset,
                         "default_overdue_days": default_overdue_days,
                         "reminder_every_few_day": reminder_every_few_day,
                         "calculate_discount_in_sequence": calculate_discount_in_sequence}}
        if auto_offset_credit:
            var = body["data"]
            var.update({"auto_offset_credit": auto_offset_credit,
                        "offset_credit_type": ["1", "2", "3", "4", "5"]})
        res = requests.post(new_url, headers=header, json=body, verify=False)
        return res.json()

    # 流程设置是否开启判断
    def is_enable_workflow(self):
        new_url = url_dev + "/api/v1/workflow/center_finance_workflow_defines/is_enable_workflow/"
        header = {"Content-Type": "application/json",
                  "Authorization": "Bearer" + " " + self.token}
        res = requests.get(new_url, headers=header, verify=False)
        return res.json()

    # 开启、关闭流程
    def open_or_close_workflow(self, enable_workflow=True):
        new_url = url_dev + "/api/v1/workflow/center_finance_workflow_defines/open_or_close/"
        header = {"Content-Type": "application/json",
                  "Authorization": "Bearer" + " " + self.token}
        body = {"enable_workflow": enable_workflow, "kind": 1}
        res = requests.post(new_url, headers=header, json=body, verify=False)
        return res.json()

    # 流程列表展示界面
    def list_of_all_kind(self):
        new_url = url_dev + "/api/v1/workflow/center_finance_workflow_defines/list_of_all_kind/"
        header = {"Content-Type": "application/json",
                  "Authorization": "Bearer" + " " + self.token}
        res = requests.get(new_url, headers=header, verify=False)
        return res.json()

    # 流程设置添加流程或更改流程
    #  workflow_id 对应的是审核流的id
    def workflow_defines_get(self, workflow_id=None):
        new_url = url_dev + "/api/v1/workflow/center_finance_workflow_defines/"
        if workflow_id:
            new_url = new_url + str(workflow_id) + "/"
        header = {"Content-Type": "application/json",
                  "Authorization": "Bearer" + " " + self.token}
        res = requests.get(new_url, headers=header, verify=False)
        return res.json()

    # 编辑、提交流程设置后提交
    def workflow_defines_put(self, kind=1, workflow_id=None, new_group=None):
        new_url = url_dev + "/api/v1/workflow/center_finance_workflow_defines/"
        if workflow_id:
            new_url = new_url + str(workflow_id) + "/"
        header = {"Content-Type": "application/json",
                  "Authorization": "Bearer" + " " + self.token}
        if new_group:
            body = {"enable_workflow": True, "kind": kind, "data": [{"pre": 0, "level": 1, "label": "审批人", "type": 3,
                                                                     "multistage": [], "contains": [92], "value": "kh"},
                                                                    {"pre": 1, "level": 2, "label": "审批人", "type": 2,
                                                                     "multistage": [], "contains": [303],
                                                                     "value": "小学老师"}]}
            res = requests.put(new_url, headers=header, json=body, verify=False)
            return res.json()
        else:
            body = {"enable_workflow": True,
                    "kind": kind,
                    "data": [{"pre": 0, "level": 1, "label": "审批人", "type": 3, "multistage": [],
                              "contains": [92], "value": "kh"}]}

            res = requests.post(new_url, headers=header, json=body, verify=False)
            return res.json()

    # 流程设置查看历史
    def workflow_defines_update_history(self, history_id):
        new_url = url_dev + "/api/v1/workflow/center_finance_workflow_defines/update_history/" + f"?define_id={history_id}"
        header = {"Content-Type": "application/json",
                  "Authorization": "Bearer" + " " + self.token}
        res = requests.get(new_url, headers=header, verify=False)
        return res.json()

    # 清除对应delete_id的审批流人员
    def workflow_defines_delete(self, delete_id):
        new_url = url_dev + f"/api/v1/workflow/center_finance_workflow_defines/{delete_id}/clear_nodes/"
        header = {"Content-Type": "application/json",
                  "Authorization": "Bearer" + " " + self.token}
        res = requests.get(new_url, headers=header, verify=False)
        return res.json()

    # 收费项列表展示
    def center_items_list(self, page_min=1, page_max=10, fee_type="", pricing_method="", source="", status="",
                          grade_id="",
                          name=""):
        new_url = url_dev + f"/api/v1/finance/center_items/?" \
                            f"page={page_min}&page_size={page_max}&fee_type={fee_type}&pricing_method={pricing_method}" \
                            f"&source{source}=&status={status}&grade_id={grade_id}&name={name}"
        header = {"Content-Type": "application/json",
                  "Authorization": "Bearer" + " " + self.token}
        res = requests.get(new_url, headers=header, verify=False)
        return res.json()

    # 收费项新增
    def center_items_add(self, name="apiname", amount=100, code="apitest", fee_type=1, pricing_method=2, submitted=True,
                         grades=110):
        discounts_time = time.strftime("%H:%M")
        discounts_day = datetime.date.today()
        new_url = url_dev + "/api/v1/finance/center_items/"
        header = {"Content-Type": "application/json",
                  "Authorization": "Bearer" + " " + self.token}
        body = {"name": f"{name}{discounts_day}/{discounts_time}", "amount": amount, "code": code, "fee_type": fee_type,
                "pricing_method": pricing_method, "submitted": submitted, "grades": [grades]}
        res = requests.post(new_url, headers=header, json=body, verify=False)
        return res.json()

    # 收费项启用、禁用
    def center_items_toggle_active(self, items_id):
        new_url = url_dev + f"/api/v1/finance/center_items/{items_id}/toggle_active/"
        header = {"Content-Type": "application/json",
                  "Authorization": "Bearer" + " " + self.token}
        res = requests.get(new_url, headers=header, verify=False)
        return res.json()

    # 折扣列表
    def center_discounts_list(self, grade_id="", page=1, page_size=10, search="", source="", status="", self_pending=0):
        new_url = url_dev + f"/api/v1/finance/center_discounts/?grade_id={grade_id}&page={page}&page_size={page_size}" \
                            f"&search={search}&source={source}&status={status}&self_pending={self_pending}"
        header = {"Content-Type": "application/json",
                  "Authorization": "Bearer" + " " + self.token}
        res = requests.get(new_url, headers=header, verify=False)
        return res.json()

    # 折扣新增/编辑
    def center_discounts_add(self, enroll_exclusive=False, isAppointGrade=False, isAppointStudents=False,
                             is_percent=False, amount=10, submitted=True, remarks="备注test", discount_id=None):
        """
        isAppointGrade           适用年级（False代表无限制）
        isAppointStudents       学生身份（False代表无限制）
        enroll_exclusive         新生优惠（False代表未勾选）
        """
        discounts_time = time.strftime("%H:%M")
        discounts_day = datetime.date.today()
        new_url = url_dev + "/api/v1/finance/center_discounts/"
        header = {"Content-Type": "application/json",
                  "Authorization": "Bearer" + " " + self.token}
        body = {"name": f"折扣api{discounts_day}/{discounts_time}", "code": "23536", "amount": amount,
                "is_percent": is_percent,
                "remarks": remarks,
                "submitted": submitted,
                "data": {"grades": [], "enroll_exclusive": False, "student_tags": [],
                         "isAppointGrade": False, "isAppointStudents": False}}
        var = body["data"]
        if isAppointGrade:
            var.update({"isAppointGrade": True, "grades": [109, 110]})
        if isAppointStudents:
            var.update({"isAppointStudents": True, "student_tags": ["业主子女", "兄弟姐妹"]})
        if enroll_exclusive:
            var.update({"enroll_exclusive": True, "enroll_exclusive_count": "13", "entranceDate": str(discounts_day)})

        if discount_id:
            new_url2 = new_url + f"{discount_id}" + "/"
            res = requests.put(new_url2, headers=header, json=body, verify=False)
            return res.json()

        res = requests.post(new_url, headers=header, json=body, verify=False)
        return res.json()

    # 查看折扣详情
    def center_discounts_items(self, items_id):
        new_url = url_dev + f"/api/v1/finance/center_discounts/{items_id}/"
        header = {"Content-Type": "application/json",
                  "Authorization": "Bearer" + " " + self.token}
        res = requests.get(new_url, headers=header, verify=False)
        return res.json()

    # 折扣审批通过  update_status:通过2 拒绝3
    def center_discounts_audit_operation(self, pending_id, update_status=2, remarks="审核通过"):
        new_url = url_dev + "/api/v1/workflow/center_finance_workflows/audit_operation/"
        header = {"Content-Type": "application/json",
                  "Authorization": "Bearer" + " " + self.token}
        body = {"update_status": update_status, "remarks": remarks, "kind": 2, "form_id": pending_id}
        res = requests.post(new_url, headers=header, json=body, verify=False)
        return res.json()

    # 折扣批量审核
    def center_discounts_batch_audit_operation(self, *pending_id, update_status=2, remarks="审核通过"):
        new_url = url_dev + "/api/v1/workflow/center_finance_workflows/batch_audit_operation/"
        header = {"Content-Type": "application/json",
                  "Authorization": "Bearer" + " " + self.token}
        body = {"form_ids": list(pending_id), "kind": 2, "update_status": update_status, "remarks": remarks}
        print(body)
        res = requests.post(new_url, headers=header, json=body, verify=False)
        return res.json()

    # 删除折扣
    def center_discounts_delete(self, items_id):
        new_url = url_dev + f"/api/v1/finance/center_discounts/{items_id}/"
        header = {"Content-Type": "application/json",
                  "Authorization": "Bearer" + " " + self.token}
        res = requests.delete(new_url, headers=header, verify=False)
        return res

    # 收费方案列表
    def payment_templates_list(self, grade_id="", page=1, page_size=10, name="", source="", status="", self_pending=0):
        new_url = url_dev + f"/api/v1/finance/payment_templates/?grade_id={grade_id}&page={page}&page_size={page_size}" \
                            f"&source={source}&status={status}&name={name}&self_pending={self_pending}"
        header = {"Content-Type": "application/json",
                  "Authorization": "Bearer" + " " + self.token}
        res = requests.get(new_url, headers=header, verify=False)
        return res.json()

    # 新增收费方案
    def payment_templates_add(self, body):
        new_url = url_dev + f"/api/v1/finance/payment_templates/"
        header = {"Content-Type": "application/json",
                  "Authorization": "Bearer" + " " + self.token}
        body = body
        res = requests.post(new_url, headers=header, json=body, verify=False)
        return res.json()

    # 收费项目审批 update_staatus:通过2 拒绝3
    # 后期优化通过kind来判断是折扣还是收费方案
    def payment_templates_audit_operation(self, form_id, update_status=2, remarks="审核通过"):
        new_url = url_dev + "/api/v1/workflow/center_finance_workflows/audit_operation/"
        header = {"Content-Type": "application/json",
                  "Authorization": "Bearer" + " " + self.token}
        body = {"update_status": update_status, "remarks": remarks, "kind": 1, "form_id": form_id}
        res = requests.post(new_url, headers=header, json=body, verify=False)
        return res.json()

    # 后期可以与折扣写一个接口（kind值区分）
    # 收费方案批量审核
    def payment_templates_batch_audit_operation(self, *pending_id, update_status=2, remarks="审核通过"):
        new_url = url_dev + "/api/v1/workflow/center_finance_workflows/batch_audit_operation/"
        header = {"Content-Type": "application/json",
                  "Authorization": "Bearer" + " " + self.token}
        body = {"form_ids": list(pending_id), "kind": 1, "update_status": update_status, "remarks": remarks}
        res = requests.post(new_url, headers=header, json=body, verify=False)
        return res.json()

    # 收费方案详情
    def payment_templates_items(self, items_id):
        new_url = url_dev + f"/api/v1/finance/payment_templates/{items_id}/"
        header = {"Content-Type": "application/json",
                  "Authorization": "Bearer" + " " + self.token}
        res = requests.get(new_url, headers=header, verify=False)
        return res.json()

    # 删除收费方案
    def payment_templates_delete(self, items_id):
        new_url = url_dev + f"/api/v1/finance/payment_templates/{items_id}/"
        header = {"Content-Type": "application/json",
                  "Authorization": "Bearer" + " " + self.token}
        res = requests.delete(new_url, headers=header, verify=False)
        return res

    # 自动生成账单列表
    def auto_invoice_list(self, page=1, page_size=10, grade_id="", template_name="", status=""):
        new_url = url_dev + f"/api/v1/finance/auto_invoice_setting/?page={page}&page_size={page_size}" \
                            f"&grade_id={grade_id}&template_name={template_name}&status={status}"
        header = {"Content-Type": "application/json",
                  "Authorization": "Bearer" + " " + self.token}
        res = requests.get(new_url, headers=header, verify=False)
        return res.json()

    # 编辑自动生成账单
    def auto_invoice_modify(self, modify_id):
        new_url = url_dev + f"/api/v1/finance/auto_invoice_setting/{modify_id}/"
        header = {"Content-Type": "application/json",
                  "Authorization": "Bearer" + " " + self.token}
        res = requests.get(new_url, headers=header, verify=False)
        return res.json()

    # 提交自动生成的账单
    def auto_invoice_submit(self,template_id,term=91,current_month=True):
        new_url = url_dev + "/api/v1/finance/auto_invoice_setting/"
        header = {"Content-Type": "application/json",
                  "Authorization": "Bearer" + " " + self.token}
        body = {"klass_students": [{"id": 165, "name": "托月班", "students": [{"id": 2109, "name": "kh小朋友"}]}],
                "students": [2109], "template_id": template_id, "term": term, "academic_year": 43,
                "auto_generate_day": 1}
        if  current_month:
            body["current_month"]=True
            body["month_list"]=["2021-09"]
            print(body)
        else:
            body["current_month"] = False
            body["month_list"] = ["2022-02"]
            print(body)
        res = requests.post(new_url, headers=header, json=body, verify=False)
        return res.json()

    # 自动生成账单查询
    def auto_invoice_items(self, item_id):
        new_url = url_dev + f"/api/v1/finance/auto_invoice_setting/{item_id}/"
        header = {"Content-Type": "application/json",
                  "Authorization": "Bearer" + " " + self.token}
        res = requests.get(new_url, headers=header, verify=False)
        return res.json()

    # 获取模板列表    暂时只有收据模板type=2
    def export_templates_items(self, type=2):
        new_url = url_dev + f"/api/v1/finance/export_templates/?type={type}"
        header = {"Content-Type": "application/json",
                  "Authorization": "Bearer" + " " + self.token}
        res = requests.get(new_url, headers=header, verify=False)
        return res.json()

    # 选择模板后确认
    def export_templates_modify(self, items_id):
        new_url = url_dev + f"/api/v1/finance/export_templates/{items_id}/active/"
        header = {"Content-Type": "application/json",
                  "Authorization": "Bearer" + " " + self.token}
        res = requests.get(new_url, headers=header, verify=False)
        return res.json()


if __name__ == '__main__':
    # baseS = base_set_get()
    # print(baseS)
    # test = base_set_post()
    # print(test)
    # test1 = is_enable_workflow()
    # print(test1)
    # test2 = list_of_all_kind()
    # pprint.pprint(test2)
    # test3 = open_or_close_workflow(False)
    # print(test3)
    # test4 = workflow_defines_get()
    # pprint.pprint(test4)
    # test5 = workflow_defines_put()
    # pprint.pprint(test5)
    # test6 = workflow_defines_update_history(27)
    # pprint.pprint(test6)
    # test7 = workflow_defines_delete(27)
    # pprint.pprint(test7)
    # test8 = center_items_list()
    # pprint.pprint(test8)
    # test9 = center_items_add()
    # pprint.pprint(test9)
    # test9 = center_items_toggle_active(29)
    # print(test9)
    # test10 = center_discounts_list(status=2, self_pending=1)
    # pprint.pprint(test10)
    # test11 = center_discounts_add()
    # print(test11)
    # test12 = center_discounts_items(78)
    # pprint.pprint(test12)
    # 已审批过的折扣，可通过接口再次审批，但不影响现有逻辑
    # test13 = center_discounts_audit_operation(11)
    # pprint.pprint(test13)
    # test14 = payment_templates_list()
    # pprint.pprint(test14)
    # test15 = payment_templates_add()
    # pprint.pprint(test15)
    # test16 = payment_templates_audit_operation(97)
    # pprint.pprint(test16)
    # test17 = center_discounts_batch_audit_operation(83,84)
    # print(test17)
    # test18 = payment_templates_batch_audit_operation(93, 94)
    # pprint.pprint(test18)
    # test19 = payment_templates_items(100)
    # pprint.pprint(test19)
    # test20 = payment_templates_delete(100)
    # print(test20)
    # test21 = center_discounts_delete(28)
    # print(test21)
    # test22 = auto_invoice_setting(template_name="hq创建的收费方案")
    # print(test22)
    # test23 = auto_invoice_modify(16)
    # print(test23)
    # test24 = auto_invoice_submit()
    # pprint.pprint(test24)
    # test25 = auto_invoice_items(56)
    # pprint.pprint(test25)
    # test26 = export_templates_items(2)
    # print(test26)
    # test27 = export_templates_modify(2)
    # pprint(test27)
    t1 = BaseSet(get_token(username="kh_test", psd="123456", access=1, idName=None))
    # tt1 = t1.base_set_get()
    # print(tt1)
    t2 = t1.center_items_list()
    pprint(t2)
    pass
