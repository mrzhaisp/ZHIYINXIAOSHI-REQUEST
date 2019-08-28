#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coding:utf-8
import unittest
import time
class Test(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		print( "--------start!")
	@classmethod
	def tearDownClass(cls):
		time.sleep(1)
		print ("---------end!")
	def test01(self):
		print ("执行测试用例 01")
	def test03(self):
		print ("执行测试用例 03")
	def test02(self):
		print ("执行测试用例 02")


if __name__ == "__main__":
	unittest.main()









