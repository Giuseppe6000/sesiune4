

'''
o conditie este o expresie care poate fi adevarata(True) sau falsa(False)
pe baza ei putem decide daca anumite blocuri de cod se vor executa sau nu
'''

'''
if conditie:
    coduse se executa daca conditia este adevarata(True)
elif:
    codul se executa daca prima conditie nu a fost true, dar acesta este
else: 
    codul se executa daca niciuna din conditiile de mai sus nu au fost adevarate'''

'''
#exemplu

varsta = 18
'''
'''if varsta >= 18:
    print('Ai voie sa votezi')
    if varsta == 18:
        print('major')
else:
    print('Esti inca prea tanar ca sa votezi')
''''''
''''''
Operatori de comparatie

== -> Egal cu Ex: a == b
!= -> Diferit de Ex: a != b
> -> Mai mare decat
< -> Mai mic decat
>= -> Mai mare sau egal
<= -> Mai mic sau egal
'''
''''''
'''numar = 10

if numar == 10:
    print('primul if')
else:
    print('al doilea if')
    
if numar != 1
    print('numarul este diferit de 1')
else:
    print('numarul este 1')
''''''
'''
'''temperatura = 30

if temperatura < 25:
    print('e cald')
else:
    print('e totusi frigut')'''
'''
''''''
operatori logici

and -> ambele conditii trebuie sa fie True
or-> cel putin o conditie trebuie sa fie True
not -> inverseaza valoarea

''''''

#ex op logici
#and
'''
'''arsta = 20
nationalitate = 'roman'

if varsta >= 18 and nationalitate == 'roman':
    print('poti vota in romania')
''''''
'''
# or

'''zi = 'sambata'

if zi == 'sambata' or zi == 'duminica'
    print('este week-end')
else:
    print('alta zi')'''


# not

'''vremea = False

if not vremea:
    print('putem iesi in oras')
else:
    print('ploua, stam in casa')'''

'''
Valori considerate Falsy in Python
- None
- False
- 0
- '' (sir gol)
- {}
-set()
'''

#ex 1
'''x = 0
if not x:
    print('este zero')

#ex 2
x = ''

if not x:
    print('este string gol')
    
x = [1,2,3]

#ex 3
if not x:
    print('lista e goala')
else:
    print('lista contine elemente')
'''

'''x = 3
if x % 2 == 0: print('Par')

x = 7 
rezultat = 'par' if x % 2 == 0 else 'Impar'
print('razultat')
'''

'''litera = 'a'

if litera in 'aeiou':
    print('Este vocala')
'''

'''x = 7

if 5 < x < 10:
    print(f"{x} este intre 5 si 10")
'''

'''nume = 'Alex'

if nume:
    print('Ai introdus un nume')'''

#nested if

'''varsta = int(input('Introdu varsta ta:'))

if varsta >= 18:
    print('Esti adult')

    if varsta >= 65:
        print('esti pensionar')
    else:
        print('esti in campul muncii')
else:
    print('esti minor')
'''
'''
numar = int(input('Numar ales: '))

if numar % 2 == 0:
    print(f'Numarul {numar} este par')
else:
    print(f'Numarul {numar} este impar')


if numar > 0 and numar % 2 == 0:
    print('pozitiv si par')
elif numar < 0 and numar % 2 != 0:
    print('negativ si impar')
elif numar < 0 and numar % 2 == 0:
    print('negativ si par')
elif numar > 0 and numar % 2 != 0:
    print('pozitiv impar')
else:
    print('zero)
'''

'''numar1 = int(input('Numarul 1:'))
numar2 = int(input('Numarul 2:'))

operatie = input('Introdu operatie:')

if operatie == '+':
    print(numar1 + numar2)
elif operatie == '-':
    print(numar1 - numar2)
elif operatie == '*':
    print(numar1 * numar2)
elif operatie == '/' and numar2 != 0:
    print(numar1 / numar2)
else:
    print('Operatie inexistenta')
'''


'''
nr1 = int(input('Primul numar: '))
nr2 = int(input('Al doilea numar: '))

if nr1 > nr2:
    print(f'Numarul {nr1} este mai mare')
elif nr1 < nr2:
    print(f'Numarul {nr1} este mai mic')
else:
    print('Numerele sunt egale')
'''
'''
an = int(input('Anul ales este: '))
if (an % 4 == 0 and an % 100 != 0) or (an % 400 == 0):
    print('An bisect')
else:
    print('Nu i an bisect')
'''

