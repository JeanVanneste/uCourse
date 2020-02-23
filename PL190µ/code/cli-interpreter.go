// cli-interpreter.go
// Author: Sébastien Combéfis
// Version: February 23, 2020

package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

// splitLine splits a non-empty line into two parts:
// - the command name is everything before the first space and
// - the argument is everything after the first space (may be empty)
func splitLine(s string) (string, string) {
	tokens := strings.SplitN(s, " ", 2)
	return tokens[0], tokens[1]
}

// echo just returns the argument to the standard output
func echo(arg string) string {
	return arg
}

// sum computes the sum of all the numbers of the argument
// that are separated by spaces
func sum(arg string) string {
	result := 0
	return fmt.Sprintf("%d", result)
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	for {
		fmt.Print("> ")
		scanner.Scan()
		line := scanner.Text()
		if line != "" {
			cmd, arg := splitLine(line)
			if cmd == "exit" {
				return
			} else if cmd == "echo" {
				r := echo(arg)
				fmt.Println(r)
			} else if cmd == "sum" {
				r := sum(arg)
				fmt.Println(r)
			} else {
				fmt.Println("Undefined command.")
			}
		}
	}
}
