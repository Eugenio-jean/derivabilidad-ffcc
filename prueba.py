# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 11:24:36 2020

@author: Jeann
"""

import xlrd
file_loc="Matrices/Book1.xlsx"
wkb=xlrd.open_workbook(file_loc)
sheet=wkb.sheet_by_index(1)

m=[]
for row in range (sheet.nrows):
    _row = []
    for col in range (sheet.ncols):
        _row.append(sheet.cell_value(row,col))
    m.append(_row)
