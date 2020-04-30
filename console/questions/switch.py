import datetime
from console.db_handle import db_handle

db_conn = db_handle()
db_conn.GRANT_TYPE = 'client_credential'
db_conn.APP_ID = 'wxb29c6899ac367ef3'
db_conn.APP_SECRET = '931410b85b44f1f287ea144d569f4f59'
access_token = db_conn.get_access_token()


# 导读
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


# 读前思考
def case1(ws, book_name):
    if ws["A1"].value:
        for cell in ws["A"]:

            localtime = datetime.datetime.now()
            is_delete = '0'
            question_type = '0'
            question = cell.value

            # 查询数据是否已存在
            data = '''db.collection(\"read_think\").where({book_name:'%s',question:'%s'}).get()''' % (
                book_name, question)
            is_data = db_conn.query_data(access_token, data)
            # print(is_data)

            if is_data:
                # 校验数据是否有修改
                query_return = db_conn.query_result_handle(is_data)
                # print(query_return)
                original = db_conn.question_read_before(query_return)
                query_result = [is_delete, question_type]
                # print(original)
                # print(query_result)
                if original == query_result:
                    print('数据无修改')
                    continue
                else:
                    data = 'db.collection(\"read_think\").where({book_name:"%s", question:"%s"}).update({' \
                           'data:{is_delete: "%s", question_type: "%s", update_time: "%s"}})' % (
                               book_name, question, is_delete, question_type, localtime)
                    # 修改数据
                    db_conn.modify_data(access_token, data)
            else:
                # 组织数据
                data = 'db.collection(\"read_think\").add({data: [{book_name: "%s", question: "%s", ' \
                       'is_delete: "%s", question_type: "%s", create_time: "%s", update_time: "%s"}]})' % (
                           book_name, question, is_delete, question_type, localtime, localtime)

                # 存储数据
                db_conn.add_data(access_token, data)
                # print(question, right_key)
                # print(option_a, option_b, option_c, option_d, )

            # print(cell.value)


# 单选题
def case2(ws, book_name):
    rows = read_all_rows(ws)
    # 获取数据
    if rows is not None:
        for x in range(0, len(rows), 3):
            question = rows[x][0].value
            question = question.replace(',', '，')
            right_key = rows[x][4].value
            if right_key == 'A':
                right_key = 'option_a'
            elif right_key == 'B':
                right_key = 'option_b'
            elif right_key == 'C':
                right_key = 'option_c'
            elif right_key == 'D':
                right_key = 'option_d'
            option_a = str(rows[x + 1][0].value)
            option_a = option_a.replace(',', '，')
            option_b = str(rows[x + 1][1].value)
            option_b = option_b.replace(',', '，')
            option_c = str(rows[x + 1][2].value)
            option_c = option_c.replace(',', '，')
            option_d = str(rows[x + 1][3].value)
            option_d = option_d.replace(',', '，')
            is_delete = '0'
            localtime = datetime.datetime.now()
            question_type = '0'
            # 新增集合
            # collection_name = {'collection_name': 'Item_bank'}
            # db_conn.add_collection(access_token, collection_name)

            # 查询数据是否已存在
            data = '''db.collection(\"Item_bank\").where({book_name:'%s',question:'%s'}).get()''' % (
                book_name, question)
            is_data = db_conn.query_data(access_token, data)
            # print(is_data)

            if is_data:
                # 校验数据是否有修改
                query_return = db_conn.query_result_handle(is_data)
                # print(query_return)
                original = db_conn.question_Single(query_return)
                query_result = [is_delete, option_a, option_b, option_c, option_d, question_type, right_key]
                # print(original)
                # print(query_result)
                if original == query_result:
                    print('数据无修改')
                    continue
                else:
                    data = 'db.collection(\"Item_bank\").where({book_name:"%s", question:"%s"}).update({' \
                           'data:{right_key:"%s", option_a: "%s", option_b: "%s", option_c: "%s", option_d: "%s",' \
                           'is_delete: "%s", question_type: "%s", update_time: "%s"}})' % (
                               book_name, question, right_key, option_a,
                               option_b, option_c, option_d, is_delete,
                               question_type, localtime)
                    # 修改数据
                    db_conn.modify_data(access_token, data)
            else:
                # 组织数据
                data = 'db.collection(\"Item_bank\").add({data: [{book_name: "%s", question: "%s", ' \
                       'right_key: "%s", option_a: "%s", option_b: "%s", option_c: "%s", option_d: "%s", ' \
                       'is_delete: "%s", question_type: "%s", create_time: "%s", update_time: "%s"}]})' % (
                           book_name, question, right_key, option_a,
                           option_b, option_c, option_d, is_delete,
                           question_type, localtime, localtime)

                # 存储数据
                db_conn.add_data(access_token, data)
                # print(question, right_key)
                # print(option_a, option_b, option_c, option_d, )


