#  Copyright (c) 2022. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

import unreal

engine_path = "/Game/PythonImportAsset"


def BuildImportTask(file_name, destination_path):
	"""
	创建导入任务，设置导入的属性

	:param file_name: 导入的文件的路径
	:param destination_path: 保存在UE编辑器下的路径
	:return: 任务对象，负责实现操作
	"""
	task = unreal.AssetImportTask()
	task.set_editor_property("automated", True)  # 是否自动，是则不显示对话框
	task.set_editor_property("destination_name", "")  # 目标名字
	task.set_editor_property("destination_path", destination_path)  # 目标路径
	# task.set_editor_property("factory", )  #工厂，看不懂是什么东西
	task.set_editor_property("filename", file_name)  # 导入文件的路径
	# task.set_editor_property("imported_object_paths", )
	# task.set_editor_property("options", )
	task.set_editor_property("replace_existing", True)  # 是否覆盖已存在的资产
	task.set_editor_property("save", True)  # 是否保存
	
	# task.get_editor_property("result", ) # 获得导入后的对象Object
	
	return task


def ImportTaskExecute(tasks):
	"""
	执行资产导入任务并并将结果打印

	:param tasks: 导入资产任务列表
	"""
	unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks(tasks)
	for task in tasks:
		print(task)


def ImportAsset(paths):
	"""
	导入资产的主函数

	:return:
	"""
	import_asset_task = []
	for file_path in paths:
		import_asset_task.append(BuildImportTask(file_path, engine_path))
	
	ImportTaskExecute(import_asset_task)


def main():
	""""""


if __name__ == '__main__':
	main()
