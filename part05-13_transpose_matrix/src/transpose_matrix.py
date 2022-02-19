# Write your solution here
def transpose(matrix: list):
    temp_matrix = []

    for row in matrix:
        temp_matrix.append(row[:])

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            matrix[i][j] = temp_matrix[j][i]