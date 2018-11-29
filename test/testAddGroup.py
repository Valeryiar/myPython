
from model.group import Group

def testAddGroup(app):
        app.session.login( username="admin", password= "secret")
        app.group.create( Group (name="name", header="header", footer="footer"))
        app.session.logout()





