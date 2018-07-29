#include <stdio.h>
#include <stdlib.h>

// gcc Basic.c -o basicc
// ./basicc

typedef struct {
	char* name;
} Person;

// note: we can't really do member functions in C
void talk(Person *p) {
	printf("Hi, I am %s\n", p->name);
}

int main(int argc, char** argv) {
	printf("There are %d arguments\n", argc);

	// note: you can initialize array like this too:
	// Person *peeps = malloc(10 * sizeof(Person));
	// note: length of statically allocated array can be found: sizeof(arr) / sizeof(arr[0])

	Person* people[2]; // array of Person pointers
	people[0] = malloc(sizeof(Person));
	people[0]->name = "Mark";

	for (int i = 0; i < 2; i++) {
		if (people[i]) {
			talk(people[i]);
			free(people[i]);
		}
	}

	// on stack:
	Person peeps[3];
	peeps[0].name = "Yurgen";
	talk(&peeps[1]);

}
