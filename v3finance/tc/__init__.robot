*** Settings ***
Library  pylib.getToken
Library  connect_sql.connectMysql
Suite Setup    run keywords   get_token    kh_test    123456    1    idName
                ...    AND     delete_basic_setting    basic_id=37
                ...    AND     delete_payment_list
                ...    AND     selected    SELECT id FROM finance_centeritem WHERE center_id=37;    idNumber1
                ...    AND     deleted     DELETE FROM finance_centerdiscount WHERE center_id=37;
                ...    AND     deleted_item_list      ${idNumber1}
                ...    AND     deleted    DELETE FROM finance_centeritem WHERE center_id=37;

