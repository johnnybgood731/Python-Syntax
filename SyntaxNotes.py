# Here are some Import Statements. By convention, imports always go at the top of a file.
from random import randint  # imports only the randint function from the random library
from datetime import *  # imports all functions from the datetime library
import math as mathematics  # imports the entire math library and changes its reference from "math" to # "mathematics"
#                             "as mathematics" is optional

print("\nLIBRARIES:")
print("Here are all of the math functions:")
print(dir(mathematics))

"""
This is technically a string variable,
but since we aren't storing it,
we can use it to make long comments!
"""

# This is a single comment line.

# Here are different ways to use Print Statements.
print("\nPRINT STATEMENTS:")
number = 5
word = "\"word\""
word2 = "\"another word\""
print("This is", "a print statement.")
print("This is", "basically the same print statement.", sep=" ")
print("Print: This prints %s, %s, and %03d"  # 1 of 3 ways to use continuation
      " padded with enough zeroes to make a total of 3 digits." % (word, word2, number))
# Here the backslash is used as a continuation character instead of an exception character.  It also works for strings.
number2 = 5 + 6 + \
        7 + 8

# Here are all of the basic Data Structures.
print("\nDATA STRUCTURES AND TYPE CONVERSIONS:")
emptyList = []
myList = list([1, 2, 3])  # () or {} are interchangeable with [], but [] is convention.
myBool = bool(False)
myBool2 = bool(5.5)  # Any nonzero value, including strings, evaluates as "True"
myInt = int(-3)
myFloat = float(3.14159)
myString = str("hello")  # Technically this is a 5-element list of characters
myStringML = str("""
This is a
multi-line string!
""")
convert = int("7") / 2  # This will automatically convert to a float since division is involved.
convert2 = int(7.8) * 2  # This will convert to an int since all arguments are ints.

print("myList = " + str(myList) + " and is of type " + str(type(myList)) +  # yet another way of using continuation
      " and is made up of elements " + str(myList[0]) + ", " + str(myList[1]) + ", and " + str(myList[2]))
print("myBool = " + str(myBool) + " and is of type " + str(type(myBool)))
print("myBool2 = " + str(myBool2) + " and is of type " + str(type(myBool2)))
print("myInt = " + str(myInt) + " and is of type " + str(type(myInt)))
print("myFloat = " + str(myFloat) + " and is of type " + str(type(myFloat)))
print("myString = " + myString + " and starts with " + myString[0] + " and is of type " + str(type(myString)))
print("\nmyStringML = " + myStringML + "It is of type " + str(type(myStringML)) + "\n")
print("convert = " + str(convert) + " and is of type " + str(type(convert)))
print("convert2 = " + str(convert2) + " and is of type " + str(type(convert2)))

# Here is a way to ask for user input
answer = input("\nEnter your input!\n")
print("\nYour input was \"" + answer + "\"!")

# Here are a bunch of ways to manipulate Strings.
print("\nSTRINGS:")
emptyString = ""
emptyString2 = str()
str1 = "Hello, "
str2 = "World!"
str1 += str2
str2 *= 5
print("str1 = " + str1)
print("str2 = " + str2)
print("The third letter of str1 is " + str1[2])
print("The length of str1 is " + str(len(str1)))
print("str1 all capitalized is " + str1.upper())
print("str1 all lowercase is " + str1.lower())
print("str1 with dashes between every character is " + "-".join(str1))
print("str1 with all dashes removed is " + str(str1.split("-")))  # str() conversion is needed b/c .split returns a list
print("Every other character of str1 starting at index 3 and ending at index 10 is \"" + str1[3:10:2] + "\"")
print("The statement that str1 contains only letters is " + str(str1.isalpha()))
print("The statement that str1 contains only letters and numbers is " + str(str1.isalnum()))

