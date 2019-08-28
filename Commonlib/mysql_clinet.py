#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymysql

class MysqlClinet:
	def __init__(self):
		#创建连接
		self.db = pymysql.connect(host="10.168.103.64",	port = 3306 ,database = "videodb151",user = "root",	passwd = "root",charset = "utf8")
		#创建游标
		self.cur = self.db.cursor()

	def select_data(self,title):
		"""接受视频名称，如果该视频名称在b_video_origin 里查询出来数据，则说明该视频已经进入待审核入库环节"""
		try:
			# sql = "SELECT size FROM  tb_video_origin where size=0 ORDER BY load_time desc "
			title_value = [title]
			sql = "SELECT * FROM  video_origin where title =  %s"
			count_result = self.cur.execute(sql,title_value)
			result = self.cur.fetchall()
			if result:
				print("视频 %s  已经进入待审核入库环节"%title)
			else:
				print("视频 %s  算法还未处理完成"%title)
		except Exception as e:
			print(e)
		finally:
			self.cur.close()
			self.db.close()


	def  titles_list(self):
		"""接受视频名称，如果该视频名称在b_video_origin 里查询出来数据，则说明该视频已经进入待审核入库环节"""
		title_list = []
		try:
			# sql = "SELECT size FROM  tb_video_origin where size=0 ORDER BY load_time desc "
			sql = "SELECT  title FROM `tb_video_origin`;"
			count_result = self.cur.execute(sql)
			result = self.cur.fetchall()
			for titles  in result:
				all_title = ''.join(titles)
				title_list.append(all_title)
		except Exception as e:
			print(e)
		return title_list


if __name__ == '__main__':
	m = MysqlClinet()
	m.titles_list()


