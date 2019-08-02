from appium import webdriver
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
caps ={
    "platformName":"Android",
    "platformVersion":"5.1.1",
    "deviceName":"emulator-5554",
    # "automationName":"uiautomator2",
    # "app":r"C:\Users\nie67\Desktop\kaoyanbang_55.apk",
    # "appPackage":"com.tencent.mm",
    # "appActivity":"com.tencent.mm.ui.LauncherUI",
    "noReset":"False",
    "appPackage":"com.mymoney",
    "appActivity":"com.mymoney.biz.splash.newguide.NewGuideActivity",
}
driver = webdriver.Remote("http://localhost:4723/wd/hub",caps)
driver.implicitly_wait(5)
def get_size():
    x  = driver.get_window_size()['width']
    y  = driver.get_window_size()['height']
    return x,y
def swipeLeft():
    l = get_size()
    x1 = int(l[0]*0.9)
    y1 = int(l[1]*0.5)
    x2 = int(l[0]*0.1)
    driver.swipe(x1,y1,x2,y1,1000)
def swipeUp():
    l = get_size()
    x1 = int(l[0]*0.5)
    y1 = int(l[1]*0.95)
    y2 = int(l[1]*0.35)
    driver.swipe(x1,y1,x1,y2,1000)
WebDriverWait(driver,6).until(lambda x:x.find_element_by_id('com.mymoney:id/next_btn'))

for i in range(2):
    swipeLeft()
    sleep(0.5)

driver.find_element_by_id('com.mymoney:id/begin_btn').click()
try:
    closeBtn = driver.find_element_by_id('com.mymoney:id/close_iv')
except NoSuchElementException:
    pass
else:
    closeBtn.click()

driver.find_element_by_id('com.mymoney:id/nav_setting_btn').click()
WebDriverWait(driver,5).until(lambda x:x.find_element_by_id('com.mymoney:id/title_tv'))
swipeUp()
driver.find_element_by_android_uiautomator('new UiSelector().text("高级")').click()
driver.find_element_by_id('com.mymoney:id/password_protected_briv').click()
driver.find_element_by_id('com.mymoney:id/lock_pattern_or_not_sriv').click()

for i in  range(2):
    TouchAction(driver).press(x=262,y=385).wait(2000)\
    .move_to(x=451,y=388).wait(2000)\
    .move_to(x=650,y=589).wait(1000)\
    .move_to(x=649,y=785).wait(1000)\
    .release().perform()



