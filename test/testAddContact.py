import pytest

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from fixture.application import Application
from model.contact import Contact

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


def testAddContact_(app):
    app.login( username="admin", password= "secret")
    app.createContact(Contact (name="name", lastname="last", address="address"))
    app.logout()


def tearDown(app):
    app.destroy()
