import random

def play():
    user = input("Rock, Paper or Scissors?! 'r' for rock, 'p' for paper, 's'for scissors \n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'Tie!'
    
    if is_win(user, computer):
        return 'Win!'
    
    return 'Lose!'

def is_win(player,opponent):
    #return true if player wins
    #r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

print(play())