import yaml
import time
from module import Site

with open("config.yaml") as f:
    testdata = yaml.safe_load(f)

site = Site(testdata["address"])
username = testdata["username"]
password = testdata["password"]


def test_step1(x_selector1, x_selector2, x_selector3, btn_selector, er1):
    input1 = site.find_element("xpath", x_selector1)
    input1.send_keys("test")
    input2 = site.find_element("xpath", x_selector2)
    input2.send_keys("test")
    btn = site.find_element("css", btn_selector)
    btn.click()
    time.sleep(testdata["sleep_time"])
    err_label = site.find_element("xpath", x_selector3)
    text = err_label.text
    #site.quit()
    assert text == "401"


def test_step2(x_selector1, x_selector2, x_selector4, btn_selector, er2):
    input1 = site.find_element("xpath", x_selector1)
    input1.clear()
    input1.send_keys(username)
    input2 = site.find_element("xpath", x_selector2)
    input2.clear()
    input2.send_keys(password)
    btn = site.find_element("css", btn_selector)
    btn.click()
    time.sleep(testdata["sleep_time"])
    user_label = site.find_element("xpath", x_selector4)
    text = user_label.text
    #site.close()
    assert text == er2


def test_step3(x_selector5, x_selector6, x_selector7, create_new_post_btn, save_post_btn, er3):
    create_btn = site.find_element("xpath", create_new_post_btn)
    create_btn.click()
    time.sleep(testdata["sleep_time"])
    input1 = site.find_element("xpath", x_selector5)
    input1.clear()
    input1.send_keys("AutoPythonWebSelenium")
    input2 = site.find_element("xpath", x_selector6)
    input2.clear()
    input2.send_keys("Pytest_Test2")
    save_btn = site.find_element("xpath", save_post_btn)
    save_btn.click()
    #time.sleep(testdata["sleep_time"])
    time.sleep(5)
    title_label = site.find_element("xpath", x_selector7)
    text = title_label.text
    #site.quit()
    assert text == er3
