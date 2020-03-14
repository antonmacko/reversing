#!/usr/bin/python
import sys
args=sys.stdin
for line in args:
   out=""
   for i in line[::-1]:
        print i
        out+=chr(ord(i)^((len(line))-line.find(i)-1))

   print line[:len(line)-1]+":"+out[1:]
