#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests,random
import time as t

labesouces = ["大数据","机器人", "电子对抗", "人工智能","下一代网络","智能制造","区块链","其他"]

dashulu_videoname_list = ['【BOO成功语录】影响世界经济的大数据.mp4', '1-19 yarn架构和执行流程 #慕课网 #大数据 #Spark SQL.mp4',
						  '1-24 -Hive环境搭建 #慕课网 #大数据 #Spark SQL.mp4',"2-2 -Spark概述及特点 #慕课网 #大数据 #Spark SQL.mp4","2-6 -Spark对比Hadoop #慕课网 #大数据 #Spark SQL.mp4","3-2 -Spark源码编译 #慕课网 #大数据 #Spark SQL.mp4",
						  "3-5 Spark Standalone模式环境搭建 #慕课网 #大数据 #Spark SQL.mp4","4-2 -Spark SQL前世今生 #慕课网 #大数据 #Spark SQL.mp4","4-4 -Spark SQL概述 #慕课网 #大数据 #Spark SQL.mp4",
						  "5-3 -B HiveContext的使用 #慕课网 #大数据 #Spark SQL.mp4","5-4 -C SparkSession的使用 #慕课网 #大数据 #Spark SQL.mp4","5-5 spark-shell&spark-sql的使用 #慕课网 #大数据 #Spark SQL.mp4",
						  "5-6 -thriftserver&beeline的使用 #慕课网 #大数据 #Spark SQL.mp4","5-7 -jdbc方式编程访问 #慕课网 #大数据 #Spark SQL.mp4","6-1 -课程目录 #慕课网 #大数据 #Spark SQL.mp4",
						  "6-2 -DataFrame产生背景 #慕课网 #大数据 #Spark SQL.mp4","6-3 -DataFrame概述 #慕课网 #大数据 #Spark SQL.mp4",]

dianziduikang_videoname_list = ['39 Countermeasure.mp4', 'Homing Weaponry - FlareCountermeasure Test.mp4','Spill Prevention Control and Countermeasure (SPCC) Plans.mp4']

rengongzhineng_videoname_list = ['Amazon SageMakers Built-in Algorithm Webinar Series Clustering with K Means.mp4',
								 'Mod 4 - Community Detection Algorithms (Linkage Clustering) - CSC641 - FALL-09272018.mp4']

jiqiren_videoname_list = ["数字货币搬砖机器人，蚂蚁智能搬砖收益计算方法.mp4","我国自主研发出液态金属机器人，让黑科技科幻变成现实！.mp4",
						  "小学生演示机器人端水 变废为宝巧手做服饰【加油吧孩子·第6季】.mp4",
						  "元气骑士.Soul Knight版本更新预告，机器人能召唤无人机，知道怎么解锁吗.mp4","这个机器人像蜘蛛，能吐丝做建筑物.mp4"]

xiayidaiwangluo_videoname_list = ["[Hindi]  What is IP Address IPv4 Vs IPv6 Explained  .mp4","08-CCNA R&S 200-125 (Lecture 3 Part 3 IPv6) By Eng-Mahmoud AttaAlla  Arabic.mp4",
								  "17 4 2 Configure and Support IPv6 Network Settings.mp4","22 4 2 Configure and Support IPv6 Network Settings.mp4",
								  "1120244   48   CCNA #048 IPv6 initial configuration and static routing using local interface I.mp4",
								  "1120244   49   CCNA #049 IPv6 static routing using next hop IPv6 address IPv6 routing Part 2.mp4"]

zhinengzhizao_videoname_list = ["[中国新闻] 聚焦高质量发展 智能制造引领产业变革  CCTV中文国际.mp4","[中国新闻] 中国智能制造发展年度报告 2020年智能制造市场将超2200亿  CCTV中文国际.mp4",
								"《辽宁新闻》20181020大连光洋智能制造装备产业园项目年底将实现局部投产.mp4","《智能制造》中国制造2025，脑子瓦特了—新语舂碗.mp4"]

qukuailian_videoname_list = ["A Lightweight Secure Data Sharing Scheme for Mobile Cloud Computing.mp4",
							 "Deshhit Consumers trust private firms over govt firms for sharing personal data.mp4",
							 "M0195   Easy data sharing and starting a virtual clinic.mp4","MSF medical data sharing project.mp4"]

