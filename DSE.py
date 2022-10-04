#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Author:时无ShiWu
#Filename:DSE.py
#Version:1.0 448.37

from math import fabs
import threading
import multiprocessing
import os
import sys
import csv
import argparse
import subprocess
from time import sleep

# 脚本默认位置
default_path=os.path.split(os.path.realpath(__file__))[0]
# vgmstream 位置
vgm_path=default_path+r'\vgmstream\test.exe'
# 数据文件列表位置
sfs_path=default_path+r'\soundfile_seq.csv'
# 音频序列位置
seq_path=default_path+r'\acbseq'
# 源文件位置
osf_path=default_path+r'\osf'
# 输出位置 
output_path=default_path+r'\output'

respond=''
cir=0

def extract_files(a,b):

    print(default_path,vgm_path)

    # 加载数据文件列表
    with open(sfs_path,'r') as sfs:
        fsreader=dict(csv.reader(sfs))

    # 序列是否存在进行判断，存在则为其创建一个文件夹
    print(a)
    fn=fsreader.get(a,-1)
    if(fn==-1):
        print('seq not found')
        sys.exit(0)
    else:
        if not (os.path.exists(output_path+'\\'+fn)):
            os.makedirs(output_path+'\\'+fn)
    
    # 加载文件序列
    print(fn)
    with open(seq_path+'\\'+fn+'.csv') as seqfs:
        sesreader=dict(csv.reader(seqfs))
    
    sn=len(sesreader)
    # print(sn,type(sn),int(b),type(int(b)))
    try:
        ib=int(b)
    except:
        print('wrong channel number,plz check argument')
        sys.exit(0)

    # 判断只导出单个声道还是导出全部声道
    if(ib!=0):
        outname=sesreader.get(str(ib))
        # cmd序列生成
        subprocess.call(vgm_path+' -s '+str(ib)+' -o '+output_path+'\\'+fn+'\\'+outname+'.wav'+' '+osf_path+'\\'+fn+'.awb',bufsize=-1)
        print('end')
    elif(ib==0):
        for i in range(1,sn):
            outname=sesreader.get(str(i))
            print(outname)
            # cmd序列生成
            subprocess.call(vgm_path+' -s '+str(i)+' -o '+output_path+'\\'+fn+'\\'+outname+'.wav'+' '+osf_path+'\\'+fn+'.awb',bufsize=-1)
    sfs.close()
    seqfs.close()


if __name__=="__main__":
    # parser settings
    parser = argparse.ArgumentParser(prog='python dse.py',usage='%(prog)s [--fileid] <file_id> ([--channel] <channel_id>)',description="Python Program for Extract Sound Files")
    parser.add_argument('--fileid',default='empty',nargs='?',help='extract file from filelist sequence')
    parser.add_argument('--channel',default=0,nargs='?',help='extract channel N from file channels,set 0 or empty extract all single channel')
    
    # merge parser
    args = parser.parse_args()
    
    # print help with boot
    # parser.print_help()

    if(args.fileid=='empty'):
        print("You can't run prog without <fileid>")
        parser.print_help()
        sys.exit(0)


    if(args.fileid=='all'):
        # 加载数据文件列表
        with open(sfs_path,'r') as psfs:
            fsreader=dict(csv.reader(psfs))
        psfi=len(fsreader)
        for s in range(1,psfi):
                extract_files(str(s),args.channel)    
    else:
        extract_files(args.fileid,args.channel)

    # debug
    print(args.fileid)
    if(args.fileid==0):
        print('extract all')
        print("now command: dse.py "+"--fileid "+str(args.fileid)+" --channel "+str(args.channel))
        print(type(args.fileid))
    else:
        print(type(args.fileid[0]))
        print("now command: dse.py "+"--fileid "+str(args.fileid)+" --channel "+str(args.channel))