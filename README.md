# Gimtadienių priminimo programa (Birthday Reminder App)

Ši programa skirta valdyti ir sekti artėjančius gimtadienius. Duomenys nuskaitomi iš tekstinio failo, o informacija atvaizduojama terminale.

## Realizuoti OOP reikalavimai:

1. **Enkapsuliacija (Encapsulation):** - Klasėje `Person` gimimo data yra paslėpta naudojant privatų kintamąjį `self.__birth_date`. 
   - Prieiga prie jos vykdoma per „getter“ metodą `get_birth_date()`.

2. **Paveldėjimas (Inheritance):** - Klasė `FamilyMember` paveldi savybes iš bazinės klasės `Person`. 
   - Naudojama `super().__init__` konstrukcija.

3. **Polimorfizmas (Polymorphism):** - Naudojamas bendras metodas `get_description()`, kuris veikia skirtingai `Person` ir `FamilyMember` objektams.
   - Programos vykdymo metu ciklas kreipiasi į objektus per bendrą sąsają.

4. **Abstrakcija (Abstraction):** - Sukurta abstraktoji bazinė klasė `BirthdayEntity` naudojant `abc` modulį.
   - Apibrėžtas abstraktus metodas `get_description()`, kurį privalo realizuoti visos vaikinės klasės.

## Projekto struktūra ir moduliavimas:

Programa yra suskaidyta į atskirus modulius, kaip reikalaujama užduotyje:
- `main.py` – pagrindinis programos failas (logika, duomenų užkrovimas).
- `models.py` – duomenų modeliai ir klasės.
- `birthdays.txt` – išorinė duomenų saugykla (duomenų apdorojimas iš failo).

## Kaip paleisti:
1. Įsitikinkite, kad turite įdiegtą Python 3.
2. Paleiskite komandą: `python main.py`