#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-14 13:54:38
# @Author  : ditto (969956574@qq.com)
# @Link    : https://github.com/dittoyy
# @Version : $Id$

import sys
sys.path.append(r'C:\Python27\Lib\site-packages\pytesser_v0.0.1')
# print sys.path
from pytesser import *
from PIL import ImageEnhance

image = Image.open(r'C:\Python27\Lib\site-packages\pytesser_v0.0.1\fnord.tif')  # Open image object using PIL
print image_to_string(image)     # Run tesseract.exe on image

print image_file_to_string(r'C:\Python27\Lib\site-packages\pytesser_v0.0.1\fnord.tif')



image = Image.open(r'C:\Python27\Lib\site-packages\pytesser_v0.0.1\fonts_test.png')# support by PIL
#使用ImageEnhance可以增强图片的识别率
enhancer = ImageEnhance.Contrast(image)
image_enhancer = enhancer.enhance(4)

print image_to_string(image_enhancer)



#im = Image.open('fnord.tif')
#im = Image.open('phototest.tif')
#im = Image.open('eurotext.tif')
im = Image.open('fonts_test.png')
text = image_to_string(im)
print text

enhancer = ImageEnhance.Contrast(image1)
image2 = enhancer.enhance(4)