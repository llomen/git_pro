# coding=utf-8
'''
auto.py模块提供后端数据校验，清除临时数据表等方法
'''
import logging,random


def check_result(field,platform,test_point,field_table,act_count):
    '''
    校验结果
    :param field: 要查询的域
    :param platform: 平台类型
    :param test_point: 测试点
    :param field_table: 数据模板表
    :param act_count: 校验条数
    :return: 
    '''
    import urllib
    from urllib.request import urlopen
    from urllib.parse import urlencode
    logging.info('check_result...')
    test_data = {}
    test_data['field']=field
    test_data['platform']=platform
    test_data['test_point']=test_point
    test_data['field_table']=field_table
    test_data['act_count']=act_count

    test_data_urlencode = urllib.parse.urlencode(test_data).encode(encoding='UTF8')
    requrl = "http://10.200.8.114/test"
    req = urllib.request.Request(url = requrl,data =test_data_urlencode)
    res_data = urllib.request.urlopen(req)
    res = res_data.read()
    res=eval(res)
    return(res)

def delete_data(platform):
    '''删除临时表的数据'''
    import urllib
    from urllib.request import urlopen
    from urllib.parse import urlencode

    logging.info('delete_data...')
    test_data = {}
    test_data['platform']=platform
    test_data_urlencode = urllib.parse.urlencode(test_data).encode(encoding='UTF8')
    requrl = "http://10.200.8.114/delete"
    req = urllib.request.Request(url=requrl, data=test_data_urlencode)
    res_data = urllib.request.urlopen(req)
    res = res_data.read()
    return(res)

def update_data(table_name,test_point,up_field,up_value):
    import urllib
    # import urllib2
    from urllib.request import urlopen
    from urllib.parse import urlencode
    test_data = {}
    test_data['table_name']=table_name
    test_data['test_point']=test_point
    test_data['up_field']=up_field
    test_data['up_value']=up_value
    test_data_urlencode = urllib.parse.urlencode(test_data).encode(encoding='UTF8')
    #requrl = "http://10.32.0.134:80/update"
    #requrl = "http://10.4.128.205:80/update"
    requrl = "http://10.200.8.114/update"
    # req = urllib.request.Request(url = requrl,data =test_data_urlencode)
    # res_data = urllib.request.urlopen(req)
    req = urllib.request.Request(url = requrl,data =test_data_urlencode)
    res_data = urllib.request.urlopen(req)
    res = res_data.read()
    return(res)

def delete_cdn():
    import urllib
    from urllib.request import urlopen
    from urllib.parse import urlencode
    test_data = {}
    test_data_urlencode = urllib.parse.urlencode(test_data).encode(encoding='UTF8')
    #requrl = "http://172.31.64.67:80/cdndelete"
    #requrl = "http://10.4.128.205:80/cdndelete"
    requrl = "http://10.200.8.114/cdndelete"
    req = urllib.request.Request(url = requrl,data =test_data_urlencode)
    res_data = urllib.request.urlopen(req)
    logging.info(res_data)
    res = res_data.read()
    return(res)

def request_result(test_point,interface_table,interface_data):
    import urllib
    from urllib.request import urlopen
    from urllib.parse import urlencode
    test_data = {}
    test_data['test_point']=test_point
    test_data['interface_table']=interface_table
    test_data['interface_data']=interface_data
    test_data_urlencode = urllib.parse.urlencode(test_data).encode(encoding='UTF8')
    #requrl = "http://172.31.64.67:80/request"
    #requrl = "http://10.4.128.205:80/test"
    requrl = "http://10.200.8.114/test"
    req = urllib.request.Request(url = requrl,data =test_data_urlencode)
    res_data = urllib.request.urlopen(req)
    res = res_data.read()
    res=eval(res)
    return(res)

def insert_cdn_config(platform):
    import urllib
    from urllib.request import urlopen
    from urllib.parse import urlencode
    test_data={}
    test_data['platform']=platform
    test_data_urlencode = urllib.parse.urlencode(test_data).encode(encoding='UTF8')
    #requrl = "http://172.31.64.67:80/insert"
    requrl = "http://10.4.128.205:80/insert"
    req = urllib.request.Request(url = requrl,data =test_data_urlencode)
    res_data = urllib.request.urlopen(req)
    res = res_data.read()
    return(res)

def adb_connect(ip_port):
    import os
    fp=os.popen("adb connect "+ip_port)
    resu=fp.read()
    print(resu)
    if resu.find('connected to')!=-1:
        print(str(ip_port)+' connect success')
        return(1)
    else:
        print(str(ip_port)+' connect failed')
        return(0)

def start_job(job_name,job_token='mpp_test'):
    import jenkins
    import time
    url='http://10.1.172.175:8080/'
    user='admin'
    pwd='1qaz2wsx'
    SERVER=jenkins.Jenkins(url=url, username=user, password=pwd)
    SERVER.build_job(name=job_name, token=job_token)
    last_build_number=SERVER.get_job_info(name=job_name)['lastBuild']['number']
    build_info = SERVER.get_build_info(job_name, last_build_number)
    build_result = build_info['result']
    return(build_result)

def stop_job(job_name):
    import jenkins
    url='http://10.1.172.175:8080/'
    user='admin'
    pwd='1qaz2wsx'
    SERVER=jenkins.Jenkins(url=url, username=user, password=pwd)
    last_build_number=SERVER.get_job_info(name=job_name)['lastBuild']['number']
    SERVER.stop_build(name=job_name,number=last_build_number)

def get_random():
    return random.randint(10000,80000)


if __name__ == '__main__':

    # res=insert_cdn_config(404)

    # delete_data('iPhoneiOS12.4.3')


    # delete_cdn()

    # field = {'act':'aplay','cpn':'4'}
    # field = {'logtype':'stay'}
    # field = {'act':'comment'}
    # field = {'act':'share','value':'0'}
    field = {'act':'pvs','cpn':'5'}

    # table='mpp_jiaohu_ipad_imy'
    # table='mpp_heartbeat_5_ipad'
    # table='mpp_jiaohu_ipad'
    # table='mpp_stay_iphone'
    table='mpp_pvs_ipad'
    test_point='login_002'
    #
    result = check_result(field,  'iPadiOS14.4.1Scale/2.00', test_point,  table,   1)
    print(result)
