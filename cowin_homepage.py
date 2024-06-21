from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


class Cowin:
    xpath_faq = "/html/body/app-root/app-header/header/div[4]/div/div[1]/div/nav/div[3]/div/ul/li[4]/a"
    xpath_partners = "/html/body/app-root/app-header/header/div[4]/div/div[1]/div/nav/div[3]/div/ul/li[5]/a"

    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def open_url(self):
        try:
            self.driver.maximize_window()
            self.driver.get(self.url)
            sleep(5)
            return True

        except:
            print("error : unable to access the url")
            return False

    def click_faq(self):
        if self.open_url():
            homepage_windowhandle = self.driver.current_window_handle
            self.driver.find_element(By.XPATH, value=self.xpath_faq).click()
            sleep(2)
            all_window_handle = self.driver.window_handles
            for windows in all_window_handle:
                if windows != homepage_windowhandle:
                    print(windows)
                    self.driver.switch_to.window(windows)
                    sleep(2)
                    self.driver.close()
            self.driver.switch_to.window(homepage_windowhandle)  # Switch back to the main window

    def click_partners(self):
        if self.open_url():
            homepage_windowhandle = self.driver.current_window_handle
            self.driver.find_element(By.XPATH, value=self.xpath_partners).click()
            sleep(2)
            all_window_handle = self.driver.window_handles
            for windows in all_window_handle:
                if windows != homepage_windowhandle:
                    print(windows)
                    self.driver.switch_to.window(windows)
                    sleep(2)
                    self.driver.close()
            self.driver.switch_to.window(homepage_windowhandle)  # Switch back to the main window


if __name__ == "__main__":
    url = "https://www.cowin.gov.in/"
    cowin_obj1 = Cowin(url)
    cowin_obj1.click_faq()
    cowin_obj1.click_partners()
