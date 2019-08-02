from test_case.kyb_test import driver
driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').clear()
driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').send_keys('nie1')
driver.find_element_by_id('com.tal.kaoyan:id/login_password_edittext').send_keys('123')
driver.save_screenshot('login.png')
driver.get_screenshot_as_file('D:/wodetest/image/login.png')
driver.find_element_by_id('com.tal.kaoyan:id/login_login_btn').click()
