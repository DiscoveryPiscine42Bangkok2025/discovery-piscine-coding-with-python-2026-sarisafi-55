def check_rook(grid, r, c):
    size = len(grid)

    # ขึ้น
    i = r - 1
    while i >= 0:
        if grid[i][c] == 'K':
            return True
        if grid[i][c] != '.':
            break
        i -= 1

    # ลง
    i = r + 1
    while i < size:
        if grid[i][c] == 'K':
            return True
        if grid[i][c] != '.':
            break
        i += 1

    # ซ้าย
    j = c - 1
    while j >= 0:
        if grid[r][j] == 'K':
            return True
        if grid[r][j] != '.':
            break
        j -= 1

    # ขวา
    j = c + 1
    while j < size:
        if grid[r][j] == 'K':
            return True
        if grid[r][j] != '.':
            break
        j += 1

    return False


def check_bishop(grid, r, c):
    size = len(grid)
    directions = [(-1,-1), (-1,1), (1,-1), (1,1)]

    for dr, dc in directions:
        i = r + dr
        j = c + dc
        while 0 <= i < size and 0 <= j < size:
            if grid[i][j] == 'K':
                return True
            if grid[i][j] != '.':
                break
            i += dr
            j += dc

    return False


def check_queen(grid, r, c):
    return check_rook(grid, r, c) or check_bishop(grid, r, c)


def check_pawn(grid, r, c):
    size = len(grid)

    # Pawn กินเฉียงขึ้น
    moves = [(-1, -1), (-1, 1)]

    for dr, dc in moves:
        i = r + dr
        j = c + dc
        if 0 <= i < size and 0 <= j < size:
            if grid[i][j] == 'K':
                return True

    return False




def checkmate(board):
    rows = board.strip().split("\n")
    grid = [list(row) for row in rows]
    size = len(grid)

    # หา King
    king_found = False
    for r in range(size):
        for c in range(size):
            if grid[r][c] == 'K':
                king_found = True

    if not king_found:
        return "Fail"

    # เช็คทุกหมาก
    for r in range(size):
        for c in range(size):
            piece = grid[r][c]

            if piece == 'R' and check_rook(grid, r, c):
                return "Success"

            if piece == 'B' and check_bishop(grid, r, c):
                return "Success"

            if piece == 'Q' and check_queen(grid, r, c):
                return "Success"

            if piece == 'P' and check_pawn(grid, r, c):
                return "Success"

    return "Fail"
