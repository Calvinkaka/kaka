from console.db_handle import db_handle
from console.questions.switch import *
from console.excel_find import excel_find
from console.execl_read import execl_read

if __name__ == "__main__":
    book_path = excel_find.input_path()
    execl_list = excel_find.find_execl(book_path, "*.xlsx")
    print(execl_list)
    book_name_list = execl_read.find_book_name(book_path)
    print(book_name_list)
    '''
        插入数据
        execl_list:所有execl列表
        execl_element:execl节点(单个execl)
        book_list:书名列表
    '''

    '''
    # 新增集合
    collection_name = {'collection_name': 'Item_bank'}
    db_conn.add_collection(access_token, collection_name)

    # 单选题
    for i in range(len(execl_list)):
        execl_element = execl_list[i]
        print(execl_element)
        print(i)
        book_list = execl_read.find_book_name(book_path)
        book_name = book_list[i]
        execl_read.read_execl(execl_element, 2, book_name)

    # 多选题
    for i in range(len(execl_list)):
        execl_element = execl_list[i]
        print(execl_element)
        print(i)
        book_list = execl_read.find_book_name(book_path)
        book_name = book_list[i]
        execl_read.read_execl(execl_element, 3, book_name)

    # 是非题
    for i in range(len(execl_list)):
        execl_element = execl_list[i]
        print(execl_element)
        print(i)
        book_list = execl_read.find_book_name(book_path)
        book_name = book_list[i]
        execl_read.read_execl(execl_element, 4, book_name)
    '''

    # 读前读后思考
    '''
    # 新增集合
    collection_name = {'collection_name': 'read_think'}
    db_conn.add_collection(access_token, collection_name)
    '''
    '''
    for i in range(len(execl_list)):
        execl_element = execl_list[i]
        print(execl_element)
        print(i)
        book_list = execl_read.find_book_name(book_path)
        book_name = book_list[i]
        execl_read.read_execl(execl_element, 1, book_name)

    for i in range(len(execl_list)):
        execl_element = execl_list[i]
        print(execl_element)
        print(i)
        book_list = execl_read.find_book_name(book_path)
        book_name = book_list[i]
        execl_read.read_execl(execl_element, 8, book_name)
    '''
    # 思维导图
    '''
    # 新增集合
    collection_name = {'collection_name': 'mind_map'}
    db_conn.add_collection(access_token, collection_name)

    for i in range(len(execl_list)):
        execl_element = execl_list[i]
        print(execl_element)
        print(i)
        book_list = execl_read.find_book_name(book_path)
        book_name = book_list[i]
        execl_read.read_execl(execl_element, 7, book_name)
    '''
    # 好词好句
    # 新增集合
    collection_name = {'collection_name': 'word_sentence'}
    db_conn.add_collection(access_token, collection_name)

    # for i in range(len(execl_list)):
    #     execl_element = execl_list[i]
    #     print(execl_element)
    #     print(i)
    #     book_list = execl_read.find_book_name(book_path)
    #     book_name = book_list[i]
    #     execl_read.read_execl(execl_element, 5, book_name)

    for i in range(len(execl_list)):
        execl_element = execl_list[i]
        print(execl_element)
        print(i)
        book_list = execl_read.find_book_name(book_path)
        book_name = book_list[i]
        execl_read.read_execl(execl_element, 6, book_name)
