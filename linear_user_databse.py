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

neeraj = User("neeraj", "neeraj", "neeraj@gmail.com")
akash = User("akash", "akash", "akash@gmail.com")
bunty = User("bunty", "bunty", "bunty@gmail.com")
chunnu = User("chunnu", "chunnu", "chunnu@gmail.com")
dheeraj = User("dheeraj", "dheeraj", "dheeraj@gmail.com")
deepak = User("deepak", "deepak", "deepak@gmail.com")
user_database = UserDatabase()
user_database.insert(neeraj)
user_database.list_all()
user_database.insert(akash)
user_database.list_all()
user_database.insert(bunty)
user_database.list_all()
user_database.insert(chunnu)
user_database.list_all()
user_database.insert(dheeraj)
user_database.list_all()
user_database.insert(deepak)
user_database.list_all()

