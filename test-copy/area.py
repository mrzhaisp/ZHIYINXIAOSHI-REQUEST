#!/usr/bin/env python
# -*- coding: utf-8 -*-

# class  Home:
# 	def __init__(self,area):
# 		self.area = area   #默认面积
# 		self.containsItem = []
#
# 	def __str__(self):
# 		msg = '当前可以用面积为' + str(self.area)
# 		if len(self.containsItem) >0:
# 			msg = msg + '容纳物品有：'
# 			for tmp in self.containsItem:
# 				msg = msg + tmp +t

# class Car:
# 	def __init__(self,color,num):
# 		self.color = color
# 		self.wheel = num
#
# 	def __str__(self):
# 		msg = '我的颜色是' + self.color + '我有' + self.wheel + '轮胎'
# 		return msg
#
# 	def move(self):
# 		print("跑起来")
#
#
# bmw = Car('reds',8)
# print(bmw)
# # print(bmw.color)
# # print(bmw.wheel)

#
# import time
#
# class Animal(object):
#
# 	def __init__(self,name):
# 		print('__init__方法调用')
# 		self.__name = name
#
# 	def __del__(self):
# 		print("__del__方法调用")
# 		print("%s对象被干掉" %self.__name)
#
# # dog = Animal("哈皮狗")
# # del dog
#
# cat = Animal("波斯猫")
# cat2 = cat
# cat3 = cat
# print("删除cat2")
# del cat2
#
# print("删除cat3")
# del cat3


class Animal(object):
	def __init__(self,name='动物',color='白色'):
		self.__name = name
		self.color = color

	def __test(self):
		print(self.__name)
		print(self.color)

	def test(self):
		print(self.__name)
		print(self.color)

class Dog(Animal):
	def dogTest1(self):
		print(self.__name)
		print(self.color)

	def dogTest2(self):
		self.test()

A = Animal()
print(A.color)
A.test()
# 	def run(self):
# 		print('%s--再跑' %self.__name)
#
# class Bosi(Cat):
# 	def setNewName(self,newName):
# 		self.name = newName
#
# 	def eat(self):
# 		print("%s在吃"%self.name)


