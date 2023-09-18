def print_operation_table(operation: object, rows: int, cols: int):
    matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            matrix[i][j] = str(operation(i+1, j+1)).ljust(3)
    [print(*i, end='\n') for i in matrix]
