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


class UIController:
    def __init__(self, master):
        # property set
        self.master = master
        self.is_open_file = False

        # widgets set
        self.label_total = ttk.Label(self.master, text="标题", font=("微软雅黑", 20))  # 统计信息
        self.left_image = ttk.Label(self.master, image=None)  # 左边的人物图片
        self.mid_image = ttk.Label(self.master, image=None)  # 中间的人物图片
        self.right_image = ttk.Label(self.master, image=None)  # 右边的人物图片
        self.label_Name = ttk.Entry(self.master)  # 人物的名字
        self.button_Next = ttk.Button(self.master, text="输入下一句文本")  # 进入下一文本的按钮
        self.button_Save = ttk.Button(self.master, text="保存", command=self.Click_Save)  # 保存按钮，将内容保存到json文件中
        # 写出左中右三个图片，一个写名字的输入框，一个头像框，和一个写剧情的输入框，一个标记当前文本行数和总计文本行数的文本框，还有保存按钮绑定json文件路径，一个

        # widgets place
        self.label_total.grid()
        self.left_image.grid()
        self.mid_image.grid()
        self.right_image.grid()
        self.button_Next.grid()
        self.button_Save.grid()

    def Click_Save(self):
        print(filedialog.askopenfile(title="保存路径", initialdir="./"))



def DataOutput(obj_list):
    with open(JsonWriter.GetFilePath(), 'w', encoding="UTF-8") as file:
        JsonWriter.JsonWriteWithListObj(obj_list, file)


def main():
    master = tkinter.Tk()

    master.title("剧情文本编辑器")
    master.geometry("800x600+100+100")

    UIController(master)

    master.mainloop()


if __name__ == '__main__':
    main()
