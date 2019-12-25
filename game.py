def displayBoard(board):
    print(board[7], ' | ', board[8], ' | ', board[9], sep='')
    print('---------')
    print(board[4], ' | ', board[5], ' | ', board[6], sep='')
    print('---------')
    print(board[1], ' | ', board[2], ' | ', board[3], sep='')


def playerInput(chainNumb):
    pPos = 0
    while pPos > 9 or pPos < 1 or gameBoard[pPos] != ' ':
        print('Player ', chainNumb, ' - Select position from 1 to 9: ', end='')
        sPos = input()
        if sPos.isdigit():
            pPos = int(sPos)
        print('Error input, not digit or position is not possible')
        displayBoard(gameBoard)
    return pPos


def checkWin(pSign):
    if gameBoard[1] == gameBoard[2] == gameBoard[3] == pSign:
        return pSign
    elif gameBoard[4] == gameBoard[5] == gameBoard[6] == pSign:
        return pSign
    elif gameBoard[7] == gameBoard[8] == gameBoard[9] == pSign:
        return pSign
    else:
        return '#'


testBoard = ['#', 'O', 'X', 'O', 'X', 'X', 'O', 'X', 'X', 'O']
gameBoard = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

print('Tic Tac Toe')
p1Sign = input('Player 1 - Select X or O: ')
while p1Sign != 'X' and p1Sign != 'O':
    print('Error input')
    p1Sign = input('Select X or O: ')
if p1Sign == 'X':
    p2Sign = 'O'
else:
    p2Sign = 'X'

for i in range(1, 9 + 1):
    print('\n' * 10)
    displayBoard(gameBoard)
    chainPlayer = (i + 1) % 2 + 1
    p1Pos = playerInput(chainPlayer)
    if chainPlayer == 1:
        gameBoard[p1Pos] = p1Sign
    else:
        gameBoard[p1Pos] = p2Sign
    if checkWin(p1Sign) != '#':
        break
displayBoard(gameBoard)
print('Player', chainPlayer, '-', p1Sign, 'wins')
