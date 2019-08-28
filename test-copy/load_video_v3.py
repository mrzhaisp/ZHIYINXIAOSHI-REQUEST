#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests,random,os
import time as t

labesouces = ["大数据","机器人", "电子对抗", "人工智能","下一代网络","智能制造","区块链","其它","历史","维稳","人物","反恐"]

langue_list = ["中文", "英语", "日语", "俄语", "法语", "德语", "越南语", "意大利语", "丹麦语", "汉语", "韩语", "瑞典语", "芬兰语",
			   "波兰语", "荷兰语", "泰语", "阿拉伯语", "捷克语", "罗马尼亚语", "匈牙利语", "其他"]

def get_all_videoname(videofilepath):
	"""拿到所有文件夹下的视频名称组成列表"""
	video_name_list=os.listdir(videofilepath)
	return video_name_list

class LoadVideo:
	"""通过接口上传视频"""
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
			video_name = random.choice(get_all_videoname(self.file_base_path + "\\大数据\\"))
		elif video_colum == '电子对抗':
			video_name = random.choice(get_all_videoname(self.file_base_path + "\\电子对抗\\"))
		elif video_colum == '人工智能':
			video_name = random.choice(get_all_videoname(self.file_base_path + "\\人工智能\\"))
		elif video_colum =='机器人':
			video_name = random.choice(get_all_videoname(self.file_base_path + "\\机器人\\"))
		elif video_colum == '下一代网络':
			video_name = random.choice(get_all_videoname(self.file_base_path + "\\下一代网络\\"))
		elif video_colum == '智能制造':
			video_name = random.choice(get_all_videoname(self.file_base_path + "\\智能制造\\"))
		elif video_colum == '区块链':
			video_name = random.choice(get_all_videoname(self.file_base_path + "\\区块链\\"))
		elif video_colum == '其它':
			video_name = random.choice(get_all_videoname(self.file_base_path + "\\其它\\"))
		elif video_colum == '反恐':
			video_name = random.choice(get_all_videoname(self.file_base_path + "\\反恐\\"))
		elif video_colum == '人物':
			video_name = random.choice(get_all_videoname(self.file_base_path + "\\人物\\"))
		elif video_colum == '维稳':
			video_name = random.choice(get_all_videoname(self.file_base_path + "\\维稳\\"))
		elif video_colum == '历史':
			video_name = random.choice(get_all_videoname(self.file_base_path + "\\历史\\"))
		load_video_path = self.file_base_path + video_colum + '\\' + video_name
		colum_videoname.append((video_colum,video_name,load_video_path))
		return colum_videoname

	def add_video(self,cookie):
		"""拆分视频路径，title，上传视频接口"""
		#视频绝对路径一定要open
		try:
			colum_add_videoname_liat = self.all_file_path()
			section = colum_add_videoname_liat[0][0]
			print("栏目Wie  ",section)
			video_attach_file = colum_add_videoname_liat[0][1]
			print(video_attach_file)
			video_file_path =  colum_add_videoname_liat[0][2]
			print("视频为  ",video_file_path )
			title = video_attach_file.strip('.mp4')
			files = {"video_attach_file":open(video_file_path ,'rb')}
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
			res = requests.post(url=base_url,data=data_add_video,files=files,cookies=cookie)
			content = res.json()
			# print(content)
			if content['infoList'][0]["mainText"] == '上传成功。':
				print("上传视频成功了!!  上传视频为  %s 栏目下的    %s"%(section,video_attach_file))
			else:
				print("完犊子，肯定有视频被删了，找不到对应路径下的视频")
		except Exception as e:
			print(e)

# if __name__ == '__main__':
# 	l = LoadVideo()
# 	l.add_video()
# 	# #运行一次上传10个视频
# 	# for i in range(1,11):
# 	# 	l.add_video()
# 	# 	t.sleep(2)
# 	# 	print("第 %s 次上传视频"%i)

