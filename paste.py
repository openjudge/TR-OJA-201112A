#!/usr/bin/env python
# Copyright (C) 2011 LIU Yu <pineapple.liu@gmail.com>
# All rights reserved.

import os
import sys
import time
import cgi
import urllib

prefix = './paste.d'

def cgi_main():
    sys.stdout.write('Content-Type: text/html\n\n')
    sys.stdout.write('Logging data ... ')
    try:
        path = os.environ['REMOTE_ADDR']
        file = "%d.txt" % int(time.time()) 
        data = os.environ['QUERY_STRING']
        os.makedirs(os.path.join(prefix, path))
        fp = open(os.path.join(prefix, path, file), 'w')
        fp.write(urllib.unquote(data))
        fp.close()
        sys.stdout.write('done\n')
    except Exception, e:
        sys.stdout.write('failed (%s)\n' % str(e))
    return 0

if __name__ == '__main__':
    sys.exit(cgi_main())

