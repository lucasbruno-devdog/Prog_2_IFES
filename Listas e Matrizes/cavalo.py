def posição_cavalo(M):
    for i in range(len(M)):
        for j in range(len(M[0])):
            if (M[i][j] == 1):
                return i+1, j+1
def cavalo(M):
    x, y = posição_cavalo(M)
    movs = 0
    
    if (y == 8 or y == 1):
        if(x == 1 or x == 8):
            return 2
        if(x == 2 or x == 7):
            return 3
        else:
            return 4
    elif (y == 2 or y == 7):
        if (x ==  1 or x == 8):
            return 3
        if(x == 2 or x == 7):
            return 4
        else:
            return 6
    else:
        if (x == 1 or x == 8):
            return 4
        if (x == 2 or x == 7):
            return 6
        else:
            return 8        
                        