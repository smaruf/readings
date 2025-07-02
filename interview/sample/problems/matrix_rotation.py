def rotate90_clockwise(matrix):
    n = len(matrix)
    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i].reverse()

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(str(val) for val in row))

if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    print("Original Matrix:")
    print_matrix(matrix)

    rotate90_clockwise(matrix)

    print("Rotated Matrix (90 degrees clockwise):")
    print_matrix(matrix)
