class User:
    def __init__(self, first_name, last_name, nickname, login_attempts = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.nickname = nickname
        self.login_attempts = login_attempts
    def describe_user(self):
        print(f"Name:{self.first_name} Surname:{self.last_name} Nackname:{self.nickname}")
    def greeting_user(self):
        print(f"Hello {self.nickname}")
    def  increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0