from user import User
from PrivAndAdmin import Admin

#  A)
print("a)")
user1 = User("User1(First)", "User1(last)","User1(nick)")
user2 = User("User2(First)", "User2(last)","User2(nick)")
user1.describe_user()
user1.greeting_user()
user2.describe_user()
user2.greeting_user()

#  B)
print("\nb)")
user = User("User(First)", "User(last)","User(nick)", 1)
print(user.login_attempts)
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(user.login_attempts)
user.reset_login_attempts()
print(user.login_attempts)

#  C)
print("\nc)")
admin = Admin("Admin(First)", "Admin(last)","Admin(nick)", 1)
admin.show_privileges()

#  D)
print("\nd)")
admin = Admin("Admin(First)", "Admin(last)","Admin(nick)", 1)
admin.priv.show_privileges()