#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import time as t
class LoadVideo:
	"""上传视频"""
	def __init__(self):
		self.get_ip='http://10.168.103.151/'
		self.add_path = 'video_analysis/tb_video/getId'
		self.add_video_path ='video_analysis/tb_video_sys/add'
		self.data_get_id = {
				"section": "其它",
				"labels_source": "0",
				"title": "ITW António",
				"video_lang": "英语",
				"info": "test_loadviero",
				"labels": "",
				"make_time": "2019-08-21",
				"load_time": "2019-08-21",
				"tenantId": "公开",
		}
		#视频绝对路径一定要open
		self.files = {"video_attach_file":open('C:\\Users\\Test\\ZHIYINXIAOSHI\\栏目视频\\人工智能\\2019-08-12\\创新工场陶宁人工智能或比互联网创造更大价值.mp4','rb')}
		self.data_add_video = {
			"video_attach_file":"创新工场陶宁人工智能或比互联网创造更大价值.mp4",
			"Content-Type":"video/mp4",
			"section": "机器人",
			"labels_source": "1",
			"title": "创新工场陶宁人工智能或比互联网创造更大价值",
			"video_lang": "英语",
			"info": "Test_request_load_vodeo",
			"labels": "",
			"make_time": t.strftime("%Y-%m-%d"),
			"load_time": t.strftime("%Y-%m-%d"),
			"tenantId": "公开",
			"id":str(self.get_id()),
		}

	def get_id(self):
		"""拿到上传视频时需要的ID"""
		base_url = self.get_ip+self.add_path
		res = requests.post(url=base_url,data=self.data_get_id)
		print(res.json())
		return res.json()

	def add_video(self):
		"""上传视频接口"""
		base_url = self.get_ip + self.add_video_path
		res = requests.post(url=base_url,data=self.data_add_video,files=self.files)
		print(res.json())

if __name__ == '__main__':
	l = LoadVideo()
	l.add_video()






