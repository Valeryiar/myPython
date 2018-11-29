
from selenium.webdriver.firefox.webdriver import WebDriver


class Application:
    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)


    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()

    def returnToGroupPage(self):
        wd = self.wd
        wd.find_element_by_link_text("group page").click()

    def createGroup(self, group):
        wd = self.wd
        self.openGroupsPage()
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        wd.find_element_by_name("submit").click()
        self.returnToGroupPage()

    def openGroupsPage(self):
        wd = self.wd
        wd.find_element_by_link_text("groups").click()

    def createContact(self, contact):
        wd=self.wd
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.name)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("submit").click()
        wd.find_element_by_link_text("home page").click()

    def login(self, username, password):
        wd = self.wd
        self.openHomePage()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def openHomePage(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()
