# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/9/1 21:00
# @Author : 赫连醉柳
# @Email : 1273103690@qq.com
# @File : QtTest.py
# @Software: PyCharm

import tkinter
from tkinter import Label

from JsonTest import JsonWriter


class MyUI:
    def __init__(self, init_windows_name: tkinter.Tk, wight, high, x_offset, y_offset):
        self.init_windows_name = init_windows_name
        self.wight = wight
        self.high = high
        self.x_offset = x_offset
        self.y_offset = y_offset
        pass

    def set_windows_attribute(self):
        """
		设置窗口属性
		"""
        self.init_windows_name.title("剧情文本生成工具")
        self.init_windows_name.geometry(
            "{0}x{1}+{2}+{3}".format(str(self.wight), str(self.high), str(self.x_offset), str(self.y_offset)))

        self.init_windows_name.attributes("-alpha", 0.8)  # 窗口背景透明度


def Button_Click(label: Label):
    print(123)


def DataOutput(obj_list):
    with open(JsonWriter.GetFilePath(), 'w', encoding="UTF-8") as file:
        JsonWriter.JsonWriteWithListObj(obj_list, file)


def main():
    init_window = tkinter.Tk()

    ui = MyUI(init_window, 800, 600, 100, 100)
    ui.set_windows_attribute()

    label: Label = tkinter.Label(init_window, text="123")
    label.pack()

    button = tkinter.Button(init_window, text="Button1", width=15, height=2, command=Button_Click(label))
    button.pack()

    init_window.mainloop()


if __name__ == '__main__':
    main()
