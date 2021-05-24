package main

import (
	"fmt"
	// "time"
)

func hello(ch chan string) {
	//
	for i := 0; ; i++ {
		fmt.Println(i)
		j, ok := <-ch
		if ok {
			fmt.Println(j)
		}
	}
}
func main() {

	ch := make(chan string)
  // Uncomment below, comment above
  // ch := make(chan string, 2)
	go hello(ch)
	ch <- "Hello, playground"
	ch <- "Hello, Hi"
	ch <- "Hello, Hi1"
  // If using buffered channel use some delay.
	// time.Sleep(10 * time.Millisecond)
	close(ch)

}
