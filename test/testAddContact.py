
from model.contact import Contact

def testAddContact_(app):
    app.session.login( username="admin", password= "secret")
    app.contact.create(Contact (name="name", lastname="last", address="address"))
    app.session.logout()


