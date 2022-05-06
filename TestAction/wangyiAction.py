from selenium import webdriver
from time import sleep
import unittest
import os
# iost = io.StringIO()
import HTMLTestRunner
from selenium.webdriver.common.by import By
chrome_driver=r"C:\anaconda\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe"

#测试网易邮箱的登陆和写信页面功能
class TestWangyi(unittest.TestCase):
    def test_wang(self):
        driver = webdriver.Chrome(executable_path=chrome_driver)
        # '''访问163邮箱网站'''
        url = 'http://mail.163.com/'
        driver.get(url)
        sleep(3)
        # '''断言页面标题正确'''
        # title = '网易免费邮箱'
        # self.assertIn(title, driver.title, '网易免费邮箱')

        # 方法1：切换内嵌网页通过索引index定位
        #driver.switch_to.frame(0)  #也可以直接通过index直接定位，用var iframes = document.querySelectorAll('iframe')列出所有的iframe，展示索引序列号，显示是0

        # 方法2：通过向上一层找到了id = loginDiv是唯一的，所以可以通过xpath定位，用iframe的固定参数frameborder = '0'定位到iframe
        iframe = driver.find_element(By.XPATH,
                                      "//div[@id = 'loginDiv']/iframe[@frameborder = '0']")
        driver.switch_to.frame(iframe)

        # browser.find_element_by_name('email').send_keys('xxxxx')
        driver.find_element(By.NAME, "email").send_keys('xxxxx')
        # browser.find_element_by_name('password').send_keys('xxxxxx')
        driver.find_element(By.NAME, 'password').send_keys('xxxxxx')
        # browser.find_element_by_id('dologin').click()
        driver.find_element(By.ID, 'dologin').click()
        sleep(2)

        # 退出iframe
        # driver.switch_to.default_content()
        '''点击写信按钮'''
        driver.find_element(By.ID,'_mail_component_149_149').click()
        sleep(2)
        '''收件人中填写收拾人邮箱'''
        driver.find_element(By.CLASS_NAME, 'nui-editableAddr-ipt').send_keys('416437020@qq.com')
        sleep(1)
        '''填写想要输入的主题'''
        driver.find_element(By.XPATH,"//div[@class = 'bz0']/div/input[@class = 'nui-ipt-input']").send_keys('这是一封测试邮件')
        sleep(1)
        '''退出当前iframe''' #可以不退出，直接进入新的页面就行
        ##切换到邮件内容填写网页，用xpath定位，已经知道
        # driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[contains(@class,'APP-editor-iframe')]"))

        driver.switch_to.frame(2)  #通过console代码查找iframe，列举出当前页面所有的内嵌页面，总共6个，邮件内容的index索引是2
        #通过唯一属性值定位
        # driver.switch_to.frame(driver.find_element(By.CLASS_NAME, 'APP-editor-iframe'))
        '''点击邮件内容，并输入想要输入的邮件详情'''
        driver.find_element(By.XPATH,'/html/body').send_keys('测试网易登录和写邮件')
        sleep(1)
        '''退出当前iframe'''
        driver.switch_to.default_content()

        '''点击发送按钮，邮件发送成功'''
        driver.find_element(By.XPATH,'//*[@class="jp0"]/div[@role="button"][1]').click()
        sleep(2)

        '''关闭浏览器'''
        driver.quit()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestWangyi))

    # '''指定位置保存测试报告'''
    # file_path = './send_email.html'
    file_path = os.path.join(os.getcwd() + '/report/' + 'wangyi2_case.html')
    p = open(file_path, 'wb')
    # '''指定测试输出报告，及标题，描述'''
    runner = HTMLTestRunner.HTMLTestRunner(stream=p, title='163邮件登录及发送邮件的测试报告',
                                               description='基于unittest的selenium自动化测试')
    runner.run(suite)
    # '''运行测试用例并输入测试报告'''
