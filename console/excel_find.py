import os
from glob import glob


class excel_find:
    def __int__(self, file_path):
        self.file_path = file_path

    # 输入题库路径
    @staticmethod
    def input_path():
        BASE_DIR = "../../data/题库"
        # BASE_DIR = "../../data/new_data"
        print("请输入路径(默认为:{%s})：" % BASE_DIR)
        new_path = input()
        if new_path:
            BASE_DIR = new_path
        return BASE_DIR

    # 返回目录下的所有子目录
    @staticmethod
    def find_dirs(file_dir):
        # file_dir = self.input_path()
        for root, dirs, files in os.walk(file_dir):
            return dirs

    # 返回目录下的所有execl列表(包括子目录)
    @staticmethod
    def find_execl(file_dir, pattern=""):
        # file_dir = self.input_path()
        root_path = os.path.abspath(file_dir)
        results = []
        for root, dirs, files in os.walk(root_path):
            for match in glob(os.path.join(root, pattern)):
                if '$' in match:
                    continue
                else:
                    results.append(match)
        return results

    # 返回目录下的execl列表（暂时弃用）
    def all_execl(self):
        BASE_DIR = self.input_path()
        all_list = []
        dirs_list = self.find_dirs(BASE_DIR)
        for i in range(len(dirs_list)):
            new_dir = BASE_DIR + '/' + (dirs_list[i])
            # print(new_dir)
            execl_list = self.find_execl(new_dir, "*.xlsx")
            # print(execl_list)
            if execl_list:
                all_list += execl_list
        return all_list
