plansza_gry = [[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]]

while True:
    wszystkie_x = all(element == 'X' for rzad in plansza_gry for element in rzad)
    #funkcja ALL, sprawdza, czy wszystkie elementy w iterowalnym obiekcie (np. liście, krotce, zbiorze) są prawdziwe (czyli nie są , ,  lub pustymi wartościami). Jeśli tak, zwraca , w przeciwnym razie
    if wszystkie_x:
        break
    for rzad in plansza_gry:
            for element in rzad:
                if element != 'X':
                     #print(element)
                     wartosc_do_usuniecia = int(input("gdzie wsatwić X: "))  # Wybór wartości do usunięcia
                     for i in range(len(plansza_gry)):
                         for j in range(len(plansza_gry[i])):
                             if plansza_gry[i][j] == wartosc_do_usuniecia:
                                 plansza_gry[i][j] = 'X'
                                 print('aktualny stan gry')
                                 for rzad in plansza_gry:
                                     print(rzad)
                     break
print('Koniec GRY')