// SWIFT
/*
Developers: Chris Lattner and Apple Inc. and open source contributors
Released: June 2014
Type system: static, strong, inferred
*/

// Compiling and Running

// swiftc basics.swift -o basics
// ./basics

print("Hello, world!")

// includes program name as 0th argument
for arg in CommandLine.arguments {
	print(arg)
}

var myVariable = 42
myVariable = 50
let myConst = 5
let explicitDouble: Double = 70

let label = "The width is "
let width = 94
let widthLabel = label + String(94)

let apples = 3
let oranges = 5
let fruitSummary = "I have \(apples + oranges) " +
									 "pieces of fruit."

let m = 5
for i in 0..<m {
	print(i)
}
for i in 0...4 {
	print(i)
}

// What I really want is a simple program that touches on all of these things in a way that's not completely contrived

let names = ["Anna", "Alex", "Brian", "Jack"]
let count = names.count
var occupations = [
	"Malcolm" : "Captain",
	"Kaylee"  : "Mechanic",
]
occupations["Jane"] = "Public relations"


