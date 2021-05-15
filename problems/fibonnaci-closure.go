// https://youtu.be/US3TGA-Dpqo?t=686

package main

import "fmt"

func fib() func() int{
  a, b := 0,1
  return func()int{
    a, b = b, a+b
    return b
  }
}
func main() {
  f := fib()
  for x:= f(); x<1000; x=f(){
    fmt.Println(x)
  }
}
