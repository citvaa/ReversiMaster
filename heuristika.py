import util

# canmove(), isLegalMove() and num_valid_moves() are helper functions to
# count the number of valid moves for a given player in a given
# board configuration


def canmove(self, opp, str):
    if str[0] != opp:
        return False
    for ctr in range(1, 8):
        if str[ctr] == 0:
            return False
        if str[ctr] == self:
            return True
    return False


def is_legal_move(self, opp, grid, startx, starty):
    if grid[startx][starty] != 0:
        return False
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            if dy == dx == 0:
                continue
            row = []
            for ctr in range(1, 9):
                x = startx + ctr * dx
                y = starty + ctr * dy
                if 0 <= x < 8 and 0 <= y < 8:
                    row.append(grid[x][y])
                else:
                    row.append(0)
            if canmove(self, opp, row):
                return True
    return False


def num_valid_moves(self, opp, grid):
    count = 0
    for i in range(0, 8):
        for j in range(0, 8):
            if is_legal_move(self, opp, grid, i, j):
                count += 1
    return count


# Assuming my_color stores your color and opp_color stores opponent's color
# '-' indicates an empty square on the board
# 'b' indicates a black tile and 'w' indicates a white tile on the board


def dynamic_heuristic_evaluation_function(grid):
    my_tiles = opp_tiles = my_front_tiles = opp_front_tiles = 0
    d = 0
    my_color = -1
    opp_color = 1

    X1 = [-1, -1, 0, 1, 1, 1, 0, -1]
    Y1 = [0, 1, 1, 1, 0, -1, -1, -1]

    V = [[] * 8 for _ in range(8)]
    V[0] = [20, -3, 11, 8, 8, 11, -3, 20]
    V[1] = [-3, -7, -4, 1, 1, -4, -7, -3]
    V[2] = [11, -4, 2, 2, 2, 2, -4, 11]
    V[3] = [8, 1, 2, -3, -3, 2, 1, 8]
    V[4] = [8, 1, 2, -3, -3, 2, 1, 8]
    V[5] = [11, -4, 2, 2, 2, 2, -4, 11]
    V[6] = [-3, -7, -4, 1, 1, -4, -7, -3]
    V[7] = [20, -3, 11, 8, 8, 11, -3, 20]

    # Piece difference, frontier disks and disk squares

    for i in range(0, 8):
        for j in range(0, 8):
            if grid[i][j] == my_color:
                d += V[i][j]
                my_tiles += 1
            elif grid[i][j] == opp_color:
                d -= V[i][j]
                opp_tiles += 1
            if grid[i][j] != 0:
                for k in range(0, 8):
                    x = i + X1[k]
                    y = j + Y1[k]
                    if 0 <= x < 8 and 0 <= y < 8 and grid[x][y] == 0:
                        if grid[i][j] == my_color:
                            my_front_tiles += 1
                        else:
                            opp_front_tiles += 1
                        break
    if my_tiles > opp_tiles:
        p = float(100 * my_tiles) / (my_tiles + opp_tiles)
    elif my_tiles < opp_tiles:
        p = float(-100 * opp_tiles) / (my_tiles + opp_tiles)
    else:
        p = 0

    if my_front_tiles > opp_front_tiles:
        f = float(-100 * my_front_tiles) / (my_front_tiles + opp_front_tiles)
    elif my_front_tiles < opp_front_tiles:
        f = float(100 * opp_front_tiles) / (my_front_tiles + opp_front_tiles)
    else:
        f = 0

    # Corner occupancy

    my_tiles = opp_tiles = 0
    if grid[0][0] == my_color:
        my_tiles += 1
    elif grid[0][0] == opp_color:
        opp_tiles += 1
    if grid[0][7] == my_color:
        my_tiles += 1
    elif grid[0][7] == opp_color:
        opp_tiles += 1
    if grid[7][0] == my_color:
        my_tiles += 1
    elif grid[7][0] == opp_color:
        opp_tiles += 1
    if grid[7][7] == my_color:
        my_tiles += 1
    elif grid[7][7] == opp_color:
        opp_tiles += 1
    c = 25 * (my_tiles - opp_tiles)

    # Corner closeness

    my_tiles = opp_tiles = 0
    if grid[0][0] == 0:
        if grid[0][1] == my_color:
            my_tiles += 1
        elif grid[0][1] == opp_color:
            opp_tiles += 1
        if grid[1][1] == my_color:
            my_tiles += 1
        elif grid[1][1] == opp_color:
            opp_tiles += 1
        if grid[1][0] == my_color:
            my_tiles += 1
        elif grid[1][0] == opp_color:
            opp_tiles += 1
    if grid[0][7] == 0:
        if grid[0][6] == my_color:
            my_tiles += 1
        elif grid[0][6] == opp_color:
            opp_tiles += 1
        if grid[1][6] == my_color:
            my_tiles += 1
        elif grid[1][6] == opp_color:
            opp_tiles += 1
        if grid[1][7] == my_color:
            my_tiles += 1
        elif grid[1][7] == opp_color:
            opp_tiles += 1
    if grid[7][0] == 0:
        if grid[7][1] == my_color:
            my_tiles += 1
        elif grid[7][1] == opp_color:
            opp_tiles += 1
        if grid[6][1] == my_color:
            my_tiles += 1
        elif grid[6][1] == opp_color:
            opp_tiles += 1
        if grid[6][0] == my_color:
            my_tiles += 1
        elif grid[6][0] == opp_color:
            opp_tiles += 1
    if grid[7][7] == 0:
        if grid[6][7] == my_color:
            my_tiles += 1
        elif grid[6][7] == opp_color:
            opp_tiles += 1
        if grid[6][6] == my_color:
            my_tiles += 1
        elif grid[6][6] == opp_color:
            opp_tiles += 1
        if grid[7][6] == my_color:
            my_tiles += 1
        elif grid[7][6] == opp_color:
            opp_tiles += 1
    l = -12.5 * (my_tiles - opp_tiles)

    # Mobility
    my_tiles = num_valid_moves(my_color, opp_color, grid)
    opp_tiles = num_valid_moves(opp_color, my_color, grid)
    if my_tiles > opp_tiles:
        m = float(100 * my_tiles) / (my_tiles + opp_tiles)
    elif my_tiles < opp_tiles:
        m = float(-100 * opp_tiles) / (my_tiles + opp_tiles)
    else:
        m = 0

    # final weighted score
    score = (10 * p) + (801.724 * c) + (382.026 * l) + (78.922 * m) + (74.396 * f) + (10 * d)
    return score


if __name__ == '__main__':
    tabla = util.inicijalizacija_table()
    print(dynamic_heuristic_evaluation_function(tabla))
