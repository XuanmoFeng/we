#!/usr/bin/env python
# coding=utf-8
# import sys
#import sys
#sys.path.append(r'..')
import DataBase
import YouDian
#from cgi.Xatu import Xatu
import string
def Grade(weid):
    if DataBase.Select(weid)==" ":
        return "请绑定教务网账号和密码格式如：\n14050205101&xasdascas"
    else:
        str=DataBase.Select(weid)
        user=str.partition('@')
        username=user[0]
        password=user[2]
<<<<<<< HEAD
        result=YouDian.Str(username,password)
        print result
        if result =='':
=======
        result=Xatu.Str(username,password)
        if result == "FALSE":
>>>>>>> origin/master
            return "查询失败请重新绑定"
        else:
            return result

def Bind(weid,str):
    user=str.partition('@')
    username=user[0]
    password=user[2]
    if DataBase.InsertData(weid,username,password)=="1":
        return "绑定成功"
    else:
        return "请检查账号和密码是否错误"
