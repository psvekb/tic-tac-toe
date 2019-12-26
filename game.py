def display_board(board):
    print('\n' * 10)
    print(board[7], ' | ', board[8], ' | ', board[9], sep='')
    print('---------')
    print(board[4], ' | ', board[5], ' | ', board[6], sep='')
    print('---------')
    print(board[1], ' | ', board[2], ' | ', board[3], sep='')


def player_input(chain_numb, chain_sign):
    p_pos = 0
    while p_pos > 9 or p_pos < 1 or game_board[p_pos] != ' ':
        print('Player ', chain_numb, ' - Select ', chain_sign, 'position from 1 to 9: ', end='')
        s_pos = input()
        if s_pos.isdigit():
            p_pos = int(s_pos)
        display_board(game_board)
        print('Error input, not digit or position is not possible')
    return p_pos


def check_win(p_sign):
    if game_board[1] == game_board[2] == game_board[3] == p_sign:
        return p_sign
    elif game_board[4] == game_board[5] == game_board[6] == p_sign:
        return p_sign
    elif game_board[7] == game_board[8] == game_board[9] == p_sign:
        return p_sign
    elif game_board[1] == game_board[4] == game_board[7] == p_sign:
        return p_sign
    elif game_board[2] == game_board[5] == game_board[8] == p_sign:
        return p_sign
    elif game_board[3] == game_board[6] == game_board[9] == p_sign:
        return p_sign
    elif game_board[1] == game_board[5] == game_board[9] == p_sign:
        return p_sign
    elif game_board[7] == game_board[5] == game_board[3] == p_sign:
        return p_sign
    else:
        return '#'


# test_board = ['#', 'O', 'X', 'O', 'X', 'X', 'O', 'X', 'X', 'O']
# game_board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

while 1:
    game_board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    display_board(game_board)
    print('Tic Tac Toe')
    p1_sign = input('Player 1 - Select X or O: ')
    while p1_sign != 'X' and p1_sign != 'O':
        print('Error input')
        p1_sign = input('Select X or O: ')
    if p1_sign == 'X':
        p2_sign = 'O'
    else:
        p2_sign = 'X'

    chain_player = 1
    p_sign = p1_sign
    for i in range(1, 9 + 1):
        display_board(game_board)
        chain_player = (i + 1) % 2 + 1
        if chain_player == 1:
            p_pos = player_input(chain_player, p1_sign)
            game_board[p_pos] = p1_sign
        else:
            p_pos = player_input(chain_player, p2_sign)
            game_board[p_pos] = p2_sign
        if check_win(p1_sign) != '#':
            p_sign = p1_sign
            break
        if check_win(p2_sign) != '#':
            p_sign = p2_sign
            break

    display_board(game_board)
    print('Player', chain_player, '-', p_sign, 'wins')

    p1_sign = input('New game - select y or n to qiut: ')
    while p1_sign != 'y' and p1_sign != 'n':
        print('Error input')
        p1_sign = input('New game - select y or n to qiut: ')
    if p1_sign == 'n':
        break

print('End game')