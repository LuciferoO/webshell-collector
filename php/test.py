#!/usr/bin/env python
# -*- coding: UTF-8 -*- 
##############################################################
# Licence: Copyright (c) 2014 pys0lve <shiqiaomu@me.com>
# Date:    2014/11/14 19:00:00
# Brief:   webshell-checker
# href:    https://github.com/shiqiaomu/webshell-collector
# V1.0     14 Nov 2014 Initial release
###############################################################

"""
check whether the webshell already has been collected
"""

import hashlib
import sys
import os
import commands


for eachFile in os.listdir("./"):
    ext = os.path.splitext(eachFile)[1]
    if ext != ".php":
        name = os.path.splitext(eachFile)[0] + "_.php"
        command = 'git mv "'  + eachFile + '" ' + '"' + name + '"'
        print command
        print commands.getstatusoutput(command)
        print name
"""
pre = ""
with open("data") as fileHandle:
    for eachLine in fileHandle:
        eachLine = eachLine.strip("\n")
        url = 
"""
