#!/usr/bin/env python
# coding=utf-8
import shutil
import sys, getopt

def process_file(r):
    path = '/home/dl/songkai/dataset/fgvc-aircraft-2013b/data/images/'
    files = f.readlines()
    print files
    for i in files:
        new_files = path + i[:-1]+'.jpg'
        shutil.copy(new_files,sys.argv[2])
if __name__ == "__main__":
    print "start"
    f = open(sys.argv[1],'r')
    process_file(f)
    f.close()

