def spiralOrder(matrix: [list[list[int]]]):
    final_list = list()

    def walk_append(list_to_walk: list, list_to_append: list, direction: bool):
        if direction:
            for step in list_to_walk:
                list_to_append.append(step)
        else:
            for step in reversed(list_to_walk):
                list_to_append.append(step)

    def walk_up_down_append(col: int, lists_to_walk: list, list_to_append: list, direction: bool):
        if direction:
            for _sublist in lists_to_walk:
                list_to_append.append(_sublist[col])
                _sublist.pop(col)
        else:
            for _sublist in reversed(lists_to_walk):
                list_to_append.append(_sublist[col])
                _sublist.pop(col)

    direction = True

    while len(matrix[0]):
        matrix_atual = 0 if direction else len(matrix) - 1
        coluna_atual = len(matrix[0]) - 1 if direction else 0

        walk_append(matrix[matrix_atual], final_list, direction)
        matrix.pop(matrix_atual)

        if len(matrix) > 0:
            walk_up_down_append(coluna_atual, matrix, final_list, direction)

        direction = not direction

    return final_list

test_matrix = [[7],[9],[6]]
print(spiralOrder(test_matrix))
