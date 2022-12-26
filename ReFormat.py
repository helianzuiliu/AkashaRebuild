#  coding:UTF-8
#  Copyright (c) 2022. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

import argparse
import ffmpy
import os

file_path = r"F:\幻书启世录\使用的资源\BGM"  # 输入文件路径
ffmpeg_path = r"D:\MyTools\ffmpeg\bin\ffmpeg.exe"  # ffmpeg的安装位置

parser = argparse.ArgumentParser(description="参数列表说明")
parser.add_argument('-input_format', '-i', help='导出的文件格式', required=True)
parser.add_argument('-output_format', '-o', help='导出的文件格式', required=True)
args = parser.parse_args()


def GetDirFiles() -> list:
	"""
	获得当前文件夹下的所有文件索引

	:return: 以列表形式返回文件索引
	"""
	task_list = []
	file_names = os.listdir(file_path)
	for target_file_name in file_names:
		if target_file_name[target_file_name.rfind(".") + 1:] == args.input_format:
			temp_file_name = target_file_name[:target_file_name.rfind(".") + 1]
			new_file_name = temp_file_name + args.output_format
			task_list.append((target_file_name, new_file_name))
	return task_list


def ffmpeg_Run(task):
	"""

	:param task:
	:return:
	"""
	
	print("输入的文件路径是:", task[0])
	print("输出的文件路径是:", task[1])
	
	input_file = file_path + "\\" + task[0]
	output_file = file_path + "\\OUT\\" + task[1]
	
	ff = ffmpy.FFmpeg(
		executable=ffmpeg_path,
		inputs={input_file: None},
		outputs={output_file: None}
	)
	
	print(ff)
	ff.run()
	pass


def main():
	task_names = GetDirFiles()
	for i in task_names:
		print(i[0] + " 转换成 " + i[1])
	print("是否确定? Y/N")
	a = input()
	if a == "Y" or a == "y":
		for file_name in task_names:
			ffmpeg_Run(file_name)
	
	os.system("pause")


if __name__ == '__main__':
	main()
