import hashlib
import datetime
import time
import calendar
from django.shortcuts import render
import requests
import pymysql
import json
from django.http import HttpResponse, JsonResponse
# from .models import form_ShiPin_Report
from datetime import datetime, timedelta
from django.db.models import Q
import pymysql
from .models import video_user as User
from .models import FormShipinReport as ShiPin
from .models import *
# Create your views here.


def index(request):
    db = pymysql.connect('localhost', 'root', '000000', 'v')
    cursor = db.cursor()
    name_sql = "select * from form_ShiPin_Report ORDER BY ID DESC limit 8"
    cursor.execute(name_sql)
    result = cursor.fetchall()
    db.commit()
    db.close()
    data = {'data':[]}
    for i in result:
        d1 = {
            'name': '-'.join(i[7].split('-')[3:]),
            'url': i[3]
        }
        data['data'].append(d1)
    response = HttpResponse(json.dumps(data))
    # response["Access-Control-Allow-Origin"] = "*"
    # response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    # response["Access-Control-Max-Age"] = "1000"
    # response["Access-Control-Allow-Headers"] = " * "
    return response


def player_video(request):
    data = {'data': []}
    player = request.GET.get('player')
    match = ShiPin.objects.filter(Q(single_line_shipinmingcheng__icontains=player))
    for i in match:
        dd = {
            'name': '-'.join(i.single_line_shipinmingcheng.split('-')[3:]),
            'url': i.url
        }
        data['data'].append(dd)
    response = HttpResponse(json.dumps(data))
    # response["Access-Control-Allow-Origin"] = "*"
    # response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    # response["Access-Control-Max-Age"] = "1000"
    # response["Access-Control-Allow-Headers"] = " * "
    return response


def project_video(request):
    data = {'data': []}
    match = request.GET.get('match')
    year = request.GET.get('year')
    project = request.GET.get('project')
    results = ShiPin.objects.filter(Q(single_line_shipinmingcheng__icontains=match))
    for i in results:
        n = i.single_line_shipinmingcheng.split('-')
        if n[0] == year:
            if int(n[5]) != 9 and n[4] == project:
                dd = {
                    'name': '-'.join(i.single_line_shipinmingcheng.split('-')[3:]),
                    'url': i.url
                }
                data['data'].append(dd)
    response = HttpResponse(json.dumps(data))
    # response["Access-Control-Allow-Origin"] = "*"
    # response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    # response["Access-Control-Max-Age"] = "1000"
    # response["Access-Control-Allow-Headers"] = " * "
    return response


