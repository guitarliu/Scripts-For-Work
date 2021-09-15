# coding: utf-8

import os

def get_source_num(draw_num):
    if int(draw_num) < 10:
        source_num = "施-排0" + draw_num
    else:
        source_num = "施-排" + draw_num
    return source_num

def get_dest_num(destination_num):
    if int(destination_num.split('-')[-1]) < 9:
        result = destination_num.split('-')[0] + "-00" + str(int(destination_num.split('-')[-1]) + 1)
    elif 9 <= int(destination_num.split('-')[-1]) < 100:
        result = destination_num.split('-')[0] + "-0" + str(int(destination_num.split('-')[-1]) + 1)
    else:
        result = destination_num.split('-')[0] + "-" + str(int(destination_num.split('-')[-1]) + 1)
    return result
                

draw_num = input("Please input source num: ")
destination_num = input("Please input destination num: ")
path = input("Please input file-path: ")
for root, dir, files in os.walk(path):
    for filename in files:
        source_num = get_source_num(draw_num=draw_num)
        if  source_num in filename:
            os.rename(root + "/" + filename, root + "/" + destination_num + filename.split(source_num)[1])
            draw_num = str(int(draw_num) + 1)
            destination_num = get_dest_num(destination_num=destination_num)

 
