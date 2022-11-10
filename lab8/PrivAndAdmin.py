from user import User
class Privileges:
    privileges = ["Allowed to add message", "Allowed to delete users", "Allowed to ban users"]

    def show_privileges(self):
        print(self.privileges)
class Admin(User):
    privileges = ["Allowed to add message", "Allowed to delete users", "Allowed to ban users"]
    def show_privileges(self):
        print(self.privileges)
    priv = Privileges()