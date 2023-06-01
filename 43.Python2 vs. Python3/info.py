History

Python 2
Introduced in 2000
make programming simple and easy to lean for the common mass

Python 3
Introduced in 2008
redundancy - writing repetitive code or writing the same piece of code again
and again - should be removed from coding

Syntax

Python 2
print "Hello World" # statement

Python 3
print("Hello World") # function

Storage of Strings

Python 2
ASCII: a method of encoding English characters with an assigned number
Do not have a enough symbols due to 7 bits

Python 3
Unicode: the practical UTF-8 (Unicode Transformation Format-8-bit)
support foreign languages and other widely used symbols and emojis.

Libraries

Python 2
Not forward compatible, Hard to porting from Python2 to Python3 is hell
No longer supported by the year 2020

Python 3
Backward-incompatible. Always gear toward future improvements
A lot of libraries are specific for Python3

Division of Integers

Python 2
Round down for the integer division ( 9 divided by 4 is 2 )

Python 3
Exact number ( 9 divided by 4 is 2.25 )

Variable leakage

Python 2
The values of global variables do change in Python 2 if they are used inside
a for-loop.

i = 0
a = [i for i in range(3)]
print(i) # Ouputs 2

Python 3
The value of variables never changes in Python 3.

i = 0
a = [i for i in range(3)]
print(i) # Outputs 0

Use case

Python 2
Used by DevOps engineer

Python 3
Used by Software Engineer, Data Science and etc

Trend

From 2015~ common used Python 3