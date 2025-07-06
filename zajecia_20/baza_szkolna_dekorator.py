from monitoring import monitor

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
    def __init__(self, imie_nazwisko2, jaki_przedmiot2, ktora_klasa2=None):
        self.imie_nazwisko = imie_nazwisko2
        self.jaki_przedmiot = jaki_przedmiot2
        self.ktora_klasa = ktora_klasa2

   # def dodaj_klase(self, ktora_klasa2):
     #   self.ktora_klasa.append(ktora_klasa2)

    def __repr__(self):
        return f"{self.imie_nazwisko} {self.jaki_przedmiot} {self.ktora_klasa}"

szkola = {
    "uczniowie": [
        uczen("Adam Nowak", "1A"),
        uczen("Piotr Adamek", "3B"),
        uczen("Marcin Kwiatek", "1A"),
        uczen("Aleksander Bok", "2C")
    ],
    "wychowawca": [
        wychowawca("P", "1A"),
        wychowawca("Zygmunt Nowak", "3B"),
        wychowawca("Filip Światek", "2C")
    ],
    "nauczyciel": [
        nauczyciel("Piotr Kowalski", "polski", ["1A", "2C"]),
        nauczyciel("Zygmunt Nowak", "matematyka", ["3B", "6E"]),
        nauczyciel("Filip Światek", "bilogia", ["2C", "8C"]),
        nauczyciel("Anatol Kobza", "geografia", ["1A", "8C"])
    ]
}
@monitor
def wyszukaj_ucznia(wyb_klasy):
    uczniowie1 =[]
    for klasa_szukaj in szkola.get("uczniowie",[]):
        if klasa_szukaj.jaka_klasa == wyb_klasy:
            uczniowie1.append(klasa_szukaj.imie_nazwisko)
    return uczniowie1
    if uczniowie1:
        return uczniowie1[0]
    else:
        return None

@monitor
def wyszukaj_wychowawce_3(wyb_klasy3): #uzycie w case4
    wychowawca3 =[]
    wychowawca33 = None
    for klasa_szukaj in szkola.get("wychowawca"):
        if klasa_szukaj.imie_nazwisko == wyb_klasy3:
            wychowawca3.append(klasa_szukaj.jaka_klasa)
            wychowawca33 = wychowawca3[0]
    return wychowawca33

@monitor
def wyszukaj_wychowawce(wyb_klasy1):
    wychowawca1 =[]
    for klasa_szukaj in szkola.get("wychowawca"):
        if klasa_szukaj.jaka_klasa == wyb_klasy1:
            wychowawca1.append(klasa_szukaj.imie_nazwisko)
    return wychowawca1

@monitor
def wyszukaj_lekcje_n(wyb_klasy2):
    nauczycie = []
    nauczycie1 = []
    for klasa_szukaj in szkola.get("nauczyciel"):
        if wyb_klasy2 in klasa_szukaj.ktora_klasa:
            nauczycie.append(klasa_szukaj.jaki_przedmiot)
            nauczycie1.append(klasa_szukaj.imie_nazwisko)
    return nauczycie, nauczycie1

@monitor
def wyszukaj_imie_ucznia(wyb_imie):
    uczniowie2 = []
    for imie_szukaj in szkola.get("uczniowie", []):  # Zabezpieczenie przed barkiem danych, podstawi pusta liste
        if imie_szukaj.imie_nazwisko == wyb_imie:
            uczniowie2.append(imie_szukaj.jaka_klasa)
    if uczniowie2:  # Sprawdzenie, czy nie puste
        return uczniowie2[0]
    else:
        return None

@monitor
def wyszukaj_nauczyciela(imie):
    nauczycie = []
    for klasa_szukaj in szkola.get("nauczyciel"):
        if klasa_szukaj.imie_nazwisko == imie:
            nauczycie.append(klasa_szukaj.ktora_klasa)
    return nauczycie

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
            if dodaj == 1: #Uczen
                imie_nazwisko = input('Podaj Imię i Nazwisko: ')
                jaka_klasa = input ('Podaj nazwę klasy: ')
                nowy_uczen = uczen(imie_nazwisko, jaka_klasa)
                szkola["uczniowie"].append(nowy_uczen)
                print(f"Dodałeś ucznia: {nowy_uczen}")
            elif dodaj == 3: #Wychowawca
                imie_nazwisko = input('Podaj Imię i Nazwisko Wychowawcy: ')
                jaka_klasa1 = input('Podaj nazwę prowadzonej klasy: ')
                nowy_wych = wychowawca(imie_nazwisko, jaka_klasa1)
                szkola["wychowawca"].append(nowy_wych)
                print(f"Dodałeś Wychowawcę: {nowy_wych}")
            elif dodaj == 2: #Nauczyciel
                imie_nazwisko = input('Podaj Imię i Nazwisko Nauczyciela: ')
                przedmiot = input('Podaj nazwę przedmiotu prowadzącego: ')
                lista_klas = []
                while True:
                    ktora_klasa2 = input('Podaj nazwę klasy: ')
                    if ktora_klasa2: #if "bez warunku" sprawdza, czy podana zmienna nie jest pusta
                        lista_klas.append(ktora_klasa2)
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
                case "1": #klasa
                    wyb_klasy = input('Podaj numer klasy: ')
                    wyszukaj_u = wyszukaj_ucznia(wyb_klasy)
                    wyszukaj_w = wyszukaj_wychowawce(wyb_klasy)
                    print(f"Uczniowie: {wyszukaj_u}")
                    print(f"Wychowawca: {wyszukaj_w}")

                case "2": # uczen
                    wyb_imie = input('Podaj imię i nazwisko ucznia: ')
                    wyszukaj_i = wyszukaj_imie_ucznia(wyb_imie)
                    if wyszukaj_i:
                        print(f"Nr klasy: {wyszukaj_i}")
                        wyszukaj_l, wyszukaj_l2 = wyszukaj_lekcje_n(wyszukaj_i)
                        if wyszukaj_l and wyszukaj_l2:
                            print("Przedmioty:", wyszukaj_l)
                            print("Nauczyciele:", wyszukaj_l2)
                        else:
                            print("Nie znaleziono żadnych lekcji dla podanej klasy.")
                    else:
                        print("Imię ucznia nie pasuje do danych w bazie.")

                case "3":  # nauczyciel
                    imie_n = input('Podaj imie i nazwisko nauczyciela: ')
                    wyszukaj_n = wyszukaj_nauczyciela(imie_n)
                    print(f"Prowadzone Klasy: {wyszukaj_n}")
                case "4": #wychowawca
                    wyb_imie = input('Podaj imię i nazwisko Wychowawcy: ')
                    wyszukaj_i = wyszukaj_wychowawce_3(wyb_imie)
                    if wyszukaj_i:
                        print(f"Nr klasy: {wyszukaj_i}")
                        wyszukaj_l2 = wyszukaj_ucznia(wyszukaj_i)
                        if wyszukaj_l2:
                            print("Uczniowie:", wyszukaj_l2)
                        else:
                            print("Nie znaleziono.")
                    else:
                        print("Imię Wychowawcy nie pasuje do danych w bazie.")
        case "3":
            break
