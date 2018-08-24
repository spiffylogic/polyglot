// SWIFT
/*
Developers: Chris Lattner and Apple Inc. and open source contributors
Released: June 2014
Type system: static, strong, inferred
*/

// COMPILING AND RUNNING

// swiftc basics.swift -o basics
// ./basics

// HELLO WORLD

print("Hello, world!")

// VARIABLES AND CONSTANTS

var myVariable = 42
myVariable = 50
let myConst = 5
let explicitDouble: Double = 70

// TYPE COERCION

let label = "The width is "
let width = 94
let widthLabel = label + String(94)

// STRING FORMATTING

let apples = 3
let oranges = 5
let fruitSummary = "I have \(apples + oranges) " +
                   "pieces of fruit."

