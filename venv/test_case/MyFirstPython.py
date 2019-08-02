# message = 'hello wrold'
# # print(message)
# message = 123456
# print(message)
"""python  始终记住变量的最新值"""
# name = 'ada lovelace'
# print(name.title())  # .title（）以首字母大写的形式输出字符串内容
# print(name.upper())  # .upper() 以全部大写的形式输出字符串内容
# print(name.lower())  # .lower() 以全部小写的形式输入字符串内容

# first_name = 'ada'
# last_name = 'lovelace'
# full_name =  first_name +' '+last_name
#
# message = "Hello, " + full_name.title()+"!"
# print(message)
#
# print("\tPyhon\tJava") # \t 添加制表符
# print("Languages:\nPython\nC\nJavaScript")  #  \n 换行符
# print("Languages:\n\tPython\n\tC\n\tJavaScript") # 在同一个字符串中同时包含制表符和换行符

# favorite_language = 'python                  '
# favorite_language = favorite_language.rsplit() #  暂时删除空白
# print(favorite_language)
# favorite_language = ' python '
# favorite_language = favorite_language.rstrip()  # 删除后面的空白
# print(favorite_language)
# favorite_language = favorite_language.lstrip()  # 删除前面的空白
# print(favorite_language)
# favorite_language = favorite_language.strip() # 删除两端的空白
# print(favorite_language)
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('http://www.itmop.com/downinfo/308478.html')
