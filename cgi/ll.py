   #-*-coding:utf-8-*-
import datetime
import random
import pytesseract	
from PIL import Image
from collections import OrderedDict
import os
import re
from lxml import etree
import requests
import urllib
import urllib2
import sys
#设置编码
headersss={
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Connection':'keep-alive',
    'Content-Type':'application/x-www-form-urlencoded',
    'Referer':'http://jwc.xatu.edu.cn/index.htm',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36',
}
reload(sys)
sys.setdefaultencoding( "utf-8" )
def DoPic(picurl):###---------处理验证
    im = Image.open(picurl);
    im=im.resize((100, 100))#,Image.ANTIALIAS).save(picurl, quality=100,dpi=(100, 100));
    vcode=pytesseract.image_to_string(im, config="-psm 8 -c tessedit_char_whitelist=1234567890");
    return vcode;
user_name = "14050205101"
password = "bhmzmdb5h"
ll="http://jwc.xatu.cn/"
s = requests.session()
url = "http://jwc.xatu.edu.cn/userlog.asp"
mm=s.get(ll,headers=headersss)
print s.cookies
imgUrl = "http://jwc.xatu.cn/js/checkcode.asp"
imgresponse = s.get(imgUrl)
print s.cookies
image = imgresponse.content
DstDir = os.getcwd()+"/"
print("保存验证码到："+DstDir+"code.jpg"+"\n")
try:
    jpg=open(DstDir+"code.jpg" ,"wb")
    jpg.write(image)
    jpg.close()
except IOError:
    print("IO Error\n")
code = DoPic("code.jpg")
co= requests.utils.dict_from_cookiejar(s.cookies)
print s.cookies.values
PostData = OrderedDict();
PostData['username']=user_name;
PostData['password']=password;
PostData['CheckCode']=code;
PostData['mynum']='1';
st = u'登 陆';
st = st.encode('gb2312');
PostData['btnlog']=st;
data=urllib.urlencode(PostData);
response = s.post(url,data,headers=headersss)
print s.cookies.values
#print response.content
#print "成功进入教务系统！"
