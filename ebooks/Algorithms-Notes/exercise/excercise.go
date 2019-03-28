package excercise

import "fmt"

func gradingStudents(grades []int32) []int32 {
	/*
	 * Write your code here.
	 */
	finalGrades := make([]int32, len(grades))
	for idx, g := range grades {
		if g < 38 || g == 100 {
			finalGrades[idx] = g
			continue
		}
		fiveExp := false
		for i := 20; i >= 0; i-- {
			exp := int32(i * 5)
			if exp-g >= 0 && exp-g < 3 {
				finalGrades[idx] = exp
				fiveExp = true
				break
			}
		}

		if !fiveExp {
			finalGrades[idx] = g
		}
	}

	return finalGrades
}

// 0, 3, 4, 2
// 0 3 6 9 12
// 4 6 8 10 12
// Complete the kangaroo function below.
func kangaroo(x1 int32, v1 int32, x2 int32, v2 int32) string {
	kg1 := x1
	kg2 := x2
	for i := int32(1); i < 10000; i++ {
		kg1 += v1
		kg2 += v2
		fmt.Println(kg1, kg2, v1, v2, "yes")
		if kg2 == kg1 {
			return "YES"
		}
	}

	if kg2 == kg1 {
		return "YES"
	}

	return "NO"
}
