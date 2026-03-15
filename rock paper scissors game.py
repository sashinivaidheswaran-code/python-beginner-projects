import random

player=input('Enter your choice (rock,paper,scissor):')
game=['rock','paper','scissor']
computer=random.choice(game)
choice={'player:':player,'computer':computer}
print(choice)

def check_win(player,compueter):
    if player==computer:
        return "It's a tie"

    elif player=='rock':
        if computer=='scissor':
            return 'Rock smashes Scissors. You win!!'
        else:
            return 'Paper covers Rock. You lose!!'
    elif player=='scissor':
        if computer=='rock':
            return 'Rock smashes Scissors. You lose!!'
        else:
            return 'Scissors cut paper. You win!!'
    elif player=='paper':
        if computer=='rock':
            return 'Paper covers Rock. You win!!'
        else:
            return 'Scissors cut paper. You lose!!'

result=check_win(player,computer)
print(result)
