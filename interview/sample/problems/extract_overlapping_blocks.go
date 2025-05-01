package main

import (
	"fmt"
)

func extractOverlappingBlocks(matrix [][]int, n int) [][][]int {
	m := len(matrix)
	if m == 0 || len(matrix[0]) != m {
		panic("Matrix must be square")
	}
	if n > m {
		panic("n must be <= m")
	}

	var blocks [][][]int
	for i := 0; i <= m-n; i++ {
		for j := 0; j <= m-n; j++ {
			block := make([][]int, n)
			for x := 0; x < n; x++ {
				block[x] = make([]int, n)
				for y := 0; y < n; y++ {
					block[x][y] = matrix[i+x][j+y]
				}
			}
			blocks = append(blocks, block)
		}
	}
	return blocks
}

func main() {
	m := 5
	n := 3

	// Create a 5x5 matrix with values 0..24
	matrix := make([][]int, m)
	counter := 0
	for i := 0; i < m; i++ {
		matrix[i] = make([]int, m)
		for j := 0; j < m; j++ {
			matrix[i][j] = counter
			counter++
		}
	}

	// Extract overlapping blocks
	blocks := extractOverlappingBlocks(matrix, n)

	// Print blocks
	for i, block := range blocks {
		fmt.Printf("Block %d:\n", i+1)
		for _, row := range block {
			fmt.Println(row)
		}
		fmt.Println()
	}
}
