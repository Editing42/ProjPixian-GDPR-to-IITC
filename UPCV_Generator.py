#!/bin/python3
# -*- coding:utf8 -*-
'''
@Author: Agent DuskPiper (github.com/duskpiper)
@Date: 2018.10.09
@Intro:
    This script helps transfer game_log.tsv data into IITC-draw-tool link in order to display on map your UPC or UPV.
    This script is based on python3.
'''

#import codecs
print('---This script is composed by DuskPiper---')
print('[NOTICE] Now load game_log.tsv. Plz put file at the same path with this script.')
input('[...]    Press ENTER to continue.')

##LOAD TSV
with open(r'./game_log.tsv',encoding='utf8') as tsv:
    data=[line.strip().split('\t') for line in tsv]
tsv.close()
print('[DONE]   Game log loaded.')
data=data[1:]

##PROCESS DATA, GENERATE upc,upv
upc,upv=set(),set()
upv_ops=('resonator deployed','hacked','mod deployed')
writer=''
for row in data:
    if row[3]=='captured portal':
        upc.add((row[1],row[2]))
        upv.add((row[1],row[2]))
        continue
    if row[3] in upv_ops:
        upv.add((row[1], row[2]))

##WRITE
w=open(r'./UPC.txt','w')
w.write('[')
for la,ln in upc:
    newline='{"latLng":{"lat":'+la+',"lng":'+ln+'},"color":"#ff00ff","radius":20,"type":"circle"},'
    writer+=newline
w.write(writer[:-1])
w.write(']')
w.close()
print('[DONE]   UPC.txt generated.')
w=open(r'./UPV.txt','w')
w.write('[')
for la,ln in upv:
    newline='{"latLng":{"lat":'+la+',"lng":'+ln+'},"color":"#ff00ff","radius":20,"type":"circle"},'
    writer+=newline
w.write(writer[:-1])
w.write(']')
w.close()
print('[DONE]   UPV.txt generated.')

##FINISH
print('[DONE]   All finished, copy all from UPC/UPV file and paste into IITC-drawtools.')
input('[...]    Press ENTER to EXIT.')



