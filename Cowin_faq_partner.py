from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


class Cowin:
    # xpath for Faq and partners
    xpath_faq = "/html/body/app-root/app-header/header/div[4]/div/div[1]/div/nav/div[3]/div/ul/li[4]/a"
    xpath_partners = "/html/body/app-root/app-header/header/div[4]/div/div[1]/div/nav/div[3]/div/ul/li[5]/a"

    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # method to call url of cowin
    def open_url(self):
        try:
            self.driver.maximize_window()
            self.driver.get(self.url)
            sleep(5)
            return True
        except:
            print("error : unable to access the url")
            return False

    # method to click on faq and partner
    def click_faq_partner(self):
        # call open url method
        if self.open_url():
            # variable to collect current window id
            homepage_window_handle = self.driver.current_window_handle
            # locate element by Xpath and then click
            self.driver.find_element(By.XPATH, value=self.xpath_faq).click()
            sleep(3)
            # switch window back to cowin home page
            self.driver.switch_to.window(homepage_window_handle)
            # Locate partner with xpath and click
            self.driver.find_element(By.XPATH, value=self.xpath_partners).click()
            sleep(2)
            # variable to collect all window ids
            all_window_handle = self.driver.window_handles
            # for loop to iterate windows ids and get window id of faq and partner windows
            for windows in all_window_handle:
                if windows != homepage_window_handle:
                    # printing windows id on console
                    print("window_id", windows)
            return True

    # method to close windows of FAQ and Partner
    def close_faq_partner(self):
        if self.open_url():
            homepage_window_handle = self.driver.current_window_handle
            self.driver.find_element(By.XPATH, value=self.xpath_faq).click()
            sleep(3)
            self.driver.switch_to.window(homepage_window_handle)
            self.driver.find_element(By.XPATH, value=self.xpath_partners).click()
            sleep(2)
            all_window_handle = self.driver.window_handles
            # logic to close windows of FAQ and partner nd get back to home window
            for windows in all_window_handle:
                if windows != homepage_window_handle:
                    self.driver.switch_to.window(windows)
                    self.driver.close()
            self.driver.switch_to.window(homepage_window_handle)
        return True
