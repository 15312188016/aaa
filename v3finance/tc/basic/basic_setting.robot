*** Settings ***
Library  pylib.financeSet.baseSet.BaseSet     ${idName}
Library  connect_sql.connectMysql
Library  config.body_dict
Library  pylib.financeSet.selections.BaseSelectios   ${idName}
Resource  rc/Create_payment.robot
*** Test Cases ***

基础设置 - tc00001

    ${res}  base_set_get
#    log to console  &{res}[code]
    should be true   $res["code"]=="00000"
    should be true   $res["msg"]=="请求成功"



基础设置添加 - tc00002

    ${res}  base_set_post
    log to console  ${res}
    ${res_data}  evaluate   $res["data"]["data"]
    should be true  $res_data["desc"]=="apitest附件信息"
    should be true  $res_data["offset_credit_type"]==['1','2','3','4','5']
    [Teardown]  delete_basic_setting    basic_id=37


添加收费方案审核流流程设置 - tc00003
    ${res}  workflow_defines_put    1
    log to console   ${res}
    should be true   $res["code"]=="00000"
    should be true   $res["msg"]=="请求成功"
    [Teardown]      delete_workflow


更改收费方案审核流流程设置 - tc00004
     ${res}  workflow_defines_put    1
     ${res_date}   evaluate   $res["data"]["id"]
     ${modify_res}  workflow_defines_put   kind=1  workflow_id=${res_date}    new_group=True
     log to console  ${modify_res}
     should be true   $modify_res["code"]=="00000"
     should be true    $modify_res["msg"]=="请求成功"
    [Teardown]      delete_workflow


开启、关闭流程设置 - tc00005
    #添加收费方案审核流
    ${res}  workflow_defines_put    1
    should be true   $res["code"]=="00000"
    should be true   $res["msg"]=="请求成功"

    ${res_close}     open_or_close_workflow    enable_workflow=False
    ${res_close_data}  evaluate    $res_close["data"]["enable_workflow"]
    should be true   $res_close_data==False
    [Teardown]    run keywords       delete_workflow      AND    open_or_close_workflow


查看审批流历史记录 - tc00006
#创建收费方案审批流
    ${res}  workflow_defines_put    1
    ${res_date}   evaluate   $res["data"]["id"]
    should be true   $res["code"]=="00000"
    should be true   $res["msg"]=="请求成功"
#获取收费方案审批流id
    ${res_list}     list_of_all_kind
    ${res_list_1}   evaluate    $res_list["data"][0]["center_info"]["define_id"]
#查看历史记录
    ${history}      workflow_defines_update_history   ${res_list_1}
    ${history_notes}    evaluate   $history["data"][0]["notes"]
    should be true     $history_notes==["kh"]
#更改审批流后，再次点击查看历史
    ${modify_res}  workflow_defines_put   kind=1  workflow_id=${res_date}    new_group=True
    ${history_2}      workflow_defines_update_history   ${res_list_1}
    ${history_notes_2}    evaluate   $history_2["data"][0]["notes"]
    should be true    $history_notes_2==["kh","小学老师"]
    [Teardown]      delete_workflow


清除收费方案审核流 - tc00007
    #创建收费方案审批流
    ${res}  workflow_defines_put    1
    ${res_date}   evaluate   $res["data"]["id"]
    should be true   $res["code"]=="00000"
    should be true   $res["msg"]=="请求成功"
#获取收费方案审批流id
    ${res_list}     list_of_all_kind
    ${res_list_1}   evaluate    $res_list["data"][0]["center_info"]["define_id"]
#删除审核流
    ${deleted}  workflow_defines_delete     ${res_list_1}
    should be true      $deleted["code"]=="00000"
    should be true      $deleted["msg"]=="请求成功"
    [Teardown]      delete_workflow




新增收费项目(提交) - tc00008
#创建一个收费项目
    ${res}  center_items_add
    log to console  ${res}
    should be true   $res["code"]=="00000"
    should be true   $res["msg"]=="请求成功"
    ${res_data}   evaluate   $res["data"]
    should be true   "apiname" in $res_data["name"]
    should be true    $res_data["refundable"]==True
#删除对应id的收费项目
     ${centeritem_dict}   selected      SELECT id FROM finance_centeritem WHERE center_id=37;
     ${centeritem_id}   evaluate   $centeritem_dict[0]["id"]
    [Teardown]    run keywords   deleted    DELETE FROM finance_centeritem_grades where centeritem_id=${centeritem_id};
                    ...     AND   deleted    DELETE FROM finance_centeritem WHERE center_id=37;


收费项目启用禁用 - tc00009
#创建一个收费方案
    ${res}  center_items_add
    should be true   $res["code"]=="00000"
    should be true   $res["msg"]=="请求成功"
    ${res_data}   evaluate   $res["data"]
