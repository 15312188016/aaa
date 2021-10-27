*** Settings ***
Library  pylib.financeSet.baseSet.BaseSet     ${idName}
Library  connect_sql.connectMysql
Library  config.body_dict
Library  pylib.financeSet.selections.BaseSelectios   ${idName}

*** Keywords ***
#自动生成账单时，使用（封装创建收费方案）
creat_payment_templates
    ${res}            center_items_add
    ${discount2}      center_discounts_add
#查找对应的收费项
    ${item_value_list}   selections_center_items
    ${item_value1}       evaluate  $item_value_list["data"][0]["value"]
    ${discounts_list}    selections_discounts
    ${discounts_1}       evaluate    $discounts_list["data"][0]["value"]
#创建body
    ${get_value}        body_templates      ${item_value1}    is_auto_generate=True   discounts=${discounts_1}
#    log to console      ${get_value}
#创建收费方案
    ${creat_payment}    payment_templates_add       ${get_value}


#封装删除收费方案
delete_payments
    delete_payment_list
    selected    SELECT id FROM finance_centeritem WHERE center_id=37;    idNumber2
    deleted     DELETE FROM finance_centerdiscount WHERE center_id=37;
    deleted_item_list      ${idNumber2}
    deleted    DELETE FROM finance_centeritem WHERE center_id=37;