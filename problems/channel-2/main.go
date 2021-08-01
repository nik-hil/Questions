package main

import "fmt"

func myfunc(ch chan<- int) {
	for j := 7; j <= 9; j++ {
		ch <- j
	}
	close(ch)
}
func myfunc1(ch1 chan<- int, ch <-chan int) {
	for i := range ch {
		ch1 <- i
	}
	close(ch1)
}
func main() {
	ch := make(chan int)
	ch1 := make(chan int)
	go myfunc(ch)
	go myfunc1(ch1, ch)
	for i := range ch1 {
		fmt.Println(i)
	}
}
