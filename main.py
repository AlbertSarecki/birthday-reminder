import datetime

class Person:
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
            
        delta = next_birthday - today
        return delta.days

def main():
    print("--- Birthday Reminder App ---")
    friend = Person("Jonas", "1995-05-20")
    print(f"Name: {friend.name}")
    print(f"Days until birthday: {friend.days_until_birthday()}")

if __name__ == "__main__":
    main()