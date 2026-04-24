import os
from models import Person, FamilyMember

def load_birthdays(filename):
    entities = []
    # Gauname pilną kelią iki šio failo vietos
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, filename)
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 3:
                    entities.append(FamilyMember(parts[0], parts[1], parts[2]))
                elif len(parts) == 2:
                    entities.append(Person(parts[0], parts[1]))
    except FileNotFoundError:
        print(f"Klaida: Failas {filename} nerastas!")
    except Exception as e:
        print(f"Įvyko klaida: {e}")
    return entities

def main():
    print("--- Gimtadienių priminimo programa ---")
    
    # Nurodome tik failo pavadinimą, nes os.path viršuje suras teisingą kelią
    data = load_birthdays("birthdays.txt")
    
    if not data:
        print("Duomenų failas tuščias arba nerastas.")
        return

    for entity in data:
        print(f"{entity.get_description()} | Likusios dienos: {entity.days_until_birthday()}")

if __name__ == "__main__":
    main()