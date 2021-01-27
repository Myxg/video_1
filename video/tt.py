import calendar

import pymysql


# db = pymysql.connect('localhost', 'root', '000000', 'video')
#
# cursor = db.cursor()
#
# cursor.execute("DROP TABLE IF EXISTS video_user")
#
# video_user = """CREATE TABLE video_user (
#          id int(11) NOT NULL AUTO_INCREMENT,
#          username CHAR(128),
#          password  CHAR(128),
#          PRIMARY KEY (`id`)
#          )character set utf8"""
#
# cursor.execute(video_user)
#
# db.close()

# !usr/bin/env python# encoding:utf-8   """__Author__:沂水寒城功能： 列表中连续数字段寻找"""
# def continusFind(num_list): ''' 列表中连续数字段寻找 '''
#     num_list.sort()
#     s=1
#     find_list=[]
#     have_list=[]
#     while s<=len(num_list)-1:
#         if num_list[s]-num_list[s-1]==1:
#             flag=s-1
#             while num_list[s]-num_list[s-1]==1:
#                 s+=1
#             find_list.append(num_list[flag:s])
#             have_list+=num_list[flag:s]
#         else:
#             s+=1
#         return find_list
# if __name__=='__main__':
#     num_list=[1,2,4,5,6,7,14,15,17,18,19,31,32,33,34,46,48,78,90,112,113,114,160,432]
#     print(continusFind(num_list))

# import datetime
# import calendar
#
# t = datetime.datetime.now()
# date = ''.join([str(t.day), '-', calendar.month_abbr[int(t.month)], '-', str(t.year)])
#
# print(date)
import requests

try:
    body = {
        'Single_Line_MingCheng': '1.4-1.10.xls',
        'Dropdown_FenLei': '训练量',
        'File_upload': 'C:\\Users\\15234\\Desktop\\wecd\\1.4-1.10.xls',
    }
    u1 = 'https://creator.zoho.com.cn/api/chunzhou.jia2/jason18/files/form/form_docs/record/add/'
    # u1 = 'https://creator.zoho.com.cn/api/v2/chunzhou.jia2/files/report/page/<record_ID>/<field_link_name>/upload'
    params = {
        'authtoken': 'd51ecfa14f98e8f14c91ac894bf8e7d4',
        'scope': 'creatorapi',
        'raw': "true",
    }
    req = requests.post(u1, params={**params, **body})
    req_json = req.json()
    print(req_json)
except Exception as e:
    pass









