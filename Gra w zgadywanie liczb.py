import random

def gra_w_zgadywanie():
    print('Witaj w grze w zgadywanie!')
    print('Mam na myśli liczbę w zakresie od 1 do 100')
    while True:
        liczba = random.randrange(1,101)
        proba = 0
        while True:
            try:
                zgadywanie = int(input('Podaj liczbę z zakresu od 1 do 100 '))
                proba += 1
                if zgadywanie == liczba:
                    print(f'Brawo Wygrałeś!!!  Liczba prób wynosiła {proba}')
                    break
                elif zgadywanie > liczba:
                    print('Liczba którą podałeś jest za duża')
                    print('-' * 30)
                elif zgadywanie < liczba:
                    print('Liczba którą podałeś jest za mała')
                    print('-' * 30)
            except ValueError:
                print('Nie poprawna wartość')
        jeszcze_raz = input('Czy chcesz zagrać jeszcze raz? tak/nie ').lower()
        if jeszcze_raz != 'tak':
            break


gra_w_zgadywanie()