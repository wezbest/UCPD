#!/usr/bin/env python3.12
''''
This for testng the rich python library 
https://github.com/Textualize/rich
'''

from rich import print as rprint

nums_list = [1, 2, 3, 4]
rprint(nums_list)

nums_tuple = (1, 2, 3, 4)
rprint(nums_tuple)

nums_dict = {'nums_list': nums_list, 'nums_tuple': nums_tuple}
rprint(nums_dict)

bool_list = [True, False]
rprint(f' bastard see {bool_list}')