# 多选题
def case3(ws, book_name):
    rows = read_all_rows(ws)
    # 获取数据

    if rows is not None:
        for x in range(0, len(rows), 3):
            question = rows[x][0].value
            right_key = rows[x][4].value
            right_key = right_key.replace('A', 'option_a，')
            right_key = right_key.replace('B', 'option_b，')
            right_key = right_key.replace('C', 'option_c，')
            right_key = right_key.replace('D', 'option_d')
            option_a = rows[x + 1][0].value
            option_b = rows[x + 1][1].value
            option_c = rows[x + 1][2].value
            option_d = rows[x + 1][3].value
            is_delete = '0'
            localtime = datetime.datetime.now()
            question_type = '1'
            # 新增集合
            # collection_name = {'collection_name': 'Item_bank'}
            # db_conn.add_collection(access_token, collection_name)

            # 查询数据是否已存在
            data = '''db.collection(\"Item_bank\").where({book_name:'%s',question:'%s'}).get()''' % (
                book_name, question)
            is_data = db_conn.query_data(access_token, data)

            if is_data:
                # 校验数据是否有修改
                query_return = db_conn.query_result_handle(is_data)
                # print(query_return)
                original = db_conn.question_Single(query_return)
                query_result = [is_delete, option_a, option_b, option_c, option_d, question_type, right_key]
                # print(original)
                # print(query_result)
                if original == query_result:
                    print('数据无修改')
                    continue
                else:
                    data = 'db.collection(\"Item_bank\").where({book_name:"%s", question:"%s"}).update({' \
                           'data:{right_key:"%s", option_a: "%s", option_b: "%s", option_c: "%s", option_d: "%s",' \
                           'is_delete: "%s", question_type: "%s", update_time: "%s"}})' % (
                               book_name, question, right_key, option_a,
                               option_b, option_c, option_d, is_delete,
                               question_type, localtime)
                    # 修改数据
                    db_conn.modify_data(access_token, data)
            else:
                # 组织数据
                data = 'db.collection(\"Item_bank\").add({data: [{book_name: "%s", question: "%s", ' \
                       'right_key: "%s", option_a: "%s", option_b: "%s", option_c: "%s", option_d: "%s", ' \
                       'is_delete: "%s", question_type: "%s", create_time: "%s", update_time: "%s"}]})' % (
                           book_name, question, right_key, option_a,
                           option_b, option_c, option_d, is_delete,
                           question_type, localtime, localtime)

                # 存储数据
                db_conn.add_data(access_token, data)


