#!/usr/bin/env python
# coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import urllib2
import pytesseract	
from PIL import Image
import cookielib
import urllib
import re
from collections import OrderedDict
import requests
import www
def DoPic(picurl):###---------处理验证
    im = Image.open(picurl);
    im=im.resize((100, 100))#,Image.ANTIALIAS).save(picurl, quality=100,dpi=(100, 100));
    vcode=pytesseract.image_to_string(im, config="-psm 8 -c tessedit_char_whitelist=1234567890");
    return vcode;

def DoData(usr,pas,code):
    PostData = OrderedDict();
    PostData['username']=usr;
    PostData['password']=pas;
    PostData['CheckCode']=code;
    PostData['mynum']='1';
    st = u'登 陆';
    st = st.encode('gb2312');
    PostData['btnlog']=st;
    data=urllib.urlencode(PostData);
    #print data;
    return data;

def Str(user_name,password):
    Posturl="http://jwc.xatu.edu.cn/userlog.asp"#教学网验证码地址
    capturl="http://jwc.xatu.cn/js/checkCode.asp"#教学网提交页面
    picName="./cgi/image.jpg"
    cookie =cookielib.CookieJar()
    handler=urllib2.HTTPCookieProcessor(cookie) 
    opener=urllib2.build_opener(handler)
    urllib2.install_opener(opener)
    picture=urllib2.urlopen(capturl)#-----****打开所要打开的网页
    local=open(picName,'wb')
    local.write(picture.read())
    local.close()
    secretCode=DoPic(picName)
    headers={
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Connection':'keep-alive',
        'Content-Type':'application/x-www-form-urlencoded',
        'Origin':'http://jwc.xatu.edu.cn',
        'Referer':'http://jwc.xatu.edu.cn/index.htm',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36',
    }
    request=urllib2.Request(Posturl,DoData(user_name,password,secretCode),headers)
#print request
    try:
        response=opener.open(request)
        result=response.read().decode('gb2312')
        gr=www.Grade(result)
        return "服务器正在维护中"
    except urllib2.HTTPError,e:
        print e.code
        return "服务器产生问题，已将错误报告给开发者"











