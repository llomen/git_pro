import xlsxwriter
from collections import Counter
from openpyxl import load_workbook
import pandas as pd

data = pd.DataFrame(pd.read_excel('123.xlsx', 'sheet2'))
no_re_row = data.drop_duplicates(subset='流量词')
no_re_row.to_excel('111.xlsx','sheet1')



