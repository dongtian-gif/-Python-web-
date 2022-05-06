from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
import time

class Testwangyi(unittest.TestCase):  #unittest.TestCase类名
    def test_login(self):
        url = 'http://mail.163.com/'
        chrome_driver=r"C:\anaconda\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe"
        browser = webdriver.Chrome(executable_path=chrome_driver)

        # firefox_driver=r"C:\anaconda\Lib\site-packages\selenium\webdriver\firefox\geckodriver.exe"
        # browser = webdriver.Firefox(executable_path=firefox_driver)
        browser.get(url)
        time.sleep(3)
        # driver.switch_to.frame(0)  #也可以直接通过index直接定位，用var iframes = document.querySelectorAll('iframe')列出所有的iframe，展示索引序列号，显示是0
        iframe = browser.find_element(By.XPATH,
                                      "//div[@id = 'loginDiv']/iframe[@frameborder = '0']") #通过向上一层找到了id = loginDiv是唯一的，所以可以通过xpath定位，用iframe的固定参数frameborder = '0'定位到iframe
        browser.switch_to.frame(iframe)
        browser.find_element(By.NAME,"email").send_keys('a416437020')
        # browser.find_element_by_name('password').send_keys('b416437020')
        browser.find_element(By.NAME,'password').send_keys('b416437020')
        # browser.find_element_by_id('dologin').click()
        browser.find_element(By.ID,'dologin').click()
        time.sleep(3)

        # ----------------------查看是否登录成功---------------------
        # 退出iframe
        browser.switch_to.default_content()
        # 断言
        name = browser.find_element(By.ID,"spnUid").text
        print(name)
        self.assertEqual(name,'a416437020@163.com','登录成功')
        # assert name == 'a416437020@163.com'
        # --------------------退出登录，退出浏览器--------------------
        # browser.find_element(By.link_text('退出').click())
        # browser.quit()

if __name__ == "__main__":
     unittest.main()