# Here are a bunch of ways to manipulate Lists.
print("\nLISTS:")
list1 = [1, 2, 3]
list2 = [7, 6, 5, 4]
list3 = ["brandon", "1", "bob", "b3", "-1", "br@ndon", "1b"]
print("list1 and list2 zipped is " + str(list(zip(list1, list2))))
print("list1 and list2 concatenated is " + str(list1 + list2))
x = list2.pop(2)  # pop is the same as remove, but it also returns the value
print("The popped value from list2 was " + str(x))
list1.append(list2)
list1.append([8])
list1.insert(2, 2.5)
list1.remove(1)
print("2.5 inserted into list1 at index 2, 1 removed from list1, and list2 and [8] appended to list1 is " + str(list1))
print("The length of list1 is " + str(len(list1)))
print("The minimum of list3 is " + str(min(list3)))
print("The maximum of list3 is " + str(max(list3)))
print("list3 sorted is " + str(sorted(list3)))
list3.sort()  # Equivalent to saying list3 = sorted(list3)
print("list3 sorted is still" + str(list3))
print("The index of 6 in list2 is " + str(list2.index(6)))
print(str("The index of list2 in list1 is " + str(list1.index([7, 6, 4]))))
list4 = range(5)
list5 = range(3, 7)
list6 = range(14, 3, -2)
print("list4 = " + str(list(list4)))
print("list5 = " + str(list(list5)))
print("list6 = " + str(list(list6)))
print("Every other element of list4 is " + str(list(list4[::2])))
print("list5 starting at index 2 is " + str(list(list5[2:])))
print("list6 ending at (but not including) index 5 is " + str(list(list6[:5])))
list4 = list(list4)  # The "del" function is not supported for range objects, so we convert it to a list
del(list4[2])
print("list4 after deleting the element indexed at 2 is " + str(list4))
# This is how to apply a filter to a list
print("list4 filtered = " + str(list(filter(lambda item: (0 < item < 5 and item % 2 == 0), list4))))

# Here are a bunch of ways to manipulate Sets
print("\nSETS")
mySet = {1, "apple", 3.7}  # sets are unordered
print("mySet = " + str(mySet))
mySet.clear()
mySet.add(10)
copycat = mySet.copy()
print("copycat = " + str(copycat))
mySet = {5}
mySet.update([10, 15, 20, 25])
mySet.remove(20)
print("copycat is a subset of mySet: " + str(copycat.issubset(mySet)))
print("mySet is a superset of copycat: " + str(mySet.issuperset(copycat)))
print("mySet and copycat are disjoint: " + str(mySet.isdisjoint(copycat)))
print("The difference of copycat and mySet is " + str(mySet.difference(copycat)))
print("The union of copycat and mySet is " + str(mySet.union(copycat)))
print("The intersection of copycat and mySet is " + str(mySet.intersection(copycat)))
print(str(mySet.pop()) + " just got popped from mySet!")  # removes the oldest item from the set

# Here are a bunch of Math-related things.
print("\nMATH STUFF:")
print("1000, base 2 = " + str(int("1000", 2)))
print("5^3 = " + str(5**3))
print("18 (mod 4) = " + str(18 % 4))
x = 0
x += 1
x -= 5
x *= 10
x /= 2
x **= 3
x = ----x  # Equivalent to saying x = x because of quadruple negative
x = int(x)  # This isn't educational, I just need x to stop being a float after line 130.
print("x = " + str(x))
print("The max of 1, 2, and 3 is " + str(max(myList)))  # max may take any combination of data types, including strings
print("The min of 1, 2, and 3 is " + str(min(myList)))  # min may take any combination of data types, including strings
print("The sum of 1, 2, and 3 is " + str(sum(myList)))  # sum may take booleans, ints, and floats
print("The absolute value of x is " + str(abs(x)))  # abs may take booleans, ints, and floats
print("A random integer between 1 and 10 is " + str(randint(1, 10)))  # 1 and 10 are both inclusive, requires import
print("x in binary is " + bin(x))  # bin returns a string
print("x in base 8 is " + oct(x))  # oct returns a string
print("x in hexadecimal is " + hex(x))  # hex returns a string

