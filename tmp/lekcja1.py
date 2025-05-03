print("Program \nKARTKA URODZINOWA")
print('Podaj dane do generacji kartki urodzinowej\n Dane odbiorcy')
imie = input('Podaj imie:')
rok = input('Podaj rok urodzenia:')
print('Podaj dane Nadawcy')
imie_n = input('Podaj imie nadawcy:')
rok_teraz = 2025
ile_lat = (rok_teraz-int(rok))
#print(ile_lat)
print('Generuje kartkę.............')
print(f"{imie}, wszystkiego najlepszego z okazji {ile_lat} urodzin!")
print(f"{imie_n}")

