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

// HELLO WORLD

fun main(args: Array<String>) {
  println("Hello, world!")
}

