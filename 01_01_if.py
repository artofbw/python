#coding: utf-8

# if warunek :
#     blok kodu wykonywany, gdy warunek jest spełniony
# elif inny_warunek :
#     blok kodu wykonywany, gdy warunek nie jest spełniony ale inny_warunek jest spełniony
# else :
#     blok kodu wykonywany, gdy żaden z wcześniejszych warunków nie został spełniony



# liczba = input('Podaj liczbę: ')
# print(type(liczba))
# if int(liczba) % 2 == 0:
#     print('Liczba', liczba, 'jest parzysta')
# elif int(liczba) % 2 == 1:
#     print(' Liczba', liczba, 'jest nieparzysta')
# else:
#     print('Liczba', liczba,  'jest dziwna')



####################### PĘTLE #################

# while warunek :
#     blok kodu


# liczba = 1
# while liczba < 10:
#     print('Python jest spoko')
#     liczba = liczba + 1

while True:
    liczba = int(input('Podaj liczbę parzystą: '))
    if liczba % 2 == 0:
        print('Brawo')
        break
    elif liczba == -1:
        print('Ehhh...')
        continue
    print('Podaj parzystą!')

# Wykonuje się tak długo, jak długo spełniony jest warunek
