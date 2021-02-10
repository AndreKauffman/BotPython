from selenium import webdriver
from socket import socket
from selenium.webdriver.common.keys import Keys
import time

class instagram:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(executable_path=r'C:\Área de Trabalho\driver\chromedriver.exe')

    def login(self):
        driver = self.driver
        driver.get('https://www.instagram.com/')
        time.sleep(3)
        user_element = driver.find_element_by_xpath("//input[@name='username']")
        user_element.clear()
        user_element.send_keys(self.username)
        password_element = driver.find_element_by_xpath("//input[@name='password']")
        password_element.clear()
        password_element.send_keys(self.password)
        password_element.send_keys(Keys.RETURN)
        time.sleep(5)
        self.curtirFotos('memesbr')


    def curtirFotos(self, hashtag):
        driver = self.driver
        driver.get('https://www.instagram.com/explore/tags/' + hashtag + '/')
        time.sleep(5)
        for i in range(0, 3):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeith);")
        hrefs = driver.find_element_by_tag_name('a')
        pegar_hrefs = [elem.get_attribute('href') for elem in hrefs]
        print(hashtag + 'fotos: ' + str(len(pegar_hrefs)))

        for pegar_hrefs in pegar_hrefs:
            driver.get(pegar_hrefs)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeith);")
            try:
                driver.find_element_by_class_name("//button[@class='wpO6b ']").click()
                time.sleep(19)
            except exception as e:
                time.sleep(5)

bot = instagram('***','***')
bot.login()

