# coding: utf-8

from pyautocad import Autocad, APoint, aDouble
from openpyxl import *
import re, os, shutil, getpass, math, time
from dxfwrite import DXFEngine as dxf


def Is_Number(str_number):
    '''
    :str: the str need to check
    '''
    if ((str_number.split(".")[0]).isdigit() or 
         str_number.isdigit() or
         (str_number.split('-')[-1]).split(".")[-1].isdigit()):
        return True
    else:
        return False

def Create_ActiveLayout_Polyline(excel_name_path, column_x, column_y):
    '''
    excel_name: excel files including verticeslist of polyline
    '''
    acad = Autocad(create_if_not_exists = True)
    column_x_num = int(column_x)
    column_y_num = int(column_y)
    points = []
    try:
        wb = load_workbook(excel_name_path)
        ws = wb.active
        for row in ws.rows:
            if (Is_Number(str(row[column_x_num-1].value)) == True and
                Is_Number(str(row[column_y_num-1].value)) == True):
                print(row[column_x_num - 1].value, row[column_y_num - 1].value)
                column_x_cood = float(row[column_x_num-1].value)
                column_y_cood = float(row[column_y_num-1].value)
                points.append(APoint(column_x_cood, column_y_cood))
        points_middle = [j for i in points for j in i]
        points_final = aDouble(points_middle)
        plineObj = acad.ActiveDocument.ActiveLayout.Block.AddPolyline(points_final)
        clr = acad.Application.GetInterfaceObject("AutoCAD.AcCmColor.%s" % acad.Application.Version.split(".")[0])  # get current cad version
        clr.SetRGB(255, 0, 0) # create red polyline
        plineObj.TrueColor = clr # define the polyline's color
        [plineObj.SetWidth(segmentindex, 2, 2) for segmentindex in  range(ws.max_row-1)]
        acad.ActiveDocument.Application.ZoomExtents()
        acad.ActiveDocument.Regen(True)  # regenate active drawings or use "acad.ActiveDocument.Application.Update()"
    except Exception:
        print("写入失败, 请查看CAD版本或写入格式!")
        
excel_files_path = input("请输入Excel坐标表坐在文件夹绝对路径: ")
column_x = int(input("请输入横坐标坐在列号: "))
column_y = int(input("请输入纵坐标坐在列号: "))
for root, dirs, files in os.walk(excel_files_path):
    for filename in files:
        if ".xlsx" in filename:
            excel_name_path = root + "/" + filename
            Create_ActiveLayout_Polyline(excel_name_path, column_x, column_y)
            time.sleep(3)