# Here are Bit-wise Operators
print("\nBIT-WISE OPERATORS")
x = 0b1011  # 0b, 0o, and 0x indicate the base where b is binary, o is octal, and x is hexadecimal
print("0b1011 is stored as " + str(x))
y = int("110101", 2)  # Converts 110101 from base 2 to an int, which is 53
print("x = " + str(x))
print("y = " + str(y))
print("y >> 2 is a right shift, so the last 2 digits are deleted. y >> 2 = " + str(y >> 2))
print("y << 2 is a left shift, so 2 zeroes are added to the end of y. y << 2 = " + str(y << 2))
print("x & y is the AND operator, which returns the intersection of 1s in x and y. x & y = " + str(x & y))
print("x | y is the OR operator, which returns the union of 1s in x and y. x | y = " + str(x | y))
print("x ^ y is the XOR operator, which returns the union minus intersection of 1s in x and y. x ^ y = " + str(x ^ y))
print("~x is the NOT operator, which returns all 1s replaced by 0s and all 0s replaced by 1s. ~x = " + str(~x))
print("Since this accounts for all 16 digits, this will usually equal -(x+1).")

# Here are Conditionals
print("\nCONDITIONALS:")
if x == 0:
    pass  # Executes if true, but does literally nothing. Useful for creating a condition for elif statements to fail.
elif x < 0:  # Stands for "else if"
    x = -x
    x = --x
elif x != 8000:
    x = 8000
else:
    x = 0
print("After the first if block, x now equals " + str(x))

x = 5
y = z = 5

if x < 0 and x / 0 == 5:
    print("This will not execute!")
    # This does not raise an error because once the computer sees that x < 0 is false, it ignores the rest.
if 0 < x < 10000 or x / 0 == 5:
    print("This does execute!")
    # This does not raise an error because once the computer sees that 0 < x < 10000 is true, it ignores the rest.
if x == y == z == 5 and not not x < 0 or not x < 0:
    #                3   2   1        5   4            1 happens first, then 2, then 3, then 4, then 5
    print("This simplifies to (True and False) or True, which overall is True. Parentheses can change the order.")
    print("It does NOT become True and (False or True), even though that is also True overall.")
if x not in myList:
    print("x is not in my list!")
if x in myList:
    print("x is in my list!")

# Here are Loops
print("\nLOOPS:")
for num in range(5):
    if num == 1:
        continue  # ends the current iteration and begins the next iteration; also applies to while loops
    if num == 3:
        break  # ends the entire loop without finishing the current iteration; also applies to while loops
    print("This is iteration #" + str(num) + " of the for loop!")
else:
    print("This doesn't get printed because the for loop executed a break statement!")
print("")

myList = ["Bob", "Alice", "Sally", "Timmy"]
for name in myList:
    print("This for loop prints names! Right now it is printing " + name + "'s name!")
else:
    print("This gets printed because the for loop exited naturally!")
print("")

for x, y in enumerate(myList):
    print("This is an enumeration! " + y + " is at index " + str(x) + " in myList!")
print("")

num = 5
while num > 0:
    print("I'm the output from a while loop! num = " + str(num))
    num -= 1
else:
    print("Now the while loop is done! num = " + str(num))

# Here are List Comprehensions
print("\nLIST COMPREHENSION")
print(["Another One" for x in range(5)])
print([x**2 for x in range(20) if x % 2 == 0])

# Here are Dictionaries. Dictionaries can do almost everything that lists can do and can be used as hash maps.
print("\nDICTIONARIES")
myDictionary = {
    1: "Bob",
    2: 5.7,
    0: "No One",
    5: [1, 2, 3],
    6: True
}  # The entire dictionary could be on one line if you wanted it to be, but this style is convention.
if True:
    myDictionary[0] = "Bob"  # Edits an entry since that entry already exists
myDictionary[4] = "Timmy"  # Adds an entry since that entry doesn't already exist
del(myDictionary[2])
print("The value that has a key of 5 in myDictionary is " + str(myDictionary[5]))
print("The value at index 2 within the list with a key of 5 in myDictionary is " + str(myDictionary[5][2]))
print("The entire contents of myDictionary are " + str(myDictionary))
print("An immutable list of (key, value) tuples in myDictionary is " + str(myDictionary.items()))
print("An immutable list of keys in myDictionary is " + str(myDictionary.keys()))
print("An immutable list of values in myDictionary is " + str(myDictionary.values()))

