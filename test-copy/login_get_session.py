#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json
def get_cookie():
	"""拿到cookie"""
	host = "http://10.168.103.151"
	url_path = "/video_analysis/login"
	url = host + url_path
	data = {
		"code": "admin",
		"pwd": "418FE8C4A00CB0CFA1909D659CB7A406D03EA0AC9DA98CDA0F9C57A157083765291ED5275B742A48D4DA123AB9CE3C9A6D53627830DBB7EE5F1750A497BACE99"
	}
	r = requests.post(url=url,data=data)
	cookie = r.cookies.get_dict()

def get_content(url,contenttype):
	"""传入url和类型，可获取首页视频的名称"""
	video_name_list = []
	base_url = url
	# yinshipn_url = 'http://10.168.103.151/video_analysis/video_origin/pageQuery'
	data= {'tag_ids':contenttype}
	r = requests.post(base_url,cookies = get_cookie(),data=data)
	content =r.json()
	#拿到国企第一页的视频
	result = content['result']
	for i in result:
		video_name_list.append(i['id'])
		video_name_list.append(i['title'])
		video_name_list.append(i['load_time'])
	print(video_name_list)

if __name__ == '__main__':
	get_content('http://10.168.103.151/video_analysis/video_origin/pageQuery','3')





