#点击禁用
    center_items_toggle_active       &{res_data}[id]
    ${item_list}   center_items_list
    ${item_status_display}    evaluate   $item_list["data"]["results"][0]["status_display"]
    should be true    $item_status_display=="已失效"
#再次启用
    center_items_toggle_active       &{res_data}[id]
    ${item_list2}   center_items_list
    ${item_status_display2}    evaluate   $item_list2["data"]["results"][0]["status_display"]
    should be true    $item_status_display2=="已生效"
#删除对应id的收费方案
     ${centeritem_dict}   selected     SELECT id FROM finance_centeritem WHERE center_id=37;
     ${centeritem_id}   evaluate   $centeritem_dict[0]["id"]
    [Teardown]    run keywords   deleted    DELETE FROM finance_centeritem_grades where centeritem_id=${centeritem_id};
                    ...     AND   deleted    DELETE FROM finance_centeritem WHERE center_id=37;


新增折扣 - tc00010
#新增折扣
    ${res}      center_discounts_add    enroll_exclusive=1    isAppointGrade=1    isAppointStudents=1
                                 ...    is_percent=True    amount=20   remarks=备注test1
    should be true   $res["code"]=="00000"
    should be true   $res["msg"]=="请求成功"
#列表展示
    ${discount_list}    center_discounts_list
    ${discount_amount}  evaluate    $discount_list["data"]["results"][0]
#    log to console  ${discount_amount}
#列表包含刚创的折扣
    should be true   $discount_amount["amount"]=="20.0000"
    [Teardown]      deleted     DELETE FROM finance_centerdiscount WHERE center_id=37;


新增折扣，保存为草稿 - tc00011
#新增折扣
     ${res}      center_discounts_add    enroll_exclusive=1    isAppointGrade=1    isAppointStudents=1
                                 ...    is_percent=True    amount=20   submitted=False   remarks=备注test1
    should be true   $res["code"]=="00000"
    should be true   $res["msg"]=="请求成功"
    #列表展示
    ${discount_list}    center_discounts_list
    ${discount_amount}  evaluate    $discount_list["data"]["results"][0]
    should be true     $discount_amount["status"]==1
    should be true     $discount_amount["status_display"]=="草稿"
    [Teardown]      deleted     DELETE FROM finance_centerdiscount WHERE center_id=37;


查看折扣详情 - tc00012
#新增折扣
    ${res}      center_discounts_add    enroll_exclusive=1    isAppointGrade=1    isAppointStudents=1
                                 ...    is_percent=True    amount=20   submitted=False   remarks=备注test1
    should be true   $res["code"]=="00000"
    should be true   $res["msg"]=="请求成功"
#列表展示
    ${discount_list}    center_discounts_list
    ${discount_id}  evaluate    $discount_list["data"]["results"][0]
    ${discount_items}   center_discounts_items      &{discount_id}[id]
    should be true    $discount_items["msg"]=="请求成功"

    [Teardown]      deleted     DELETE FROM finance_centerdiscount WHERE center_id=37;

删除折扣 - tc00013
#新增折扣
      ${res}      center_discounts_add    enroll_exclusive=1    isAppointGrade=1    isAppointStudents=1
                                 ...    is_percent=True    amount=20   submitted=False   remarks=备注test1
    should be true   $res["code"]=="00000"
    should be true   $res["msg"]=="请求成功"
#列表展示
     ${discount_list}    center_discounts_list
     ${discount_id}  evaluate    $discount_list["data"]["results"][0]
     ${delete}      center_discounts_delete     &{discount_id}[id]
     ${discount_list}    center_discounts_list
     ${discount_count}  evaluate    $discount_list["data"]
     should be true     &{discount_count}[count]==0
     [Teardown]      deleted     DELETE FROM finance_centerdiscount WHERE center_id=37;

编辑折扣 - tc00014
#新增折扣
    ${res}      center_discounts_add    enroll_exclusive=1    isAppointGrade=1    isAppointStudents=1
                                 ...    is_percent=True    amount=20   submitted=False   remarks=备注test1
    should be true   $res["code"]=="00000"
    should be true   $res["msg"]=="请求成功"
#列表展示
    ${discount_list}    center_discounts_list
    ${discount_id}  evaluate    $discount_list["data"]["results"][0]
    ${discount_items}   center_discounts_items      &{discount_id}[id]

    ${modify_dis}    center_discounts_add    enroll_exclusive=1    isAppointGrade=1    isAppointStudents=1
                                 ...    is_percent=True    amount=19   submitted=True   remarks=备注test3
                                 ...    discount_id=&{discount_id}[id]
    #列表展示
    ${discount_list2}    center_discounts_list
    ${discount_results}     evaluate    $discount_list2["data"]["results"][0]
    should be true       $discount_results["status_display"]=="已生效"
    should be true       $discount_results["amount"]=='19.0000'

    [Teardown]    deleted     DELETE FROM finance_centerdiscount WHERE center_id=37;


