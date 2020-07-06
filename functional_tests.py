# -*- coding:utf-8 -*-
# @Time    : 2020/7/1 10:36
# @Author  : supakito

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 伊迪斯听说有一个很酷的在线待办事项应用
        # 她去看了这个应用的首页
        self.browser.get('http://localhost:8000')

        # 她注意到网页标题和头部都包含“To-Do”这个词
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # 应用邀请她输入一个待办事项
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # 她在一个文本框中输入了“Buy peacock feathers"
        # 伊迪斯的爱好是使用假蝇做饵带钓鱼
        inputbox.send_keys('Buy peacock feather')

        # 她按回车键后，页面更新了
        # 待办事项表格中显示了“1： Buy peacock feather”
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1： Buy peacock feather' for row in rows),
            "New to-do item did not appear in table"
        )

        # 页面中有显示了一个文本框，可以输入其他的待办事项
        # 她输入了“Use peacock feathers to make a fly”
        # 伊迪斯做事很有条理
        self.fail('Finish the test')



if __name__ == '__main__':
    unittest.main()