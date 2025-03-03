"""
肖子淅
日期：2024年07月24日
从数据库获取video和clip数据的方法
从波塞冬接口获取video和clip数据的方法
"""
import operator
from connect_db import MysqlUtil
from interface_data import Myrq
import pymysql
from pymysql.cursors import DictCursor
import pandas as pd
import json
import numpy as np



# sql_vrs_clip = 'SELECT DISTINCT clip_id,clip_name,is_pay,charge_type,asset_source,is_independent,category_id,serial_count,mpp_status,mpp_release_time FROM vrs_clip'
# url_vrs_clip = ''
# data_vrs_clip = MysqlUtil().fetchone(sql_vrs_clip)
# df = pd.DataFrame(data_vrs_clip)
# df.to_excel('data_vrs_clip.xlsx', index=False)
# sql_vrs_video = 'SELECT DISTINCT video_id,video_name,is_pay,charge_type,asset_source,category_id,mpp_status,mpp_release_time FROM vrs_video'
# data_vrs_video = MysqlUtil().fetchone(sql_vrs_video)
# df = pd.DataFrame(data_vrs_video)
# df.to_excel('data_vrs_video.xlsx', index=False)

# video_id = '2992014'
# url_vrs_video = "http://10.200.19.60:8501/api/v1/parts/multi/"+ video_id +"?invokes=ito-admin&type=12&returnFields=all"
# dt = Myrq().get(url_vrs_video)['data']
# vipInfoMpp = list(map(operator.itemgetter('vipInfoMpp'),dt))[0]
# mark_number = json.loads(vipInfoMpp).get("mark")#处理接口返回的vipinfoMpp字段中mark对应的json
# charge_type_number =  json.loads(vipInfoMpp).get("charge_type")
# if mark_number != None and charge_type_number != None:
#     #data_video输出list ['partId','partName','assetSource','fstlvlId','mppstatus','releaseTime','mark_number','charge_type_number']
#     #mark_number、charge_type_number可能为空的情况，此时列表补0处理
#     data_video = np.array(
#         list(map(operator.itemgetter('partId','partName','assetSource','fstlvlId','mppstatus','releaseTime'),
#                  dt)))
#     data_video = np.append(data_video, [mark_number, charge_type_number])
# elif mark_number != None and charge_type_number == None:
#     data_video = np.array(
#         list(map(operator.itemgetter('partId', 'partName', 'assetSource', 'fstlvlId', 'mppstatus', 'releaseTime'),
#             dt))[0])
#     data_video = np.append(data_video, [mark_number, '0']) #charge_type_number为空，所以补0处理
# elif mark_number == None and charge_type_number != None:
#     data_video = np.array(
#         list(map(operator.itemgetter('partId', 'partName', 'assetSource', 'fstlvlId', 'mppstatus', 'releaseTime'),
#             dt))[0])
#     data_video = np.append(data_video,['0', charge_type_number])#mark_number为空，补0处理
# else:
#     data_video = np.array(
#         list(map(operator.itemgetter('partId', 'partName', 'assetSource', 'fstlvlId', 'mppstatus', 'releaseTime'),
#             dt))[0])
#     data_video = np.append(data_video, ['0', '0'])

def getdb_data():
    """从数据库获取video和clip数据，并写入excel"""
    sql_vrs_clip = 'SELECT DISTINCT clip_id,clip_name,is_pay,charge_type,asset_source,is_independent,category_id,serial_count,mpp_status,mpp_release_time FROM vrs_clip'
    data_vrs_clip = MysqlUtil().fetchone(sql_vrs_clip)
    df = pd.DataFrame(data_vrs_clip)
    df.to_excel('data_vrs_clip.xlsx', index=False)
    sql_vrs_video = 'SELECT DISTINCT video_id,video_name,is_pay,charge_type,asset_source,category_id,mpp_status,mpp_release_time FROM vrs_video'
    data_vrs_video = MysqlUtil().fetchone(sql_vrs_video)
    df = pd.DataFrame(data_vrs_video)
    df.to_excel('data_vrs_video.xlsx', index=False)


