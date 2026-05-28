import random,sys

print("ROCK, PAPER , SCISSORS")

# this variables keeps track of wins, loses, ties
win = 0
lose = 0
tie = 0

while True: # this is the main game loop
    print("%s wins,%s lose,%s tie" % (win,lose,tie))

    while True:  # the player input loop
        player_move = input("Enter your move: (r)ock, (p)aper, (s)cissors. or q to quit: ")
        if player_move == 'q':
            sys.exit() # Quit the program
        elif player_move == "r" or player_move == 'p' or player_move == 's':
            break # player exit the input loop
        else:
            print("You have to enter r,p,s or q")
    
    # Display player's move
    if player_move == 'r':
        print("ROCK verses...")
    elif player_move == 'p':
        print("PAPER verses...")
    elif player_move == 's':
        print("SCISSORS verses...")

    # Display computer's move
    move_number = random.randint(1,3)
    if move_number == 1:
        computer_move = 'r'
        print("ROCK")
    elif move_number == 2:
        computer_move = 'p'
        print("PAPER")
    elif move_number == 3:
        computer_move = 's'
        print("SCISSORS")
        
    # Display result and record the win/loes/tie
    if player_move == computer_move:
        print("It is a tie!")
        tie = tie + 1
    elif player_move == 'r' and computer_move == 's':
        print("You Win!")
        win = win + 1
    elif player_move == 'p' and computer_move == 'r':
        print("You Win!")
        win = win + 1
    elif player_move == 's' and computer_move == 'p':
        print("You Win!")
        win = win + 1
    elif player_move == 'r' and computer_move == 'p':
        print("You Lose!")
        lose = lose + 1
    elif player_move == 'p' and computer_move == 's':
        print("You Lose!")
        lose = lose + 1
    elif player_move == 's' and computer_move == 'r':
        print("You Lose!")
        lose = lose + 1
    