#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import warnings

class Commonlib:
	def __init__(self):
		self.host = "http://10.168.103.151"
		self.base_url = "/video_analysis/login"
		self.url = self.host + self.base_url
		self.data = {
			"code": "admin",
			"pwd": "418FE8C4A00CB0CFA1909D659CB7A406D03EA0AC9DA98CDA0F9C57A157083765291ED5275B742A48D4DA123AB9CE3C9A6D53627830DBB7EE5F1750A497BACE99"
		}

	def solv_log_waring(self):
		"""输出日志后未关闭文件，报异常，只需要在此类初始化的时候调用该方法"""
		warnings.simplefilter("ignore", ResourceWarning)

	def get_cookie(self):
		"""拿到cookie"""
		r = requests.post(url=self.url, data=self.data)
		cookie = r.cookies.get_dict()
		print(cookie)
		return cookie

	def get_info_forvideo(self, type_content):
		"""传入栏目 类型，拿到首页的视频名称"""
		video_name_list = []
		# 这个接口传一个data 值为tag_ids，就可以切换个个栏目  央企(3),国资委(2)
		# 人工智呢(10), 电子对抗(11),下一代网络(12),只能制造(13),区块链(14),其他(9)
		url = 'http://10.168.103.151/video_analysis/video_origin/pageQuery'
		# data = {'tag_ids': type_content}
		data = type_content
		r = requests.post(url=url, data=data, cookies=self.get_cookie())
		# 拿到一个栏目下的所有信息
		content = r.json()
		result = content['result']
		for dic in result:
			# video_name_list.append(dic['id'])
			video_name_list.append(dic['title'])
		# video_name_list.append(dic['load_time'])
		# video_name_list.append(dic['section'])
		# print('工具类中打印的结果--     ',video_name_list)
		print(video_name_list)
		return video_name_list



if __name__ == '__main__':
	# c =Commonlib()
	# for i in (2,3,10,11,12,13,14,9):
	# 	c.get_info_forvideo({'tag_ids': i})
	# c = Commonlib()
	# c.get_info_forvideo({'search_keywords': '普京'})
	# c.get_info_forvideo({'search_keywords': '特雷莎·梅'})
	# c.get_onepage_viideocolun_name("2")
	c = Commonlib()
	c.get_cookie()