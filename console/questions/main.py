from console.db_handle import db_handle
from console.questions.switch import *
from console.excel_find import excel_find, BASE_DIR
from console.execl_read import execl_read

if __name__ == "__main__":
    dirs_list = excel_find.find_dirs(BASE_DIR)
    print(dirs_list)
    execl_list = excel_find.find_execl(BASE_DIR, "*.xlsx")
    print(execl_list)

    # 新增集合
    collection_name = {'collection_name': 'Item_bank'}
    db_conn.add_collection(access_token, collection_name)

    '''
        插入数据
        execl_list:所有execl列表
        execl_element:execl节点(单个execl)
        book_list:书名列表
    '''
    # 单选题
    for i in range(len(execl_list)):
        execl_element = execl_list[i]
        print(execl_element)
        print(i)
        book_list = execl_read.read_book_name()
        book_name = book_list[i]
        execl_read.read_execl(execl_element, 1, book_name)

    # 多选题
    for i in range(len(execl_list)):
        execl_element = execl_list[i]
        print(execl_element)
        print(i)
        book_list = execl_read.read_book_name()
        book_name = book_list[i]
        execl_read.read_execl(execl_element, 2, book_name)

    # 是非题
    for i in range(len(execl_list)):
        execl_element = execl_list[i]
        print(execl_element)
        print(i)
        book_list = execl_read.read_book_name()
        book_name = book_list[i]
        execl_read.read_execl(execl_element, 3, book_name)
