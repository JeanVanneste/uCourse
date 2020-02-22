// contactbook.go
// Author: Sébastien Combéfis
// Version: February 22, 2020

package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
)

type ContactBook struct {
}

// meanBirthYear computes the mean birth year
// of the contacts from a given contact book
func meanBirthYear(cb *ContactBook) float64 {
	return 0
}

func main() {
	cb := ContactBook{}
	content, _ := ioutil.ReadFile("contacts.json")
	json.Unmarshal(content, &cb)

	fmt.Printf("Mean birth year: %.2f\n", meanBirthYear(&cb))
}
