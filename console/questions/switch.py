import datetime
from console.db_handle import db_handle

db_conn = db_handle()
db_conn.GRANT_TYPE = 'client_credential'
db_conn.APP_ID = 'wxb29c6899ac367ef3'
db_conn.APP_SECRET = '931410b85b44f1f287ea144d569f4f59'
access_token = db_conn.get_access_token()


def case0(ws):
    # 读取数据
    introduce = ws['A1'].value
    # 处理数据中的换行和空格
    introduce = introduce.replace(' ', '')
    introduce = introduce.replace('\r', '').replace('\n', '')
    print(introduce)

    # 新增集合
    # collection_name = {'collection_name': 'introduction'}
    # db_conn.add_collection(access_token, collection_name)

    # 新增数据
    data = 'db.collection(\"introduction\").add({data: [{introduce: "%s"}]})' % introduce
    db_conn.add_data(access_token, data)
    # print(access_token)


# 单选题
def case1(ws, book_name):
    rows = read_all_rows(ws)
    # 获取数据

    if rows is not None:
        for x in range(0, len(rows), 3):
            question = rows[x][0].value
            right_key = rows[x][4].value
            if right_key == 'A':
                right_key = 'option_a'
            elif right_key == 'B':
                right_key = 'option_b'
            elif right_key == 'C':
                right_key = 'option_c'
            elif right_key == 'D':
                right_key = 'option_d'
            option_a = rows[x + 1][0].value
            option_b = rows[x + 1][1].value
            option_c = rows[x + 1][2].value
            option_d = rows[x + 1][3].value
            is_delete = 0

            # 新增集合
            # collection_name = {'collection_name': 'Item_bank'}
            # db_conn.add_collection(access_token, collection_name)

            # 组织数据
            localtime = datetime.datetime.now()
            question_type = 0
            data = 'db.collection(\"Item_bank\").add({data: [{book_name: "%s", question: "%s", ' \
                   'right_key: "%s", option_a: "%s", option_b: "%s", option_c: "%s", option_d: "%s", ' \
                   'is_delete: "%d", question_type: "%d", localtime: "%s"}]})' % (
                       book_name, question, right_key, option_a,
                       option_b, option_c, option_d, is_delete,
                       question_type, localtime)

            # 存储数据
            db_conn.add_data(access_token, data)
            # print(question, right_key)
            # print(option_a, option_b, option_c, option_d, )


def case2(ws, book_name):
    rows = read_all_rows(ws)
    # 获取数据

    if rows is not None:
        for x in range(0, len(rows), 3):
            question = rows[x][0].value
            right_key = rows[x][4].value
            right_key = right_key.replace('A', 'option_a,')
            right_key = right_key.replace('B', 'option_b,')
            right_key = right_key.replace('C', 'option_c,')
            right_key = right_key.replace('D', 'option_d')
            option_a = rows[x + 1][0].value
            option_b = rows[x + 1][1].value
            option_c = rows[x + 1][2].value
            option_d = rows[x + 1][3].value
            is_delete = 0

            # 新增集合
            # collection_name = {'collection_name': 'Item_bank'}
            # db_conn.add_collection(access_token, collection_name)

            # 组织数据
            localtime = datetime.datetime.now()
            question_type = 1
            data = 'db.collection(\"Item_bank\").add({data: [{book_name: "%s", question: "%s", ' \
                   'right_key: "%s", option_a: "%s", option_b: "%s", option_c: "%s", option_d: "%s", ' \
                   'is_delete: "%d", question_type: "%d", localtime: "%s"}]})' % (
                       book_name, question, right_key, option_a,
                       option_b, option_c, option_d, is_delete,
                       question_type, localtime)

            # 存储数据
            db_conn.add_data(access_token, data)


def case3(ws, book_name):
    rows = read_all_rows(ws)
    # 获取数据

    if rows is not None:
        for x in range(0, len(rows), 3):
            question = rows[x][0].value
            right_key = rows[x][3].value
            if right_key == '是':
                right_key = 'option_a'
            else:
                right_key = 'option_b'
            option_a = rows[x + 1][0].value
            option_b = rows[x + 1][1].value
            is_delete = 0

            # 新增集合
            # collection_name = {'collection_name': 'Item_bank'}
            # db_conn.add_collection(access_token, collection_name)

            # 组织数据
            localtime = datetime.datetime.now()
            question_type = 2
            data = 'db.collection(\"Item_bank\").add({data: [{book_name: "%s", question: "%s", ' \
                   'right_key: "%s", option_a: "%s", option_b: "%s", ' \
                   'is_delete: "%d", question_type: "%d", localtime: "%s"}]})' % (
                       book_name, question, right_key, option_a,
                       option_b, is_delete, question_type, localtime)

            # 存储数据
            db_conn.add_data(access_token, data)


def case4(ws):
    # print(ws['A'])
    if ws["A1"].value:
        for cell in ws["A"]:
            print(cell.value)


def case5(ws):
    if ws["A1"].value:
        for cell in ws["A"]:
            print(cell.value)


def case6(ws):
    read_all_rows(ws)


# 读取当前页的所有内容
def read_all_rows(ws):
    rows = []
    for row in ws.iter_rows():
        rows.append(row)
    return rows


switch = {0: case0,
          1: case1,
          2: case2,
          3: case3,
          4: case4,
          5: case5,
          6: case6}