def getbds_video_data(video_id):
    """从波塞冬接口获取video媒资数据"""
    url_vrs_video = "http://10.200.19.60:8501/api/v1/parts/multi/" + video_id + "?invokes=ito-admin&type=12&returnFields=all"
    try:
        dt = Myrq().get(url_vrs_video)['data']
        if dt[0].get("vipInfoMpp") != None:                               #如果接口返回data中有vipInfoMpp字段
            vipInfoMpp = list(map(operator.itemgetter('vipInfoMpp'), dt))[0]
            mark_number = json.loads(vipInfoMpp).get("mark")  # 处理接口返回的vipinfoMpp字段中mark对应的json
            charge_type_number = json.loads(vipInfoMpp).get("charge_type")
            if mark_number != None and charge_type_number != None:
                # data_video输出list ['partId','partName','assetSource','fstlvlId','mppstatus','releaseTime','mark_number','charge_type_number']
                # mark_number、charge_type_number可能为空的情况，此时列表补0处理
                data_video = np.array(
                    list(map(operator.itemgetter('partId', 'partName', 'assetSource', 'fstlvlId', 'mppstatus',
                                                 'releaseTime'),
                             dt)))
                data_video = np.append(data_video, [mark_number, charge_type_number])
                return data_video
            elif mark_number != None and charge_type_number == None:
                data_video = np.array(
                    list(map(operator.itemgetter('partId', 'partName', 'assetSource', 'fstlvlId', 'mppstatus',
                                                 'releaseTime'),
                             dt))[0])
                data_video = np.append(data_video, [mark_number, '0'])  # charge_type_number为空，所以补0处理
                return data_video
            elif mark_number == None and charge_type_number != None:
                data_video = np.array(
                    list(map(operator.itemgetter('partId', 'partName', 'assetSource', 'fstlvlId', 'mppstatus',
                                                 'releaseTime'),
                             dt))[0])
                data_video = np.append(data_video, ['0', charge_type_number])  # mark_number为空，补0处理
                return data_video
            else:
                data_video = np.array(
                    list(map(operator.itemgetter('partId', 'partName', 'assetSource', 'fstlvlId', 'mppstatus',
                                                 'releaseTime'),
                             dt))[0])
                data_video = np.append(data_video, ['0', '0'])
                return data_video
        else:
            data_video = np.array(
                list(map(operator.itemgetter('partId', 'partName', 'assetSource', 'fstlvlId', 'mppstatus',
                                             'releaseTime'),
                         dt))[0])
            data_video = np.append(data_video, ['0', '0'])
            return data_video
    except IndexError:
        print(f"媒资{video_id}返回值异常")




    #vipInfoMpp = list(map(operator.itemgetter('vipInfoMpp'), dt))[0]
    # mark_number = json.loads(vipInfoMpp).get("mark")  # 处理接口返回的vipinfoMpp字段中mark对应的json
    # charge_type_number = json.loads(vipInfoMpp).get("charge_type")
    # if mark_number != None and charge_type_number != None:
    #     # data_video输出list ['partId','partName','assetSource','fstlvlId','mppstatus','releaseTime','mark_number','charge_type_number']
    #     # mark_number、charge_type_number可能为空的情况，此时列表补0处理
    #     data_video = np.array(
    #         list(map(operator.itemgetter('partId', 'partName', 'assetSource', 'fstlvlId', 'mppstatus', 'releaseTime'),
    #                  dt)))
    #     data_video = np.append(data_video, [mark_number, charge_type_number])
    #     return data_video
    # elif mark_number != None and charge_type_number == None:
    #     data_video = np.array(
    #         list(map(operator.itemgetter('partId', 'partName', 'assetSource', 'fstlvlId', 'mppstatus', 'releaseTime'),
    #                  dt))[0])
    #     data_video = np.append(data_video, [mark_number, '0'])  # charge_type_number为空，所以补0处理
    #     return data_video
    # elif mark_number == None and charge_type_number != None:
    #     data_video = np.array(
    #         list(map(operator.itemgetter('partId', 'partName', 'assetSource', 'fstlvlId', 'mppstatus', 'releaseTime'),
    #                  dt))[0])
    #     data_video = np.append(data_video, ['0', charge_type_number])  # mark_number为空，补0处理
    #     return data_video
    # else:
    #     data_video = np.array(
    #         list(map(operator.itemgetter('partId', 'partName', 'assetSource', 'fstlvlId', 'mppstatus', 'releaseTime'),
    #                  dt))[0])
    #     data_video = np.append(data_video, ['0', '0'])
    #     return data_video




