from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		#访问首页
		self.browser.get('http://localhost:8000')

		#验证网页标题和头部都包含“To-Do”
		self.assertIn('To-Do',self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do',header_text)
		
		#页面中可输入一个待办事项
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a to-do item'
		)

		#在文本框输入“Buy peacock feathers”
		inputbox.send_keys('Buy peacock feathers')
		#按回车后页面刷新，且待办事项表格中显示了“1:Buy peacock feathers”
		inputbox.send_keys(Keys.ENTER)

		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertTrue(
			any(row.text == '1:Buy peacock feathers' for row in rows),
			"New to-do not appear in table"
		)

		#页面又显示了一个文本框，可以输入其他待办事项，他输入“Use peacock feathers to make a fly"
		self.fail('Finish the test!')

if __name__ == '__main__':
	unittest.main()
	#unittest.main(warnings='ignore')