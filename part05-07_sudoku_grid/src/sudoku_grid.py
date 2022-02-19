# Write your solution here
def sudoku_grid_correct(sudoku: list):
    for i in range(len(sudoku)):
        row_status = row_correct(sudoku, i)
        if not row_status:
            return False

    for i in range(len(sudoku)):
        column_status = column_correct(sudoku, i)
        if not column_status:
            return False
    
    for i in range(0, len(sudoku), 3):
        for j in range(0, len(sudoku), 3):
            block_status = block_correct(sudoku, i, j)
            if not block_status:
                return False
    
    return True

def row_correct(sudoku: list, row_no: int):
    checked = []
    
    for num in sudoku[row_no]:
        if num > 0 and num in checked:
            return False
        else:
            checked.append(num)
    return True

def column_correct(sudoku: list, column_no: int):
    numbers = []
    for row in sudoku:
        if row[column_no] > 0 and row[column_no] in numbers:
            return False
        numbers.append(row[column_no])
    return True

def block_correct(sudoku: list, row_no: int, column_no: int):
    numbers = []

    for i in range(row_no, row_no + 3):
        for j in range(column_no, column_no + 3):
            element = sudoku[i][j]
            if element > 0 and element in numbers:
                return False
            numbers.append(element)

    return True