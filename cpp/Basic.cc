#include <stdlib.h>
#include <iostream>
#include <vector>

using namespace std;

// use g++ or clang++
// clang++ Basic.cc -o basic
// ./basic

class Person {
	string name;

	public:
    //Person(string name) : name("anon") {
		//}

		void talk() {
			cout << "Hi, I am " << this->name << endl;
		}
};

int main(int argc, char* argv[]) {
	vector<Person> people = vector<Person>(3);
	people[1].talk();
  return 0;
}
