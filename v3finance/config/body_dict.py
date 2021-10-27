import time
import datetime

# 获取当前年月日和时间
discounts_time = time.strftime("%H:%M")
discounts_day = datetime.date.today()


# 收费方案新增(number!=1时，可以传多个收费项)
def body_templates(*item_id,discounts=None,submitted=True,is_auto_generate=False,number=1):
    if number ==1:
        if discounts:
            body_template = {"grade": "", "name": f"收费方案{discounts_day}/{discounts_time}", "is_auto_generate": is_auto_generate,
                             "submitted": submitted,
                             "items": [{"quantity": 2, "discounts": [discounts], "item_id": f"{item_id[0]}"}],
                             "student_tags": []}
        else:
            body_template = {"grade": "", "name": f"收费方案{discounts_day}/{discounts_time}", "is_auto_generate": is_auto_generate,
                             "submitted": submitted,
                             "items": [{"quantity": 2, "discounts": [], "item_id": f"{item_id[0]}"}],
                             "student_tags": []}

    if number !=1:
        body_template = {"grade": "", "name": f"收费方案{discounts_day}/{discounts_time}", "is_auto_generate": is_auto_generate,
                         "submitted": submitted,
                         "student_tags": []}
        list_item = []
        if discounts:
            item = {"quantity": 1, "discounts": [discounts]}
        else:
            item = {"quantity": 1, "discounts": []}

        for var in item_id:
            item["item_id"] = var
            list_item.append(item.copy())
        body_template["items"] = list_item
        print(body_template)
    return body_template


if __name__ == "__main__":
    print(body_templates(12,56,number=2))
