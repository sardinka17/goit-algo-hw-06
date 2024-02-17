from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        super().__init__(value)

        if not self.is_valid(value):
            raise ValueError

        self.value = value

    def is_valid(self, value):
        return len(value) == 10 and value.isdigit()


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
        self.phones.append(Phone(phone_str))

    def remove_phone(self, phone_str):
        phone_index = self.__find_phone_index__(phone_str)

        if phone_index is None:
            raise ValueError
        else:
            del self.phones[phone_index]

    def edit_phone(self, old_phone, new_phone):
        phone_index = self.__find_phone_index__(old_phone)

        if phone_index is None:
            raise ValueError
        else:
            self.phones[phone_index] = Phone(new_phone)

    def find_phone(self, phone_str):
        phone_index = self.__find_phone_index__(phone_str)

        if phone_index is None:
            raise ValueError
        else:
            return self.phones[phone_index]


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        if name in self.data.keys():
            return self.data[name]
        else:
            return None

    def delete(self, name):
        if name in self.data.keys():
            del self.data[name]
