import random,sys

print ('ROCK,PAPER,SCISSORS')
result={'w':0,'l':0,'t':0}
hand={'r':'ROCK','p':'PAPER','s':'SCISSORS'}
rps=['r','p','s']
while True:
    print(str(result['w'])+'Wins'+str(result['l'])+'Losses'+str(result['t'])+'Ties')
    while True:
        print('Enter your move: (r)ock (p)aper (s)cissors')
        player_move=input()
        if player_move == 'q':
            sys.exit()
        if player_move == 'r' or player_move == 'p' or player_move =='s':
            break
    print(f"{hand[player_move]} versus...")
    random_number = random.randint(0,2)
    print(f"{rps[random_number]}")
    computer_move=rps[random_number]
    if player_move == computer_move:
        print('It is a tie!')
        result['t']+=1
    elif (player_move == 'r' and computer_move == 's') or (player_move == 'p' and computer_move == 'r' )or (player_move == 's' and computer_move == 'p'):
        print('You win!')
        result['w']+=1
    else:
        print('You lose!')
        result['l']+=1
