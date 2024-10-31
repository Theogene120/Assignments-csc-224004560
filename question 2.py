#python program accept and inform amount due
from dis import code_info

valid_coin=[25,10,5]
amount_due=50
while True:
    print(f'Amount due:{amount_due}')
    coin=int(input('Insert coin(25,10,5):'))
    if coin in valid_coin:
        amount_due-=coin
    else:
        print('Invalid coin')
    if amount_due<=0:
        print('THANK YOU, NO AMOUNT DUE')
        break