from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
#
class Name(Field):
    def __init__(self, value):
        if len(value) != 0:
            super().__init__(value)
        else :
            raise ValueError ("Incorrect Name")
#
class Phone(Field):
    def __init__(self, value):
        if  len(value) == 10:
            super().__init__(value)
        else :
            raise ValueError ("Incorrect phone format")


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone (self, phone ) :
          self.phones.append(Phone(phone)) 
    
    def remove_phone(self, phone):
        for  ph in self.phones:
            if ph.value == phone:
               self.phones.remove(ph)
           
    def edit_phone(self, oldphone, newphone):
        for ph in self.phones:
            if ph.value == oldphone :
                ph.value = newphone
             
    def find_phone(self, phone):
        for ph in self.phones:
            if ph.value == phone :
                return ph.value
                 
    def getRecord (self):
        return self.name.value, self.phones

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    
    def add_record(self, record):
        self.data[record.name.value] = record
    
    def delete(self, namephone):
        for name in self.data:
            if name == namephone :
                return self.data.pop(name)
            
    def find(self, namephone):
        if namephone in self.data :
            return self.data[namephone]
        

# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# Видалення запису Jane
book.delete("Jane")
      
for name, record in book.data.items():
    print(record)
