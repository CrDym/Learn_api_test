# -*- coding: utf-8 -*-
# @Time    : 2018/7/9 14:40
# @Author  : Cr
# @File    : mock_demo.py
from mock import mock
def mock_test(mock_method,request_data,url,method,response_data):
    mock_method= mock.Mock(return_value=response_data)
    res = mock_method(url,method,request_data)
    return res