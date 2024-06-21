from Cowin_faq_partner import Cowin
import pytest

url = "https://www.cowin.gov.in/"
# object of cowin class
cowin_obj1 = Cowin(url)


# testcase method to test url is accessible
def test_openurl():
    assert cowin_obj1.open_url() == True
    print("success : test Url pass")


# testcase to click FAQ and partner windows
def test_click_windows():
    assert cowin_obj1.click_faq_partner() == True
    print("success : test click of windows")


# testcase method to test url are closing
def test_close_url():
    assert cowin_obj1.close_faq_partner() == True
    print("success : test close pass")
