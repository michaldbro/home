wiek = int(input("Podaj swoj wiek: "))
haslo = input("Podaj Haslo: ")
#haslo = haslo.lower()
pracownik = input('Czy jestes pracownikiem firmy (tak/nie)' )
pracownik = pracownik.lower()

wiek_ok = wiek >= 18
haslo_ok = haslo == "admin123"
pracownik_ok = pracownik == "tak"

wiek_nok = wiek < 18
haslo_nok = haslo != "admin123"
pracownik_nok = pracownik == "nie"

print('Dostep przyznany!' * ((wiek_ok) + (haslo_ok) + (pracownik_ok)) + 'Dostep nieprzyznany!' * ((wiek_nok) + (haslo_nok) + (pracownik_nok)) )
