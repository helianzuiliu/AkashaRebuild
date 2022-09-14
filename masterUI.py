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
from tkinter import Tk
from tkinter import ttk
from tkinter import filedialog

from JsonWriter import JsonWriter
import Mymethod


class UIController:
    def __init__(self, master: Tk, history_list: Tk, width, height):
        # Tk set
        self.master = master
        self.history_list = history_list

        self.master.geometry("{0}x{1}+{2}+{3}".format(width, height, 100, 100))
        self.history_list.geometry("{0}x{1}+{2}+{3}".format(400, 600, 900, 100))

        # property set
        self.line = 1
        self.list_obj = []
        self.width = width
        self.height = height
        self.im_label = Mymethod.GetImage("F:\\幻书启世录\\物料资源\\BG CG\\IMG (3).png", 960, 540)
        self.left_image = Mymethod.GetImage("F:\\幻书启世录\\物料资源\\幻书立绘\\幻书立绘\\初音立绘.png", 200, 300)

        self.have_actor_var = tkinter.StringVar(value="0")

        # master widgets set
        self.canvas_background = tkinter.Canvas(self.master, width=self.width, height=self.height)  # 背景图片

        self.label_total = ttk.Label(self.master, text="标题", font=("Adobe 宋体 Std L", 20))  # 统计信息

        self.combobox_ = ttk.Combobox(master=self.master, font="微软雅黑", state='readonly',
                                      values=["继续对话", "黑屏独白", "选项", "结束对话"])  # 这句话的类型

        self.label_left_image = ttk.Label(self.master, image=self.left_image)  # 左边的人物图片
        self.label_mid_image = ttk.Label(self.master, image=None)  # 中间的人物图片
        self.label_right_image = ttk.Label(self.master, image=None)  # 右边的人物图片

        self.combobox_left_image = ttk.Combobox(master=self.master, font=("微软雅黑", 12), state='readonly',
                                                values=Mymethod.GetImageNameInFile())
        self.combobox_mid_image = ttk.Combobox(master=self.master, font=("微软雅黑", 12), state='readonly',
                                               values=Mymethod.GetImageNameInFile())
        self.combobox_right_image = ttk.Combobox(master=self.master, font=("微软雅黑", 12), state='readonly',
                                                 values=Mymethod.GetImageNameInFile())

        self.actor_image = tkinter.Canvas(self.master, width=120, height=150)  # 人物头像框
        self.checkbutton_have_actor = ttk.Checkbutton(self.master, variable=self.have_actor_var)

        self.entry_name = ttk.Entry(self.master, font=("Adobe 宋体 Std L", 16))  # 写人物名字的输入框
        self.text_dialog = tkinter.Text(self.master, font=("Adobe 宋体 Std L", 16))  # 写剧情的输入框

        self.button_next = ttk.Button(self.master, text="输入下一句文本", command=self.Click_Next)  # 进入下一文本的按钮

        # history_list widgets set
        self.button_save = ttk.Button(self.history_list, text="Save", command=self.Click_Save)  # 保存按钮，将内容保存到json文件中
        self.button_load = ttk.Button(self.history_list, text="Load", command=self.Click_Load)  # 读取按钮
        self.button_test = ttk.Button(self.master, text="TestButton", command=self.Click_Test)  # 测试按钮

        # event bind
        self.combobox_.bind('<<ComboboxSelected>>', self.DialogTypeChange)
        self.combobox_left_image.bind('<<ComboboxSelected>>', self.ImageChange)
        self.combobox_mid_image.bind('<<ComboboxSelected>>', self.ImageChange)
        self.combobox_right_image.bind('<<ComboboxSelected>>', self.ImageChange)

        # self.checkbutton_have_actor.bind("<<>>",self.HaveActor)

        # background
        self.canvas_background.create_image(self.width / 2, self.height / 2, image=self.im_label)

        # master widgets place
        self.canvas_background.pack()
        self.label_total.place(x=355, y=30, width=240, height=40)  # 统计信息
        self.combobox_.place(x=40, y=30, width=120, height=40)  # 这句话的类型

        self.label_left_image.place(x=100, y=100, width=220, height=340)  # 左边的人物图片
        self.label_mid_image.place(x=365, y=100, width=220, height=340)  # 中间的人物图片
        self.label_right_image.place(x=630, y=100, width=220, height=340)  # 右边的人物图片

        self.combobox_left_image.place(x=100, y=70, width=120, height=30)  #
        self.combobox_mid_image.place(x=365, y=70, width=120, height=30)  #
        self.combobox_right_image.place(x=630, y=70, width=120, height=30)  #

        self.actor_image.place(x=60, y=320, width=150, height=200)  # 人物头像框
        self.entry_name.place(x=210, y=320, width=240, height=40)  # 写人物名字的输入框
        self.text_dialog.place(x=210, y=360, width=650, height=160)  # 写剧情的输入框

        # self.button_next.place(x=790, y=30, width=120, height=40)  # 进入下一文本的按钮

        # history_list widgets place
        self.button_save.place(x=0, y=0, width=10, height=10)  # 保存按钮
        # self.button_load.place(x=0, y=0, width=10, height=10)  # 读取按钮
        self.button_test.place(x=0, y=0, width=10, height=10)  # 功能测试按钮

    def Click_Save(self):
        """
        :return:
        """
        path = filedialog.asksaveasfilename(title="保存路径", initialdir="./")
        if path != "":
            with open(path, 'w', encoding="UTF-8") as file:
                JsonWriter.JsonWriteWithListObj(file, self.list_obj)
                print("Json write success!")
                file.close()
                print(123)
        # 这个函数能用，但是逻辑没有完善，容易出bug

    def Click_Load(self):
        """
        联动剧情总览列表,将读取到的数据返回到总览列表
        """

    def Click_Test(self):
        print(self.combobox_.get())

    def Click_Next(self):
        self.line += 1
        self.label_total["text"] = self.line

    def Make_Dialog(self):
        """
        :return:
        """
        dialog = JsonWriter.DialogStruct
        dialog["Name"] = self.line
        dialog["Next"] = self.combobox_.get()
        dialog["CharacterName"] = self.entry_name.get()
        # dialog["CharacterImage"]=

    def DialogTypeChange(self):
        """
        :return:
        """

    def ImageChange(self, event):
        """
        :param event:
        :return:
        """
        image_path = Mymethod.GetThisDir() + "\\image\\" + self.combobox_left_image.get()
        self.left_image["file"] = image_path
        self.label_left_image["image"] = self.left_image

    def HaveActor(self):
        """
        :return:
        """
        if self.have_actor_var.get():
            self.actor_image["state"] = "disabled"
        else:
            self.actor_image["state"] = "normal"


def main():
    master = Tk()
    history_list = Tk()

    master.title("剧情文本编辑器")
    history_list.title("历史预览")

    # master.geometry("{0}x{1}+{2}+{3}".format(960, 540, 100, 100))
    history_list.geometry("{0}x{1}+{2}+{3}".format(400, 600, 900, 100))

    UIController(master, history_list, 960, 540)

    master.mainloop()


if __name__ == '__main__':
    main()
