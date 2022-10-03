#  Copyright (c) 2022. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

import os

list_file = os.listdir("./")
for old_name in list_file:
	new_name = "".join(old_name.split())
	if new_name != old_name:
		os.renames(old_name, new_name)
		print("将{}改名为{}".format(old_name, new_name))

os.system("pause")
