# Runs launches a multi user tic tac toe game
from random import randint

board = ['#', '', '', '', '', '', '', '', '', '']
markedNumbers = []
player1selections = []
player2selections = []
winningCombinations = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [3, 6, 9], [2, 5, 8], [1, 5, 9], [3, 5, 7]]
winningCombinations.sort()


# Counter class used to create an object to track player turns and also to randomise the starting player.
class Counter:
    c = 0

    def __init__(self, count):
        self.c = count


counter = Counter(randint(0, 10))
turnCounter = Counter(1)


# Creates a board which uses the 'board' list to set a 'x' or a '0'

def display_board(boardindex):
    if not boardindex:
        print('No board index supplied')
        exit(1)
    else:
        print(f'''
  {boardindex[1]} | {boardindex[2]} | {boardindex[3]}
----------
  {boardindex[4]} | {boardindex[5]} | {boardindex[6]}
----------
  {boardindex[7]} | {boardindex[8]} | {boardindex[9]}
            ''')


def get_player_input(markednumbers):
    if markednumbers.sort() == [1, 2, 3, 4, 5, 6, 8, 9]:
        print('Draw!')
        exit(0)

    players = {'currentPlayer': '', 'player1': [{'number': int(), 'marker': 'x'}],
               'player2': [{'number': int(), 'marker': '0'}]}

    if counter.c % 2 == 0:
        print('Player 1 your go!')
        currentplayer = 'player1'
    else:
        print('Player 2 your go!')
        currentplayer = 'player2'

    validinput = False
    while validinput != True:

        playerinput = int(input('Enter a number form 1-9 '))

        if playerinput in markedNumbers:
            print('Number has already been chosen, try again')
            continue

        if playerinput in range(1, 10):
            print('valid number entered')
            counter.c += 1
            turnCounter.c += 1
            players['currentPlayer'] = currentplayer
            players[currentplayer][0]['number'] = playerinput
            return players

        elif playerinput is None:
            print('Nothing entered, try again')

        else:
            print('Invalid input entered, try again: ')


# Function which reads in player input form input function and updates 'board' list with an 'x' or an '0'


def add_input_to_board(players, boardindex):

    if players['currentPlayer'] == 'player1':
        index = players['player1'][0]['number']
        boardindex[index] = players['player1'][0]['marker']

    else:
        index = players['player2'][0]['number']
        boardindex[index] = players['player2'][0]['marker']


# check for winner
def player_count(boardindex, markedNumbers):

    loop = True

    while loop:

        for a in winningCombinations:

            for b in a:
                # If number in Marked numbers it has already been selected

                if b not in markedNumbers:
                    if boardindex[b] == 'x':
                        player1selections.append(b)
                        player1selections.sort()
                        markedNumbers.append(b)
                    elif boardindex[b] == '0':
                        player2selections.append(b)
                        player2selections.sort()
                        markedNumbers.append(b)
        break

def check_for_draw():
    if turnCounter.c > 9:
        print("Game is a draw!")
        exit(0)

def check_winner():
    for combination in winningCombinations:
        if combination == player1selections:
                print('\nPlayer 1 wins \n')
                exit(0)

        elif combination == player2selections:
                print('\nPlayer 2 wins\n')
                exit(0)


# running the game loop is exited only if a player wins or a draw is declared.

end = False

while end != True:
    # Display the board as a grid
    display_board(board)

    # Prompt user for input
    aninput = get_player_input(markedNumbers)

    # Add the input to the game board
    add_input_to_board(aninput, board)

    # Keep track of the player inputs
    player_count(board, markedNumbers)

    # Check if a  player has won, if they have then change quit to = True
    check_winner()

    # check for a draw
    check_for_draw()
