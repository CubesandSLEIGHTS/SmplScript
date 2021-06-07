## How to write a program in SmplScript

#### What is SmplScript?
SmplScript is an interpreted scripting language. It is meant for the beginner programmer and based off of the English language as much as possible.

---

#### What is the syntax to print something?
The following code gives an example of how to print out "Hello world"
```SmplScript
print("Hello world")
```

---
#### How do I make a variable and how do I reassign the variable's value?

To make a variable, you must use the ```assign``` keyword. Here is an example:

```
assign x = 10
```

Then when you  want to reassign the variable use the same syntax:

```
assign x = "hello there"
```

---

#### How do I make a function?

To make a function, you have to use the ```define-func``` keyword then the arrow (```->```) for a single line function. Here is an example:

```
define-func hello_there() -> print("Hello there")
```
Then call the function by caling the function name and arguments if there are any:

```
hello_there()
```
this would print out:

> Hello there

---

#### What loops are there?

There are ```for``` loops and ```while``` loops

##### How do I use ```for``` loops?
This is a basic ```for``` loop:

```
for assign i = 1 to 99 then print(i)
```
This will print out the numbers 1 to 98 as this function is not inclusive.