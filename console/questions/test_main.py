import time

from console.db_handle import db_handle
import datetime

# print("请输入题库路径：")
# BASE_DIR = input()
# print(BASE_DIR)
if __name__ == "__main__":
    db_conn = db_handle()
    db_conn.GRANT_TYPE = 'client_credential'
    db_conn.APP_ID = 'wxb29c6899ac367ef3'
    db_conn.APP_SECRET = '931410b85b44f1f287ea144d569f4f59'
    access_token = db_conn.get_access_token()

    '''
    # db_conn.add_collection(access_token)
    introduce =       动物绝对不该穿衣服！为什么？因为山羊会把衣服当午餐吃掉，蛇会穿不进去裤子，绵羊穿上衣服会感觉很热，小负鼠一不小心就会把衣服穿反…...

    这是一本让人忍俊不禁的图画书，教会孩子发现动物的美，天生的美。
    introduce = introduce.replace(' ', '')
    introduce = introduce.replace('\r', '').replace('\n', '')
    print(introduce)
    data = 'db.collection(\"introduction\").add({data: [{introduce: "%s"}]})' % introduce
    '''

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
    # db_conn.query_data(access_token)
    # db_conn.delete_data(access_token, '87017e375ea4fe390033dd7f6fda8221')
    print(access_token)
