#  Copyright (c) 2022. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/9/1 21:00
# @Author : 赫连醉柳
# @Email : 1273103690@qq.com
# @File : QtTest.py
# @Software: PyCharm
import tkinter
from tkinter import ttk
from tkinter import filedialog

from JsonWriter import JsonWriter
import Mymethod


class UIController:
	def __init__(self, master: tkinter.Tk, width, height):
		"""
		:param master:
		"""

		""" 窗口初始化"""
		self.master = master
		self.history_list = None

		self.master.geometry("{0}x{1}+{2}+{3}".format(width, height, 100, 100))
		# self.history_list.geometry("{0}x{1}+{2}+{3}".format(400, 600, 900, 100))

		"""属性设置"""
		self.width = width
		self.height = height

		self.line_now: int = 1
		self.line_total = 1

		self.dialog_list = []

		# 需要的所有图片资源
		self.list_background: list = Mymethod.GetImageNameInFile("background")
		self.list_background.append("")
		self.list_character: list = Mymethod.GetImageNameInFile("image")
		self.list_character.append("")
		self.list_avatar: list = Mymethod.GetImageNameInFile("avatar")
		self.list_avatar.append("")

		# 所有正在使用的图片的引用
		self.image_background = None
		self.image_left = None
		self.image_mid = None
		self.image_right = None
		self.image_avatar = None

		# 用于获取CheckButton的内容的容器
		self.have_avatar_var = tkinter.IntVar(value=1)

		# 初始化所有控件
		self.canvas_image = tkinter.Canvas(self.master, width=self.width, height=self.height)  # 背景图片

		self.label_total = ttk.Label(self.master, text="标题", font=("微软雅黑", 16))  # 统计信息

		self.combobox_dialog_type = ttk.Combobox(master=self.master, font="微软雅黑", state='readonly',
		                                         values=["继续对话", "黑屏独白", "选项", "结束对话"])  # 这句话的类型

		# 是否有对话框边的图片
		self.checkbutton_have_avatar = ttk.Checkbutton(self.master, variable=self.have_avatar_var,
		                                               command=self.HaveAvatar)

		# 图片选择
		self.combobox_background_image = ttk.Combobox(master=self.master, font=("微软雅黑", 12), state='readonly',
		                                              values=self.list_background)  # 背景
		self.combobox_left_image = ttk.Combobox(master=self.master, font=("微软雅黑", 12), state='readonly',
		                                        values=self.list_character)  # 左侧人物
		self.combobox_mid_image = ttk.Combobox(master=self.master, font=("微软雅黑", 12), state='readonly',
		                                       values=self.list_character)  # 中间人物
		self.combobox_right_image = ttk.Combobox(master=self.master, font=("微软雅黑", 12), state='readonly',
		                                         values=self.list_character)  # 右侧人物
		self.combobox_avatar_image = ttk.Combobox(master=self.master, font=("微软雅黑", 10), state='readonly',
		                                          values=self.list_avatar)  # 对话框的头像

		# self.label_avatar = ttk.Label(self.master, image=self.image_avatar)

		# 剧情的文本内容
		self.entry_name = ttk.Entry(self.master, font=("微软雅黑", 16))  # 写人物名字的输入框
		self.text_dialog = tkinter.Text(self.master, font=("微软雅黑", 16))  # 写剧情的输入框\

		self.entry_choice1 = ttk.Entry(self.master, font=("微软雅黑", 16))
		self.entry_choice2 = ttk.Entry(self.master, font=("微软雅黑", 16))

		self.button_next = ttk.Button(self.master, text="输入下一句文本", command=self.Click_Next)  # 进入下一文本的按钮
		self.button_history = ttk.Button(self.master, text="历史", command=self.HistoryWindowCreate)
		"""放在history_list窗口的控件"""
		self.button_save = ttk.Button()  # 保存按钮
		self.button_load = ttk.Button()  # 读取按钮

		self.button_test = ttk.Button(self.master, text="TestButton", command=self.Click_Test)  # 测试按钮

		self.EventBind()
		self.WidgetsPlace()

	def EventBind(self):
		"""
		事件绑定
		"""
		self.combobox_dialog_type.bind('<<ComboboxSelected>>', self.DialogTypeChange)
		self.combobox_background_image.bind('<<ComboboxSelected>>', self.B_ImageChange)
		self.combobox_left_image.bind('<<ComboboxSelected>>', self.L_ImageChange)
		self.combobox_mid_image.bind('<<ComboboxSelected>>', self.M_ImageChange)
		self.combobox_right_image.bind('<<ComboboxSelected>>', self.R_ImageChange)
		self.combobox_avatar_image.bind('<<ComboboxSelected>>', self.A_ImageChange)

	def WidgetsPlace(self):
		# 背景图
		self.canvas_image.create_image(0, 0, anchor="nw", image=self.image_background)

		# 放置控件
		self.canvas_image.pack()
		self.label_total.place(x=355, y=30, width=240, height=40)  # 统计信息
		self.combobox_dialog_type.place(x=40, y=30, width=120, height=40)  # 这句话的类型
		self.combobox_background_image.place(x=200, y=30, width=120, height=40)  # 背景图

		self.combobox_left_image.place(x=100, y=70, width=120, height=30)  # 左侧人物
		self.combobox_mid_image.place(x=365, y=70, width=120, height=30)  # 中间人物
		self.combobox_right_image.place(x=630, y=70, width=120, height=30)  # 右侧人物

		self.checkbutton_have_avatar.place(x=60, y=300, width=20, height=20)  # 复选框
		self.combobox_avatar_image.place(x=80, y=300, width=130, height=20)  # 人物头像框
		# self.label_avatar.place(x=60, y=320, width=150, height=200)

		self.entry_name.place(x=210, y=320, width=240, height=40)  # 写人物名字的输入框
		self.text_dialog.place(x=210, y=360, width=650, height=160)  # 写剧情的输入框

		self.button_next.place(x=790, y=30, width=120, height=40)  # 进入下一文本的按钮
		self.button_history.place(x=630, y=320, width=100, height=40)  # 创建历史控件

		self.button_test.place(x=760, y=320, width=100, height=40)  # 功能测试按钮

	def Click_Save(self):
		"""
		todo 这个函数能用，但是逻辑没有完善，容易出bug
		:return:
		"""
		path = filedialog.asksaveasfilename(title="保存路径", initialdir="./")
		if path != "":
			with open(path, 'w', encoding="UTF-8") as file:
				JsonWriter.JsonWriteWithListObj(file, self.dialog_list)
				print("Json write success!")
				file.close()

	def Click_Load(self):
		"""
		todo 欸，才写一点呢,还不知道能不能用
		联动剧情总览列表,将读取到的数据返回到总览列表
		"""
		path = filedialog.asksaveasfilename(title="保存路径", initialdir="./")
		if path != "":
			with open(path, 'r', encoding="UTF-8") as file:
				self.dialog_list = JsonWriter.JsonLoadByFile(file)
				file.close()

	def Click_Test(self):
		for i in self.dialog_list:
			print(i)

	def Click_Next(self):
		self.line_now += 1
		if self.line_now > self.line_total:
			self.line_total += 1
		text = "当前第" + str(self.line_now) + "句,总共有" + str(self.line_total) + "句"
		self.label_total["text"] = text
		self.dialog_list.insert(self.line_now, self.Make_Dialog())

	def Make_Dialog(self):
		"""
		:rtype: dict
		:return: 返回整理完成的对话结构体
		"""
		dialog_struct = JsonWriter.DialogStruct
		dialog_struct["Name"] = self.line_now
		dialog_struct["Next"] = self.combobox_dialog_type.get()

		dialog_struct["BackgroundImage"] = self.ImageFileGet(0)
		dialog_struct["左侧人物图像"] = self.ImageFileGet(1)
		dialog_struct["中间人物图像"] = self.ImageFileGet(2)
		dialog_struct["右侧人物图像"] = self.ImageFileGet(3)
		dialog_struct["CharacterImage"] = self.ImageFileGet(4)

		dialog_struct["CharacterName"] = self.entry_name.get()
		dialog_struct["DialogText"] = self.text_dialog.get(1.0, 'end')

		if self.combobox_dialog_type.get() == '选项':
			dialog_struct["选项"] = [self.entry_choice1.get(), self.entry_choice2.get()]
		else:
			dialog_struct["选项"] = []
		return dict(dialog_struct)

	def HaveAvatar(self):
		"""
		判断是否有avatar
		有则启用combobox_avatar_image控件
		没有则禁用并删除之前有的avatar图片
		"""
		if self.have_avatar_var.get():
			print(self.have_avatar_var.get())
			self.combobox_avatar_image['state'] = "readonly"
		else:
			print(self.have_avatar_var.get())
			self.canvas_image.delete('a_image')
			self.combobox_avatar_image['state'] = "disabled"

	def DialogTypeChange(self, event):
		"""
		"""
		dialog_type = self.combobox_dialog_type.get()
		if dialog_type == "继续对话":
			self.ComboboxStateSet('readonly')
			self.ChoicePlaceForget()
		elif dialog_type == "黑屏独白" or dialog_type == "结束对话":
			self.ComboboxStateSet('disable')
			self.ChoicePlaceForget()
			self.WidgetsContentClear()
			self.AllImageClear()
		else:
			self.ComboboxStateSet('readonly')
			self.ChoicePlace()

	def B_ImageChange(self, event):
		"""
		:param event:
		:return:
		"""
		if self.combobox_background_image.get() != "":
			image_path = Mymethod.GetThisDir() + "\\background\\" + self.combobox_background_image.get()
			self.image_background = Mymethod.GetImage(image_path, self.width, self.height)
			self.canvas_image.delete("b_image")
			self.canvas_image.create_image(0, 0, anchor="nw", image=self.image_background, tag="b_image")
		else:
			self.canvas_image.delete('b_image')

	def L_ImageChange(self, event):
		"""
		:param event:
		:return:
		"""
		if self.combobox_left_image.get() != "":
			image_path = Mymethod.GetThisDir() + "\\image\\" + self.combobox_left_image.get()
			self.image_left = Mymethod.GetImage(image_path, 768, 768)
			self.canvas_image.delete("l_image")
			self.canvas_image.create_image(-200, -100, anchor="nw", image=self.image_left, tag="l_image")
		else:
			self.canvas_image.delete('l_image')

	def M_ImageChange(self, event):
		"""
		:param event:
		:return:
		"""
		if self.combobox_mid_image.get() != "":
			image_path = Mymethod.GetThisDir() + "\\image\\" + self.combobox_mid_image.get()
			self.image_mid = Mymethod.GetImage(image_path, 768, 768)
			self.canvas_image.delete("m_image")
			self.canvas_image.create_image(150, -100, anchor="nw", image=self.image_mid, tag="m_image")
		else:
			self.canvas_image.delete('m_image')

	def R_ImageChange(self, event):
		"""
		:param event:
		:return:
		"""
		if self.combobox_right_image.get() != "":
			image_path = Mymethod.GetThisDir() + "\\image\\" + self.combobox_right_image.get()
			self.image_right = Mymethod.GetImage(image_path, 768, 768)
			self.canvas_image.delete("r_image")
			self.canvas_image.create_image(450, -100, anchor="nw", image=self.image_right, tag="r_image")
		else:
			self.canvas_image.delete('r_image')

	def A_ImageChange(self, event):
		"""
		:param event:
		:return:
		"""
		if self.combobox_avatar_image.get() != "":
			image_path = Mymethod.GetThisDir() + "\\avatar\\" + self.combobox_avatar_image.get()
			self.image_avatar = Mymethod.GetImage(image_path, 150, 200)
			self.canvas_image.delete("a_image")
			self.canvas_image.create_image(60, 320, anchor="nw", image=self.image_avatar, tag="a_image")
		else:
			self.canvas_image.delete('a_image')

	def ImageFileGet(self, index: int):
		"""
		:rtype: str
		"""
		if index == 0:
			path = Mymethod.TransImageFileToUE(self.combobox_background_image.get(), 0)
		elif index == 1:
			path = Mymethod.TransImageFileToUE(self.combobox_left_image.get(), 1)
		elif index == 2:
			path = Mymethod.TransImageFileToUE(self.combobox_mid_image.get(), 1)
		elif index == 3:
			path = Mymethod.TransImageFileToUE(self.combobox_right_image.get(), 1)
		else:
			path = Mymethod.TransImageFileToUE(self.combobox_avatar_image.get(), 2)
		return path

	def HistoryWindowCreate(self):
		"""
		创建整体剧情预览窗口
		"""
		self.history_list = tkinter.Tk()
		self.history_list.title("历史预览")
		self.history_list.geometry("{0}x{1}+{2}+{3}".format(400, 600, 900, 100))

		self.button_save = ttk.Button(self.history_list, text="Save", command=self.Click_Save)  # 保存按钮
		self.button_load = ttk.Button(self.history_list, text="Load", command=self.Click_Load)  # 读取按钮
		# 放置history_list窗口控件
		self.button_save.place(x=50, y=540, width=100, height=30)  # 保存按钮
		self.button_load.place(x=250, y=540, width=100, height=30)  # 读取按钮

	def ComboboxStateSet(self, state: str):
		"""
		:param state:  修改后的状态
		"""
		self.combobox_background_image["state"] = state
		self.combobox_left_image["state"] = state
		self.combobox_mid_image["state"] = state
		self.combobox_right_image["state"] = state
		self.combobox_avatar_image["state"] = state

		self.checkbutton_have_avatar['state'] = state

	def ChoicePlace(self):
		"""
		"""
		self.entry_choice1.place(x=660, y=120, width=220, height=40)
		self.entry_choice2.place(x=660, y=180, width=220, height=40)

	def ChoicePlaceForget(self, ):
		"""
		"""
		self.entry_choice1.place_forget()
		self.entry_choice2.place_forget()

	def WidgetsContentClear(self):
		"""
		清除Combobox的内容
		"""
		self.combobox_background_image.set('')
		self.combobox_left_image.set('')
		self.combobox_mid_image.set('')
		self.combobox_right_image.set('')
		self.combobox_avatar_image.set('')

		self.entry_choice1.delete(0, 'end')
		self.entry_choice2.delete(0, 'end')

		self.entry_name.delete(0, 'end')
		self.text_dialog.delete(1.0, 'end')

	def AllImageClear(self):
		self.canvas_image.delete('b_image')
		self.canvas_image.delete('l_image')
		self.canvas_image.delete('m_image')
		self.canvas_image.delete('r_image')
		self.canvas_image.delete('a_image')


def main():
	master = tkinter.Tk()

	master.title("剧情文本编辑器")

	UIController(master, 960, 540)

	master.mainloop()


if __name__ == '__main__':
	main()
