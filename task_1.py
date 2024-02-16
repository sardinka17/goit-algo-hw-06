from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def is_valid(self):
        return len(self.value) == 10


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def __str__(self):
        return f"Contact name: {self.name}, phones: {"; ".join(list(map(lambda phone: str(phone), self.phones)))}"

    def __find_phone_index__(self, phone_str):
        phone_index = None

        for i in range(len(self.phones)):
            if self.phones[i].value == phone_str:
                phone_index = i

        return phone_index

    def add_phone(self, phone_str):
        phone = Phone(phone_str)

        if phone.is_valid():
            self.phones.append(phone)
        else:
            print(f"{phone_str} is not valid.")

    def remove_phone(self, phone_str):
        phone_index = self.__find_phone_index__(phone_str)

        if phone_index is None:
            print(f"{phone_str} doesn't exist.")
        else:
            del self.phones[phone_index]

    def edit_phone(self, old_phone, new_phone):
        phone = Phone(new_phone)
        phone_index = self.__find_phone_index__(old_phone)

        if phone_index is None:
            print(f"{old_phone} doesn't exist.")
        elif not phone.is_valid():
            print(f"{new_phone} is not valid.")
        else:
            self.phones[phone_index] = Phone(new_phone)

    def find_phone(self, phone_str):
        phone_index = self.__find_phone_index__(phone_str)

        if phone_index is None:
            return phone_index
        else:
            return self.phones[phone_index]


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data[name]

    def delete(self, name):
        del self.data[name]
