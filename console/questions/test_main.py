import time
from console.db_handle import db_handle
import datetime
from console.excel_find import *
from console.execl_read import *

if __name__ == "__main__":
    db_conn = db_handle()
    db_conn.GRANT_TYPE = 'client_credential'
    db_conn.APP_ID = 'wxb29c6899ac367ef3'
    db_conn.APP_SECRET = '931410b85b44f1f287ea144d569f4f59'
    access_token = db_conn.get_access_token()

    '''
    BASE_DIR = "../../data"
    execl_list = excel_find.find_execl(BASE_DIR, "*.xlsx")
    book_name_list = []
    for i in range(len(execl_list)):
        # print(execl_list[i])
        book_name = execl_list[i].split('\\')
        book_name_list.append(book_name[-2])
    print(book_name_list)
    execl_read = execl_read()
    book_name_list = execl_read.read_book_name()
    print(book_name_list)
    '''

    # 新增集合测试
    '''
    # db_conn.add_collection(access_token)
    introduce =       动物绝对不该穿衣服！为什么？因为山羊会把衣服当午餐吃掉，蛇会穿不进去裤子，绵羊穿上衣服会感觉很热，小负鼠一不小心就会把衣服穿反…...

    这是一本让人忍俊不禁的图画书，教会孩子发现动物的美，天生的美。
    introduce = introduce.replace(' ', '')
    introduce = introduce.replace('\r', '').replace('\n', '')
    print(introduce)
    data = 'db.collection(\"introduction\").add({data: [{introduce: "%s"}]})' % introduce
    '''

    # 插入数据测试
    '''
    collection_name = {'collection_name': 'Item_bank'}
    db_conn.add_collection(access_token, collection_name)
    book_name = '100层的房子'
    question = '多奇在上楼的过程中遇到了几种小动物？'
    right_key = 'B'
    option_a = '8种'
    option_b = '10种'
    option_c = '7种'
    option_d = '11种'
    is_delete = 0
    localtime = datetime.datetime.now()
    question_type = 0
    data = 'db.collection(\"Item_bank\").add({data: [{book_name: "%s", question: "%s", ' \
           'right_key: "%s", option_a: "%s", option_b: "%s", option_c: "%s", option_d: "%s", ' \
           'is_delete: "%d", question_type: "%d", localtime: "%s"}]})' % (book_name, question, right_key, option_a,
                                                                          option_b, option_c, option_d, is_delete,
                                                                          question_type, localtime)
    '''
    # db_conn.add_data(access_token, data)

    # 查询测试
    '''
    update方法只能更新数据，可以为数据新增字段
    set方法可以更新数据，也可以新增数据
    
    query = 
             db.collection(\"Item_bank\").where({book_name:"宫西达也永远永远爱你", question:"“不、不对......我不是.......”良太闭上了眼睛。这里良太的心情是？"}).get()
            
    query_response = db_conn.query_data_one(access_token, query)

    a = db_conn.query_result_handle(query_response)
    print(a)

    query_result = db_conn.question_Single(a)
    print(query_result)
    '''

    # print(type(query_response))
    # query_response = query_response[0]
    # query_response = query_response.split(',')
    # print(query_response)
    # query_result = []
    # for i in range(len(query_response)):
    #     element = query_response[i].split(':')
    #     element = element[1].replace('"', '')
    #     print(element)
    #     query_result.append(element)
    # print(query_result)

    # 修改测试
    '''
    book_name = '100层的房子'
    question = '多奇在上楼的过程中遇到了几种小动物？'
    right_key = 'B'
    option_a = '8种'
    option_b = '10种'
    option_c = '7种'
    option_d = '11种'
    is_delete = 0
    localtime = datetime.datetime.now()
    question_type = 0
    data = 'db.collection(\"Item_bank\").where({book_name:\"%s\", question:\"%s\"}).update({' \
           'data:{right_key:\"%s\", option_a: \"%s\", option_b: \"%s\", option_c: \"%s\", option_d: \"%s\",' \
           'is_delete: \"%d\", question_type: \"%d\", update_time: \"%s\"}})' % (
               book_name, question, right_key, option_a,
               option_b, option_c, option_d, is_delete,
               question_type, localtime)
    data = 'db.collection(\"Item_bank\").where({book_name:"%s", question:"%s"}).update({data:{' \
           'right_key:"%s",, is_delete:%d}})' % (
               book_name, question, right_key, is_delete)
    data = 
        db.collection(\"test\").doc(\"19762d645ea8e7ca000a50405ac278f2\").update({data:{age:2}})
    
    data = 
        db.collection(\"test\").doc(\"19762d645ea8e7ca000a50405ac278f1\").set({data:{
            description: \"set\",
            done: true
            }})
    
    data = 
        db.collection(\"test\").doc(\"19762d645ea8e7ca000a50405ac278f3\").set({data:{
            name: "kaka",
            kaka: 20
            }})
            
    db_conn.modify_data(access_token, data)
    '''

    # print(a['errcode'])
    # db_conn.delete_data(access_token, '87017e375ea4fe390033dd7f6fda8221')

    # 读前读后思考测试
    '''
    book_path = excel_find.input_path()
    execl_list = excel_find.find_execl(book_path, "*.xlsx")
    print(execl_list)
    # sheet_list = execl_read.read_execl(execl_list)
    wb = load_workbook(execl_list[0])
    wb_sheet = wb.sheetnames
    print(wb_sheet)
    book_name_list = execl_read.find_book_name(book_path)
    print(book_name_list)

    for i in range(len(execl_list)):
        execl_element = execl_list[i]
        print(execl_element)
        print(i)
        book_list = execl_read.find_book_name(book_path)
        book_name = book_list[i]
        execl_read.read_execl(execl_element, 1)
    '''

    # 思维导图测试
    '''
    book_path = '../../data/test_data'
    execl_list = excel_find.find_execl(book_path, "*.xlsx")
    # print(execl_list)
    wb = load_workbook(execl_list[0])
    wb_sheet = wb.sheetnames
    # print(wb_sheet)
    book_name_list = execl_read.find_book_name(book_path)
    # print(book_name_list)
    # ws = wb[wb_sheet[7]]
    # print(ws['B1'].value)
    for i in range(len(execl_list)):
        execl_element = execl_list[i]
        # print(execl_element)
        book_list = execl_read.find_book_name(book_path)
        book_name = book_list[i]
        execl_read.read_execl(execl_element, 7, book_name)
    '''

    # 好词好句测试
    '''
    book_path = excel_find.input_path()
    execl_list = excel_find.find_execl(book_path, "*.xlsx")
    print(execl_list)
    book_name_list = execl_read.find_book_name(book_path)
    print(book_name_list)
    collection_name = {'collection_name': 'word_sentence'}
    db_conn.add_collection(access_token, collection_name)

    for i in range(len(execl_list)):
        execl_element = execl_list[i]
        print(execl_element)
        print(i)
        book_list = execl_read.find_book_name(book_path)
        book_name = book_list[i]
        execl_read.read_execl(execl_element, 5, book_name)

    for i in range(len(execl_list)):
        execl_element = execl_list[i]
        print(execl_element)
        print(i)
        book_list = execl_read.find_book_name(book_path)
        book_name = book_list[i]
        execl_read.read_execl(execl_element, 6, book_name)
    '''
    print(access_token)
