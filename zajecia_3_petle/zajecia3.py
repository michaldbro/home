print("Program Paczki")
ile_paczek = int(input("Podaj ilość paczek: "))
if ile_paczek<1:
    print('Brak Paczek!')
else:
    ile_kg_all = 0
    ktora_paczka = 1
    while ile_paczek > 0:
        ile_kg = int(input(f'Podaj wage paczki {ktora_paczka}: '))
        if ile_kg<1 or ile_kg>10:
            break
        else:
            ile_kg_all = ile_kg_all+ile_kg
            ile_paczek -= 1
            ktora_paczka += 1
    print("Podsumowanie:")

    if ile_kg_all//20 <1:
        print('Ilość paczek jaka zostanie wysłana: 1')
    else:
        if ile_kg_all % 20 >0:
            print(f'iloś paczek jaka zostanie wysłana: {(ile_kg_all//20)+1}')
    ile_paczek_wyslano = ((ile_kg_all//20)+1) * 20
    print(f'Wysłano (paczki ważą w sumie): {ile_kg_all}kg')
    print(f'Ilość pustych kg w jednej paczce: {ile_paczek_wyslano-ile_kg_all}')
