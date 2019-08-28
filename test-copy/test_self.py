#!/usr/bin/env python
# -*- coding: utf-8 -*-

class SweetPotato:
	'''烤地瓜'''
	def __init__(self):
		self.cookedLevel = 0
		self.cookedString = '生的'   #状态
		self.condiments = []  #调料

	#定制print内容
	def __str__(self):
		msg = self.cookedString + '地瓜'
		if len(self.condiments)>0:
			msg = msg + '('
			for tmp in self.condiments:
				msg = msg + tmp + ','
			msg = msg.strip(',')
			msg = msg + ')'
		return msg

	#添加调料
	def addCondiments(self,condiments):
		self.condiments.append(condiments)

	def cook(self,time):
		self.cookedLevel += time
		if self.cookedLevel>8:
			self.cookedString='成灰'
		elif self.cookedLevel >5:
			self.cookedString='考好了'
		elif self.cookedLevel>3:
			self.cookedString='不熟'
		else:
			self.cookedString='生的'

s = SweetPotato()
print('还没开始烤地瓜')
print(s.cookedLevel)
print(s.cookedString)
print(s.condiments)
print("考了四分钟")
s.cook(4)
print(s)







