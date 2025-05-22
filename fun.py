import random

player_card1 = random.randint(1, 11)
player_card2 = random.randint(1, 11)
total_player = player_card1 + player_card2
dealer_card1 = random.randint(1, 11)
dealer_card2 = random.randint(1, 11)
total_dealer = dealer_card1 + dealer_card2

print(f'Players first card:{player_card1} & second card:{player_card2}')
print(f'Total player points:{total_player}')
print(f'Dealers first card:{dealer_card1} & second card:{dealer_card2}')
print(f'Total dealer points:{total_dealer}')

Hit = input('Another card? Yes/No: ')
if Hit == 'da':
    player_card3 = random.randint(1, 11)
    total_player2 = total_player + player_card3
    print(f'Hit:{player_card3}')
    print(f'Total: {total_player2}')

if total_dealer < 17:
    dealer_card3 = random.randint(1, 11)
    dealer_total2 = total_dealer + dealer_card3
    print(f'Hit:{dealer_card3}')
    print(f'Total D:{dealer_total2}')


if total_dealer == 21:
    print('Dealer Wins')
elif total_player == 21:
    print('Player Win')


