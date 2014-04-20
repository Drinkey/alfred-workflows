#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2
import urllib
import cookielib
import re, sys, os
import json,time

base_url = 'http://www.yyets.com'

data = {}
data['account'] = "USER_NAME"
data['password'] = "PASSWORD"
data['from'] = "loginpage"

# Setup cookie and user-agent in HTTP header
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36')]
urllib2.install_opener(opener)

def _(string):
    try:
        return string.encode("u8")
    except:
        return string

def _print(str):
    print (_(str))


def req(type,page,request=''):
    try:
        payload = urllib.urlencode(request)

        if (request == ''):
            req = urllib2.Request(page)
        else:
            if (type == 'get'):
                req = urllib2.Request(page+'?'+payload)
            elif (type == 'post'):
                req = urllib2.Request(page, payload)
            else:
                raise Exception
        html = urllib2.urlopen(req)
    except Exception, e:
        print 'Error when calling urllib2.'
        print e
        return None
    return html.read()


resp = req('post',base_url+'/User/Login/ajaxLogin',data)
json_doc = json.loads(resp)

if (json_doc['status'] != 1):
    print "<?xml version=\"1.0\"?>\n<items>"
    print "  <item uid=\"yyets\" arg=\""+base_url+"/user/fav\" >"
    print "    <title>Login failed</title>"
    print "    <subtitle>please verifyy your login credentials</subtitle>"
    print "    <icon type=\"fileicon\">/Applications/Safari.app/</icon>"
    print "  </item>"
    print "</items>"
    sys.exit(1)

resp = req('get',base_url+"/user/fav")
# print resp
item_list = re.findall(r'\<h2\>\<a href\=\"http\:\/\/www\.yyets\.com\/resource\/(\d*)\" target\=\"\_blank\"\>(.*)\<strong\>(.*)\<\/strong\>',resp)
desc_list = re.findall(r'.*\<p class\=\"desc\"\>(.*)\<\/p\>',resp)
update_list = re.findall(r'\<label class=\"resource_time\" time=\"(\d*)\"\>\<\/label\>',resp)


print "<?xml version=\"1.0\"?>\n<items>"
for i in range(len(item_list)):
    # _print(item_list[i][0]+item_list[i][1]+item_list[i][2]+desc_list[i])
    # _print(item[1])
    title = _(item_list[i][1]+item_list[i][2])
    link = base_url+"/resource/"+item_list[i][0]
    update_time = update_list[i]
    desc = _(desc_list[i])
    display_time = time.strftime("%Y-%m-%d %X", time.localtime(int(update_time)))
    print "  <item uid=\""+update_time+"\" arg=\""+link+"\" >"
    print "    <title>"+ display_time +"    "+ title +"</title>"
    print "    <subtitle>"+desc+"</subtitle>"
    print "    <icon type=\"fileicon\">/Applications/Safari.app/</icon>"
    print "  </item>"

print "</items>"






