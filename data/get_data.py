# -*- coding: utf-8 -*-
# @ProjectName：Python_InterfaceAutoTest
# @Author: dudu.zhang
# @File: get_data.py
# @Time: 2019-08-18 15:23

from utils.operation_excel import OperationExcel
from data import data_config
from utils.operation_json import OperetionJson

class GerData:

    def __init__(self):
        self.opera_excel = OperationExcel()

    #去获取excel行数，就是我们的case个数
    def get_case_lines(self):
        return self.opera_excel.get_lines()


    #判断是否执行
    def get_is_run(self,row):
        flag = None
        col = int(data_config.get_run())
        run_model =self.opera_excel.get_cell_velue(row,col)
        if run_model == 'yes':
            return True
        else:
            return False
        return flag

    #判断是否携带header
    def is_header(self,row):
        col = int(data_config.get_header())
        header = self.opera_excel.get_cell_velue(row,col)
        if header == 'yes':
            return data_config.get_header_value()
        else:
            return None

    #获取请求方式
    def get_request_method(self,row):
        col = int(data_config.get_run_way())
        request_method = self.opera_excel.get_cell_velue(row,col)
        return request_method

    #获取url
    def get_request_url(self,row):
        col = int(data_config.get_url())
        url = self.opera_excel.get_cell_velue(row,col)
        return url

    #获取请求数据
    def get_request_data(self,row):
        col = int(data_config.get_data())
        data = self.opera_excel.get_cell_velue(row,col)
        if data == '':
            return None
        return data

    #通过关键字拿到data数据
    def get_data_for_json(self,row):
        opera_json = OperetionJson()
        request_data = opera_json.get_data(self.get_request_data(row))
        return request_data


    #获取预期结果
    def get_expect_data(self,row):
        col = int(data_config.get_expect())
        expect = self.opera_excel.get_cell_velue(row,col)
        #print(expect)
        if expect == '':
            return None
        return expect

    #获取实际结果
    def write_result(self,row,value):
        col = int(data_config.get_result())
        self.opera_excel.write_value(row,col,value)

    #获取依赖数据的key
    def get_depend_key(self,row):
        col = int(data_config.get_data_depend())
        depent_key = self.opera_excel.get_cell_velue(row,col)
        if depent_key == '':
            return None
        else:
            print("依赖的key:",depent_key)
            return depent_key

    #判断是否有case依赖
    def is_depend(self,row):
        col = int(data_config.get_case_depend())
        depend_case_id = self.opera_excel.get_cell_velue(row,col)
        if depend_case_id == "":
            return None
        else:
            print("依赖的caseid：",depend_case_id)
            return depend_case_id

    #获取数据依赖字段
    def get_depend_field(self,row):
        col = int(data_config.get_field_depend())
        depend_data = self.opera_excel.get_cell_velue(row,col)
        if depend_data == "":
            return None
        else:
            print('依赖的字段：',depend_data)
            return depend_data