# 判断题
def case4(ws, book_name):
    rows = read_all_rows(ws)
    # 获取数据

    if rows is not None:
        for x in range(0, len(rows), 3):
            question = rows[x][0].value
            # 处理数据中的换行和空格
            question = question.replace(' ', '')
            question = question.replace('\r', '').replace('\n', '')
            right_key = rows[x][3].value
            # print(right_key)
            if right_key == '是':
                right_key = 'option_a'
            else:
                right_key = 'option_b'
            option_a = rows[x + 1][0].value
            option_b = rows[x + 1][1].value
            is_delete = '0'
            localtime = datetime.datetime.now()
            question_type = '2'

            # 新增集合
            # collection_name = {'collection_name': 'Item_bank'}
            # db_conn.add_collection(access_token, collection_name)

            # 查询数据是否已存在
            data = '''db.collection(\"Item_bank\").where({book_name:'%s',question:'%s'}).get()''' % (
                book_name, question)
            is_data = db_conn.query_data_one(access_token, data)

            if is_data:
                # 校验数据是否有修改
                query_return = db_conn.query_result_handle(is_data)
                original = db_conn.question_judge(query_return)
                query_result = [is_delete, option_a, option_b, question_type, right_key]
                # print(original)
                # print(query_result)
                if original == query_result:
                    print('数据无修改')
                    continue
                else:
                    data = 'db.collection(\"Item_bank\").where({book_name:"%s", question:"%s"}).update({' \
                           'data:{right_key:"%s", option_a: "%s", option_b: "%s",' \
                           'is_delete: "%s", question_type: "%s", update_time: "%s"}})' % (
                               book_name, question, right_key, option_a,
                               option_b, is_delete, question_type, localtime)
                    # 修改数据
                    db_conn.modify_data(access_token, data)
            else:
                # 组织数据
                data = 'db.collection(\"Item_bank\").add({data: [{book_name: "%s", question: "%s", ' \
                       'right_key: "%s", option_a: "%s", option_b: "%s", is_delete: "%s", ' \
                       'question_type: "%s", create_time: "%s", update_time: "%s"}]})' % (
                           book_name, question, right_key, option_a,
                           option_b, is_delete, question_type, localtime, localtime)

                # 存储数据
                db_conn.add_data(access_token, data)


# 好词
def case5(ws, book_name):
    # print(ws['A'])
    if ws["A1"].value:
        for cell in ws["A"]:

            localtime = datetime.datetime.now()
            is_delete = '0'
            ws_type = '0'
            words_sentence = cell.value

            # 查询数据是否已存在
            data = '''db.collection(\"word_sentence\").where({book_name:'%s',words_sentence:'%s'}).get()''' % (
                book_name, words_sentence)
            is_data = db_conn.query_data(access_token, data)
            # print(is_data)

            if is_data:
                # 校验数据是否有修改
                query_return = db_conn.query_result_handle(is_data)
                # print(query_return)
                original = db_conn.words_sentence(query_return)
                query_result = [is_delete, ws_type]
                # print(original)
                # print(query_result)
                if original == query_result:
                    print('数据无修改')
                    continue
                else:
                    data = 'db.collection(\"word_sentence\").where({book_name:"%s", words_sentence:"%s"}).update({' \
                           'data:{is_delete: "%s", ws_type: "%s", update_time: "%s"}})' % (
                               book_name, words_sentence, is_delete, ws_type, localtime)
                    # 修改数据
                    db_conn.modify_data(access_token, data)
            else:
                # 组织数据
                data = 'db.collection(\"word_sentence\").add({data: [{book_name: "%s", words_sentence: "%s", ' \
                       'is_delete: "%s", ws_type: "%s", create_time: "%s", update_time: "%s"}]})' % (
                           book_name, words_sentence, is_delete, ws_type, localtime, localtime)

                # 存储数据
                db_conn.add_data(access_token, data)
            print(cell.value)


# 好句
def case6(ws, book_name):
    if ws["A1"].value:
        for cell in ws["A"]:

            localtime = datetime.datetime.now()
            is_delete = '0'
            ws_type = '0'
            words_sentence = cell.value
            words_sentence = words_sentence.replace(',', '，')
            words_sentence = words_sentence.replace(' ', '')
            words_sentence = words_sentence.replace('\r', '').replace('\n', '')

            # 查询数据是否已存在
            data = '''db.collection(\"word_sentence\").where({book_name:'%s',words_sentence:'%s'}).get()''' % (
                book_name, words_sentence)
            is_data = db_conn.query_data(access_token, data)
            # print(is_data)

            if is_data:
                # 校验数据是否有修改
                query_return = db_conn.query_result_handle(is_data)
                # print(query_return)
                original = db_conn.words_sentence(query_return)
                query_result = [is_delete, ws_type]
                # print(original)
                # print(query_result)
                if original == query_result:
                    print('数据无修改')
                    continue
                else:
                    data = 'db.collection(\"word_sentence\").where({book_name:"%s", words_sentence:"%s"}).update({' \
                           'data:{is_delete: "%s", ws_type: "%s", update_time: "%s"}})' % (
                               book_name, words_sentence, is_delete, ws_type, localtime)
                    # 修改数据
                    db_conn.modify_data(access_token, data)
            else:
                # 组织数据
                data = 'db.collection(\"word_sentence\").add({data: [{book_name: "%s", words_sentence: "%s", ' \
                       'is_delete: "%s", ws_type: "%s", create_time: "%s", update_time: "%s"}]})' % (
                           book_name, words_sentence, is_delete, ws_type, localtime, localtime)

                # 存储数据
                db_conn.add_data(access_token, data)
            print(cell.value)


