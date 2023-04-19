# coding:utf-8
import matplotlib
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from collections import Counter
import xlsxwriter
import matplotlib.font_manager as fm
# mpl.rcParams['font.sans-serif'] = ['Microsoft YaHei'] # 指定默认字体：解决plot不能显示中文问题
# mpl.rcParams['axes.unicode_minus'] = False
# cn_font = fm.FontProperties(fname='/System/Library/Fonts/PingFang.ttc')
#
#
# workbook = xlsxwriter.Workbook('new.xlsx')
# worksheet = workbook.add_worksheet()
# data = pd.read_excel('data.xlsx')
# dt = data['解决结果'].values
# result = dict(Counter(dt))
# dt1 = list(result.keys())
# dt2 = list(result.values())
# headings = ['status', 'number']
# worksheet.write_row('A1', headings)
# worksheet.write_column('A2',dt1)
# worksheet.write_column('B2',dt2)
# workbook.close()
# bg = pd.read_excel('new.xlsx', index_col='status')
# bg['number'].plot.pie(startangle = 90)
# plt.title('status of bugs', fontsize = 24)
# plt.tight_layout()
# plt.show()
for i in range(1,2):
    print(i)


