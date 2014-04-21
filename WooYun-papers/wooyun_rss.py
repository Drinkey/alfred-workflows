#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2
import urllib
import cookielib
import re, sys, os
import time
import xml.etree.cElementTree as ET

base_url = 'http://drops.wooyun.org/feed'

class RssXml:

    def __init__(self, xmlString):
        self.root = ET.fromstring(xmlString)
        # self.root = self.tree.getroot()
        # return self.root

    def getTitle(self, doc):
        # get name attribute
        return doc.find('title').text
    
    def getCategory(self, doc):
        # get externalid child data
        return doc.find('category').text  
    
    def getDescription(self, doc):
        return doc.find('description').text
    
    def getLink(self, doc):
        return doc.find('link').text
    
    def getPubDate(self, doc):
        return doc.find('pubDate').text



data = {}

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

def main():
    resp = req('get',base_url)
    # print resp
    rss = RssXml(resp)

    print "<?xml version=\"1.0\"?>\n<items>"
    for item in rss.root.findall('.//item'):
        # print _(rss.getTitle(item))
        # print _(rss.getCategory(item))
        # print item.tag
        print "  <item uid=\""+_(rss.getTitle(item))+"\" arg=\""+rss.getLink(item)+"\" >"
        print "    <title>["+ _(rss.getCategory(item)) +"] "+ _(rss.getTitle(item)) +"</title>"
        print "    <subtitle>"+_(rss.getDescription(item))+"</subtitle>"
        print "    <icon type=\"fileicon\">/Applications/Safari.app/</icon>"
        print "  </item>"
    
    print "</items>"

if __name__ == "__main__":
    main()
