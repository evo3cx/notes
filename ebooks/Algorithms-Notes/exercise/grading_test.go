package excercise

import (
	"testing"

	"github.com/stretchr/testify/require"
)

func Test_Grading(t *testing.T) {
	inputs := []int32{84, 94, 67, 21, 0, 18, 100}
	outputs := []int32{85, 95, 67, 21, 0, 18, 100}

	out := gradingStudents(inputs)
	require.Equal(t, outputs, out)
}

func Test_Kangoroo(t *testing.T) {
	out := kangaroo(0, 3, 4, 2)
	require.Equal(t, "YES", out)

	out = kangaroo(0, 2, 5, 3)
	require.Equal(t, "NO", out)
}
