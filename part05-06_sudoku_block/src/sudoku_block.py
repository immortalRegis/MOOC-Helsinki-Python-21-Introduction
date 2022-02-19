# Write your solution here
def block_correct(sudoku: list, row_no: int, column_no: int):
    numbers = []

    for i in range(row_no, row_no + 3):
        for j in range(column_no, column_no + 3):
            element = sudoku[i][j]
            if element > 0 and element in numbers:
                return False
            numbers.append(element)

    return True


