from file_handler import file_handler

saldo = file_handler.saldo
lista_produktow = file_handler.lista_produktow
historia_operacji = file_handler.hist_operacji

print('')
print('Program Księgowy / Magazyn')
print('--------------------------')
while True:
    print('Wybierz i Wprowadź NUMER operacji:')
    wybor = input("""
    1 - saldo
    2 - sprzedaż
    3 - zakup
    4 - konto
    5 - lista
    6 - magazyn
    7 - przegląd
    8 - koniec
    
    ---------------------------
    Twój wybór: """)
    match wybor:
        case "1":
            print('')
            print(f'Aktualnie saldo wynosi: {saldo}')
            kwota = float(input('Podaj kwotę o jaką zmienisz saldo: ')) #float - konwertuje ją na liczbę zmiennoprzecinkową
            if saldo + kwota <0:
                print('Saldo nie może być ujemne!')
            else:
                saldo += kwota
            print(f'Teraz saldo wynosi: {saldo}')
            print('')
            print('---------------------------------')
        case "2":
            print('Podaj dane sprzedanego towaru: ')
            nazwa2 = input("Podaj nazwe produktu: ")
            marka2 = input('Podaj markę: ')
            cena2 = float(input("Podaj cene jednostkową produktu: "))
            ilosc2 = int(input("Podaj ilość sprzedanego produktu: "))
            zla_nazwa = False
            for produkt2 in lista_produktow:  # Pętla iteruje przez listę 'lista_produktow', gdzie każdy element (produkt6) jest słownikiem.
                if produkt2.get("nazwa") == nazwa2 and produkt2.get("marka") == marka2:  # pobiera wartość dla klucza 'nazwa' ze słownika
                    zla_nazwa = True
                    ilosc22 = produkt2["ilosc"]
                    czy_sa = int(ilosc22) - ilosc2
                    if czy_sa > 0:
                        produkt2["ilosc"] -= ilosc2
                        saldo += (cena2*ilosc2)
                        print(f'Sprzedałeś {ilosc2} sztuk towaru')
                        historia_operacji.append(f'Sprzedaż towaru: {nazwa2},{marka2},{ilosc2}')
                        break
                    else:
                        print('Nie ma tyle sztuk na stanie')
                        break
            if not zla_nazwa:
                print('Brak produktu na stanie')
                historia_operacji.append(f'Próba sprzedaży towaru, którego nie było na stanie: {nazwa2},{marka2},{ilosc2}')

        case "3":
            print('Podaj dane kupowanego towaru: ')
            nazwa3 = input("Podaj nazwe produktu: ")
            marka3 = input('Podaj markę: ')
            cena3 = float(input("Podaj cene jednostkową produktu: "))
            ilosc3 = int(input("Podaj ilość zakupionego produktu: "))
            if saldo - (cena3 * ilosc3) <0:
                print('Posiadasz za mało środków do zakupu. Zakup niemożliwy')
                historia_operacji.append(f'Próba zakupu: {nazwa3},{cena3},{ilosc3} sztuk - nieudana, brak funduszy')
                continue
            else:
                saldo -= (cena3 * ilosc3)
            zla_nazwa = False
            for produkt3 in lista_produktow:            #Pętla iteruje przez listę 'lista_produktow', gdzie każdy element (produkt6) jest słownikiem.
                if produkt3.get("nazwa") == nazwa3 and produkt3.get("marka") == marka3: #pobiera wartość dla klucza 'nazwa' ze słownika
                    zla_nazwa = True
                    produkt3["ilosc"] += ilosc3
                    print(f'Kupiłeś {ilosc3} sztuk towaru')
                    historia_operacji.append(f'Zakup towaru: {nazwa3},{marka3},{ilosc3}')
                    break
            if not zla_nazwa:
                lista_produktow.append( # .append do listy dodaje kolejny slownik
                    {"nazwa": nazwa3,
                      "marka": marka3,
                      "ilosc": ilosc3,
                    }
                )
                print(f'Kupiłeś {ilosc3} sztuk towaru')
                historia_operacji.append(f'Zakup towaru: {nazwa3},{marka3},{ilosc3}')

        case "4":
            print(f'Aktualny stan konta wynosi: {saldo}')
            print('')
            print('---------------------------------')
        case "5":
            print('Całkowity stan magazynu:')
            print("")
            print(lista_produktow)
            print('')
            print('---------------------------------')
        case "6": #listowanie slownika, ktory jest w liscie
            print('Stan magazynowy podanego produktu')
            nazwa_prod = input('Podaj NAZWĘ produktu (np. procesor, plyta glowna, karta graficzna): ')
            marka_prod = input('Podaj MARKĘ produktu (np. intel, amd): ')
            zla_nazwa = False
            for produkt6 in lista_produktow:            #Pętla iteruje przez listę 'lista_produktow', gdzie każdy element (produkt6) jest słownikiem.
                if produkt6.get("nazwa") == nazwa_prod and produkt6.get("marka") == marka_prod: #pobiera wartość dla klucza 'nazwa' ze słownika
                    zla_nazwa = True
                    print('Aktualny stan magazynowy: ')
                    print(produkt6["ilosc"])
                    print('---------------------------------')
                    break
            if not zla_nazwa:
                print('Podałeś błędną nazwę.')
                print('---------------------------------')
        case "7":
            od = input("Podaj numer transakcji od którego mam szukać (pierwsza wartość to 1 ): ")
            do = input("Podaj numer transakcji do którego mam szukać: ")
            if od:
                od = int(od)-1 #odejmuje 1, ponieważ lista jest numerowana od 0, a user pewnie poda 1 jako pierwsza pozycje
            else:
                od = 0
            if do:
                do = int(do)
            else:
                do = len(historia_operacji)
            print('---------------------------------')
            print('Historia transakcji: ')
            print(historia_operacji[od:do])
            print('---------------------------------')
        case "8":
            print('Koniec programu. Dziękuję :)')
            break

file_handler.lista_produktow = lista_produktow
file_handler.hist_operacji = historia_operacji
file_handler.saldo = saldo
file_handler.save_lista_produktow_file()
file_handler.save_hist_operacji_file()
file_handler.save_saldo_file()