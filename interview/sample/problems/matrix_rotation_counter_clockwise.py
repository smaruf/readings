def rotate90_counter_clockwise(matrix):
    n = len(matrix)
    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # Reverse each column
    for j in range(n):
        top, bottom = 0, n - 1
        while top < bottom:
            matrix[top][j], matrix[bottom][j] = matrix[bottom][j], matrix[top][j]
            top += 1
            bottom -= 1

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))

if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print("Original Matrix:")
    print_matrix(matrix)
    rotate90_counter_clockwise(matrix)
    print("Rotated Matrix (90 degrees counter-clockwise):")
    print_matrix(matrix)
