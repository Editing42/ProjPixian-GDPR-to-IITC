#! /usr/bin/env python3
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
print('[DONE]   Game log loaded.')
data=data[1:]

##PROCESS DATA, GENERATE upc,upv
upc,upv=set(),set()
upv_ops=('resonator deployed', 'resonator upgraded', 'hacked friendly portal', 'hacked enemy portal', 'hacked neutral portal')
for row in data:
    if row[3]=='captured portal':
        upc.add((row[1],row[2]))
        upv.add((row[1],row[2]))
        continue
    if row[3] in upv_ops and row[4] == 'success':
        upv.add((row[1], row[2]))
upv_only = upv-upc

##WRITE
upc_log=''
upv_log=''

with open(r'./UPC.log','w') as f:
    f.write('[')
    for la,ln in upc:
        newline='{"latLng":{"lat":'+la+',"lng":'+ln+'},"color":"#ff0000","radius":20,"type":"circle"},'
        upc_log+=newline
    f.write(upc_log[:-1])
    f.write(']')
print('[DONE]   UPC.log generated.')

with open(r'./UPV.log','w') as f:
    f.write('[')
    for la,ln in upv:
        newline='{"latLng":{"lat":'+la+',"lng":'+ln+'},"color":"#ff0000","radius":20,"type":"circle"},'
        upv_log+=newline
    f.write(upv_log[:-1])
    f.write(']')
print('[DONE]   UPV.log generated.')

with open(r'./UPCV.log','w') as f:
    f.write('[')
    for la,ln in upv_only:
        newline='{"latLng":{"lat":'+la+',"lng":'+ln+'},"color":"#a24ac3","radius":20,"type":"circle"},'
        upc_log+=newline
    f.write(upc_log[:-1])
    f.write(']')
print('[DONE]   UPCV.log generated.')

##FINISH
print('[DONE]   All finished, copy all from UPC/UPV file and paste into IITC-drawtools.')
input('[...]    Press ENTER to EXIT.')
