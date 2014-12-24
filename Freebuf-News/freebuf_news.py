#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2
import urllib
import cookielib
import re, sys, os
import json,time

base_url = 'http://www.freebuf.com'

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

# <dt>
#     <a style="color:#ED4747" href="http://www.freebuf.com/news/special/38727.html" target="_blank" title="走进科学：酒店保险箱真的保险么？">走进科学：酒店保险箱真的保险么？</a>
# </dt>
# <dd class="text">
#           本文是FreeBuf《走进科学》系列最新力作，翻译自国外安全组织G DATA SecurityLabs一篇针对酒店保险箱的分析报告。他们的研究对象是一款产自中国并且以很多不同的品牌出售的保险柜。</dd>

resp = req('get',base_url)
# print resp
item_list = re.findall(r'\<dt\>\n.*\<a.* href\=\"(.*)\".*\>(.*)\<\/a\>\n.*\<\/dt\>\n.*\<dd.*\>\n.*\"(.*)\"\n.*\<\/dd\>',resp)
# desc_list = re.findall(r'.*\<p class\=\"desc\"\>(.*)\<\/p\>',resp)
# update_list = re.findall(r'\<label class=\"resource_time\" time=\"(\d*)\"\>\<\/label\>',resp)
print item_list

# print "<?xml version=\"1.0\"?>\n<items>"
# for i in range(len(item_list)):
#     # _print(item_list[i][0]+item_list[i][1]+item_list[i][2]+desc_list[i])
#     # _print(item[1])
#     title = _(item_list[i][1]+item_list[i][2])
#     link = base_url+"/resource/"+item_list[i][0]
#     update_time = update_list[i]
#     desc = _(desc_list[i])
#     display_time = time.strftime("%Y-%m-%d %X", time.localtime(int(update_time)))
#     print "  <item uid=\""+update_time+"\" arg=\""+link+"\" >"
#     print "    <title>"+ display_time +"    "+ title +"</title>"
#     print "    <subtitle>"+desc+"</subtitle>"
#     print "    <icon type=\"fileicon\">/Applications/Safari.app/</icon>"
#     print "  </item>"

# print "</items>"






