#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
class ReadJson:
	"""从json中读取请求数据"""
	def __init__(self,file_path=None):
		if file_path:
			self.file_path = file_path
		else:
			self.file_path="../Data/login_data.json"
		self.data = self.read_data()

	def read_data(self):
		"""拿到数据"""
		with open(self.file_path) as fp:
			data = json.load(fp)
			return data

	def get_data(self,id):
		"""根据关键字获取数据"""
		return self.data[id]

if __name__ == '__main__':
	r = ReadJson("../Data/login_data2.json")
    # r = ReadJson()
	#根据json的 key拿到  value值
    datakey = r.get_data("buy")
    print(datakey)