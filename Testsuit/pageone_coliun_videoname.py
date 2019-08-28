#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Commonlib.commonlib import Commonlib
import requests
import unittest

class GetColumNameList(unittest.TestCase):
	def setUp(self) -> None:
		self.com = Commonlib()

def test_get_onepage_viideocolun_name(self, num):
	"""传入栏目id 可得到首页的视频名称"""
	# 3:央企  2:国资委   10:人工智能  11电子对抗   12下一代网络  13只能制造  14区块链  9其他
	all_video_list = []
	base_url = '/video_analysis/video_origin/pageQuery'
	url = self.host + base_url
	data = {'tag_ids': num}
	res = requests.post(url=url, data=data, cookies=self.com.get_cookie())
	result = res.json()
	result_detail = (result['result'])
	for i in result_detail:
		all_video_list.append(i['title'])
	print(all_video_list)
	return all_video_list

if __name__ == '__main__':
    unittest.main()