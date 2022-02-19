# Write your solution here
def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    holder = []

    for row in sudoku:
        holder.append(row[:])
# or we can just use holder =[[row:] for row in sudoku]
    holder[row_no][column_no] = number

    return holder
    
    