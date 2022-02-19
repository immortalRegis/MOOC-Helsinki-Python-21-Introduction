# Write your solution here
def print_sudoku(sudoku: list):
    for i in range(len(sudoku)):
        if i in [3,6]:
            print()
        for j in range(len(sudoku)):
            value = sudoku[i][j]
            if j in [3,6]:
                print(" ", end="")
            if value == 0:
                print("_ ", end="")
            else:
                print(f"{value} ", end="")
        print()

def add_number(sudoku: list, row_no: int, column_no: int, number:int):
    sudoku[row_no][column_no] = number

