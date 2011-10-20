#!/usr/bin/env python

import os

dir_jar = '/home/paullzn/software/yuicompressor-2.4.6/build/yuicompressor-2.4.6.jar'
dir_src = './'
dir_dst = '../src/public/javascripts/client/'

files = os.listdir(dir_src)

for name in files:
    if name[-2:] == 'js':
        os.system('java -jar ' + dir_jar + ' ' + name + ' -o ' + dir_dst + name)
        print 'compressing ' + name

