#!/usr/bin/python
#
# play mp3 file on bluetooth, if present

import subprocess32 as subprocess
import sys
import os.path

if len(sys.argv) <2:
  print "Syntax: "+sys.argv[0]+" <mp3 filename(s)>"
  quit()

fnames = sys.argv[1:]
for fname in fnames:
  if not os.path.isfile(fname):
    print "File not found: "+fname
    quit() 

fnames = " ".join(fnames)

try:
  a=subprocess.check_output('cat /proc/bus/input/devices | grep -B 2 virtual | grep -m 1 Name=  | awk -F\'"\' \'{print $2}\'', shell=True)
  if not a:
    print "virtual output not found - is your bluetooth device connected?"
    quit()
  a=a.rstrip()
  print "Using virtual device "+a
  print 'Command: mpg123 -q -a bluealsa:HCI=hci0,DEV='+a+',PROFILE=a2dp '+fnames
  subprocess.Popen('mpg123 -q -a bluealsa:HCI=hci0,DEV='+a+',PROFILE=a2dp '+fnames+' &>/dev/null &', shell=True) 
except subprocess.CalledProcessError:
  print "wups"
