#!/usr/bin/python
# -*- coding: utf-8 -*-

import re, sys, json, os

shuttle_config = os.path.expanduser("~")+"/.shuttle.json"

host_name = ""

pattern = re.compile('^'+host_name, flags=re.IGNORECASE)

found_flag = 0

def listHosts(hosts):
    # found_flag = found_flag
    for host in hosts:
        if (not host.has_key(u'cmd')):
            listHosts(host[host.keys()[0]])
        else:
            if pattern.match(host['name']):
                global found_flag
                found_flag += 1
                print "  <item uid=\""+host['name']+"\" arg=\""+host['cmd']+"\" >"
                print "    <title>"+ host['name'] +"</title>"
                print "    <subtitle>"+host['cmd']+"</subtitle>"
                print "    <icon>icon.png</icon>"
                print "  </item>"
    

shuttle_file = file(shuttle_config)
# print shuttle_file

try:
    json_string = json.dumps(json.load(shuttle_file))
    # print json_string
    host_list = json.loads(json_string)
    # print host_list
    print "<?xml version=\"1.0\"?>\n<items>"
    listHosts(host_list['hosts'])
    if (found_flag == 0):
        print "  <item uid=\"Not Found\" arg=\"\" >"
        print "    <title>No Match!</title>"
        print "    <subtitle>Cannot find "+host_name+"</subtitle>"
        print "    <icon>icon.png</icon>"
        print "  </item>"
    print "</items>"
except Exception,e:
    shuttle_file.close()
    print e
    sys.exit(1)

