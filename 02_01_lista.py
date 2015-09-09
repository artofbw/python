#coding: utf-8

moja_lista = []

moja_lista = [1, 3.14, 'Ala ma kota']

# moja_lista. wyświetla listę komend dla listy

moja_lista.append(42)
moja_lista.append(52)

#print(moja_lista)

inna = [6,7,8]

moja_lista.extend(inna)

#print(moja_lista)

#moja_lista.append(inna) #doda listę do listy

moja_lista.remove('Ala ma kota')

#print(moja_lista)

#print(moja_lista[-1]) #ostatni element listy
#print(moja_lista[-2]) #przedostatni element listy

#print(moja_lista.pop(1))

#print(moja_lista[0])

x = moja_lista[0]
#print(x)

moja_lista[3] = 111 #wpisze w 3 index listy nowa wartosc
#moja_lista[10] = 222 / nie utworzy nie istniejacego indexu

#print(moja_lista)

print(len(moja_lista))

moja_lista.extend(moja_lista) # - powieli liste


print(moja_lista)
print(moja_lista[2:5])

for i in moja_lista[2:5]:
    print(i)

# moja_lista[2:9:2] = [gdzie zaczac: gdzie skonczyc: co ktory element]

for i in moja_lista[2:9:2]:
    print(i)