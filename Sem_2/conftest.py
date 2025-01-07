import pytest
import yaml

with open("config.yaml") as f:
    testdata = yaml.safe_load(f)

name = testdata["username"]


@pytest.fixture()
def x_selector1():
    return """//*[@id="login"]/div[1]/label/input"""


@pytest.fixture()
def x_selector2():
    return """//*[@id="login"]/div[2]/label/input"""


@pytest.fixture()
def x_selector3():
    return """//*[@id="app"]/main/div/div/div[2]/h2"""


@pytest.fixture()
def x_selector4():
    return """//*[@id="app"]/main/nav/ul/li[3]/a"""


@pytest.fixture()
def x_selector5():
    return """//*[@id="create-item"]/div/div/div[1]/div/label/input"""


@pytest.fixture()
def x_selector6():
    return """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea"""


@pytest.fixture()
def x_selector7():
    return """//*[@id="app"]/main/div/div[1]/h1"""


@pytest.fixture()
def btn_selector():
    return "button"


@pytest.fixture()
def create_new_post_btn():
    return """//*[@id="create-btn"]"""


@pytest.fixture()
def save_post_btn():
    return """//*[@id="create-item"]/div/div/div[7]/div/button"""


@pytest.fixture()
def er1():
    return "401"


@pytest.fixture()
def er2():
    return "Hello, {}".format(name)


@pytest.fixture()
def er3():
    return "AutoPythonWebSelenium".format(name)
