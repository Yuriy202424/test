import random

you = {'hp' : 30,
       'atk' : 10,
       'money' : 30}

    
enemies = {
    1: {'name': 'Ork','hp': 10, 'atk': 15},
    2: {'name': 'Elf','hp': 20, 'atk': 8},
    3: {'name': 'Spider','hp': 15, 'atk': 12}
 }

def fight():
    while you['hp'] > 0:
        a(['hp']) - you.get(['atk'])
        print(a(['hp']) - you.get(['atk']))
        
    

start = input(('(Y/N) Are you ready?: '))

if start.lower() == 'y':
    a = random.randint(1,4)
    print(f'You are fighting {enemies.get(a)}!')
    fight()




else:
    print('Error')

    
#     enemies = {
#     'spider': {'hp': 10, 'atk': 15},
#     'ork': {'hp': 20, 'atk': 8},
#     'elf': {'hp': 15, 'atk': 12}
# }