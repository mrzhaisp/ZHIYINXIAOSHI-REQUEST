#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
all_video_list = []
url  = "http://10.168.103.151/video_analysis/video_origin/pageQuery"
num_list= [2,3,9,10,11,12,13,14]

for num in num_list:
	print(num)
	data = {'tag_ids': num}    #3:央企  2:国资委   10:人工智能  11电子对抗   12下一代网络  13只能制造  14区块链  9其他
	res = requests.post(url,data=data)
	print(data)
	result = res.json()
	result_detail = (result['result'])
	for i in result_detail:
		all_video_list.append(i['title'])
	if result_detail:
		print('{}栏目下的视频列表为{}'.format(num,all_video_list))








