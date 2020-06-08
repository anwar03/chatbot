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
        self._name = ""
        self._email = ""
        self._phone = ""

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email: str):
        self._email = email

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, phone: str):
        self._phone = phone
