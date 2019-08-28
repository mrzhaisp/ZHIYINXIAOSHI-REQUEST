#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
class BuildDate:
	def __init__(self,file_path=None):
		if file_path == None:
			self.file_path = '../Data/search_video.json'
		else:
			self.file_path = file_path

		self.data = self.read_json()

	def read_json(self):
		"""拿到所有的数据"""
		with open (self.file_path,encoding="utf-8") as f:
			data = json.load(f)
		return data

	def get_value(self,one=None,two=None,sec=None):
		resultlist = []
		for obj in self.data.values():
			resultlist.append((obj.get(one), obj.get(two), obj.get(sec)))
		# print(resultlist)
		return resultlist


# b = BuildDate()
# b.get_value("keywords","expect","is_sucess")




































