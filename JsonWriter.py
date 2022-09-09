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
        "Next": "继续对话",
        "CharacterName": "None",
        "CharacterImage": "None",
        "DialogText": "",
        "选项": [],
        "左侧人物图像": "None",
        "中间人物图像": "None",
        "右侧人物图像": "None"
    }

    @staticmethod
    def GetFilePath():
        """
        :return: 获取文件的绝对路径
        """
        file_name: str = input(" 输入文件名字:")
        return os.path.abspath("./" + file_name + ".json")

    @staticmethod
    def JsonWriteWithSingleObj(path: str, fp):
        """
        :param fp:
        :param path:
        :return:
        """
        fp.write(json.dumps(fp, indent=4, ensure_ascii=False))

    @staticmethod
    def JsonWriteWithListObj(obj_list: list, fp):
        """
        :param obj_list:
        :param fp:
        :return:
        """
        with fp as file:
            json.dump(obj_list, file, indent=4, ensure_ascii=False)

    @staticmethod
    def JsonLoadByFile(fp):
        """
        :param fp: 输入的文件对象
        :return: 返回读取到的数据，一般为列表
        """
        with fp as file:
            return json.load(file)

    @staticmethod
    def JsonLoadByStr():
        pass
