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
# @File : masterUI.py
# @Software: PyCharm

import tkinter
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

from JsonWriter import JsonWriter
import MyMethod


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
		self.line_total: int = 1

		self.list_dialog = []

		# 需要的所有图片资源
		self.list_background: list = MyMethod.GetImageNameInFile("BackgroundImage")
		self.list_background.append("")
		self.list_character: list = MyMethod.GetImageNameInFile("CharacterImage")
		self.list_character.append("")
		self.list_avatar: list = MyMethod.GetImageNameInFile("AvatarImage")
		self.list_avatar.append("")

		# 所有使用的图片的引用
		self.image_background = None
		self.image_left = None
		self.image_mid = None
		self.image_right = None
		self.image_avatar = None

		# 用于获取CheckButton的内容的容器
		self.have_avatar_var = tkinter.IntVar(value=1)

		"""初始化所有控件"""
		self.canvas_image = tkinter.Canvas(self.master, width=self.width, height=self.height)  # 背景图片

		self.label_total = ttk.Label(self.master, text="当前第{}句,总共{}句".format(self.line_now, self.line_total),
		                             font=("微软雅黑", 16))  # 统计信息

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

		# 剧情文本的内容
		self.entry_name = ttk.Entry(self.master, font=("微软雅黑", 16))  # 写人物名字的输入框
		self.text_dialog = tkinter.Text(self.master, font=("微软雅黑", 16))  # 写剧情的输入框

		self.entry_choice1 = ttk.Entry(self.master, font=("微软雅黑", 16))
		self.entry_choice2 = ttk.Entry(self.master, font=("微软雅黑", 16))

		self.button_next = ttk.Button(self.master, text="输入下一句文本", command=self.Click_Next)  # 进入下一文本的按钮
		self.button_history = ttk.Button(self.master, text="历史", command=self.HistoryWindowCreate)
		self.button_test = ttk.Button(self.master, text="TestButton", command=self.Click_Test)  # 测试按钮

		"""放在history_list窗口的控件"""
		self.button_save = ttk.Button()  # 保存按钮
		self.button_load = ttk.Button()  # 读取按钮
		self.button_read = ttk.Button()  # 跳转

		self.listbox_history_slot = tkinter.Listbox()  # 列表框
		self.scrollbar_history = ttk.Scrollbar()  # 滚动条

		self.combobox_dialog_type.set("继续对话")
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

	def LabelTotalUpdate(self):
		text = "当前第" + str(self.line_now) + "句,总共有" + str(self.line_total) + "句"
		self.label_total["text"] = text

	def Click_Save(self):
		"""
		将dialog_list存入文件中
		"""
		fp = filedialog.asksaveasfile(title="保存路径", initialdir="./", defaultextension='json',
		                              filetypes=[('json文件', 'json'), ('All Files', '*')])
		if fp:

			with open(fp.name, 'w', encoding="UTF-8") as file:
				if file:
					JsonWriter.JsonWriteWithListObj(file, self.DialogImageNameChangeToUE())
					print("Json write success!")
					file.close()

			if not fp.closed:
				fp.close()

	def Click_Load(self):
		"""
		从json文件中读取数据
		"""
		if messagebox.askokcancel("读取", "直接读取会丢失当前的文件,是否继续"):
			fp = filedialog.askopenfile(title="保存路径", initialdir="./",
			                            filetypes=[('json文件', 'json'), ('All Files', '*')])
			if fp:
				with open(fp.name, 'r', encoding='UTF-8') as file:
					if file:
						new_list = []
						temp_list_dialog = JsonWriter.JsonLoadByFile(file)
						for dialog in temp_list_dialog:
							# 将ue文件转换成普通可用文件并导入
							new_dict = JsonWriter.DialogStruct
							new_dict["Name"] = dialog["Name"]
							new_dict["DialogType"] = dialog["DialogType"]
							new_dict["B_Image"] = dialog["B_Image"][
							                      dialog["B_Image"].rfind("/") + 1:dialog["B_Image"].rfind(
								                      ".")] + ".png"
							new_dict["L_Image"] = dialog["L_Image"][
							                      dialog["L_Image"].rfind("/") + 1:dialog["L_Image"].rfind(
								                      ".")] + ".png"
							new_dict["M_Image"] = dialog["M_Image"][
							                      dialog["M_Image"].rfind("/") + 1:dialog["M_Image"].rfind(
								                      ".")] + ".png"
							new_dict["R_Image"] = dialog["R_Image"][
							                      dialog["R_Image"].rfind("/") + 1:dialog["R_Image"].rfind(
								                      ".")] + ".png"
							new_dict["A_Image"] = dialog["A_Image"][
							                      dialog["A_Image"].rfind("/") + 1:dialog["A_Image"].rfind(
								                      ".")] + ".png"
							new_dict["CharacterName"] = dialog["CharacterName"]
							new_dict["Text"] = dialog["Text"]
							new_dict["Choice"] = dialog["Choice"]
							new_list.append(dict(new_dict))
						self.list_dialog = new_list
						self.line_now = 1
						self.line_total = self.list_dialog.__len__()
						file.close()

				if not fp.closed:
					fp.close()

			self.HistoryListUpdate()

	def Click_Test(self):
		"""
		"""
		print("没有写测试内容")

	# self.line_now = self.listbox_history_slot.get(self.listbox_history_slot.curselection())[9]
	# print(self.list_dialog[int(self.line_now)])

	def Click_Next(self):
		if self.line_now == self.line_total:
			self.list_dialog.insert(self.line_now, self.Make_Dialog())
		else:
			self.list_dialog[self.line_now - 1] = self.Make_Dialog()

		self.line_now += 1
		if self.line_now > self.line_total:
			self.line_total += 1

		self.LabelTotalUpdate()
		self.HistoryListUpdate()

	def Click_Read(self):
		"""跳转文本"""
		if messagebox.askyesno("跳转", "直接跳转将会丢失当前的文本,是否继续"):
			self.line_now = self.listbox_history_slot.curselection()[0] + 1
			dialog: dict = self.list_dialog[self.line_now]

			# 类型修改
			self.combobox_dialog_type.set(dialog["DialogType"])

			# 设置combobox内的文本
			self.combobox_background_image.set("" if dialog["B_Image"] == "None"
			                                   else dialog["B_Image"])
			self.combobox_left_image.set("" if dialog["L_Image"] == "None"
			                             else dialog["L_Image"])
			self.combobox_mid_image.set("" if dialog["M_Image"] == "None"
			                            else dialog["M_Image"])
			self.combobox_right_image.set("" if dialog["R_Image"] == "None"
			                              else dialog["R_Image"])
			self.combobox_avatar_image.set("" if dialog["A_Image"] == "None"
			                               else dialog["A_Image"])

			# 文本修改
			self.entry_name.delete(0, 'end')
			self.text_dialog.delete(1.0, 'end')
			self.entry_name.insert(0, dialog["CharacterName"])
			self.text_dialog.insert(1.0, dialog["Text"])

			# 选择框修改
			self.entry_choice1.delete(0, 'end')
			self.entry_choice2.delete(0, 'end')
			if dialog["Choice"].__len__():
				self.entry_choice1.insert(0, dialog["Choice"][0])
				self.entry_choice2.insert(0, dialog["Choice"][1])

			# 修改事件手动触发
			self.LabelTotalUpdate()
			self.DialogTypeChange()
			self.B_ImageChange()
			self.L_ImageChange()
			self.M_ImageChange()
			self.R_ImageChange()
			self.A_ImageChange()

	def Make_Dialog(self):
		"""
		:rtype: dict
		:return: 返回整理完成的对话结构体
		"""
		dialog_struct = JsonWriter.DialogStruct
		dialog_struct["Name"] = self.line_now - 1
		dialog_struct["DialogType"] = self.combobox_dialog_type.get()

		dialog_struct["B_Image"] = self.GetImageName(0)
		dialog_struct["L_Image"] = self.GetImageName(1)
		dialog_struct["M_Image"] = self.GetImageName(2)
		dialog_struct["R_Image"] = self.GetImageName(3)
		dialog_struct["A_Image"] = self.GetImageName(4)

		dialog_struct["CharacterName"] = self.entry_name.get()
		dialog_struct["Text"] = self.text_dialog.get(1.0, 'end').strip()
		# todo DialogText读取出的文本最后有一个换行符,不知道有没有影响

		if self.combobox_dialog_type.get() == '选项':
			dialog_struct["Choice"] = [self.entry_choice1.get(), self.entry_choice2.get()]
		else:
			dialog_struct["Choice"] = []
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

	def DialogTypeChange(self, event=None):
		"""
		"""
		dialog_type = self.combobox_dialog_type.get()
		if dialog_type == "继续对话" or dialog_type == "":
			self.ComboboxStateSet('readonly')
			self.entry_name["state"] = "normall"
			self.ChoicePlaceForget()
		elif dialog_type == "黑屏独白" or dialog_type == "结束对话":
			self.ComboboxStateSet('disable')
			self.entry_name.delete(0, 'end')
			self.entry_name["state"] = "disable"
			self.ChoicePlaceForget()
			self.WidgetsContentClear()
			self.AllImageClear()
		else:
			self.ComboboxStateSet('readonly')
			self.entry_name["state"] = "normall"
			self.ChoicePlace()

	def B_ImageChange(self, event=None):
		"""
		:param event:
		:return:
		"""
		if self.combobox_background_image.get() != "":
			image_path = MyMethod.GetThisDir() + "\\BackgroundImage\\" + self.combobox_background_image.get()
			self.image_background = MyMethod.GetImage(image_path, self.width, self.height)
			self.canvas_image.delete("b_image")
			self.canvas_image.create_image(0, 0, anchor="nw", image=self.image_background, tag="b_image")
		else:
			self.canvas_image.delete('b_image')

	def L_ImageChange(self, event=None):
		"""
		:param event:
		:return:
		"""
		if self.combobox_left_image.get() != "":
			image_path = MyMethod.GetThisDir() + "\\CharacterImage\\" + self.combobox_left_image.get()
			self.image_left = MyMethod.GetImage(image_path, 768, 768)
			self.canvas_image.delete("l_image")
			self.canvas_image.create_image(-200, -100, anchor="nw", image=self.image_left, tag="l_image")
		else:
			self.canvas_image.delete('l_image')

	def M_ImageChange(self, event=None):
		"""
		:param event:
		:return:
		"""
		if self.combobox_mid_image.get() != "":
			image_path = MyMethod.GetThisDir() + "\\CharacterImage\\" + self.combobox_mid_image.get()
			self.image_mid = MyMethod.GetImage(image_path, 768, 768)
			self.canvas_image.delete("m_image")
			self.canvas_image.create_image(150, -100, anchor="nw", image=self.image_mid, tag="m_image")
		else:
			self.canvas_image.delete('m_image')

	def R_ImageChange(self, event=None):
		"""
		:param event:
		:return:
		"""
		if self.combobox_right_image.get() != "":
			image_path = MyMethod.GetThisDir() + "\\CharacterImage\\" + self.combobox_right_image.get()
			self.image_right = MyMethod.GetImage(image_path, 768, 768)
			self.canvas_image.delete("r_image")
			self.canvas_image.create_image(450, -100, anchor="nw", image=self.image_right, tag="r_image")
		else:
			self.canvas_image.delete('r_image')

	def A_ImageChange(self, event=None):
		"""
		:param event:
		:return:
		"""
		if self.combobox_avatar_image.get() != "":
			image_path = MyMethod.GetThisDir() + "\\AvatarImage\\" + self.combobox_avatar_image.get()
			self.image_avatar = MyMethod.GetImage(image_path, 150, 200)
			self.canvas_image.delete("a_image")
			self.canvas_image.create_image(60, 320, anchor="nw", image=self.image_avatar, tag="a_image")
		else:
			self.canvas_image.delete('a_image')

	def GetImageName(self, index: int):
		"""
		:rtype: str
		"""
		if index == 0:
			image_name = self.combobox_background_image.get()
		elif index == 1:
			image_name = self.combobox_left_image.get()
		elif index == 2:
			image_name = self.combobox_mid_image.get()
		elif index == 3:
			image_name = self.combobox_right_image.get()
		else:
			image_name = self.combobox_avatar_image.get()
		return image_name

	def HistoryWindowCreate(self):
		"""
		创建整体剧情预览窗口
		"""
		self.history_list = tkinter.Tk()
		self.history_list.title("历史预览")
		self.history_list.geometry("{0}x{1}+{2}+{3}".format(400, 600, 900, 100))

		self.button_read = ttk.Button(self.history_list, text="Read", command=self.Click_Read)
		self.button_save = ttk.Button(self.history_list, text="Save", command=self.Click_Save)  # 保存按钮
		self.button_load = ttk.Button(self.history_list, text="Load", command=self.Click_Load)  # 读取按钮

		self.listbox_history_slot = tkinter.Listbox(self.history_list)
		self.scrollbar_history = ttk.Scrollbar(self.listbox_history_slot)

		# 放置history_list窗口控件
		self.button_read.place(x=30, y=540, width=100, height=30)  # 跳转
		self.button_save.place(x=150, y=540, width=100, height=30)  # 保存按钮
		self.button_load.place(x=270, y=540, width=100, height=30)  # 读取按钮

		self.listbox_history_slot.place(x=30, y=30, width=340, height=500)  # 列表框

		self.HistoryListUpdate()

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

	def HistoryListUpdate(self):
		"""
		"""
		self.listbox_history_slot.delete(0, 'end')
		for dialog in self.list_dialog:
			self.listbox_history_slot.insert('end', self.DialogResample(dialog))

	@staticmethod
	def DialogResample(dialog):
		"""
		:param dialog:
		:rtype: str
		"""
		index = dialog["Name"] + 1
		text = dialog["Text"]
		# b_image=self.FindFileName(dialog["BackgroundImage"])
		return "Line:" + str(index) + " | Text:" + str(text)

	def DialogImageNameChangeToUE(self):
		"""
		:rtype: list
		:return: 返回重新生成的可以对应UE的json文件
		"""
		dialog_in_ue = []
		for dialog in self.list_dialog:
			dialog["B_Image"] = MyMethod.TransImageFileToUE(dialog["B_Image"], 0)
			dialog["L_Image"] = MyMethod.TransImageFileToUE(dialog["L_Image"], 1)
			dialog["M_Image"] = MyMethod.TransImageFileToUE(dialog["M_Image"], 1)
			dialog["R_Image"] = MyMethod.TransImageFileToUE(dialog["R_Image"], 1)
			dialog["A_Image"] = MyMethod.TransImageFileToUE(dialog["A_Image"], 2)
			dialog_in_ue.append(dialog)
		return dialog_in_ue


def main():
	master = tkinter.Tk()

	master.title("剧情文本编辑器")

	UIController(master, 960, 540)

	master.mainloop()


if __name__ == '__main__':
	main()