折扣列表筛选 - tc00015
#创建2个折扣（一个折扣草稿，一个折扣提交）
    ${res1}    center_discounts_add    enroll_exclusive=1    isAppointGrade=1    isAppointStudents=1
                                 ...    is_percent=True    amount=20   submitted=False   remarks=备注test1
    ${res2}    center_discounts_add       remarks=第二个备注
    ${discount_list}    center_discounts_list
    should be true   $discount_list["data"]["count"]==2
    ${discount_list2}    center_discounts_list   grade_id=111
    should be true   $discount_list2["data"]["count"]==1
     ${discount_list3}    center_discounts_list   status=1
     should be true   $discount_list2["data"]["count"]==1
    [Teardown]    deleted     DELETE FROM finance_centerdiscount WHERE center_id=37;


新增收费方案 - tc00016
#创建2个收费项和2个折扣
    ${res}         center_items_add
    ${res2}        center_items_add    name=apiname2     amount=20    code=1234567     fee_type=2
                            ...     pricing_method=1     submitted=True     grades=111
    ${discount1}      center_discounts_add    enroll_exclusive=1    isAppointGrade=1    isAppointStudents=1
                             ...    is_percent=True    amount=20   remarks=备注test1
    ${discount2}      center_discounts_add
#查找对应的收费项
    ${item_value_list}   selections_center_items
    ${item_value}     evaluate  $item_value_list["data"][0]["value"]
#创建body
    ${get_value}        body_templates      ${item_value}
#创建收费方案
    ${creat_payment}    payment_templates_add       ${get_value}
    should be true   $creat_payment["code"]=="00000"
    should be true   $creat_payment["msg"]=="请求成功"
    ${payment_list}     payment_templates_list
    ${payment_01}   evaluate    $payment_list["data"]["results"][0]["total_amount"]
    should be true     $payment_01==40
#查找收费项的id，用于删除
    ${centeritem_dict}   selected      SELECT id FROM finance_centeritem WHERE center_id=37;

    [Teardown]     run keywords     delete_payment_list
                         ...    AND    selected    SELECT id FROM finance_centeritem WHERE center_id=37;    idNumb3
                         ...    AND    deleted     DELETE FROM finance_centerdiscount WHERE center_id=37;
                         ...    AND    deleted_item_list       ${idNumb3}
                        ...     AND    deleted    DELETE FROM finance_centeritem WHERE center_id=37;



添加2个收费项的收费方案 - tc00017

    ${res}         center_items_add
    ${res2}        center_items_add    name=apiname2     amount=20    code=1234567     fee_type=2
                            ...     pricing_method=1     submitted=True     grades=111
    ${discount1}      center_discounts_add    enroll_exclusive=1    isAppointGrade=1    isAppointStudents=1
                             ...    is_percent=True    amount=20   remarks=备注test1
    ${discount2}      center_discounts_add
#查找对应的收费项
    ${item_value_list}   selections_center_items
    ${item_value1}     evaluate  $item_value_list["data"][0]["value"]
    ${item_value2}     evaluate  $item_value_list["data"][1]["value"]
#创建body-2个收费项
    ${get_value}        body_templates      ${item_value1}   ${item_value2}     number=2
#创建收费方案
    ${creat_payment}    payment_templates_add       ${get_value}
    should be true   $creat_payment["code"]=="00000"
    should be true   $creat_payment["msg"]=="请求成功"
    ${payment_count}     payment_templates_list
    ${count}      evaluate   $payment_count["data"]["count"]
    should be true     $count==1
    ${total_amount}      evaluate   $payment_count["data"]["results"][0]["total_amount"]
    should be true          $total_amount==120
    [Teardown]     run keywords       delete_payment_list
                         ...    AND    selected    SELECT id FROM finance_centeritem WHERE center_id=37;    idNumber2
                         ...    AND    deleted     DELETE FROM finance_centerdiscount WHERE center_id=37;
                         ...    AND    deleted_item_list      ${idNumber2}
                         ...    AND    deleted    DELETE FROM finance_centeritem WHERE center_id=37;

添加有折扣的收费方案 - tc00018
    ${res}         center_items_add
    ${discount2}      center_discounts_add
#查找对应的收费项
    ${item_value_list}   selections_center_items
    ${item_value1}     evaluate  $item_value_list["data"][0]["value"]
    ${discounts_list}    selections_discounts
    ${discounts_1}     evaluate    $discounts_list["data"][0]["value"]

