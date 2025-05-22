

class uczen:
    def __init__(self, imie_nazwisko, jaka_klasa):
        self.imie_nazwisko = imie_nazwisko
        self.jaka_klasa = jaka_klasa
    def __repr__(self):
        return f"{self.imie_nazwisko} {self.jaka_klasa}"

class wychowawca:
    def __init__(self, imie_nazwisko1, jaka_klasa1):
        self.imie_nazwisko = imie_nazwisko1
        self.jaka_klasa = jaka_klasa1
    def __repr__(self):
        return f"{self.imie_nazwisko} {self.jaka_klasa}"

class nauczyciel:
    def __init__(self, imie_nazwisko2, jaki_przedmiot2, ktora_klasa2):
        self.imie_nazwisko = imie_nazwisko2
        self.jaki_przedmiot = jaki_przedmiot2
        self.ktora_klasa = ktora_klasa2

    def dodaj_klase(self, ktora_klasa2):
        self.ktora_klasa.append(ktora_klasa2)

    def __repr__(self):
        return f"{self.imie_nazwisko} {self.jaki_przedmiot} {self.ktora_klasa}"

szkola = {
    "uczniowie": [
        uczen("Adam Nowak", "1A"),
        uczen("Piotr Adamek", "3B"),
        uczen("Marcin Kwiatek", "2C")
    ],
    "wychowawca": [
        wychowawca("Piotr Kowalski", "1A"),
        wychowawca("Zygmunt Nowak", "3B"),
        wychowawca("Filip Światek", "2C")
    ],
    "nauczyciel": [
        nauczyciel("Piotr Kowalski", "polski", ["1A", "3C"]),
        nauczyciel("Zygmunt Nowak", "matematyka", ["3B", "6E"]),
        nauczyciel("Filip Światek", "bilogia", ["2C", "8C"])
    ]
}

#-----------------------------------------------------------------------------
while True:
    print('*****')
    print('Program Baza Szkolna')
    wybor_menu = input('Wybierz numer opcji:\n1. Utwórz\n2. Zarządzaj\n3. Koniec\n Twój wybór: ')
    print('*****')
    match wybor_menu:

        case "1":
            print('Proces tworzenia użytkownika\n ')
            dodaj = int(input('Podaj (numer) kogo mam dodać:\n1. Uczeń\n2. Nauczyciel\n3. Wychowawca\n Twój wybór: '))
            if dodaj == 1:
                imie_nazwisko = input('Podaj Imię i Nazwisko: ')
                jaka_klasa = input ('Podaj nazwę klasy: ')
                nowy_uczen = uczen(imie_nazwisko, jaka_klasa)
                szkola["uczniowie"].append(nowy_uczen)
                print(f"Dodałeś ucznia: {nowy_uczen}")
            elif dodaj == 2:
                imie_nazwisko = input('Podaj Imię i Nazwisko Nauczyciela: ')
                jaka_klasa = input('Podaj nazwę prowadzonej klasy: ')
                nowy_wych = wychowawca(imie_nazwisko, jaka_klasa)
                szkola["wychowawca"].append(nowy_wych)
                print(f"Dodałeś wychowawcę: {nowy_wych}")
            elif dodaj ==3:
                imie_nazwisko = input('Podaj Imię i Nazwisko Wychowawcy: ')
                przedmiot = input('Podaj nazwę przedmiotu prowadzącego: ')
                lista_klas = []
                while True:
                    jaka_klasa = input('Podaj nazwę klasy: ')
                    if jaka_klasa: #if sprawdza, czy podana zmienna nie jest pusta
                        lista_klas.append(jaka_klasa)
                    else:
                        break
                nowa_klasa = nauczyciel(imie_nazwisko, przedmiot, lista_klas)
                szkola["nauczyciel"].append(nowa_klasa)
                print(f"Dodałeś Nauczyciela i klasy: {nowa_klasa}")
        case "2":
            zarzadzanie = input(
               "Co chcesz przejrzeć?:\n"
               "1. klasa\n"
               "2. uczen\n"
               "3. nauczyciel\n"
               "4. wychowawca\n"
            )
            match zarzadzanie:
                case "1":
                    wyb_klasy = input('Podaj numer klasy: ')

        case "3":
            break
