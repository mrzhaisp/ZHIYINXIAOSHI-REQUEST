#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Commonlib.commonlib import Commonlib
from parameterized import parameterized
import requests
import unittest
class SearchPeople(unittest.TestCase):
	"""人物库搜索人物"""
	def setUp(self) -> None:
		self.c = Commonlib()
		self.url = 'http://10.168.103.151/video_analysis/dim_people/pageQuery'
		# self.data = {'name': '张三'}

	@parameterized.expand([
		({'name': '普京'},'弗拉基米尔·弗拉基米罗维奇·普京',True),
		({'name': '张三'}, [] , False),
		({'name': '··'}, [], False),])
	def test_search_people(self,key_word,expect,is_sucess):
		res = requests.post(url=self.url, data=key_word, cookies=self.c.get_cookie())
		res_json = res.json()
		if is_sucess:
			persion_name = res_json['result'][0]['name_cn']      #弗拉基米尔·弗拉基米罗维奇·普京
			self.assertEqual(persion_name,expect)
			print('搜索到关键人物---->',persion_name)
			print('期望人物为---->',expect)
		else:
			error_result = res_json['result']
			print("输入框为空值时搜索到结果为--->",error_result)
			print('输入框为空值时期望值为--->',expect)
			self.assertEqual(error_result,expect)

if __name__ == '__main__':
	unittest.main()
