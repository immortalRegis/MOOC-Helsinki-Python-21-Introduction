# Write your solution here
def row_correct(sudoku: list, row_no: int):
    checked = []
    
    for num in sudoku[row_no]:
        if num > 0 and num in checked:
            return False
        else:
            checked.append(num)
    return True