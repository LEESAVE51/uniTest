import unittest
from selenium import webdriver
import time


class testLogin(unittest.TestCase):
    def setUp(self):
        self.dr = webdriver.Chrome()
        self.dr.implicitly_wait(3)
        self.dr.get("http://192.168.1.249:8080/ticai/dist/main.html#login.html")
        print("打开浏览器")

    # 恢复环境
    def tearDown(self):
        self.dr.quit()
        print("关闭浏览器")  # print里面一定要有内容。

    #测试用例（操作步骤）
    def test_Login(self):
        dr = self.dr
        dr.frameA = dr.find_element_by_id("page")
        dr.switch_to.frame(dr.frameA)
        dr.find_element_by_class_name("el-input__inner").send_keys("lsw")
        dr.find_element_by_class_name("s-submit-area").click()
        time.sleep(5)
        dr.switch_to.parent_frame()
        dr.frameB = dr.find_element_by_id("page")
        dr.switch_to.frame(dr.frameB)
        #dr.textA = dr.find_element_by_xpath("/html/head/title").text
        #dr.textA = dr.find_element_by_xpath("//*[@id='app']/div/div[1]/ul[1]/li[5]").text
        print(self.dr.title)
        self.assertEqual(self.dr.title,"首页" )








if __name__ == '__main__':
    unittest.main()
