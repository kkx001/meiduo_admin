# *_*coding:utf-8 *_*

import unittest


from selenium import webdriver


chromedriver = "/usr/local/chromedriver/chromedriver"


class TestLogin(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(chromedriver)
        url = "http://127.0.0.1:8000/login/"
        self.driver.get(url)

        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        print("setUp")

    def test_login(self):
        # 登陆测试
        driver = self.driver
        driver.find_element_by_css_selector(".name_input").send_keys('kkx001')
        driver.find_element_by_css_selector(".pass_input").send_keys('wb135936')
        driver.find_element_by_css_selector(".input_submit").click()


    def tearDown(self) -> None:

        self.driver.quit()
        print('tearDown')


if __name__ == '__main__':
    # 调用main方法执行unitetest内所有test开头方法
    unittest.main()