def getbds_clip_data(clip_id):
    """从波塞冬接口获取clip媒资数据"""
    url_vrs_clip = "http://10.200.19.60:8501//api/v1/clips/" + clip_id + "?invokes=ito-admin&type=12&returnFields=all"
    try:
        dt = Myrq().get(url_vrs_clip)['data']
        if dt.get("vipMarkMpp") != None:
            # 如果接口返回data中有vipInfoMpp字段
            vipMarkMpp = dt['vipMarkMpp']
            mark_number = json.loads(vipMarkMpp).get("mark")  # 处理接口返回的vipinfoMpp字段中mark对应的json
            charge_type_number = json.loads(vipMarkMpp).get("charge_type")
            if mark_number != None and charge_type_number != None:
                # data_clip输出list ['partId','partName','assetSource','fstlvlId','mppstatus','releaseTime','mark_number','charge_type_number']
                # mark_number、charge_type_number可能为空的情况，此时列表补0处理
                data_clip = []
                for key in ['clipId', 'clipName', 'assetSource', 'isIndependent','fstlvlId','serialCount', 'mppstatus', 'releaseTime']:
                    data_clip.append(dt[key])
                data_clip.append(mark_number)
                data_clip.append(charge_type_number)
                return data_clip
            elif mark_number != None and charge_type_number == None:
                # data_clip = dt['clipId', 'clipName', 'assetSource', 'isIndependent','fstlvlId','serialCount', 'mppstatus',
                #                                  'releaseTime']
                data_clip = []
                for key in ['clipId', 'clipName', 'assetSource', 'isIndependent','fstlvlId','serialCount', 'mppstatus', 'releaseTime']:
                    data_clip.append(dt[key])
                data_clip.append(mark_number)  # charge_type_number为空，所以补0处理
                data_clip.append('0')
                return data_clip
            elif mark_number == None and charge_type_number != None:
                data_clip = []
                for key in ['clipId', 'clipName', 'assetSource', 'isIndependent','fstlvlId','serialCount', 'mppstatus', 'releaseTime']:
                    data_clip.append(dt[key])
                data_clip.append('0')  # mark_number，所以补0处理
                data_clip.append(charge_type_number)
                return data_clip
            else:
                data_clip = []
                for key in ['clipId', 'clipName', 'assetSource', 'isIndependent','fstlvlId','serialCount', 'mppstatus', 'releaseTime']:
                    data_clip.append(dt[key])
                data_clip.append('0')  # mark_number和charge_type_number为空，所以补0处理
                data_clip.append('0')
                return data_clip
        else:
            data_clip = []
            for key in ['clipId', 'clipName', 'assetSource', 'isIndependent', 'fstlvlId', 'serialCount', 'mppstatus',
                        'releaseTime']:
                data_clip.append(dt[key])
            data_clip.append('0')  # mark_number和charge_type_number为空，所以补0处理
            data_clip.append('0')
            return data_clip
    except IndexError:
        print(f"合集{clip_id}返回值异常")



