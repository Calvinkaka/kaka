from openpyxl import load_workbook

from console.excel_find import excel_find, BASE_DIR
from console.questions.switch import switch


class execl_read:
    # 读取一个excel的所有内容
    @staticmethod
    def read_execl(file_path, page, book_name):
        # 实例化一个workbook对象
        wb = load_workbook(file_path)
        # 获取一个excel的所有sheet
        wb_sheet = wb.sheetnames
        # 遍历一个excel的所有sheet
        # for page in range(len(wb_sheet)):
        ws = wb[wb_sheet[page]]
        # 这里可以接参数，调用固定的sheet处理函数
        switch[page](ws, book_name)

    # 获取书名
    @staticmethod
    def read_book_name():
        books_list = excel_find.find_dirs(BASE_DIR)
        return books_list

