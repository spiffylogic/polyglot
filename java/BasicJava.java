// javac classname.java
// java classname

// Define class
// create array of instances of that class
// iterate over array and call a method to print out a string

public class BasicJava {

	// note this has to be static to be able to "new" it from main
	public static class Person {
		String name = "anonymous";

		Person() {}

		Person(String name) {
			this.name = name;
		}

		public void talk() {
			System.out.println(String.format("Hi, I am %s", this.name));
		}
	}

	public static void main(String[] args) {
		System.out.println(String.format("There are %d arguments", args.length));

		Person[] people = new Person[2]; // this allocates space but doesn't initialize any objects
		people[0] = new Person("Mark");
		people[1] = new Person();

		for (Person p : people) {
			p.talk();
		}
	}
}
