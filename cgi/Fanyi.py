#!/usr/bin/env python
# coding=utf-8

import urllib
import json
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
def Trans(content):
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=http://www.youdao.com/'
    data = {}
    data['type'] = 'AUTO'
    data['i'] = content
    data['doctype'] = 'json'
    data['xmlVersion'] = '1.8'
    data['keyfrom'] = 'fanyi.web'
    data['ue'] = 'UTF-8'
    data['action'] = 'FY_BY_CLICKBUTTON'
    data['typoResult'] = 'true'
    data = urllib.urlencode(data).encode('utf-8')
    response = urllib.urlopen(url, data)
    html = response.read().decode('utf-8')
    target = json.loads(html)
    #print('翻译的结果：%s' % target['translateResult'][0][0]['tgt'])
    return target['translateResult'][0][0]['tgt']

