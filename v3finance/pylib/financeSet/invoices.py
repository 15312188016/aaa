from pylib.getself.self.token import *

self.token = get_self.token()


# 未审核账单列表
def center_invoices_list(klass_id="", date_created_from="", date_created_to="", search="", status="", self_pending=0,
                         template_name="", is_auto_generated="", page=1, page_size=10, invoice_no=""):
    new_url = url_dev + f"/api/v1/finance/invoices/not_approved_list/?klass_id={klass_id}&" \
                        f"date_created_from={date_created_from}&date_created_to={date_created_to}&" \
                        f"search={search}&status={status}&self_pending={self_pending}&template_name={template_name}&" \
                        f"is_auto_generated={is_auto_generated}&page={page}&page_size={page_size}&" \
                        f"invoice_no={invoice_no}"
    header = {"Content-Type": "application/json",
              "Authorization": "Bearer" + " " + self.token}

    res = requests.get(new_url, headers=header, verify=False)
    return res.json()


# 添加账单（待优化）
def center_invoices_add():
    new_url = url_dev + "/api/v1/finance/invoices/"
    header = {"Content-Type": "application/json",
              "Authorization": "Bearer" + " " + self.token}
    body = {"submitted": True, "student": 756, "date_created": "2021-9-24", "date_due": "2024-6-7", "batch_no": "",
            "payment_template": "", "klass": 123, "title": "", "remarks": "rrrTEST", "total_amount": 9800, "items": [
            {"amount": 9800, "discount_amount": 0, "total_amount": 9800, "quantity": 1, "discounts": [], "id": 17,
             "unit_price": 9800, "month_count": 1, "pricing_method": 1, "name": "学费 - 3570", "date_from": "2021-09-02",
             "date_to": "2021-09-02", "center_item": 17, "discount_names": "", "balance": 9800, "revenues": [
                {"name": "学费 - 3570", "month": "2021-09-01", "month_display": "2021-09", "unit_price": 9800,
                 "quantity": 1, "month_count": 1, "amount": 9800, "discount_names": "", "discounts": [],
                 "discount_amount": 0, "total_amount": 9800, "center_discount_records": []}]}]}
    res = requests.post(new_url, headers=header, json=body, verify=False)
    return res.json()


# 创建预付款账单（待优化）
def center_create_advance_payment_invoice():
    new_url = url_dev + "/api/v1/finance/invoices/create_advance_payment_invoice/"
    header = {"Content-Type": "application/json",
              "Authorization": "Bearer" + " " + self.token}
    body = {"submitted": True, "date_created": "2021-9-24", "date_due": "2024-6-7",
            "batch_no": "202109241420CreatePrepareStudents", "title": "",
            "students": [770, 769, 767, 765, 752, 720, 718, 717], "remarks": "预备生test", "total_amount": "10.0000",
            "items": [{"amount": "10.0000", "discount_amount": "0", "total_amount": "10.0000", "quantity": 1,
                       "unit_price": "10.0000", "value": 28, "pricing_method": 2, "center_item": 28,
                       "date_from": "2021-09-01", "date_to": "2021-09-30", "discounts": [], "revenues": [], "gst": "0",
                       "balance": "10.0000", "month_count": 1}]}
    res = requests.post(new_url, headers=header, json=body, verify=False)
    return res.json()


# 编辑账单
def center_invoices_modify(modify_id):
    new_url = url_dev + f"/api/v1/finance/invoices/{modify_id}/"
    header = {"Content-Type": "application/json",
              "Authorization": "Bearer" + " " + self.token}
    body = {"submitted": False, "student": 1019, "date_created": "2021-09-17", "date_due": "2021-09-24", "batch_no": "",
            "payment_template": "", "klass": 131, "title": "", "remarks": "qwe", "total_amount": 10, "items": [
            {"id": 6, "center_item": 6, "date_from": "2021-09-01", "date_to": "2021-09-01", "unit_price": "10.0000",
             "quantity": 1, "amount": "10.0000", "total_amount": "10.0000", "discounts": [], "revenues": [
                {"id": 89552, "month": "2021-09-01", "unit_price": "10.0000", "quantity": 1, "amount": "10.0000",
                 "discounts": [], "discount_amount": "0.0000", "total_amount": "10.0000", "center_discount_records": [],
                 "discount_names": "", "month_display": "2021-09-01", "name": "其他费用10"}], "pricing_method": 1,
             "discount_amount": "0.0000", "gst": "0.0000", "balance": "10.0000", "description": "其他费用10",
             "discounts_name": "", "month_count": 1, "name": "其他费用10"}]}
    res = requests.put(new_url, headers=header, json=body, verify=False)
    return res.json()


