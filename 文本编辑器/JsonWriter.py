#  Copyright (c) 2022. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/8/29 22:55
# @Author : 赫连醉柳
# @Email : 1273103690@qq.com
# @File : JsonWriter.py
# @Software: PyCharm

import json
import os.path


class JsonWriter:
	DialogStruct: dict = {
		"Name": 0,
		"DialogType": "继续对话",
		"B_Image": "None",
		"L_Image": "None",
		"M_Image": "None",
		"R_Image": "None",
		"A_Image": "None",
		"CharacterName": "None",
		"Text": "",
		"Choice": []
	}

	@staticmethod
	def GetFilePath(file_name: str):
		"""
		:return: 获取当前目录的绝对路径
		"""
		return os.path.abspath("./" + file_name + ".json")

	@staticmethod
	def JsonWriteWithSingleObj(fp, obj):
		"""
		:param fp:
		:param obj:
		"""
		fp.write(json.dumps(obj, indent=4, ensure_ascii=False))

	@staticmethod
	def JsonWriteWithListObj(fp, obj_list: list):
		"""
		:param fp:
		:param obj_list:
		"""
		with fp as file:
			json.dump(obj_list, file, indent=4, ensure_ascii=False)

	@staticmethod
	def JsonLoadByFile(fp):
		"""
		:param fp: 输入的文件对象
		:return: 返回读取到的数据，一般为列表
		:rtype: list
		"""
		return json.load(fp)

	@staticmethod
	def JsonLoadByStr(obj):
		"""
		:param obj:
		:return:
		:rtype: str
		"""
		# 这边没看懂出什么问题了,暂时不能用
		if type(obj) is str:
			return json.loads(obj)
		else:
			print("Error,the object is not str type!")
