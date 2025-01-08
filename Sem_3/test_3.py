from testpage import OperationsHelper
import logging
import yaml
import time

with open("config.yaml") as f:
    testdata = yaml.safe_load(f)
    username = testdata["username"]
    password = testdata["password"]


def test_step1(browser):
    logging.info("Test1 Starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login("test")
    testpage.enter_pass("test")
    testpage.click_login_button()
    assert testpage.get_error_text() == "401"


def test_step2(browser):
    logging.info("Test2 Starting")
    testpage = OperationsHelper(browser)
    testpage.enter_login(username)
    testpage.enter_pass(password)
    testpage.click_login_button()
    assert testpage.get_user_text() == f"Hello, {username}"


def test_step3(browser):
    logging.info("Test3 Starting")
    testpage = OperationsHelper(browser)
    testpage.click_new_post_btn()
    testpage.enter_title("AutoPythonWebSelenium")
    testpage.enter_description("Pytest_Test2")
    testpage.click_save_post_btn()
    time.sleep(5)
    assert testpage.get_post_title_text() == "AutoPythonWebSelenium"


def test_step4(browser):
    logging.info("Test4 Starting")
    testdata = OperationsHelper(browser)
    testdata.click_home_link()
    testdata.click_contact_link()
    testdata.enter_contact_name("Name")
    testdata.enter_contact_email("test@test.ru")
    testdata.enter_contact_description("Test")
    testdata.click_contact_send_btn()
    time.sleep(5)
    assert testdata.get_alert_text() == "Form successfully submitted"
