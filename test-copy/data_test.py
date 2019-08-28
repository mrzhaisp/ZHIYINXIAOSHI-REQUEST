#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time as t,random

title = "创新工场陶宁人工智能或比互联网创造更大价值.mp4"
print(title.strip('.mp4'))

# colum = random(len(['大数据','电子对抗','人工智能']))
# print(colum)
# class LoadVideo:
# 	"""上传视频"""
# 	def __init__(self):
# 		self.get_ip='http://10.168.103.151/'
# 		self.add_path = 'video_analysis/tb_video/getId'
# 		self.add_video_path ='video_analysis/tb_video_sys/add'
# 		#上传视频的主路径
# 		self.file_base_path ='C:\\Users\\Test\\ZHIYINXIAOSHI\\栏目视频\\request_loadvideo\\'
# 		self.data_get_id = {
# 				"section": "其它",
# 				"labels_source": "0",
# 				"title": "ITW António",
# 				"video_lang": "英语",
# 				"info": "test_loadviero",
# 				"labels": "",
# 				"make_time":  t.strftime("%Y-%m-%d"),
# 				"load_time":  t.strftime("%Y-%m-%d"),
# 				"tenantId": "公开",
# 		}
#
# 	def all_file_path(self):
# 		colum_videoname = []
# 		video_colum = random.choice(["大数据", "电子对抗", "人工智能"])
# 		if video_colum == '大数据':
# 			video_name = random.choice(['【BOO成功语录】影响世界经济的大数据.mp4', '1-19 yarn架构和执行流程 #慕课网 #大数据 #Spark SQL.mp4',
# 										'1-24 -Hive环境搭建 #慕课网 #大数据 #Spark SQL.mp4'])
# 		elif video_colum == '电子对抗':
# 			video_name = random.choice(['39 Countermeasure.mp4', 'Homing Weaponry - FlareCountermeasure Test.mp4',
# 										'Spill Prevention Control and Countermeasure (SPCC) Plans.mp4'])
# 		elif video_colum == '人工智能':
# 			video_name = random.choice(
# 				['Amazon SageMakers Built-in Algorithm Webinar Series Clustering with K Means.mp4',
# 				 'Mod 4 - Community Detection Algorithms (Linkage Clustering) - CSC641 - FALL-09272018.mp4'])
# 		load_video_path = self.file_base_path + video_colum + '\\' + video_name
# 		colum_videoname.append((video_colum,video_name,load_video_path))
# 		return colum_videoname
#
# 	def get_path_name(self):
# 		all_list = self.all_file_path()
# 		print(all_list[0][2])
#
# lo = LoadVideo()
# # lo.all_file_path()
# lo.get_path_name()