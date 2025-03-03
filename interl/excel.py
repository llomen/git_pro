"""
肖子淅
日期：2024年08月12日
该文件用来处理各个excel
"""
from openpyxl import load_workbook
import pandas as pd


def bsd_video_excel():
    #重新排序波塞冬video数据excel
    df = pd.read_excel('data_bsd_video.xlsx')
    new_order = ['video_id','video_name','is_pay','charge_type','asset_source','category_id','mpp_status','mpp_release_time']
    df = df.reindex(columns=new_order)
    colums_to_copy = ['video_id','video_name','is_pay','charge_type','asset_source','category_id','mpp_status','mpp_release_time']
    df_copid = df[colums_to_copy]
    df_copid.to_excel('data_bsd_video_neworder.xlsx',index=False)

