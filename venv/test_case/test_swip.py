from test_case.kyb_test import driver
from time import sleep
def get_size():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return x,y
l = get_size()
print(l)

def swipeLeft():
    l = get_size()
    x1 = int(l[0]*0.9)
    print(x1)
    y1 = int(l[1]*0.5)
    print(y1)
    x2 = int(l[0]*0.1)
    print(x2)
    driver.swipe(x1,y1,x2,y1,1000)

for i in range(2):
    swipeLeft()
    sleep(0.5)

driver.find_element_by_id('com.tal.kaoyan:id/activity_splash_guidfinish').click()