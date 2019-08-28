#!/usr/bin/env python
# -*- coding: utf-8 -*-
# class Car(object):
# 	def move(self):
# 		print("车再跑")
#
# 	def stop(self):
# 		print('停车')
#
# class CarStore(object):
# 	def order(self):
# 		self.car = Car()
# 		self.car.move()
# 		self.car.stop()
# c = CarStore()
# c.order()
#伊兰特车型
class YiLanTeCar(object):
	def move(self):
		print("车在跑")
	def stop(self):
		print("车在跑")

#索纳塔车型
class SuoNaTa(object):
	def move(self):
		print("车在跑")

	def stop(self):
		print("车在跑")

#店面
# class CarStore(object):
# 	def order(self,typeName ):
# 		if typeName == "伊兰特":
# 			car = YiLanTeCar()
# 		elif typeName  == '索纳塔':
# 			car = SuoNaTa()
# 		return car
#生成对象
class CarFactory():
	def create_car(self,typeName ):
		if typeName == "伊兰特":
			car = YiLanTeCar()
		elif typeName  == '索纳塔':
			car = SuoNaTa()
		return car


#基本的4s店
class CarStore():
	def __init__(self):
		self.carFactory = CarFactory()

	def order(self):
		car = self.carFactory.create_car(typeName)
		return car