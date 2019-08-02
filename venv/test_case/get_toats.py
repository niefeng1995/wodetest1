# coding=utf-8
# from test_case.kyb_test import driver
# from selenium.webdriver.support.ui import WebDriverWait
# driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').clear()
# driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').send_keys('nie1')
# driver.find_element_by_id('com.tal.kaoyan:id/login_password_edittext').send_keys('123')
# driver.find_element_by_id('com.tal.kaoyan:id/login_login_btn').click()
#
# error_message = "用户名或密码错误，你还可以尝试3次"
# limit_message ="验证失败次数过多，请15分钟后再试"
#
# message ="//*[@text=\'{}\']".format(error_message)
# # message ="//*[@text=\'{}\']".format(limit_message)
# toast = WebDriverWait(driver,5).until(lambda x:x.find_element_by_xpath(message))
# print(toast.text)
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
caps ={
    "platformName":"Android",
    "platformVersion":"5.1.1",
    "deviceName":"emulator-5554",
    # "automationName":"uiautomator2",
    # "app":r"C:\Users\nie67\Desktop\kaoyanbang_55.apk",
    # "appPackage":"com.tencent.mm",
    # "appActivity":"com.tencent.mm.ui.LauncherUI",
    "noReset":"False",
    "appPackage":"com.wondershare.drfone",
    "appActivity":"com.wondershare.drfone.ui.activity.Main2Activity",
}
driver = webdriver.Remote("http://localhost:4723/wd/hub",caps)
driver.implicitly_wait(5)

driver.find_element_by_id('com.wondershare.drfone:id/btnBackup').click()
WebDriverWait(driver,10).until(lambda x:x.find_element_by_id('com.wondershare.drfone:id/btnRecoverData'))
driver.find_element_by_id('com.wondershare.drfone:id/btnRecoverData').click()
WebDriverWait(driver,20).until(lambda x:x.find_element_by_class_name('android.webkit.WebView'))
context = driver.contexts
print(context)
driver.switch_to.context('WEBVIEW_com.wondershare.drfone')
driver.find_element_by_id('email').send_keys('15070248234@163.com')
driver.find_element_by_class_name('btn_send').click()

driver.switch_to.context('NATIVE_APP')
driver.find_element_by_class_name('android.widget.ImageButton').click()