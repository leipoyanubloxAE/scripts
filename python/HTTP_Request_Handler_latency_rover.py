#!/usr/bin/env python

from datetime import datetime
from datetime import timedelta
import urllib2
import time
import re
import logging

hostname = "http://ubloxsingapore.asuscomm.com:4004/latencytest"
#hostname = "http://10.122.253.32:8007/latencytest"
count = 3600 * 24
pretag = "Timestamp :"
posttag = "; "
timeformat = "%Y-%m-%d %H-%M-%S-%f"

logger = logging.getLogger('rover')
hdlr = logging.FileHandler('latency_rover.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)

for ite in range(1, count):
   time.sleep(0.2)
   ctime = datetime.now()
   request = urllib2.Request(hostname)
   response = urllib2.urlopen(request)
   content = response.read()
   response.close()
   #print content
   try:
      ### match the last time stamp
      #pattern = '.*' + pretag + '(.+?)' + posttag + '$';
      ### match the first time stamp
      pattern = pretag + '(.+?)' + posttag;

      ptime = re.search(pattern, content).group(1)
      #print "found time is " + ptime
      try:
         ptime = datetime.strptime(ptime, timeformat)
      except ValueError:
         ptime = ctime
   except AttributeError:
      ptime = ctime

   latency_ms = int((ctime - ptime).total_seconds() * 1000)
   #print (ctime, ptime)
   print str(latency_ms) + "ms"
   logger.info(str(latency_ms) + "ms")
   

