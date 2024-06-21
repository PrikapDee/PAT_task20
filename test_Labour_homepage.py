from Labour_homepage import Labour

import pytest

url = "https://labour.gov.in/"
# object of Labour class
labour_obj1 = Labour(url)


# test to verify url is open
def test_open_url():
    assert labour_obj1.open_url() == True
    print("success : testcase Url pass")


# test to verify download report method
def test_click_document():
    assert labour_obj1.documents() == True
    print("success : testcase of document pass")


# test to download monthly report
def test_download_monthly_report():
    assert labour_obj1.download_monthly_report() == True
    print("success :testcase download report pass")


# test to click on menu and submenu
def test_media_menu():
    assert labour_obj1.menu_media() == True
    print("success : testcase of media pass")


# test to take save image
def test_screenshot_image():
    assert labour_obj1.download_save_images() == True
    print("success : testcase of image save pass")
