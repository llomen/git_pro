"""
肖子淅
日期：2024年07月30日
"""
from data_get import getbds_video_data, getbds_clip_data
import pandas as pd
from openpyxl import Workbook
import numpy as np

#video相关数据处理
def bsd_video():
    df = pd.read_excel('data_vrs_video.xlsx')
    column_name = 'video_id'
    select_columns = df[column_name]
    data_list = []
    for i in range(0, len(select_columns)):
        video_id = str(select_columns[i])
        try:
            df_bsd_video = getbds_video_data(video_id).tolist()
            data_list.append(df_bsd_video)
        except AttributeError:
            pass
    df_data_list = pd.DataFrame(data_list)
    df_data_list.columns = ['video_id', 'video_name', 'asset_source', 'category_id', 'mpp_status', 'mpp_release_time','is_pay', 'charge_type']
    #bsd接口中应'partId','partName','assetSource','fstlvlId','mppstatus','releaseTime','vipMarkMpp.mark','vipMarkMpp.charge_type'，按照映射关系，改成下行名称
    #'video_id', 'video_name', 'asset_source', 'category_id', 'mpp_status', 'mpp_release_time','is_pay', 'charge_type'
    df_data_list.to_excel('data_bsd_video.xlsx', index=False)

#clip相关数据处理
def bsd_clip():
    df_clip = pd.read_excel('data_vrs_clip.xlsx')
    column_name = 'clip_id'
    select_columns = df_clip[column_name]
    data_clip_list = []
    for i in range(0, len(select_columns)):
        clip_id = str(select_columns[i])
        try:
            print(getbds_clip_data(clip_id))
            #df_bsd_clip = getbds_clip_data(clip_id).tolist()
            df_bsd_clip = getbds_clip_data(clip_id)
            data_clip_list.append(df_bsd_clip)
        except AttributeError:
            pass
    df_clip_data_list = pd.DataFrame(data_clip_list)
    df_clip_data_list.columns = ['clipId', 'clipName', 'assetSource', 'isIndependent', 'fstlvlId', 'serialCount', 'mppstatus', 'releaseTime','vipMarkMpp.mark', 'vipMarkMpp.charge_type']
    df_clip_data_list.to_excel('data_bsd_clip.xlsx', index=False)

