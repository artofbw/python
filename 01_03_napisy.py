#coding: utf-8

# napis_1 = "Napis 1"
# napis_2 = 'Napis 2'
# napis_3 = """Napis 3
# wielolinijkowy """
# napis_4 = '''Napis 4
# też wielolinijkowy '''
#
# napis_3a = "Napis 3\nwielolinijkowy"
#
# enter = "\n"
# tabulator = "\t"
# cudzyslow = " \" "
# apostrof = ' \' '
#
# print(napis_1, napis_2, napis_3, napis_3a, napis_4, enter, tabulator, cudzyslow, apostrof)


####################### FORMATOWANIE NAPISÓW %%%%%%%%%%%%%%%%%%%%%

liczba = 5.25
podatek = 0.25

napis = "Kwota do zapłaty: %5.2f zł, z czego podatek: %.2f zł." % (liczba, podatek)

print(napis)