#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: Fenghua Ye
@license: Apache Licence
@contact: wildplant@gmail.com
@site: http://www.fangworks.com
@software: PyCharm
@time: 2018-11-7 00:30
说明：
督导每周自己抽样。需要找出抽样店面的导购员照片，随EXCEL表一同发给各省市的访问员或代理

思路：
1、按省进行分组，以省为目录
2、遍历excel抽样库，找出店面ID
3. os.walk 照片文件夹，与店面ID匹配，如果相同或拷贝到新目录里去

"""

# 抽样库文件
example_file = ""
# 店面id所在列
id_col = ""
# 照片库目录
mcs_pic = ""
# 照片存放目录
save_folder = ""


