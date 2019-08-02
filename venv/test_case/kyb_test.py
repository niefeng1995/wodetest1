from appium import webdriver
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
    "appPackage":"com.tal.kaoyan",
    "appActivity":"com.tal.kaoyan.ui.activity.SplashActivity",
}
driver = webdriver.Remote("http://localhost:4723/wd/hub",caps)
driver.implicitly_wait(2)
def check_cancelBtn():
    print('check_cancelBtn')

    try:
        cancel_btn = driver.find_element_by_id('android:id/button2')
    except NoSuchElementException:
        print('NO cancelBtn')
    else:
        cancel_btn.click()
def check_skipBtn():
    print("check_skipBtn")

    try:
        skip_Btn = driver.find_element_by_id('com.tal.kaoyan:id/tv_skip')
    except NoSuchElementException:
        print('no skipBtn')
    else:
        skip_Btn.click()

check_cancelBtn()
# check_skipBtn()