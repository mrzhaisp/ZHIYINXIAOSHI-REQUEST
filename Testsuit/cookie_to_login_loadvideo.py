#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Testsuit.load_video_filter import LoadVideo
from Commonlib.mysql_clinet import MysqlClinet
from Commonlib.commonlib import Commonlib
import unittest
import requests,time as t

class TestLoadvideo(unittest.TestCase):
	"""登录一次 获取cookie，拿着cookie去"""

	@classmethod
	def setUpClass(cls) -> None:
		cls.c = Commonlib()
		cls.load_video_fun = LoadVideo()
		cls.db_cli = MysqlClinet()
		cls.c.solv_log_waring()
		cls.host = "http://10.168.103.151"
		cls.base_url = "/video_analysis/login"
		cls.url = cls.host + cls.base_url
		cls.data = {
			"code": "admin",
			"pwd": "418FE8C4A00CB0CFA1909D659CB7A406D03EA0AC9DA98CDA0F9C57A157083765291ED5275B742A48D4DA123AB9CE3C9A6D53627830DBB7EE5F1750A497BACE99"
		}
		r = requests.post(url=cls.url, data=cls.data)
		cls.cookie = r.cookies.get_dict()
		print("---------------登录系统成功，准备随机上传视频---------------")

	@classmethod
	def tearDownClass(cls) -> None:
		"""退出系统"""
		cls.path = "/video_analysis/exit"
		cls.log_out_path = cls.host+cls.path
		requests.get(cls.log_out_path)
		print("---------------上传所有的视频完毕，退出系统---------------")

	def test01(self):
		print("""*************执行测试0001*************""")
		for i in range(1):
			self.load_video_fun.add_video(self.cookie)
			t.sleep(1)

	def test02(self):
		print("*************执行测试0002*************")

if __name__ == '__main__':
    unittest.main()