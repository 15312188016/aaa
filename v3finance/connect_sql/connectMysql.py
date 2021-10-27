import MySQLdb
from connect_sql.sql_config import *
from robot.libraries.BuiltIn import BuiltIn

# db = MySQLdb.connect(host = "127.0.0.1",user = "root",passwd = "123456",port = 3306,db="plesson" )
db = MySQLdb.connect(host=host_taidii, user=user_taidii, passwd=password_taidii,
                     port=port_taidii, db=db_taidii, charset="utf8")
cu = db.cursor(MySQLdb.cursors.DictCursor)


def sql_search(table, search_id):
    return f"SELECT id FROM {table} WHERE center_id={search_id};"


# 查询
def selected(sql, idNumber2=None):
    cu.execute(sql)
    fc = cu.fetchall()
    print(fc)
    if idNumber2:
        BuiltIn().set_global_variable("${%s}" % idNumber2, fc)
    return fc


def deleted(sql):
    cu.execute(sql)
    db.commit()


# 批量删除收费项
def deleted_item_list(aList):
    for i in aList:
        centeritem_id = i["id"]
        sql = f"DELETE FROM finance_centeritem_grades WHERE centeritem_id = {centeritem_id};"
        deleted(sql)


# 批量删除收费方案
def delete_payment_list():
    sql1 = "SELECT id  FROM finance_paymenttemplate  where center_id=37;"
    # 获取paymenttemplate_id
    paymenttemplate_id = selected(sql1)
    for var in paymenttemplate_id:
        var_name = var["id"]
        # print(var_name)
        sql2 = f"DELETE FROM  finance_paymenttemplate_student_tags WHERE paymenttemplate_id={var_name};"
        deleted(sql2)
        sql3 = f"SELECT id  FROM finance_paymenttemplateitem  where template_id={var_name};"
        temp_id = selected(sql3)[0]["id"]
        # print(temp_id)
        sql4 = f"DELETE FROM  finance_paymenttemplateitem_discounts WHERE paymenttemplateitem_id={temp_id};"
        deleted(sql4)
        sql5 = f"DELETE FROM  finance_paymenttemplateitem  WHERE template_id={var_name};"
        deleted(sql5)
        sql6 = f"DELETE FROM  finance_paymenttemplate WHERE center_id=37 and id={var_name};"
        deleted(sql6)


# 删除基础设置
def delete_basic_setting(basic_id=37):
    sql = f"DELETE FROM finance_financesetting WHERE center_id = {basic_id};"
    cu.execute(sql)
    # data = cu.fetchone()
    db.commit()
    # cu.close()
    # db.close()


# 待优化
def delete_workflow(center_id=37, updated_by_id=61):
    sql = f"DELETE FROM workflow_financeworkflowdefinehistory WHERE updated_by_id = {updated_by_id};"
    cu.execute(sql)
    sq2 = f"DELETE FROM workflow_financeworkflowdefine WHERE center_id = {center_id};"
    cu.execute(sq2)
    db.commit()


if __name__ == "__main__":
    # set_delete = delete_basic_setting(37)
    # a = delete_workflow()
    sql = "SELECT id FROM finance_centeritem WHERE center_id=37;"
    selected(sql,1)
    #     # item_list = selected(sql)
    #     # deleted("DELETE FROM finance_centeritem WHERE center_id = 37;")
    # sql = "SELECT id  FROM finance_paymenttemplate  where center_id=37;"
    # t1 = selected(sql)
    # value = t1[1]["id"]
    # print(value)
    # sql2 =f"DELETE FROM	finance_paymenttemplate_student_tags WHERE paymenttemplate_id={value};"
    # t2 = deleted(sql2)
    # sql3 = "SELECT id FROM finance_paymenttemplateitem where template_id = 124;"
    # print(delete_payment_list())
    # delete_payment_list()
    pass
