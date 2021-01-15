package kyu6

import (
	"fmt"
	"strings"
)

//make cleaner
func CreatePhoneNumber(numbers [10]uint) string {
	area_code := strings.Trim(strings.Join(strings.Split(fmt.Sprint(numbers[0:3]), " "), ""), "[]")
	exchange_number := strings.Trim(strings.Join(strings.Split(fmt.Sprint(numbers[3:6]), " "), ""), "[]")
	phone_numb := strings.Trim(strings.Join(strings.Split(fmt.Sprint(numbers[6:]), " "), ""), "[]")

	return fmt.Sprintf("(%s) %s-%s", area_code, exchange_number, phone_numb)

}
