package main

import "fmt"

func print(text <-chan string) {
	fmt.Println(<-text)
}
func main() {

	channel := make(chan string)
	go print(channel)
	channel <- "Ha ha"
}
