import time

import pytest
from testpage import OperationHelper
username = "rav53-85@mail.ru"
password = "X578Z4AE"

def test_step_1(browser):
    test_page1 = OperationHelper(browser)
    test_page1.go_to_site()
    test_page1.enter_login("rav53-85@mail.ru")
    test_page1.enter_pswd("X578Z4AE")
    test_page1.click_button()
    time.sleep(3)
  
    test_page1.click_contact()
    time.sleep(3)
    
    test_page1.enter_cont_name("RAv")
    test_page1.enter_cont_email("mail@mail.ru")
    test_page1.enter_cont_text("Hi, and...)?")
    time.sleep(1)
    
    test_page1.click_button()
    time.sleep(1)

    assert test_page1.get_alert_text() == "Form successfully submitted"