# -*- coding: utf-8 -*-
# @ProjectName：Python_InterfaceAutoTest
# @Author: dudu.zhang
# @File: commonUtil.py
# @Time: 2019-08-18 15:23

class CommonUtil:
    def is_contain(self,str_one,str_two):
        '''
        判断一个字符串是否再另一个字符串中
        str_one:查找的字符串
		str_two：被查找的字符串
        :return:
        '''
        flag = None
        if str_one in str_two:
            flag = True
        else:
            flag = False
        return flag
