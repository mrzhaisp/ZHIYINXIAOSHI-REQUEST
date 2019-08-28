#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Commonlib.run_get_post import RunMain
import HTMLTestRunnerNew
import unittest

class TestMethod(unittest.TestCase):
	"""登录接口测试"""
	def setUp(self) -> None:
		self.req = RunMain()
		# self.host = "http://10.168.103.151"
		# self.url_path = "/video_analysis/login"
		# self.url = self.host + self.url_path
		# self.data = {
		# 	"code": "admin",
		# 	"pwd": "418FE8C4A00CB0CFA1909D659CB7A406D03EA0AC9DA98CDA0F9C57A157083765291ED5275B742A48D4DA123AB9CE3C9A6D53627830DBB7EE5F1750A497BACE99"
		#
		self.host = "http://10.168.103.151"
		self.url_path = "/video_analysis/login"
		self.url =self.host + self.url_path

	def tearDown(self) -> None:
		pass

	def test_001(self):

		data = {
			"code": "admin",
			"pwd": "418FE8C4A00CB0CFA1909D659CB7A406D03EA0AC9DA98CDA0F9C57A157083765291ED5275B742A48D4DA123AB9CE3C9A6D53627830DBB7EE5F1750A497BACE99"
		}
		responseone = self.req.run_main(self.url, "post", data)
		# print(responseone["infoList"][0]["mainText"])
		self.assertEqual(responseone["infoList"][0]["mainText"],"登录成功。")
		#全局变量
		# print("这是第一个用例")
		# globals()['userid']='100086'

	def test_002(self):
		# print(userid)
		# host = "http://10.168.103.151"
		# url_path = "/video_analysis/login"
		# url = host + url_path
		data = {
			"code": "admin111",
			"pwd": "418FE8C4A00CB0CFA1909D659CB7A406D03EA0AC9DA98CDA0F9C57A157083765291ED5275B742A48D4DA123AB9CE3C9A6D53627830DBB7EE5F1750A497BACE99"
		}
		response = self.req.run_main(self.url, "post", data)
		# print(response["errorList"][0]["mainText"])
		print("这是第二个用例")
		self.assertEqual(response["errorList"][0]["mainText"],"登录失败!")

if __name__ == '__main__':
	unittest.main()