def playercn_info(request):
    data = {}
    player = request.GET.get('player')
    jctn = [Form3000M, Form30M, FormBmi, FormWotuiMax, FormZuoweitiqianqu, FormChuizhizongtiao, FormYintixiangshang, FormShendunMax, FormBeijinaili, FormFujinaili]
    zxtn = [Form400Mx5, FormLidingtiaoyuan, FormYuandierjitiaoZuo, FormYuandierjitiaoYou, Form5000M, FormShendun90Kg, FormShuangyao1500, FormSijiaopao20]
    pinfen_jctn = [[], [], [], [], [], []]
    pinfen_zxtn = [[], [], [], [], [], []]
    pinfen_fms = [[], [], [], [], [], []]
    lds = [jctn, zxtn]
    for x in lds:
        for i in x:
            result = i.objects.filter(form_yundongyuan=player)
            pf = []
            for j in result:
                try:
                    pinfen = j.dropdown_pingfen
                except Exception as e:
                    pinfen = j.number_pingfen
                if pinfen != '':
                    pf.append(pinfen)
            while len(pf) < 6:
                pf.append('0')
            for n in range(6):
                if lds.index(x) == 0:
                    pinfen_jctn[n].append(pf[n])
                elif lds.index(x) == 1:
                    pinfen_zxtn[n].append(pf[n])

    fms = ['上踏步（左）', '上踏步（右）', '直线弓箭步（左）', '直线弓箭步（右）', '肩部灵活性（左）', '肩部灵活性（右）', '直腿主动上抬（左）', '直腿主动上抬（右）', '深蹲', '躯干稳定俯卧撑', '扭转稳定性（左）', '扭转稳定性（右）']
    for i in fms:
        res_fms = Fms.objects.filter(Q(form_yundongyuan=player) & Q(dropdown_dongzuo=i))
        pf = []
        for j in res_fms:
            pinfen = j.number_pingfen
            if pinfen != '':
                pf.append(pinfen)
        while len(pf) < 6:
            pf.append('0')
        for n in range(6):
            pinfen_fms[n].append(pf[n])

    res_xxl = FormXunlianliang.objects.filter(form_yundongyuan=player)
    result_xxl = []
    key_list = []
    for i in res_xxl:
        xx_time = i.date_field_xunlianriqi.split('-')
        y = str(xx_time[2])
        m = str(list(calendar.month_abbr).index(xx_time[1])).zfill(2)
        d = str(xx_time[0])
        t1 = int(y+m+d)
        result_xxl.append([t1, i.dropdown_xunliankemu, int(i.number_xunlianshichang)])
        if t1 not in key_list:
            key_list.append(t1)
    key_list.sort(reverse=True)
    key_list = key_list[:6]
    # result_xxl.reverse()
    shichang_xxl = []
    for i in key_list:
        shichang = [0, 0, 0, 0]
        for j in result_xxl:
            if j[0] == i:
                if j[1] == '技术（技战术）':
                    shichang[0] = j[2]
                elif j[1] == '技术（小技术）':
                    shichang[1] = j[2]
                elif j[1] == '体能（专项）':
                    shichang[2] = j[2]
                elif j[1] == '体能（力量）':
                    shichang[3] = j[2]
        shichang_xxl.append(shichang)

    res_slsh = FormShenglishenghua.objects.filter(form_yundongyuan=player)
    result_slsh = []
    t_list = []
    for i in res_slsh:
        xx_time = i.date_field_ceshiriqi.split('-')
        y = str(xx_time[2])
        m = str(list(calendar.month_abbr).index(xx_time[1])).zfill(2)
        d = str(xx_time[0])
        t1 = int(y + m + d)
        result_slsh.append([t1, i.formula_ceshixiangmu, float(i.decimal_ceshijieguo)])
        if t1 not in t_list:
            t_list.append(t1)
    t_list.sort(reverse=True)
    t_list = t_list[:6]
    slsh_t = []
    for i in t_list:
        ts1 = str(i)
        ts2 = ts1[:4] + '-' + ts1[4:6] + '-' + ts1[6:8]
        slsh_t.append(ts2)
    r1_slsh = []
    for i in result_slsh:
        if i[0] in t_list:
            r1_slsh.append(i)
    # r1_slsh.sort(key=lambda x:x[0], reverse=True)
    csjg_slsh = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
    bxb = []
    pzc = []
    gt = []
    hxb = []
    jsjm = []
    xns = []
    xqyj = []
    xhdb = []
    for i in r1_slsh:
        if i[1] == '白细胞':
            bxb.append(i)
        elif i[1] == '皮质醇':
            pzc.append(i)
        elif i[1] == '睾酮':
            gt.append(i)
        elif i[1] == '红细胞':
            hxb.append(i)
        elif i[1] == '肌酸激酶':
            jsjm.append(i)
        elif i[1] == '血尿素':
            xns.append(i)
        elif i[1] == '血球压积':
            xqyj.append(i)
        elif i[1] == '血红蛋白':
            xhdb.append(i)
    slsh_all = [bxb, pzc, gt, hxb, jsjm, xns, xqyj, xhdb]
    for o in slsh_all:
        m = slsh_all.index(o)
        for i in o:
            for t in t_list:
                n = t_list.index(t)
                print(m, n, i, t)
                if i[0] == t:
                    csjg_slsh[m][n] = i[2]
    data['jctn'] = pinfen_jctn
    data['zxtn'] = pinfen_zxtn
    data['fms'] = pinfen_fms
    data['xxl'] = shichang_xxl
    data['slsh_time'] = slsh_t
    data['slsh'] = csjg_slsh
    # print(list_3000)
    # response = HttpResponse(json.dumps(data))
    response = HttpResponse(json.dumps(data))
    return response


def search(request):
    if request.method == 'POST':
        a = request.POST.get('data')
        data = {'data': 1}
        response = HttpResponse(json.dumps(data))
        # response["Access-Control-Allow-Origin"] = "*"
        # response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
        # response["Access-Control-Max-Age"] = "1000"
        # response["Access-Control-Allow-Headers"] = " * "
        return response


def login(request):
    if request.method == 'POST':
        name = request.POST.get('user')
        pwd = request.POST.get('pwd')
        # result = User.objects.filter(username=name)[0]
        if '111' == pwd:
            data = {'data': name}
        else:
            data = {'data': ''}
        # if name == 'my':
        # request.session['name'] = name
        # response = HttpResponse('set cookie')

        # data = {'data': name}
        response = HttpResponse(json.dumps(data))

        # response.set_cookie("name", 'my')
        # response["Access-Control-Allow-Origin"] = "null"
        # response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
        # response["Access-Control-Max-Age"] = "1000"
        # response["Access-Control-Allow-Headers"] = " * "
        return response






