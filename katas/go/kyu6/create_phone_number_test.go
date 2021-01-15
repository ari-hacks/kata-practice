package kyu6

import (
	"reflect"
	"testing"
)

func TestCreatePhoneNumber(t *testing.T) {

	checkNumber := func(t *testing.T, got, want string) {
		t.Helper()
		if !reflect.DeepEqual(got, want) {
			t.Errorf("got %v want %s", got, want)
		}
	}

	t.Run("basic test", func(t *testing.T) {
		got := CreatePhoneNumber([10]uint{1, 2, 3, 4, 5, 6, 7, 8, 9, 0})
		want := "(123) 456-7890"
		checkNumber(t, got, want)
	})
}
