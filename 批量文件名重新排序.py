# coding: utf-8

import os, re

file_path = input("请输入文件绝对路径: ")

for root, dir, files in os.walk(file_path):
    for filename in files:
        if ".dwg" in filename and re.match("^CPS", filename):
            filename_num = filename.split(" ")[0]
            filename_new_num = int(filename_num.split("-")[-1]) + 18
            if filename_new_num < 10:
                filename_new = filename_num.split("-")[0] + "-00" + str(filename_new_num) + " " + filename.split(" ")[-1]
            elif 10 <= filename_new_num < 100:
                filename_new = filename_num.split("-")[0] + "-0" + str(filename_new_num) + " " + filename.split(" ")[-1]
            os.rename(root + "/" + filename, root + "/" + filename_new)