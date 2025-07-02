def rotate90_clockwise(matrix):
    m, n = len(matrix), len(matrix[0])
    rotated = [[0] * m for _ in range(n)]
    for i in range(m):
        for j in range(n):
            rotated[j][m - 1 - i] = matrix[i][j]
    return rotated

def rotate90_counterclockwise(matrix):
    m, n = len(matrix), len(matrix[0])
    rotated = [[0] * m for _ in range(n)]
    for i in range(m):
        for j in range(n):
            rotated[n - 1 - j][i] = matrix[i][j]
    return rotated

def rotate180(matrix):
    m, n = len(matrix), len(matrix[0])
    rotated = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            rotated[m - 1 - i][n - 1 - j] = matrix[i][j]
    return rotated

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(str(val) for val in row))

if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    print("Original Matrix:")
    print_matrix(matrix)

    print("\n90° Clockwise:")
    print_matrix(rotate90_clockwise(matrix))

    print("\n90° Counter-Clockwise:")
    print_matrix(rotate90_counterclockwise(matrix))

    print("\n180° Rotation:")
    print_matrix(rotate180(matrix))
