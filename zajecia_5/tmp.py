user = {
    "imie": "michal",
    "nazwisko": "dbro",
    "wiek": 20,
    "czy_uczen" :True,
}

#print(user)


#jak pobierc wartosi z listy

#print(user["wiek"])
#(user["imie"]) #:- user to slownik a imie to klucz to wartosc ze slownika,wyswietli michal (tu jak podasz zly klucz to error bedzie.
#print(user["imie"].lower()) :-wyrzuci dane małymi liuterami

#print(user.get("plec")) :- ta opcja pozwala na wyciaganie danych ze slownika, nawet jak jej nie ma i nie wywali errora

zmienna6 = "michal"
if zmienna6 in user.values():
    print(user["wiek"])
'''
for zmienna6 in user.values():
    if zmienna6_1.get("imie") == zmienna6:
     print(user["wiek"])
else:
    print('zla nazwa')
    
    '''
#or key in user.keys():
  #  print(key)