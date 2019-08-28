#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xlrd
# class ReadExcel:
# 	def __init__(self,file_path=None,sheet_id=None):
# 		if file_path:
# 			self.file_path= file_path
# 			self.sheet_id = sheet_id
# 		else:
# 			self.file_path="../Data/interface.xlsx"
# 			self.sehht_id = 0
# 		self.data = self.get_data()
#
# 	def get_data(self):
# 		#拿到数据
# 		data = xlrd.open_workbook(self.file_path)
# 		tables = data.sheets()[self.sheet_id] #拿到sheet名称
# 		print(tables.nrows)  #总行数
# 		return tables
#
# if __name__ == '__main__':
# 	r = ReadExcel()
# 	r.get_data()



# file_path="../Data/interface.xlsx"
# sheet_id = 0
# data = xlrd.open_workbook(file_path)
#
# sheet_all = data.sheets()[sheet_id]  #拿到第一个sheet
# print(sheet_all.nrows)  #所有的行数
# print(sheet_all.cell_value(2,3))

class ReadExcel:
	def __init__(self,file_path=None,sheet_id=None):
		if file_path:
			self.file_path = file_path
			self.sheet_id = sheet_id
		else:
			self.file_path = "../Data/interface.xlsx"
			self.sheet_id = 0
		self.data = self.get_data()

	def get_data(self):
		"""拿到所有sheee的内容"""
		data = xlrd.open_workbook(self.file_path)
		sheet_all = data.sheets()[self.sheet_id]  # 拿到第一个sheet
		# print(sheet_all.cell_value(2,3))  #拿到sheet下的 具体坐标的数值
		return sheet_all  #拿到所有的数据

	def get_lines(self):
		"""拿到所有的行数"""
		tables = self.data
		return tables.nrows

	def get_cell_value(self,row,col):
		"""获取单元格内容"""
		return self.data.cell_value(row,col)

if __name__ == '__main__':
    r  = ReadExcel()
    # r.get_data(file_path,sheet_id)
    # print(r.get_data().cell_value(2,3))
    print(r.get_lines())
    print(r.get_cell_value(2,3))















