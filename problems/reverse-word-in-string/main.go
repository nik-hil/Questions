package main

import (
	"fmt"
	"strings"
)

func reverse(in string) (out string) {
	for _, r := range in {
		out = string(r) + out
	}
	return
}
func main() {
	str := "my name is xx khan"
	words := strings.Fields(str)
	var str1 string
	for _, word := range words {
		str1 += reverse(word) + " "
	}
	fmt.Println(str1)
}
