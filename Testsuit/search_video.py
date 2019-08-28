#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Commonlib.commonlib import Commonlib
from parameterized import parameterized, param
import unittest

def bulid_data():
	return [
		({'search_keywords': '《直播港澳台》他是法国总统马克龙身后的中国通 曾拿书给习近平签名'}, "['《直播港澳台》他是法国总统马克龙身后的中国通 曾拿书给习近平签名']", True),
		({'search_keywords': '张三'}, "[]", False),
		({'search_keywords': '···'}, "[]", False)
	]

class SearchKeyWords(unittest.TestCase):
	"""搜索框输入正确关键词，无效关键词，特殊符号"""
	def setUp(self) -> None:
		self.c = Commonlib()

	# @parameterized.expand(
	# 	[
	# 		( {'search_keywords': '《直播港澳台》他是法国总统马克龙身后的中国通 曾拿书给习近平签名'}, "['《直播港澳台》他是法国总统马克龙身后的中国通 曾拿书给习近平签名']",True),
	# 		({'search_keywords': '张三'}, "[]",False),
	# 		({'search_keywords': '···'}, "[]",False)
	# 	]
	# 					)
	@parameterized.expand(bulid_data)
	def test_get_video_name_sucess(self, type_content, expect, is_sucess):
		if is_sucess:
			name_list = self.c.get_info_forvideo(type_content)
			print('搜索到视频---->', name_list)
			self.assertEqual(name_list, ['《直播港澳台》他是法国总统马克龙身后的中国通 曾拿书给习近平签名'])
		else:
			print('this is expect----->', expect)
			self.assertEqual(expect, '[]')

if __name__ == '__main__':
	unittest.main()

