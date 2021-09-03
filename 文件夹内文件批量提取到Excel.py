# coding: utf-8

import os
from openpyxl import Workbook

wb = Workbook()
ws = wb.active
for root, dirs, files in os.walk("C:\\Users\\administrator\\Desktop\\dirname"):
    for filename in files:
        if "CPS0305" in filename:
            draw_num = filename.split(" ")[0]
            draw_name = filename.split(" ")[1].split(".")[0]
            print(draw_num, draw_name)
            ws.append((draw_num, draw_name))
            
wb.save("c:/users/administrator/desktop/1.xlsx")
