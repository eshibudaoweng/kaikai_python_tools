#!/usr/bin/env python
# coding=utf-8
import os
import shutil
import sys, getopt

def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        # 这里的h表示该选项无参数，i：表示i选项后需要有参数
        opts,args = getopt.getopt(argv,"hi:s:o:",["ifile=","sfile=","ofile="])
    except getopt.GetoptError:
        print 'shutil_images.py -i <firstfile> -s <secondfile> -o <outputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'shutil_images.py -i <firstfile> -s <secondfile> -o <outputfile>'
            sys.exit()
        elif opt in ("-i","--ifile"):
            firstfile = arg
        elif opt in ("-s","--sfile"):
            secondfile = arg
        elif opt in ("-o","--ofile"):
            outputfile = arg
    print 'first file :',firstfile
    print 'secondfile :',secondfile
    print 'output file:',outputfile
    path = secondfile
    #f = open('/home/dl/songkai/dataset/fgvc-aircraft-2013b/data/images_val.txt','r')
    f = open(firstfile,'r')
    files = f.readlines()
    #files = os.listdir('/home/dl/songkai/dataset/fgvc-aircraft-2013b/data/images/')
    for i in files:
        new_files = path + i[:-1] +'.jpg'
        #shutil.copy(new_files,'/home/dl/songkai/dataset/fgvc-aircraft-2013b/data/val/')
        print i[:-1] + '.jpg'
        shutil.copy(new_files,outputfile)

if __name__ == "__main__":
    main(sys.argv[1:])


