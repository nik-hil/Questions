// merge sort in go.
// https://www.educative.io/blog/50-golang-interview-questions
// https://gist.github.com/julianshen/3940045

package main

import "fmt"

func merge(ldata []int, rdata []int) (result []int) {
	result = make([]int, 0, len(ldata)+len(rdata))
	for len(result) < cap(result) {
		if len(ldata) == 0 {
			result = append(result, rdata...)
		} else if len(rdata) == 0 {
			result = append(result, ldata...)
		} else if ldata[0] < rdata[0] {
			result = append(result, ldata[0])
			ldata = ldata[1:]
		} else if ldata[0] > rdata[0] {
			result = append(result, rdata[0])
			rdata = rdata[1:]
		}
	}
	return
}
func mergeSort(arr []int, ch chan<- []int) {
	if len(arr) == 1 {
		ch <- arr
		return
	}
	mid := len(arr) / 2

	leftchan := make(chan []int)
	rightchan := make(chan []int)
	go mergeSort(arr[:mid], leftchan)
	go mergeSort(arr[mid:], rightchan)

	ldata := <-leftchan
	rdata := <-rightchan
	close(leftchan)
	close(rightchan)

	ret := merge(ldata, rdata)
	ch <- ret
	return
}
func main() {
	arr := []int{2, 4, 1, 5, 7, 3, 9, 8}
	result := make(chan []int)
	go mergeSort(arr, result)
	for _, i := range <-result {
		fmt.Println(i)
	}
	close(result)
}
