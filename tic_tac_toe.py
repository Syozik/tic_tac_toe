from random import choice

FIELD = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']   
]

def check_status():
    s1 = []
    s2 = []
    
    for i in range(3):
        if len(set(FIELD[i])) == 1 and FIELD[i][0] != ' ':
            return True
        s = []
        for j in range(3):
            s.append(FIELD[j][i])
        if len(set(s)) == 1 and s[0] != ' ':
            return True
        s1.append(FIELD[i][i])
        s2.append(FIELD[i][2-i])
    if (len(set(s1)) == 1 and s1[0] != ' ') or (len(set(s2)) == 1 and s2[0] != ' '):
        return True
    if sum([x.count(' ') for x in FIELD]) == 0:
        return 'deadlock'
    
    return False

def player_move(i, j):
    if FIELD[i][j] != ' ' or i < 0 or j < 0 or i > 2 or j > 2:
        return False
    else:
        FIELD[i][j] = 'x'
        return True

def check_win(i,j):
    
    FIELD[i][j] = 'o'
    res = check_status()
    FIELD[i][j] = ' '
    return res

def check_lose(i,j):
    FIELD[i][j] = 'x'
    res = check_status()
    FIELD[i][j] = ' '
    return res

def computer_move():
    s = []
    for row in range(3):
        for column in range(3):
            if FIELD[row][column] == ' ':
                if check_win(row,column):
                    FIELD[row][column] = 'o'
                    return (column,row)
                s.append((row,column))
    
        for idx in s:
            if check_lose(*idx):
                FIELD[idx[0]][idx[1]] = 'o'
                return (idx[::-1])

    i, j = choice(s)
    FIELD[i][j] = 'o'
    return (j,i)
 
def see_the_field():
    print('  1 2 3')
    for i in range(3):
        print(i+1,end = '')
        for j in range(3):
            s = FIELD[i][j]
            print('|',end=s)
        print('|')
