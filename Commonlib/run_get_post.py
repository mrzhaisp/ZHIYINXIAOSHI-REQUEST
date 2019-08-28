#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json


class RunMain:
	# def __init__(self, url, method, data=None):
	# 	self.reso = self.run_main(url, method, data)

	def send_get(self, url, data):
		"""封装get"""
		res = requests.get(url=url, data=data).json()
		jsondata = json.dumps(res, ensure_ascii=False, indent=2, sort_keys=True)
		return jsondata

	def send_post(self, url, data):
		"""封装post"""
		res = requests.post(url=url, data=data).json()
		jsondata = json.dumps(res, ensure_ascii=False, indent=2, sort_keys=True)
		return jsondata

	def run_main(self, url, method, data=None):
		# 添加判断方法，传入url，请求方式，数据
		res = None
		if method == "post":
			res = self.send_post(url, data)
		else:
			res = self.send_get(url, data)
		return eval(res)


if __name__ == '__main__':
	host = "http://10.168.103.151"
	url_path = "/video_analysis/login"
	url = host + url_path
	data = {
		"code": "admin1",
		"pwd": "418FE8C4A00CB0CFA1909D659CB7A406D03EA0AC9DA98CDA0F9C57A157083765291ED5275B742A48D4DA123AB9CE3C9A6D53627830DBB7EE5F1750A497BACE99"
	}
	# r = RunMain(url, "post", data).reso
	# print(r)
	r = RunMain()
	response = r.run_main(url, "post", data)
	print(response["errorList"][0]["mainText"])


