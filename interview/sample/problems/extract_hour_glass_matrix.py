def extract_hourglass_blocks(matrix, hourglass_size):
    matrix_size = len(matrix)
    
    # Validation
    if matrix_size == 0 or any(len(row) != matrix_size for row in matrix):
        raise ValueError("Matrix must be square (m x m)")
    if hourglass_size > matrix_size or hourglass_size % 2 == 0:
        raise ValueError("hourglass_size must be odd and <= matrix size")
    
    center = hourglass_size // 2
    hourglass_blocks = []

    # Slide the hourglass window over the matrix
    for row_start in range(matrix_size - hourglass_size + 1):
        for col_start in range(matrix_size - hourglass_size + 1):
            hourglass_block = []
            for local_row in range(hourglass_size):
                current_row = []
                for local_col in range(hourglass_size):
                    global_row = row_start + local_row
                    global_col = col_start + local_col
                    
                    # Keep top/bottom rows, or center of center row
                    if (local_row == 0 or local_row == hourglass_size - 1 or
                        (local_row == center and local_col == center)):
                        current_row.append(matrix[global_row][global_col])
                    else:
                        current_row.append(0)  # filler for clarity
                hourglass_block.append(current_row)
            hourglass_blocks.append(hourglass_block)
    
    return hourglass_blocks

def print_matrix(matrix):
    for row in matrix:
        print(row)
    print()

# Example usage
if __name__ == "__main__":
    matrix_size = 5
    hourglass_size = 3

    # Create a 5x5 matrix with values 0..24
    matrix = [[row * matrix_size + col for col in range(matrix_size)] for row in range(matrix_size)]

    hourglasses = extract_hourglass_blocks(matrix, hourglass_size)

    for idx, hourglass in enumerate(hourglasses):
        print(f"Hourglass {idx + 1}:")
        print_matrix(hourglass)
