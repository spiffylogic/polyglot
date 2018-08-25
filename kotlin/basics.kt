// KOTLIN

/*
Story: JetBrains looking for features like Scala, but without the slow compile time. One of the stated goals of Kotlin is to compile as quickly as Java. Open-sourced in Feb 2012.
Developers: JetBrains and open source contributors
Released: 2011
Type system: static, strong, inferred
Platform: Outputs JVM bytecode and JavaScript source code
OS: Any supporting JVM or JavaScript interpreter
*/

// COMPILING AND RUNNING

// kotlinc basics.kt
// kotlin BasicsKt

// Alternatively, as Java program:
// kotlinc basics.kt -include-runtime -d basics.jar
// java -jar basics.kt

fun main(args: Array<String>) {
	println("Hello, world!")

	// === Command Line Arguments
	for (arg in args) {
		println(arg)
	}

	// === Variables and Constants ===
	var myVariable = 42
	myVariable = 50
	val myConst = 42

	// === Types ===
	val explicitDouble: Double = 70.0 // double literal required
	val label = "The width is "
	val width = 94
	val widthLabel = label + width

	val apples = 3
	val oranges = 5
	val fruitSummary = "I have ${apples + oranges} " +
										 "pieces of fruit."

	// === Range Operators ===
	val names = arrayOf("Anna", "Alex", "Brian", "Jack")
	val count = names.count()
	for (i in 0 .. count-1) {
		println("Person ${ i+1 } is called ${ names[i] }")
	}
}
