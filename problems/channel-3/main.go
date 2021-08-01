package main

import "fmt"

func main() {
	var ch chan int
	ch = make(chan int, 2)
	fmt.Printf("%T %v", ch, ch)
	ch <- 10
	ch <- 20
	fmt.Println(<-ch, len(ch))
	fmt.Println(<-ch, len(ch))
}
