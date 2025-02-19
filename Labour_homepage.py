import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class Labour:
    # locators
    img_locator = (
        "/html/body/section[3]/div/div/div[3]/div[2]/div[1]/div/div/div[2]/div[2]/table/tbody/tr/td/div[1]/div/img")
    folder_path = "E:\Priyanka\workspace\dowload_image\image"

    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # method to call url of labour
    def open_url(self):
        try:
            self.driver.maximize_window()
            self.driver.get(self.url)
            sleep(2)
            return True
        except:
            print("error : unable to access the url")
            return False

    # method to click on document and then submenu
    def documents(self):
        try:
            self.open_url()
            # locate element by Link text
            documents_loc = self.driver.find_element(By.LINK_TEXT, "Documents")
            # use of action class for mouse hover
            actions = ActionChains(self.driver)
            # move to element method to go over document
            actions.move_to_element(documents_loc)
            actions.perform()
            # visibility_of _element method to locate element and wait method to wait till we locate element
            monthly_report = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Monthly Progress Report")))
            monthly_report.click()
            return True
        except:
            print("error in code")

    # method to download report
    def download_monthly_report(self):
        try:
            self.documents()
            sleep(7)
            self.driver.find_element(By.LINK_TEXT, "Download(139.61 KB)").click()
            # using switch to alert for click on ok of dialog box appear
            self.driver.switch_to.alert.accept()
            sleep(3)
            # self.driver.close()
            return True
        except:
            print("error")

    def menu_media(self):
        try:
            self.open_url()
            media_loc = self.driver.find_element(By.LINK_TEXT, value="Media")
            actions = ActionChains(self.driver)
            actions.move_to_element(media_loc)
            actions.perform()
            photo_gallery = WebDriverWait(self.driver, timeout=10).until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Photo Gallery")))
            photo_gallery.click()
            sleep(4)
            return True
        except:
            print("error")

    #  function to take screenshot of images and store it in a folder
    def download_save_images(self):
        try:
            self.menu_media()
            sleep(5)
            # list of elements located through xpath
            list_img = self.driver.find_elements(By.XPATH, value=self.img_locator)
            # for loop to iterate through list of image
            for i in range(len(list_img)):
                # we need count of 10 images
                if i <= 10:
                    # screenshot function and save it into download folder and str(i) used to give different name
                    # to image
                    list_img[i].screenshot("E:\Priyanka\workspace\dowload_image\image" + str(i) + ".png")
            return True
        except:
            print("error")
