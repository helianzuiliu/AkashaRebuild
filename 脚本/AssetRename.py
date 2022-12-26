#  Copyright (c) 2022. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.


import unreal

sys_lib = unreal.SystemLibrary()
editor_lib = unreal.EditorUtilityLibrary()
string_lib = unreal.StringLibrary()


def AssetsRename():
	"""
	获得编辑器中选中的资产
	"""
	selected_assets = editor_lib.get_selected_assets()
	assets_len = len(selected_assets)
	unreal.log("选择了{}个资产".format(assets_len))
	for asset in selected_assets:
		name_index = asset.get_name()[-2:]
		new_name = "T_BGImage_{}".format(name_index)
		editor_lib.rename_asset(asset, new_name)


AssetsRename()
