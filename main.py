import datetime
from abc import ABC, abstractmethod

class BirthdayEntity(ABC):
    @abstractmethod
    def get_description(self):
        pass

class Person(BirthdayEntity):
    def __init__(self, name, birth_date):
        self.name = name
        self.__birth_date = datetime.datetime.strptime(birth_date, "%Y-%m-%d").date()

    def get_birth_date(self):
        return self.__birth_date

    def days_until_birthday(self):
        today = datetime.date.today()
        next_birthday = self.__birth_date.replace(year=today.year)
        if next_birthday < today:
            next_birthday = next_birthday.replace(year=today.year + 1)
        return (next_birthday - today).days

    def get_description(self):
        return f"Friend: {self.name}"

class FamilyMember(Person):
    def __init__(self, name, birth_date, relationship):
        super().__init__(name, birth_date)
        self.relationship = relationship

    def get_description(self):
        return f"Family Member: {self.name} ({self.relationship})"

def main():
    print("--- Birthday Reminder App ---")
    
    
    entities = [
        Person("Jonas", "1995-05-20"),
        FamilyMember("Marija", "1970-10-15", "Mother")
    ]
    
    for entity in entities:
        print(f"{entity.get_description()} | Days left: {entity.days_until_birthday()}")

if __name__ == "__main__":
    main()