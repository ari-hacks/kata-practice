package kyu6

import (
	"fmt"
	"strings"
)

func CreatePhoneNumber(numbers [10]uint) string {
	// return "(123) 456-7890"
	// for _, number := range numbers {
	if len(numbers) == 10 {
		area_code := numbers[0:3]
		//   exchange_code = ''.join(str(x) for x in n[3:6])
		//   number = ''.join(str(x) for x in n[6:10])
		fmt.Println(area_code)
		return area_code
	}

}
