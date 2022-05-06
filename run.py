import unittest
# from BeautifulReport import BeautifulReport
import os
import HTMLTestRunner
from TestAction.wangyiAction import TestWangyi

#创建一个测试执行计划，采用BeautifulReport生成测试报告
# suite = unittest.TestSuite()
#
# suite.addTest(unittest.makeSuite(TestWangyi))  #括号里面跟的是测试类
#
# #zhiixng
# #TextTestRunner  --以文本的形式输出测试结果
# #unittest.TextTestRunner().run(suite)
#
# #unittest框架还可以生成html测试报告
# BeautifulReport(suite).report(filename = "test_report_wangyi",description = "unittest自动化生成的测试报告")  #filename路径就是当前目录下


#创建一个测试执行计划，采用HTMLTestRunner生成测试报告
file_path = os.path.join(os.getcwd() + '/report/' + 'wangyi_case.html')
p = open(file_path, 'wb')
# '''指定测试输出报告，及标题，描述'''
suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestWangyi))
runner = HTMLTestRunner.HTMLTestRunner(stream=p, title='163邮件登录及发送邮件的测试报告',
                                       description='基于unittest的selenium自动化测试')
runner.run(suite)
# with open(file_path, 'wb') as rf:
#     '''指定测试输出报告，及标题，描述'''
#     runner = HTMLTestRunner.HTMLTestRunner(stream=rf, title='163邮件登录及发送邮件的测试报告',
#                                            description='基于unittest的selenium自动化测试')
# '''运行测试用例并输入测试报告'''