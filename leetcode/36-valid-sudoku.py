from typing import List


# Cada linha deve conter os dígitos de 1 a 9 sem repetição. v
#
# Cada coluna deve conter os dígitos de 1 a 9 sem repetição.
#
# Cada uma das nove subcaixas 3 x 3 da grade deve conter os dígitos de 1 a 9 sem repetição.

def isValidSudoku(board: List[List[str]]):

    # occurrences for line
    for row in board:
        counter = {}
        for element in row:
            if element != '.':
                counter[element] = 1 if element not in counter else counter[element] + 1

        for occurrences in counter.values():
            if occurrences > 1:
                return False

    # occurrences for columns
    for col in range(len(board)):
        counter = {}
        for element in board:
            if element[col] != '.':
                counter[element[col]] = 1 if element[col] not in counter else counter[element[col]] + 1

        for occurrences in counter.values():
            if occurrences > 1:
                return False


    # occurrences for boxes
    start_range = 0
    end_range = 3

    while end_range <= 9:
        sub_start_range = 0
        sub_end_range = 3

        while sub_end_range <= 9:
            counter = {}
            for sub_list in board[start_range:end_range]:
                for element in sub_list[sub_start_range:sub_end_range]:
                    if element != '.':
                        counter[element] = 1 if element not in counter else counter[element] + 1

            for occurrences in counter.values():
                if occurrences > 1:
                    return False

            sub_start_range += 3
            sub_end_range += 3

        start_range += 3
        end_range += 3

    return True


board = [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]

print(isValidSudoku(board))