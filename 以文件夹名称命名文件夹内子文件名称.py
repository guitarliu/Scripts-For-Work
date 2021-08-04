# coding: utf-8

import os, re

for root, dirs, files in os.walk("F:/2020-11-7-博罗县石湾镇滘吓村源头村雨污分流管网工程归档文件夹/11施工联系/17份工作联系单回复"):
    for filename in files:
        result = re.search("\d\d\d\d", filename)
        if result:
            print(result.group(), root)
            new_filename = filename.split(result.group())[0] + root.split("\\")[-1] + filename.split(result.group())[-1]
            os.rename(root + "/" + filename, root +"/" + new_filename)