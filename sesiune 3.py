import random

'''Instructiunea FOR
-> Ibstrunctiunea for este utilizata pentru a itera (parcurge) o secventa

sinteza de baza:

for element de baza:

for element in secventa:
    bloc de cod

element - > variabila care ia pe rand fiecare valoare din secventa
secventa -> orice obiect iterabil (sir, lista, etc.)'''
from lib2to3.pygram import python_grammar_no_print_statement
from operator import truediv

#literare printr-un sir:
'''for litera in 'itschool':
    print(litera)
  '''
#literare printr-o lista:
'''
for litera in ['itschool', 'programare', 'python']:
    print(litera)
'''

#Explicatie:
'''
itschool este un sir de caractere
bucla for ia fiecare caracter din acest sir, unul cae unul, si ii atribuie variabilei litera, 

iteratie 1 -> litera i
iteratie 2 -> litera t
'''


#Functie range ->
'''
for i in range(5):
    print(i)
'''

#Variante

#range(5) -> 0 pana la 4
#range(1, 6) -> de la 1 pana la 5
#range(1, 10, 2) -> 1, 3, 5, 7, 9 (pas/salt de 2)

#FOR cu ELSE -> Blocul else se executa daca bucla nu a fost intrerupta cu BREAK
'''
for i in range(3):
    print(i)
else:
    print('Bucla s-a termiant normal')
'''
#BREAK & CONINUE

'''
BREAK -> intrerupe bucla
'''
'''
for i in range(10):
    if i == 5:
        break
    print(i)
'''

#CONTINUE -> sare peste restul iteratiei curente
'''
for i in range(10):
    if i == 5:
        continue
    print(i)
'''

#nested loop -> bucla FOR inlantuita
'''
for i in range(3):
    for j in range(2):
        print(f'i = {i} si j = {j}'''
#Explicatie detaliata

'''
range(3) -> genereaza 0, 1, 2 pentru i
pentru fiecare valoare a lui i, bucla interioara va parcurge valorile 0 si 1
print() -> va afisa toate combinatiile posibile dintre valorile lui i si j

i = 0
    j = 0
        i = 0, j = 0
    j = 1
        i = 0, j = 1    

i = 1
    j = 0
        i = 1, j = 0
    j = 1 
        i = 1, j = 1
'''

#Exemple de exercitii
#Afiseaza numerele pare de la 1 la 10
'''
for i in range(1, 11):
    if i % 2 == 0:
        print(i)
'''

#Calculeaza suma numerelor de la 1 la 100
''''
suma = 0
for i in range(1, 101):
    suma += i
print(suma)'''


'''
for i in range(1, 21):
    if i % 2 != 0:
        print(i)'''

'''
cuvant = input('Introdu cuvantul: ')
sir_vocale = 'aeiou'

numar_vocale = 0


for i in cuvant:
    if i in sir_vocale:
        numar_vocale += 1
print(f'{cuvant} are {numar_vocale} vocale')
'''

#Afiseaza un triunghi de *
#Cu n randuri

'''
numar =  int(input('Introdu numarul: '))

for i in range(numar, 0, -1):
    print('*' *i)
'''

'''
WHILE LOOP

While -> este o structura de control care executa un bloc de cod, atata timp cat o conditie este adevarata
while conditie:
    secventa de cod executata daca condita este True
    
'''

#EX
'''x = 0
while x < 5:
    print(x)
    x += 1'''

'''while True:
    print('ruleaza la nesfarsit')'''

'''x = 0
#BREAK
while True:
    if x == 3:
        break
    print(x)
    x += 1'''

#CONTINUE
'''x = 0
while x < 5:
    x += 1
    if x == 3:
        continue
    print(x)'''

'''def test(a, b):
    return a + b

rezultat = test(5, 3)
print(rezultat)'''

#ELSE in WHILE -> se executa doar daca bucla se incheie natural (fara BREAK)

'''x = 0
while x < 3:
    print(x)
    x += 1
else:
    print('S-A OPRIT OK')'''

#Cazuri utilizare

#Numarare

'''n = 10

while n > 0:
    print(n)
    n -= 1'''

#Asteapta conditiile

'''conditie = ''

while conditie != "exit":
    conditie = input('Scrie "exit" pentru a iesi: ').lower()'''

#lower() -> face caracterele dintr-un string dat cu CAPS in litere mici

#Validare input
'''valoare = int(input('Introdu un numar pozitiv: '))
while valoare <= 0:
    valoare = int(input('Numar invalid. Reincearca'))'''

#Citire caracter cu caracter pana la conditie data

'''text = 'python'
i = 0
while i < len(text):
    if text[i] == 'h':
        i += 1
        continue
    print(text[i])
    i += 1'''

#try / except

'''try:
    x = 10 / 0:
except ZeroDivisionError 
    print('Nu merge')'''

'''secret = random.randint(1, 5)
incercari_maxime = 3
incercari = 0
ghicire = None

print('Ghiceste nr. Ai 3 inercari')
while ghicire != secret and incercari < incercari_maxime:
    try:
        ghicire = int(input('Ghiceste numarul(1, 5): '))
        incercari += 1

        if ghicire < secret:
            print('Numarul este mai mare')
        elif ghicire > secret:
            print('Numarul este mai mic')
    except:
        print('Introdu un numar valid: ')
        continue

if ghicire == secret:
    print(f'Ai ghicit din {incercari} incercari')
else:
    print(f'Ai pierdut numarul era: {secret}')
'''

'''optiuni = ['piatra', 'foarfeca', 'hartie']

while True:
    alegere_1 = input(f'Alege o varianta dintre {optiuni}: ')
    if alegere_1 not in optiuni:
        print('Optiune invalida')
        continue
    alegere_2 = random.choice(optiuni)
    print(f'Bot a ales:{alegere_2}')
    if alegere_1 == alegere_2:
        print('Egal')
    elif ((alegere_1 == 'piatra' and alegere_2 == 'foarfeca' ) or
          (alegere_1 == 'hartie' and alegere_2 == 'piatra') or
          (alegere_1 == 'foarfeca' and alegere_2 == 'hartie')):
        print('Ai castigar')
    else:
        print('Ai pierdut')

    iesire = input('Mai incerci?').lower()
    if iesire in ['nu', 'n']:
        print('Salut')
        break'''






