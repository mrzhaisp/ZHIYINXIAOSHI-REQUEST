#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Commonlib.commonlib import Commonlib
import requests
import csv
c = Commonlib()

video_id_list = [4862,4863,4864,55]
base_host = "http://10.168.103.151/video_analysis/video_origin/getEntityById?id="

def get_all_url_list():
	"""组装所有的url列表"""
	video_url_list = []
	for id in video_id_list:
		req_url = base_host + str(id)
		video_url_list.append(req_url)
	# print(video_url_list)
	# print(len(video_url_list))
	return video_url_list

def get_all_error_true():
	title_id_list = []
	error_id_list = []
	for url in get_all_url_list():
		try:
			res = requests.get(url,cookies=c.get_cookie())
			content_uni = res.json()
			title_id_list.append((url.split('getEntityById?id=')[1],content_uni['title']))
			print("√√√   当前有效id数据数量为%s 列表为%s"%(len(title_id_list),title_id_list))
			posi = {
				'id':url.split('getEntityById?id=')[1],
				'title':content_uni['title']
			}
			title_id_list.append(posi)
		except:
			error_id_list.append(url.split('getEntityById?id=')[1])
			print("xxx   当前无效id数据列表数量为%s 列表为%s" %(len(error_id_list), error_id_list))

	return title_id_list,error_id_list

def write_csv():
	print("开始写入csv")
	headers = {'id','title'}
	with open('151_test_id.csv','a',newline='',encoding="gbk") as f:
		writer = csv.DictWriter(f,headers)
		writer.writerows(get_all_error_true()[0])

get_all_error_true()
write_csv()
# print("可以拿到数据的个数为%s<--->数据列表为%s"%(len(title_id_list),title_id_list))
# print("错误id的数据个数为%s<--->数据列表为%s" % (len(error_id_list), error_id_list))
#