# Here is Error Testing
try:
    print(10/num)  # num = 0, so this throws a ZeroDivisionError
    raise IndexError  # causes an error, useful for testing your code
except(ZeroDivisionError, IndexError):
    print("This is an error message!")

# Here is File Reading / Writing
print("\nFILE HANDLING")
example = open("example.txt", "w+")  # Either creates (and then opens) or just opens example.txt.
# w+ is read + write, r is read, w is (over)write, x is exclusive creation, a is append, b is binary mode,
# t is text mode, u is universal newlines mode. By default, a file will be read only and text mode.
print("example.txt is currently closed: " + str(example.closed))
example.write("This is the first line of the file!\n")
example.write("This is the second line of the file!\nThis is the third line of the file!")
example.close()

with open("example.txt", "r") as example:  # Automatically closes the file when done
    exampleContents = example.read()  # Reads the entire file
with open("example.txt", "w") as example:
    example.write("This is the NEW first line of the file!")
    example.write("\nThis is the NEW second line of the file!")
with open("example.txt", "r") as example:
    print(example.readline() + example.readline())
    print(example.readline())  # This only prints a blank line because the old contents are gone.

print(exampleContents)
print("example.txt is currently closed: " + str(example.closed))

# Here are Date and Time Methods
print("\nDATE AND TIME")
# The datetime library needs to be imported first
print("This exact moment is " + str(datetime.now()))
print("Or you can specify just the seconds as " + str(datetime.now().second))

# Here are Functions
print("\nFUNCTIONS")


# Functions are supposed to have 2 blank lines before and after them by convention
def myFunction(parameter1, parameter2):
    parameter1 += 1
    parameter2 -= 1
    return parameter1, parameter2


x, y = myFunction(5, 10)
print("x = " + str(x))
print("y = " + str(y))


def recursiveFunction(myNumber):
    if myNumber == 0:
        return
    print("I'm in a recursive function!  num = " + str(myNumber))
    recursiveFunction(myNumber - 1)


recursiveFunction(4)

# Here are Classes
print("\nCLASSES")


class Shapes (object):
    def __init__(self, shapeName, numSides, regular):
        self.name = shapeName
        self.sides = numSides
        self.isRegular = regular

    isTwoDimensional = True

    def calculateAvgAngle(self):
        return (self.sides - 2) * 180 / self.sides

    def printName(self, index):
        print("I'm a shape! My " + index + " name is " + self.name + "!")


class StarShapes (Shapes):
    def __init__(self, shapeName, idNum, numSides, regular):
        super(StarShapes, self).__init__(shapeName, numSides, regular)  # "super" calls the parent method with same name
        self.idNumber = idNum

    def __repr__(self):
        return "a " + self.name

    isConvex = False

    def calculateAvgAngle(self):
        if self.isConvex:
            return super(StarShapes, self).calculateAvgAngle()
        else:
            return ((self.sides - 1) * 180) / self.sides

    def printID(self):
        print("I'm a star! My ID Number is " + self.idNumber + ".")


shape1 = Shapes("rectangle", 4, True)
shape2 = StarShapes("5-point star", "1", 5, True)
print("shape1 is " + str(shape1))
print("shape2 is " + str(shape2))
shape1.printName("middle")
shape2.printName("first")
shape2.printID()
print("A " + str(shape1.name) + " is 2-Dimensional: " + str(shape1.isTwoDimensional))
print("A " + str(shape2.name) + " is 2-Dimensional: " + str(shape2.isTwoDimensional))
print("shape2 is convex: " + str(shape2.isConvex))
print("The average angle in a " + shape1.name + " is " + str(shape1.calculateAvgAngle()))
print("The average angle in a " + shape2.name + " is " + str(shape2.calculateAvgAngle()))
shape2.isConvex = True
print("The average angle in a convex " + shape2.name + " would be " + str(shape2.calculateAvgAngle()) + ".")
print("shape2 is convex: " + str(shape2.isConvex))
