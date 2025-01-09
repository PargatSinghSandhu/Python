Python function first looks for variable in the local scope, if not then go to the global scope.
Nomenclature in c++ it is function name leetCode in py it is leet_code
Always write code in modules, keep your code into modules for better understanding.
 Use try/except for best coding practices, 
Use Exception keyword in the except block to catch the exception and print
Encapsulation: Use __ in front of a variable
 to make it private, so that it can not be accessed outside the through objects, or through any other class. Can only be accessed through getter. For example : __brand 
Use getter to get the value, and can use setter to set the value.. 
Use lambda functions when required:


cube = lambda x, y: x**y


print(cube(3,4))


cube = lambda parameters1, parameters1 : parameters1**parameters2


print(cube(x:3, y:4))

*args
def sum_all(*args):
   print(args) # it prints the tuple
   print(*args) #it prints the each element seprately
   return sum(args)




print(sum_all(1, 2, 3))



10.In a closure, when an inner function is defined within an outer function, it carries with it all the variables from the outer function's scope (known as free variables) and their references. This "bag" of variables is bundled together with the inner function, allowing it to access these variables even after the outer function has finished executing. This bundled environment, called a closure, makes it possible to retain and use the state of the outer function whenever the inner function is called later.

def cube(n):
   def inner_cal():
       return n**3
   return inner_cal  #this will pack  the whole bundle of inner_cal function with the variable and its reference


closure = cube(3) #this  will pass the 3 to the cube function, and will get the whole bundle or funcition def with it variable , and referencews back




print(closure()) #it will print the value

Case 2:
def cube(n):
   def inner_cal(cube_value):
       return n**cube_value
   return inner_cal  #this will pack  the whole bundle of inner_cal function with the variable and its reference


closure = cube(3) #this  will pass the 3 to the cube function, and will get the whole bundle or funcition def with it variable , and referencews back
closure2 = cube(2)


print(closure(3)) #it will print the value
print(closure(2))


def outer_function(greeting, name):
    def inner_function():
        # Access variables from the outer function
        return f"{greeting}, {name}!"
    return inner_function  # Return the inner function

# Create the closure
closure = outer_function("Hello", "Pargat")

# Call the closure
print(closure())  # Output: Hello, Pargat!

11. In scope it goes upward, if the variable is not in that black it goes outside the block to look 
x = 22


def print_x():
   print(x)


print_x()
2nd case, here value of globe is not changing and can be accessed:
x = 22


def print_x():
   x =23
   print(x)


print_x()
print(x)


This is bad practise of using the globe, it changes the value of global x from the function.
x = 22


def print_x():
   global x
   x = 23
   print(x)


print_x()
print(x)


13. There are two major categories of data types in the Python, Mutable and Immutable. 
Mutable, which can be modified-
Immutable, which can not be modified-


x=10
y=x

print(x)
print(y)

x =11
print(y)
Output:
10
10
10

The reason why it does not changes the y, because 
X was referring to memory block which was having value 10, then y was referring to the same block, now when x=11, the x will refer to new memory block with 11, and y is still referring to the same block with the value 10.

One important point
Let’s say score = 10

Now there will be a block in the memory space with the value 10, so the datatype int will be given to the memory block 10, not to the score. Score variable name is irrelevant of any data type.
