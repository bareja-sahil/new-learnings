class UserDatabase:
    def __init__(self):
        self.users = []

    def insert(self, user):
        i = 0
        while i < len(self.users):
            if self.users[i].username > user.username:
                break
            i += 1
        self.users.insert(i, user)

    def find(self, username):
        i = 0
        while i < len(self.users):
            if self.users[i].username == username:
                return self.users[i]

    def update(self, user):
        target = self.find(username=user.username)
        target.name, target.email = user.name, user.email

    def list_all(self):
        print(self.users)


class User:
    def __init__(self, name, username, email):
        self.name = name
        self.username = username
        self.email = email

    def __repr__(self):
        return f"User is {self.name}"



