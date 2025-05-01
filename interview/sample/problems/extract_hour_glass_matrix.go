package main

import (
	"fmt"
)

func extractHourglassBlocks(matrix [][]int, hourglassSize int) [][][]int {
	matrixSize := len(matrix)

	// Validation
	if matrixSize == 0 || len(matrix[0]) != matrixSize {
		panic("Matrix must be square (m x m)")
	}
	if hourglassSize > matrixSize || hourglassSize%2 == 0 {
		panic("Hourglass size must be odd and <= matrix size")
	}

	center := hourglassSize / 2
	var hourglassBlocks [][][]int

	for rowStart := 0; rowStart <= matrixSize-hourglassSize; rowStart++ {
		for colStart := 0; colStart <= matrixSize-hourglassSize; colStart++ {
			hourglass := make([][]int, hourglassSize)

			for localRow := 0; localRow < hourglassSize; localRow++ {
				hourglass[localRow] = make([]int, hourglassSize)

				for localCol := 0; localCol < hourglassSize; localCol++ {
					globalRow := rowStart + localRow
					globalCol := colStart + localCol

					// Keep top/bottom rows, or center of center row
					if localRow == 0 || localRow == hourglassSize-1 || (localRow == center && localCol == center) {
						hourglass[localRow][localCol] = matrix[globalRow][globalCol]
					} else {
						hourglass[localRow][localCol] = 0 // filler
					}
				}
			}
			hourglassBlocks = append(hourglassBlocks, hourglass)
		}
	}

	return hourglassBlocks
}

// Utility function to print a 2D matrix
func printMatrix(matrix [][]int) {
	for _, row := range matrix {
		fmt.Println(row)
	}
	fmt.Println()
}

func main() {
	matrixSize := 5
	hourglassSize := 3

	// Create a 5x5 matrix with values from 0 to 24
	matrix := make([][]int, matrixSize)
	value := 0
	for i := 0; i < matrixSize; i++ {
		matrix[i] = make([]int, matrixSize)
		for j := 0; j < matrixSize; j++ {
			matrix[i][j] = value
			value++
		}
	}

	hourglasses := extractHourglassBlocks(matrix, hourglassSize)

	for idx, hg := range hourglasses {
		fmt.Printf("Hourglass %d:\n", idx+1)
		printMatrix(hg)
	}
}
