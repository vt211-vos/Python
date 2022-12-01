from user import User
from PrivAndAdmin import Admin

user = User("User1(First)", "User1(last)","User1(nick)")
def test_describe_user():
    assert user.describe_user() == 'Name:User1(First) Surname:User1(last) Nackname:User1(nick)'
def test_greeting_user():
    assert user.greeting_user() == 'Hello User1(nick)'

user1 = User("User(First)", "User(last)","User(nick)", 1)
def test_increment_login_attempts():
    user1.increment_login_attempts()
    user1.increment_login_attempts()
    user1.increment_login_attempts()
    assert user1.login_attempts == 4

def test_reset_login_attempts():
    user1.reset_login_attempts()
    assert user1.login_attempts == 0

def test_show_privileges():
    admin = Admin("Admin(First)", "Admin(last)", "Admin(nick)", 1)
    assert admin.show_privileges() == ["Allowed to add message", "Allowed to delete users", "Allowed to ban users"]

def test_show_privileges2():
    admin = Admin("Admin(First)", "Admin(last)","Admin(nick)", 1)
    assert admin.priv.show_privileges() == ["Allowed to add message", "Allowed to delete users", "Allowed to ban users"]

