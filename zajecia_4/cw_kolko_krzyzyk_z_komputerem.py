import random

plansza_gry = [[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]]
#prinotwanie macierzy
for rzad in plansza_gry:
    print(rzad)
while True:
    wszystkie_x = all(element == 'X' for rzad in plansza_gry for element in rzad)
    if wszystkie_x:
        print("Koniec GRY!")
        break
#pierwszy ruch gracza
    wartosc_do_usuniecia = int(input("Gdzie wstawić X: "))

    for i in range(len(plansza_gry)):
        for j in range(len(plansza_gry[i])):
            if plansza_gry[i][j] == wartosc_do_usuniecia:
                plansza_gry[i][j] = 'X'
                print('Aktualny stan gry:')
                for rzad in plansza_gry:
                    print(rzad)

                # Znalezienie wolnego sąsiedniego pola dla komputera, przelatuje przez macierz i tworzy nowa maciez aktualna z x wtawionymi
                sasiednie_pola = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
                dostepne_pola = []

                for x, y in sasiednie_pola:
                    if 0 <= x < len(plansza_gry) and 0 <= y < len(plansza_gry[x]) and plansza_gry[x][y] not in ('X', 'Y'):
                        dostepne_pola.append((x, y)) #append dodaje nowe wartosci do listy

                # Jeśli istnieją wolne pola obok, komputer wykonuje ruch
                if dostepne_pola:
                    x, y = random.choice(dostepne_pola)  # Wybór wolnego sąsiada
                    plansza_gry[x][y] = 'Y'
                    print("Komputer wykonał ruch:")
                    for rzad in plansza_gry:
                        print(rzad)
                else:
                    print("Brak wolnych pól obok. KONIEC GRY!")
                    exit()  # Zakończenie gry

                break