# 批量审核账单 （king=4账单审核）
def center_invoices_batch_audit_operation(*pending_id, update_status=2, remarks="审核通过"):
    new_url = url_dev + "/api/v1/workflow/center_finance_workflows/batch_audit_operation/"
    header = {"Content-Type": "application/json",
              "Authorization": "Bearer" + " " + self.token}
    body = {"form_ids": list(pending_id), "kind": 4, "update_status": update_status, "remarks": remarks}
    print(body)
    res = requests.post(new_url, headers=header, json=body, verify=False)
    return res.json()


# 账单单独审核
def center_invoices_audit_operation(pending_id, update_status=2, remarks="审核通过"):
    new_url = url_dev + "/api/v1/workflow/center_finance_workflows/audit_operation/"
    header = {"Content-Type": "application/json",
              "Authorization": "Bearer" + " " + self.token}
    body = {"update_status": update_status, "remarks": remarks, "kind": 4, "form_id": pending_id}
    res = requests.post(new_url, headers=header, json=body, verify=False)
    return res.json()


# 删除账单
def center_invoice_delete(items_id):
    new_url = url_dev + f"/api/v1/finance/invoices/{items_id}/"
    header = {"Content-Type": "application/json",
              "Authorization": "Bearer" + " " + self.token}
    res = requests.delete(new_url, headers=header, verify=False)
    return res


# 已审核账单列表展示
def center_invoices_approved_list(klass_id="", search="", payment_status="", self_pending=0, template_name="", page=1,
                                  page_size=10, is_auto_generated="", date_payment_from="", date_payment_to="",
                                  date_created_from="", date_created_to="", invoice_no=""):
    new_url = url_dev + f"/api/v1/finance/invoices/approved_list/?klass_id={klass_id}&search={search}&" \
                        f"payment_status={payment_status}&self_pending={self_pending}&template_name={template_name}" \
                        f"&page={page}&page_size={page_size}&is_auto_generated={is_auto_generated}&" \
                        f"date_payment_from={date_payment_from}&date_payment_to={date_payment_to}&" \
                        f"date_created_from={date_created_from}&date_created_to={date_created_to}&" \
                        f"invoice_no={invoice_no}"
    header = {"Content-Type": "application/json",
              "Authorization": "Bearer" + " " + self.token}

    res = requests.get(new_url, headers=header, verify=False)
    return res.json()


# 账单详情（未审核、已审核、已作废账单）
def center_invoice_items(items_id):
    new_url = url_dev + f"/api/v1/finance/invoices/{items_id}/"
    header = {"Content-Type": "application/json",
              "Authorization": "Bearer" + " " + self.token}
    res = requests.get(new_url, headers=header, verify=False)
    return res.json()


# 已审核账单作废
def center_invoices_approved_void(void_id, void_remarkes="作废了（后面加上时间戳）"):
    new_url = url_dev + f"/api/v1/finance/invoices/{void_id}/void/"
    header = {"Content-Type": "application/json",
              "Authorization": "Bearer" + " " + self.token}
    body = {"void_remarks": void_remarkes}
    res = requests.post(new_url, headers=header, json=body, verify=False)
    return res.json()


# 已作废账单列表
def center_invoices_void_list(klass_id="", search="", template_name="",
                              page=1, page_size=10, invoice_no=""):
    new_url = url_dev + f"/api/v1/finance/invoices/void_list/?klass_id={klass_id}&search={search}&" \
                        f"template_name={template_name}&page={page}&page_size={page_size}&invoice_no={invoice_no}"
    header = {"Content-Type": "application/json",
              "Authorization": "Bearer" + " " + self.token}
    res = requests.get(new_url, headers=header, verify=False)
    return res.json()


# 未结清账单列表
def center_invoices_outstanding_list(klass_id="", search="", template_name="", page=1, date_from="", date_to="",
                                     page_size=10, invoice_no=""):
    new_url = url_dev + f"/api/v1/finance/invoices/outstanding_list/?klass_id={klass_id}&search={search}&" \
                        f"template_name={template_name}&page={page}&page_size={page_size}&date_from={date_from}" \
                        f"&date_to={date_to}&invoice_no={invoice_no}"
    header = {"Content-Type": "application/json",
              "Authorization": "Bearer" + " " + self.token}
    res = requests.get(new_url, headers=header, verify=False)
    return res.json()


