'''Problema 3. Sa se afiseze toate toate puterile lui 3 cuprinse intre 200 si 300.'''
from itertools import count

'''Problema 1. Se citeste de la tastatura o parola. Sa se verifice daca parola introdusa are
    cel putin 10 caractere si nu contine spatiu.
Sa se afiseze un mesaj corespunzator pentru fiecare neregula gasita
    sau mesajul "OK" in cazul in care parola respecta regulile.
    hints: boolean, conditionals'''

parola = input('Parola este: ')
caractere = 0

for i in parola:
    if i in parola:
        caractere += 1
if caractere < 10:
    print('Parola invalida!')
elif caractere > 10:
    print('Parola invalida!')
elif caractere == 10:
    print('Ok')

