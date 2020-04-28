import os
from glob import glob

BASE_DIR = "../../data/题库"


class excel_find:

    # 返回目录下的所有子目录
    @staticmethod
    def find_dirs(file_dir):
        for root, dirs, files in os.walk(file_dir):
            return dirs

    # 返回目录下的所有execl列表(包括子目录)
    @staticmethod
    def find_execl(root_path="", pattern=""):
        root_path = os.path.abspath(root_path)
        results = []
        for root, dirs, files in os.walk(root_path):
            for match in glob(os.path.join(root, pattern)):
                if '$' in match:
                    continue
                else:
                    results.append(match)
        return results

    # 返回目录下的execl列表
    def all_execl(self):
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
