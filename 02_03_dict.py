#coding: utf-8

d = {}

d = {'Ala': 'kot', 'Ola': 'pies'} # Ala = klucz, kot = wartość - jako całość item (element) słownika

zwierzak = d['Ala']
#print(zwierzak)

d['Tomek'] = 'pyton'

# print(d)

# for i in d:
#     print(i) # KLUCZ
#
# for i in d:
#     print(d[i]) # WARTOŚĆ

# print(d.items())

# for key, value in d.items():
#     print(key, value)

l1 = [1,2,3,4,5,6,7]
l2 = [9,8,7,6,5]

# for w1, w2 in zip(l1, l2):
#     print(w1, w2)
#
d.update({'Ola': 'chomik', 'Jacek': 'lew'})
#
# print(d)

d.get