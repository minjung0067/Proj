#! /usr/bin/env python
# $Id: testupnpigd.py,v 1.7 2020/04/06 10:23:02 nanard Exp $
# MiniUPnP project
# Author : Thomas Bernard
# This Sample code is public domain.
# website : https://miniupnp.tuxfamily.org/

# import the python miniupnpc module
import miniupnpc
import socket
import sys

try:
    from http.server import BaseHTTPRequestHandler, HTTPServer
except ImportError:
    from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

# function definitio
def list_redirections():
    i = 0
    while True:
        p = u.specific
        
        if (p != None):
            print(i, p)
        if i > 64444:
            break
        i = i + 1


u = miniupnpc.UPnP()
# list_redirections()
print(u.statusinfo(), u.connectiontype())