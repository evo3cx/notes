package main

import (
	"fmt"
	"math/rand"

	"gonum.org/v1/gonum/mat"
)

// Week 1 Matrix-Vector Multiplication
func matrixVectorMultiplication() {
	headerText("Week 1 Matrix-Vector Multiplication")
	vectors := []float64{2, 1, 1}
	matrices := [][]float64{
		{1, 2, 3},
		{4, 5, 6},
		{7, 8, 9},
	}

	results := make([]float64, 3)

	for i, matrix := range matrices {
		for j, m := range matrix {
			results[i] += vectors[j] * m
		}
	}

	fmt.Printf("\nvector x matrix: %#v \n\n", results)

	one := mat.NewDense(3, 3, []float64{1, 2, 3, 4, 5, 6, 7, 8, 9})
	two := mat.NewDense(3, 1, []float64{2, 1, 1})

	fmt.Printf("\n %v", mat.Formatted(two))

	one.Mul(two, one)

	fmt.Printf("\n %#v", mat.Formatted(one))
}

func matrixMatrixMultiplication() {
	headerText("Week 1 Matrix-Matrix Multiplication")

	//  Case 1
	matrix := [][]float64{
		{1, 3, 2},
		{4, 0, 1},
	}
	matrixTwo := [][]float64{
		{1, 3},
		{0, 1},
		{5, 2},
	}

	multiplicationVector := func(matrices [][]float64, vectors []float64) []float64 {
		results := make([]float64, len(vectors))

		for i, matrix := range matrices {
			for j, m := range matrix {

				results[i] += vectors[j] * m
				fmt.Println(results[i], vectors[j]*m)
			}
		}

		fmt.Println(results)

		return results
	}

	var results [][]float64
	for _, v := range matrixTwo {
		result := multiplicationVector(matrix, v)
		results = append(results, result)
	}

	fmt.Printf("\n case #1 matrix x matrix: %#v \n\n", results)

	// //  Case 2
	// matrix = [][]float64{
	// 	{1, 3},
	// 	{2, 4},
	// 	{0, 5},
	// }
	// matrixTwo = [][]float64{
	// 	{1, 0},
	// 	{2, 3},
	// }
	// var results2 [][]float64
	// for _, v := range matrixTwo {
	// 	result := multiplicationVector(matrix, v)
	// 	results2 = append(results2, result)
	// }

	// fmt.Printf("\n case #2 matrix x matrix: %#v \n\n", results2)

	// use gonum
	// case #1
	one := mat.NewDense(2, 3, []float64{1, 3, 2, 4, 0, 1})
	two := mat.NewDense(3, 3, []float64{1, 3, 0, 1, 5, 2, 1, 2, 3})

	_, oneR := one.Dims()
	twoC, _ := two.Dims()
	fmt.Println(oneR, twoC)
	one.Mul(one, two)
	fmt.Printf("\n use gomun case #1 \n%v\n", mat.Formatted(two))

	// case #2
	threeTwo := mat.NewDense(3, 2, []float64{1, 3, 2, 4, 0, 5})
	twoTwo := mat.NewDense(2, 2, []float64{1, 0, 2, 3})
	threeTwo.Mul(threeTwo, twoTwo)

	fmt.Printf("\n use gomun case #2 \n%v\n", mat.Formatted(threeTwo))
}

func headerText(text string) {
	line := func() {
		char := 20
		fmt.Println()
		for i := 0; i < char; i++ {
			fmt.Print("-")
		}
		fmt.Println()
	}

	line()
	fmt.Println(text)
	line()
}

func playWithGonum() {
	headerText("playWithGonum")

	// Allocate a real matrix of size 3x2 with allocated value
	threeXTwo := mat.NewDense(3, 2, []float64{1, 2, 3, 4, 5, 6})
	threeXTwoDimension, _ := threeXTwo.Dims()
	fmt.Printf("3x2 \n%v \n dimension %d \n\n", mat.Formatted(threeXTwo), threeXTwoDimension)

	// Generate a 6x6 real matrix of random values
	data := make([]float64, 36)
	for i := range data {
		data[i] = rand.NormFloat64()
	}
	sixForSix := mat.NewDense(6, 6, data)
	sixForSixDimension, _ := sixForSix.Dims()
	fmt.Printf("\n6x6 random \n %v \n dimension %v \n",
		mat.Formatted(sixForSix), sixForSixDimension,
	)
	trace := mat.Trace(sixForSix)

	fmt.Printf("\ntrace 6x6 \n %#v \n", trace)
}

func main() {
	matrixVectorMultiplication()
	matrixMatrixMultiplication()
	// playWithGonum()
}
