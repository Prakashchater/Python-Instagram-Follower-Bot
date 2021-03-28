from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from time import sleep

EMAIL = "chaterprakash@gmail.com"
PASSWORD = "pcchater@160997"
SIMILAR_ACCOUNT = "chefsteps"
webdriver_path = "C:\Chrome driver\chromedriver.exe"
url = "https://www.instagram.com/"
sleep(3)
class InstaFollower:
    def __init__(self,driver):
        self.driver = webdriver.Chrome(executable_path=webdriver_path)

    def login(self):
        self.driver.get(url)
        sleep(5)
        email = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        email.send_keys(EMAIL)
        password = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.send_keys(PASSWORD)
        password.send_keys(Keys.ENTER)
        sleep(5)
        save_info = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
        save_info.click()
        sleep(5)
        notification = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
        notification.click()
        sleep(5)


    def find_followers(self):
        self.driver.get("https://www.instagram.com/chefsteps/")
        sleep(3)
        followers = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()
        sleep(2)
        modal = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
        for i in range(10):
            try:
                self.follow()
            except NoSuchElementException:
                try:
                    sleep(1)
                    follow = self.driver.find_elements_by_css_selector("li button")
                    for button in follow:
                        button.click()
                        sleep(1)
                except ElementClickInterceptedException:
                    cancel = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]')
                    cancel.click()
            # In this case we're executing some Javascript, that's what the execute_script() method does.
            # The method can accept the script as well as a HTML element.
            # The modal in this case, becomes the arguments[0] in the script.
            # Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height of the modal (popup)"
        self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
        sleep(2)


    def follow(self):
        follow = self.driver.find_elements_by_css_selector("li button")
        for button in follow:
            try:
                button.click()
                sleep(1)
            except ElementClickInterceptedException:
                cancel = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]')
                cancel.click()





bot = InstaFollower(webdriver_path)
bot.login()
bot.find_followers()
bot.follow()


