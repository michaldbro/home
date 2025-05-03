punktacja = 0
#pyt1
odpowiedz = input('1. Typ zmiennej 5: ')
punktacja += 1 * (odpowiedz.lower() == "int")

#pyt2
odpowiedz = input('pyt')
punktacja += 1 * (odpowiedz.lower()= 'xx')

print('zaliczony ' * (punktacja >= 7) + 'niezaliczony' * (punktacja <7))