#创建body
    ${get_value}        body_templates      ${item_value1}       discounts=${discounts_1}
    log to console      ${get_value}
#创建收费方案
    ${creat_payment}    payment_templates_add       ${get_value}
    should be true   $creat_payment["code"]=="00000"
    should be true   $creat_payment["msg"]=="请求成功"
    ${payment_count}     payment_templates_list
    ${money}    evaluate   $payment_count["data"]["results"][0]["total_amount"]
    should be true    $money==190
    [Teardown]     run keywords       delete_payment_list
                         ...    AND    selected    SELECT id FROM finance_centeritem WHERE center_id=37;    idNumber2
                         ...    AND    deleted     DELETE FROM finance_centerdiscount WHERE center_id=37;
                         ...    AND    deleted_item_list      ${idNumber2}
                         ...    AND    deleted    DELETE FROM finance_centeritem WHERE center_id=37;

添加草稿状态的收费方案 - tc00019
    ${res}         center_items_add
    ${discount2}      center_discounts_add
#查找对应的收费项
    ${item_value_list}   selections_center_items
    ${item_value1}     evaluate  $item_value_list["data"][0]["value"]
    ${discounts_list}    selections_discounts
    ${discounts_1}     evaluate    $discounts_list["data"][0]["value"]
#创建body
    ${get_value}        body_templates      ${item_value1}       discounts=${discounts_1}   submitted=False
    log to console      ${get_value}
#创建收费方案
    ${creat_payment}    payment_templates_add       ${get_value}
    should be true   $creat_payment["code"]=="00000"
    should be true   $creat_payment["msg"]=="请求成功"
    ${payment_status}     payment_templates_list

    ${status}    evaluate   $payment_status["data"]["results"][0]["status_display"]
    should be true    $status=="草稿"
    [Teardown]     run keywords       delete_payment_list
                         ...    AND    selected    SELECT id FROM finance_centeritem WHERE center_id=37;    idNumber2
                         ...    AND    deleted     DELETE FROM finance_centerdiscount WHERE center_id=37;
                         ...    AND    deleted_item_list      ${idNumber2}
                         ...    AND    deleted    DELETE FROM finance_centeritem WHERE center_id=37;


删除收费方案（草稿状态下的收费方案） - tc0020
    ${res}         center_items_add
    ${discount2}      center_discounts_add
#查找对应的收费项
    ${item_value_list}   selections_center_items
    ${item_value1}     evaluate  $item_value_list["data"][0]["value"]
    ${discounts_list}    selections_discounts
    ${discounts_1}     evaluate    $discounts_list["data"][0]["value"]
#创建body
    ${get_value}        body_templates      ${item_value1}       discounts=${discounts_1}   submitted=False
    log to console      ${get_value}
#创建收费方案
    ${creat_payment}    payment_templates_add       ${get_value}
    should be true   $creat_payment["code"]=="00000"
    should be true   $creat_payment["msg"]=="请求成功"
    ${payment_status}     payment_templates_list
    ${status}    evaluate   $payment_status["data"]["results"][0]["status_display"]
    should be true    $status=="草稿"
    ${get_payment_id}    evaluate    $creat_payment["data"]["id"]
    ${delete_payment}   payment_templates_delete    ${get_payment_id}
#获取列表，判断列表count是否为0
    ${payment_count}     payment_templates_list
    ${count}    evaluate   $payment_count["data"]["count"]
    should be true    $count==0

    [Teardown]     run keywords       delete_payment_list
                         ...    AND    selected    SELECT id FROM finance_centeritem WHERE center_id=37;    idNumber2
                         ...    AND    deleted     DELETE FROM finance_centerdiscount WHERE center_id=37;
                         ...    AND    deleted_item_list      ${idNumber2}
                         ...    AND    deleted    DELETE FROM finance_centeritem WHERE center_id=37;



自动生成收费方案列表展示 - tc0021
#创建一个循环的收费方案
    #rc文件中获取
    creat_payment_templates
    ${res_auto_list}   auto_invoice_list
    log to console      ${res_auto_list}
    ${auto_list_count}      evaluate   $res_auto_list["data"]["count"]
    should be true   $auto_list_count==1
    [Teardown]      delete_payments         #rc文件中获取（重新封装）

编辑自动生成收费方案并提交 - tc0022
#创建一个循环的收费方案
    #rc文件中获取
    creat_payment_templates
    ${res_auto_list}   auto_invoice_list
    ${auto_list_count}      evaluate   $res_auto_list["data"]["results"][0]["id"]
    ${res_submit}   auto_invoice_submit     ${auto_list_count}
    [Teardown]      delete_payments         #rc文件中获取（重新封装）








