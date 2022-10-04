#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Author:时无ShiWu
#Filename:ACB File Parser.py
#Version:1.0 448.38

import csv
import binascii
import re
import os

# 脚本默认位置
default_path=os.path.split(os.path.realpath(__file__))[0]
# 文件列表位置
sfs_path=default_path+r'\soundfile_seq.csv'
# acb序列位置
acb_path=default_path+r'\acbfile'
# 中间处理位置
trans_path=default_path+r'\trans'
# 输出csv文件位置
ex_csv_path=default_path+r'\acbseq'

with open(sfs_path,'r') as sfs:
    fsreader=dict(csv.reader(sfs))
    seqlen=len(fsreader)
    for i in range(1,seqlen):
        exfn=fsreader.get(str(i),-1)
        print(exfn)
        with open(acb_path+'\\'+exfn+'.acb','rb') as f:
            alldata=f.readlines()

            if(os.path.exists(trans_path+'\\'+exfn+'.txt')==True):
                with open(trans_path+'\\'+exfn+'.txt','w+') as oa:
                    oa.write(str(alldata)+'\n')
            else:
                with open(trans_path+'\\'+exfn+'.txt','a+') as oa:
                    oa.write(str(alldata)+'\n')
            oa.close()

        with open(trans_path+'\\'+exfn+'.txt','rt') as nf:
            nfr=nf.readlines()
            nfraw=str(nfr[0])
            fd=nfraw.find('CueIndex')
            fn=nfraw.find(r'\x00\x00',fd)
            print(fd,fn)
            hseq=nfraw[fd:fn]
            hseq=hseq.replace(r'\x00',",")
            hseq=hseq.split(',')
            hsl=len(hseq)
            result=[]
            for i in range(0,hsl):
                if(i==0):
                    result.append('id')
                else:
                    result.append(i)
            print(fn)
            with open(ex_csv_path+'\\'+exfn+'.csv','w',newline='') as wcsv:
                fwl=[]
                fwl.append(result)
                fwl.append(hseq)
                writer=csv.writer(wcsv)
                for column in zip(*[i for i in fwl]):
                    writer.writerow(column)
wcsv.close()
nf.close()
oa.close()
f.close()
sfs.close()
