"""
肖子淅
日期：2024年08月08日
数据库数据和波塞冬数据对比
"""
import pandas as pd
from data_get import getdb_data
from bsd_interface_data import bsd_clip,bsd_video
from excel import bsd_video_excel

getdb_data()
bsd_video()
#bsd_clip()
bsd_video_excel()


df1 = pd.read_excel('data_vrs_video.xlsx')
df2 = pd.read_excel('data_bsd_video_neworder.xlsx')
diff = pd.concat([df1,df2]).drop_duplicates(keep=False)
diff.to_excel('diff_video.xlsx', index=False)

if __name__== '__main__':
    bsd_clip()