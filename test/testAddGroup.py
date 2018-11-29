
import pytest

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from fixture.application import Application
from model.group import Group

cap = DesiredCapabilities().FIREFOX
cap["marionette"] = False
browser = webdriver.Firefox(capabilities=cap, executable_path="C:\\path\\to\\geckodriver.exe")
browser.get('http://google.com/')
browser.quit()


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def testAddGroup(app):
        app.login( username="admin", password= "secret")
        app.createGroup( Group (name="name", header="header", footer="footer"))
        app.logout()

def tearDown(app):
        app.destroy()



