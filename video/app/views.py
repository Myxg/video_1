from django.shortcuts import render
import requests
import pymysql
import json
from django.http import HttpResponse
from .models import form_ShiPin_Report
from django.db.models import Q
# Create your views here.


def index(request):
    db = pymysql.connect('localhost', 'root', '000000', 'v')
    cursor = db.cursor()
    name_sql = "select * from form_shipin_report ORDER BY ID DESC limit 8"
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
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = " * "
    return response


def player_video(request):
    data = {'data': []}
    player = request.GET.get('player')
    match = form_ShiPin_Report.objects.filter(Q(Single_Line_ShiPinMingCheng__icontains=player))
    for i in match:
        html = requests.head(i.Url)
        re = html.status_code
        if re == 200:
            dd = {
                'name': '-'.join(i.Single_Line_ShiPinMingCheng.split('-')[3:]),
                'url': i.Url
            }
            data['data'].append(dd)
    response = HttpResponse(json.dumps(data))
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = " * "
    return response


def project_video(request):
    data = {'data': []}
    match = request.GET.get('match')
    year = request.GET.get('year')
    project = request.GET.get('project')
    results = form_ShiPin_Report.objects.filter(Q(Single_Line_ShiPinMingCheng__icontains=match))
    for i in results:
        n = i.Single_Line_ShiPinMingCheng.split('-')
        if n[0] == year:
            if int(n[5]) != 9 and n[4] == project:
                html = requests.head(i.Url)
                re = html.status_code
                if re == 200:
                    dd = {
                        'name': '-'.join(i.Single_Line_ShiPinMingCheng.split('-')[3:]),
                        'url': i.Url
                    }
                    data['data'].append(dd)
    response = HttpResponse(json.dumps(data))
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = " * "
    return response


def search(request):
    if request.method == 'POST':
        a = request.POST.get('data')
        data = {'data': 1}
        response = HttpResponse(json.dumps(data))
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = " * "
        return response


