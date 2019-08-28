#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Commonlib.commonlib import Commonlib
from parameterized import parameterized,param
import unittest
def bulid_data():
	return [
		("{'search_keywords': '《直播港澳台》他是法国总统马克龙身后的中国通 曾拿书给习近平签名'}",True)
	]

class SerachKeywords(unittest.TestCase):
	def setUp(self) -> None:
		self.c = Commonlib()

	def tearDown(self) -> None:
		pass

	#输入关键词搜到结果
	# @parameterized.expand(bulid_data)
	def search_video(self):
		if True:
			video_list = self.c.get_info_forvideo({'search_keywords': '《直播港澳台》他是法国总统马克龙身后的中国通 曾拿书给习近平签名'})
			print(video_list)  #----   ['《直播港澳台》他是法国总统马克龙身后的中国通 曾拿书给习近平签名', '外交']
			return video_list
if __name__ == '__main__':
	unittest.main()
	# s = SerachKeywords()
	s.search_video()

















