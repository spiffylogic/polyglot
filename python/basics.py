# === Summary ===

''' Python is an interpreted high-level general-purpose programming language

 * created by Guido van Rossum and first released in 1991
 * design philosophy emphasizes code readability, notably using significant whitespace
 * provides constructs that enable clear programming on both small and large scales
 * in July 2018, Van Rossum stepped down as the leader in the language community after 30 years
 * features a dynamic type system and automatic memory management
 * supports multiple programming paradigms, including object-oriented, imperative, functional and procedural
 * has a large and comprehensive standard library
 * version 3.0 was released in 2008
'''

# === How To Run ===

# Use version 3.x
# python basics.py

# === Declaration/Initialization ===

# Values, not variables, have data types.
# A variable can be reassigned to contain a different data type.
answer = 42
answer = "The answer is 42."

# === Data Types ===

bool = True

int = 1
float = 1.1

str = "Strings can be declared with single or double quotes."

# No native array data structure in Python. Use lists!
list = ["Lists can have", 1, 2, 3, 4, "or more types together!"]
len(list) # length of list

# Tuples are fixed size in nature whereas lists are dynamic.
# In other words, a tuple is immutable whereas a list is mutable. Consequently tuples are generally faster.
tuple = ("Tuples", "can have", "more than", 2, "elements!")
len(tuple) # length of tuple

dict = {'one': 1, 2: '2', 'three': 3}

for item in dict:
    print(item) # prints the key

dict.keys()
dict.values()

variable_with_no_data = None

# === Logging ===

print("Printed!")

# === Conditionals ===

cake = "delicious"

if cake == "delicious":
    print("Yes please!")
elif cake == "okay":
    print("I'll have a small piece.")
else:
    print("No, thank you.")

# ternary
print("yes" if cake == "delicious" else "no")

# === Loops ===

for item in list:
    print(item)

# range(start, end) = list of integers from start (inclusive, default 0) to end (EXclusive)
for i in range(5,10): # 5, 6, 7, 8, 9
    print(i)

values = [1.1, 2.2, 3.3, 4.4, 5.5]
i = 0
max = 5
total = 0
while (total < max):
    total += values[i]
    i += 1

# Functions

def divide(dividend, divisor):
    quotient = dividend / divisor
    remainder = dividend % divisor
    return quotient, remainder

def calculate_stuff(x, y):
    (q, r) = divide(x,y)
    print(q, r)

# Classes

# Python 2.x: Person(object)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birthday(self):
        self.age += 1

# Inheritance

class Employee(Person):

    def __init__(self, name, age, staffnum):
        # Python 2.x: super(Employee,self)
        super().__init__(name, age)
        self.staffnumber = staffnum

    def birthday(self):
        self.age += 2

    def employeeId(self):
        return self.name + ", " +  self.staffnumber

x = Person("Marge Simpson", 45)
x.birthday()
y = Employee("Homer Simpson", 49, "1007")
y.birthday()

print(x.name, x.age)
print(y.employeeId(), y.age)


