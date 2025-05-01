import numpy as np

def extract_overlapping_blocks(matrix, n):
    m = matrix.shape[0]
    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("Matrix must be square (m x m)")
    if n > m:
        raise ValueError("n must be less than or equal to m")

    blocks = []
    for i in range(m - n + 1):
        for j in range(m - n + 1):
            block = matrix[i:i+n, j:j+n]
            blocks.append(block)
    return blocks

# Example
m = 5
n = 3
matrix = np.arange(m * m).reshape(m, m)
blocks = extract_overlapping_blocks(matrix, n)

# Show results
for idx, block in enumerate(blocks):
    print(f"Block {idx+1}:\n{block}\n")
