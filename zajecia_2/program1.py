wiek = int(input("Podaj swoj wiek: "))
zgoda = input("czy masz zgode rodzica?  tak / nie ")
zgoda = zgoda.lower()

zgoda_potwierdzona = zgoda == "tak"
ma_dostep_18plus = wiek >=18
ma_dostep_13plus = wiek >=13 or zgoda_potwierdzona

print(f'user ma {wiek} lat')
print (f'user ma zgode rodziciow {zgoda_potwierdzona}')

# mnozymy te zmienne wedlug reguly ze 0 to falasz a 1 prawda 0* cos to zero 1 * cos to cos ;)
print('filmy 18+' * ma_dostep_18plus + 'filmy 13' * ma_dostep_13plus + 'tylko bajki' * (not ma_dostep_18plus and not ma_dostep_13plus))

#-----
#print('natych iterwencja' * (serwer_awaria == "tak" and baza_awaria == "tak") + --kolejne warunki--)