# 思维导图
def case7(ws, book_name):
    time = ws['B1'].value
    place = ws['B2'].value
    people = ws['B3'].value
    cause = ws['B4'].value
    after = ws['B5'].value
    result = ws['B6'].value

    localtime = datetime.datetime.now()
    is_delete = '0'

    # 查询数据是否已存在
    data = '''db.collection(\"mind_map\").where({book_name:'%s'}).get()''' % book_name
    is_data = db_conn.query_data(access_token, data)
    # print(is_data)

    if is_data:
        # 校验数据是否有修改
        query_return = db_conn.query_result_handle(is_data)
        # print(query_return)
        original = db_conn.mind_think(query_return)
        query_result = [after, cause, is_delete, people, place, result, time, ]
        # print(original)
        # print(query_result)
        if original == query_result:
            print('数据无修改')
        else:
            data = 'db.collection(\"mind_map\").where({book_name:"%s"}).update({data:{is_delete: "%s",' \
                   'update_time: "%s"time: "%s", place: "%s", people: "%s",' \
                   'cause: "%s", after: "%s", result: "%s"}})' % (
                       book_name, is_delete, localtime, time, place, people, cause, after, result)
            # 修改数据
            db_conn.modify_data(access_token, data)
    else:
        # 组织数据
        data = 'db.collection(\"mind_map\").add({data: [{book_name: "%s", is_delete: "%s", ' \
               'create_time: "%s", update_time: "%s", time: "%s", place: "%s", people: "%s", ' \
               'cause: "%s", after: "%s", result: "%s"}]})' % (
                   book_name, is_delete, localtime, localtime, time, place, people, cause, after, result)

        # 存储数据
        db_conn.add_data(access_token, data)


# 读后思考
def case8(ws, book_name):
    if ws["A1"].value:
        for cell in ws["A"]:

            localtime = datetime.datetime.now()
            is_delete = '0'
            question_type = '1'
            question = cell.value

            # 查询数据是否已存在
            data = '''db.collection(\"read_think\").where({book_name:'%s',question:'%s'}).get()''' % (
                book_name, question)
            is_data = db_conn.query_data(access_token, data)
            # print(is_data)

            if is_data:
                # 校验数据是否有修改
                query_return = db_conn.query_result_handle(is_data)
                # print(query_return)
                original = db_conn.question_read_before(query_return)
                query_result = [is_delete, question_type]
                # print(original)
                # print(query_result)
                if original == query_result:
                    print('数据无修改')
                    continue
                else:
                    data = 'db.collection(\"read_think\").where({book_name:"%s", question:"%s"}).update({' \
                           'data:{is_delete: "%s", question_type: "%s", update_time: "%s"}})' % (
                               book_name, question, is_delete, question_type, localtime)
                    # 修改数据
                    db_conn.modify_data(access_token, data)
            else:
                # 组织数据
                data = 'db.collection(\"read_think\").add({data: [{book_name: "%s", question: "%s", ' \
                       'is_delete: "%s", question_type: "%s", create_time: "%s", update_time: "%s"}]})' % (
                           book_name, question, is_delete, question_type, localtime, localtime)

                # 存储数据
                db_conn.add_data(access_token, data)


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
          6: case6,
          7: case7,
          8: case8, }
