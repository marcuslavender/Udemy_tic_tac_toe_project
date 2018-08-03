# Runs launches a multi user tic tac toe game
from random import randint

board = ['#', '', '', '', '', '', '', '', '', '']
markedNumbers = []
player1selections = []
player2selections = []
winningCombinations = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [3, 6, 9], [2, 5, 8], [1, 5, 9], [3, 5, 7]]
winningCombinations.sort()


# Counter class used to create an object to track player turns
class Counter:
    c = 0

    def __init__(self, count):
        self.c = count


counter = Counter(randint(0, 10))
turnCounter = Counter(1)


# Creates a board which uses the 'board' list to set a 'x' or a '0'

def display_board(boardIndex):
    if not boardIndex:
        print('No board index supplied')
        exit(1)
    else:

        # print(f'       |     |    ')
        # print(f'   {board[1]}   |   {board[2]}  |  {board[3]}  ')
        # print(f'       |     |    ')
        # print('-------------------')
        # print(f'       |     |    ')
        # print(f'   {board[4]}   |   {board[5]}  |  {board[6]}  ')
        # print(f'       |     |    ')
        # print('-------------------')
        # print(f'       |     |    ')
        # print(f'   {board[7]}   |   {board[8]}  |  {board[9]}  ')
        # print(f'       |     |    ')

        print(f'''
  {boardIndex[1]} | {boardIndex[2]} | {boardIndex[3]}
----------
  {boardIndex[4]} | {boardIndex[5]} | {boardIndex[6]}
----------
  {boardIndex[7]} | {boardIndex[8]} | {boardIndex[9]}
            ''')


def get_player_input(markedNumbers):
    if markedNumbers.sort() == [1, 2, 3, 4, 5, 6, 8, 9]:
        print('Draw!')
        exit(0)

    players = {'currentPlayer': '', 'player1': [{'number': int(), 'marker': 'x'}],
               'player2': [{'number': int(), 'marker': '0'}]}
    # whichPlayer = ''
    # currentPlayer = ''

    if counter.c % 2 == 0:
        print('Player 1 your go!')
        currentPlayer = 'player1'
    else:
        print('Player 2 your go!')
        currentPlayer = 'player2'

    validinput = False
    while validinput != True:

        playerInput = int(input('Enter a number form 1-9 '))

        if playerInput in markedNumbers:
            print('Number has already been chosen, try again')
            continue

        if playerInput in range(1, 10):
            print('valid number entered')
            counter.c += 1
            turnCounter.c += 1
            players['currentPlayer'] = currentPlayer
            players[currentPlayer][0]['number'] = playerInput
            return players

        elif playerInput is None:
            print('Nothing entered, try again')

        else:
            print('Invalid input entered, try again: ')


# Function which reads in player input form input function and updates 'board' list with an 'x' or an '0'


def add_input_to_board(players, board):

    if players['currentPlayer'] == 'player1':
        index = players['player1'][0]['number']
        board[index] = players['player1'][0]['marker']

    else:
        index = players['player2'][0]['number']
        board[index] = players['player2'][0]['marker']


# check for winner
def player_count(boardIndex, markedNumbers):

    loop = True

    while loop:

        for a in winningCombinations:

            for b in a:
                # If number in Marked numbers it has already been checked

                if b not in markedNumbers:
                    if boardIndex[b] == 'x':
                        player1selections.append(b)
                        print(player1selections)
                        markedNumbers.append(b)
                    elif boardIndex[b] == '0':
                        player2selections.append(b)
                        markedNumbers.append(b)
        break

def check_for_draw():
    print(counter.c)
    if turnCounter.c > 9:
        print("Game is a draw!")
        exit(0)

def check_winner():
    for a in winningCombinations:
            print(a)

            if a == player1selections:
                    print('''
                    player 1 wins
                    ''')
                    exit(0)

            elif a == player2selections:
                    print('''
                    Player 2 wins
                    ''')
                    exit(0)


# running the game loop is exited only if a player wins or a draw is declared.

end = False

while end != True:
    # Display the board as a grid
    display_board(board)

    # Prompt user for input
    anInput = get_player_input(markedNumbers)

    # Add the input to the game board
    add_input_to_board(anInput, board)

    # Keep track of the player inputs
    player_count(board, markedNumbers)

    # Check if a  player has won, if they have then change quit to = True
    check_winner()

    # check for a draw

    check_for_draw()
