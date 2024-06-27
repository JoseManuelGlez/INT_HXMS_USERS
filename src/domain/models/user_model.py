class UserModel:
    def __init__(self, email, password, name, surname):
        self.email = email
        self.password = password
        self.name = name
        self.surname = surname

    def to_dict(self):
        return {
            'name': self.name,
            'email': self.email,
            'password': self.password,
            'surname': self.surname
        }