#!/usr/bin/env python
# coding=utf-8
from  string  import maketrans
import www
def Text(toUser,UserText):
    content=""
    if UserText=="成绩":
        content=www.Grade(toUser)
    elif UserText.count('&')==1:#绑定
        ind ="&"
        optd ="@"
        trantab = maketrans(ind,optd)  
        UserText=UserText.translate(trantab)
        content=www.Bind(toUser,UserText)
    elif UserText=="家":
        content="<a href=\"http://119.29.115.52:8080/\">家</a>"
    elif UserText=="公交":
        pass
    elif UserText=="微博":
        pass
    elif UserText=="豆瓣":
        pass
    return content