qita_videoname_list = ["Splurge x WETEMUH type beat G A N G - Prod.By Sarøz.mp4","Stage program old song  bengala gan  Indian Mad.mp4",
					   "Tania Ayu dan Siva Aprilia sex hot banget gan! duo toket besar lesbian!!!.mp4","Tạp 1 gan tang qua.mp4","The first replacable cube design GMS(GAN Magnets System).mp4",
					   "Tik tok rumantic gan.mp4","TL-GAN interface demo run 1.mp4","Todos k gan.mp4","Tonton gan seru nih.mp4",
					   "Tor name Mon chuye jaoa gan.mp4","trinath thakur gan.mp4","Tu bewafa hai go me gan gata.mp4","Tumar-name-gan-gahiya-song-by-abu rayhan kalarab- subscrabe.mp4",
					   "Unboxing GAN 356 air SM 2019 version.mp4","Upload video status WA gan.mp4","Uplod Lagi Ni Gan Jangan Lupa Like Subcribe Ya Kalau Suka Like Kalau Enggak Dislike Juga Gpp.mp4",
					   "valo lagar moto akta gan.mp4","Valo lagar mto gan(2).mp4"]

langue_list = ["中文", "英语", "日语", "俄语", "法语", "德语", "越南语", "意大利语", "丹麦语", "汉语", "韩语", "瑞典语",
			   "芬兰语", "波兰语", "荷兰语", "泰语", "阿拉伯语", "捷克语", "罗马尼亚语", "匈牙利语", "其他"]

class LoadVideo:
	"""上传视频"""
	def __init__(self):
		self.get_ip='http://10.168.103.151/'
		self.add_path = 'video_analysis/tb_video/getId'
		self.add_video_path ='video_analysis/tb_video_sys/add'
		#上传视频的主路径
		self.file_base_path ='C:\\Users\\Test\\ZHIYINXIAOSHI\\栏目视频\\request_loadvideo\\'
		self.data_get_id = {
				"section": "其它",
				"labels_source": "0",
				"title": "ITW António",
				"video_lang": "英语",
				"info": "test_loadviero",
				"labels": "",
				"make_time":  t.strftime("%Y-%m-%d"),
				"load_time":  t.strftime("%Y-%m-%d"),
				"tenantId": "公开",
		}

	def get_id(self):
		"""拿到上传视频时需要的ID"""
		base_url = self.get_ip+self.add_path
		res = requests.post(url=base_url,data=self.data_get_id)
		# print(res.json())
		return res.json()

	def all_file_path(self):
		"""随机组装视频名称，视频路径，title"""
		colum_videoname = []
		video_colum = random.choice(labesouces)
		if video_colum == '大数据':
			video_name = random.choice(dashulu_videoname_list)
		elif video_colum == '电子对抗':
			video_name = random.choice(dianziduikang_videoname_list)
		elif video_colum == '人工智能':
			video_name = random.choice(rengongzhineng_videoname_list)
		elif video_colum =='机器人':
			video_name = random.choice(jiqiren_videoname_list)
		elif video_colum == '下一代网络':
			video_name = random.choice(xiayidaiwangluo_videoname_list)
		elif video_colum == '智能制造':
			video_name = random.choice(zhinengzhizao_videoname_list)
		elif video_colum == '区块链':
			video_name = random.choice(qukuailian_videoname_list)
		elif video_colum == '其他':
			video_name = random.choice(qita_videoname_list)
		load_video_path = self.file_base_path + video_colum + '\\' + video_name
		colum_videoname.append((video_colum,video_name,load_video_path))
		return colum_videoname


	def add_video(self):
		"""拆分视频路径，title，上传视频接口"""
		#视频绝对路径一定要open

		colum_add_videoname_liat = self.all_file_path()
		section = colum_add_videoname_liat[0][0]
		# print(section)
		video_attach_file = colum_add_videoname_liat[0][1]
		# print(video_attach_file)
		video_file_path =  colum_add_videoname_liat[0][2]
		# print(video_file_path )
		title = video_attach_file.strip('.mp4')
		# print(title)
		files = {"video_attach_file":open(video_file_path ,'rb')}
		# # files = {"video_attach_file":open('C:\\Users\\Test\\ZHIYINXIAOSHI\\栏目视频\\人工智能\\2019-08-12\\创新工场陶宁人工智能或比互联网创造更大价值.mp4','rb')}
		data_add_video = {
			"video_attach_file":video_attach_file,
			"Content-Type":"video/mp4",
			"section": section,
			"labels_source": "1",
			"title": title,
			"video_lang": random.choice(langue_list),
			"info": "Test_request_load_vodeo"+title,
			"labels": "",
			"make_time": t.strftime("%Y-%m-%d"),
			"load_time": t.strftime("%Y-%m-%d"),
			"tenantId": "公开",
			"id":str(self.get_id()),
		}
		base_url = self.get_ip + self.add_video_path
		res = requests.post(url=base_url,data=data_add_video,files=files)
		content = res.json()

		try:
			if content['infoList'][0]["mainText"] == '上传成功。':
				print("上传视频成功了!!  上传视频为  %s 栏目下的    %s"%(section,video_attach_file))
		except Exception as e:
			print(e)

if __name__ == '__main__':
	l = LoadVideo()
	for i in range(1,11):
		l.add_video()
		t.sleep(2)
		print("第 %s 次上传视频"%i)





