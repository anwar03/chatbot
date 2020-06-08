from enum import Enum


class EnumUser(Enum):
    NAME = 1
    EMAIL = 2
    PHONE = 3
    DONE = 4


class ConState:

    def __init__(self):
        self.profile = EnumUser.NAME

    @property
    def current_pos(self):
        return self.profile

    @current_pos.setter
    def current_pos(self, current: EnumUser):
        self.profile = current


class UserProfile:

    def __init__(self):
        self.name = ""
        self.email = ""
        self.phone = ""

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, name: str):
        self.name = name

    @property
    def email(self):
        return self.email

    @email.setter
    def email(self, email: str):
        self.email = email

    @property
    def phone(self):
        return self.phone

    @phone.setter
    def phone(self, phone: str):
        self.phone = phone