# 未结清账单普通账单缴费(未完成)
def center_receipts_single_payment(invoice_ids):
    new_url = url_dev + f"/api/v1/finance/receipts/single_payment/"
    header = {"Content-Type": "application/json",
              "Authorization": "Bearer" + " " + self.token}
    body = {"invoice_ids": [invoice_ids], "payment_methods": [{"payMethod": "银行转账", "payment_method": 2,
                                                               "payment_reference": "2362", "amount": "9801"}],
            "offset_radio": False, "credit_notes": []}
    res = requests.post(new_url, headers=header, json=body, verify=False)
    return res.json()


# 未结清账单预注册账单缴费（未完成）
def center_receipts_payment_for_advance(invoice_ids):
    new_url = url_dev + f"/api/v1/finance/receipts/payment_for_advance/"
    header = {"Content-Type": "application/json",
              "Authorization": "Bearer" + " " + self.token}
    body = {"invoice_ids": [invoice_ids], "payment_methods": [{"payMethod": "银行转账", "payment_method": 2,
                                                               "payment_reference": "qwe", "amount": "10"}],
            "offset_radio": False, "credit_notes": []}
    res = requests.post(new_url, headers=header, json=body, verify=False)
    return res.json()


# 未结清账单批量缴费（未完成）
def center_receipts_bulk_payment():
    new_url = url_dev + f"/api/v1/finance/receipts/bulk_payment/"
    header = {"Content-Type": "application/json",
              "Authorization": "Bearer" + " " + self.token}
    body = {"invoices": [{"id": 19330, "payment_method": 1, "payment_reference": "", "remarks": ""},
                         {"id": 19329, "payment_method": 1, "payment_reference": "", "remarks": ""},
                         {"id": 19328, "payment_method": 1, "payment_reference": "", "remarks": ""}]}
    res = requests.post(new_url, headers=header, json=body, verify=False)
    return res.json()


# 收据清单列表
def center_receipts_list(klass_id="", search="", template_id="", page=1, page_size=10, date_from="", date_to=""):
    new_url = url_dev + f"/api/v1/finance/receipts/?klass_id={klass_id}&search={search}&template_id={template_id}&" \
                        f"page={page}&page_size={page_size}&date_from={date_from}&date_to={date_to}"
    header = {"Content-Type": "application/json",
              "Authorization": "Bearer" + " " + self.token}
    res = requests.get(new_url, headers=header, verify=False)
    return res.json()


# 收据清单作废
def center_receipts_void_receipt():
    new_url = url_dev + f"/api/v1/finance/receipts/void_receipt/"
    header = {"Content-Type": "application/json",
              "Authorization": "Bearer" + " " + self.token}
    body = {"receipt_ids": [150, 149], "remarks": "123e"}
    res = requests.post(new_url, headers=header, json=body, verify=False)
    return res.json()


# 收据清单导出
def center_receipts_export(*ids):
    new_url = url_dev + f"/api/v1/finance/receipts/export/"
    header = {"Content-Type": "application/json",
              "Authorization": "Bearer" + " " + self.token}
    ids_list = [str(i) for i in ids]
    body = {"file_format": "pdf", "ids": ids_list}
    res = requests.post(new_url, headers=header, json=body, verify=False)
    return res


if __name__ == '__main__':
    # test1 = invoices_list(search="周小杰")
    # pprint(test1)
    # test2 = invoices_add()
    # print(test2)
    # test3 = center_invoices_batch_audit_operation(19341)
    # pprint(test3)
    # test4 = center_invoices_audit_operation(19330)
    # pprint(test4)
    # test5 = center_invoice_delete(19321)
    # pprint(test5)
    # test6 = center_invoices_approved_list(invoice_no="INV20210924017")
    # pprint(test6)
    # test7 = center_invoice_items(1636)
    # print(test7)
    # test8 = center_invoices_approved_void(19340)
    # print(test8)
    # test9 = center_invoices_modify(19316)
    # print(test9)
    # test10 = center_invoices_void_list()
    # pprint(test10)
    # test11 = center_invoices_outstanding_list()
    # pprint(test11)
    # test12 = center_receipts_single_payment()
    # pprint(test12)
    # test13 = center_receipts_bulk_payment()
    # pprint(test13)
    # test14 = center_receipts_list()
    # pprint(test14)
    # test15 = center_receipts_export(149,150)
    # pprint(test15)

    pass
