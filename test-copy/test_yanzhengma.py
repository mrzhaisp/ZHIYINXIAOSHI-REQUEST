#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PIL import Image,ImageEnhance
from selenium import webdriver
import time as t
import  pytesseract
# image = Image.open('../picture/yanzhengma.png')
# # image.show()
# enh_bri = ImageEnhance.Brightness(image)
# brightness = 1.5
# image_brightness = enh_bri.enhance(brightness)
# # image_brightness.show()
# enh_col = ImageEnhance.Color(image)
# color = 1.5
# image_colored = enh_col.enhance(color)
# # image_colored.show()
# enh_con = ImageEnhance.Contrast(image)
# contrast = 1.5
# image_contrasted = enh_con.enhance(contrast)
# # image_contrasted.show()
# enh_sha = ImageEnhance.Sharpness(image)
# sharpness = 3.0
# image_sharped = enh_sha.enhance(sharpness)
# image_sharped.show()
from selenium import webdriver
dr = webdriver.Chrome()
dr.maximize_window()
dr.get("http://www.sbrainx.com/#/")
t.sleep(2)
dr.find_element("xpath",".//body/descendant::span[3]").click()
t.sleep(1)
dr.find_element("xpath",".//body/descendant::input[8]").send_keys("admin")
t.sleep(1)
dr.find_element("xpath",".//body/descendant::input[9]").send_keys("1q2w3e4r5t@")
dr.save_screenshot('../picture/test.png')
imgelement = dr.find_element("xpath",".//body/descendant::div[@class='el-form-item__content'][3]/img")
location = imgelement.location
size = imgelement.size
rangle = (int(location['x']),
         int(location['y']),
         int(location['x']+size['width']),
         int(location['y']+size['height']))

i = Image.open('../picture/test.png')
verifycodeimage=i.crop(rangle)
verifycodeimage.save('../picture/yanzhengma.png')
image = Image.open('../picture/yanzhengma.png')
imgry = image.convert('L')
sharpenss = ImageEnhance.Contrast(imgry)
i3 = sharpenss.enhance(3.0)
i3.save("../picture/zengqinagpic.png")
i4 = Image.open("../picture/zengqinagpic.png")
text = pytesseract.image_to_string(i).strip()
print("----为   ",text)






