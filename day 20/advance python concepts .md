# GENRATOR:

* is a specific sort of function that genrate the sequence of value usung the yeild keyword
* A generator in Python is a special function that gives values one by one using yield instead of returning all values at once.It saves memory and is useful for loops.



# Difference Between `return` and `yield`

| return                | yield                   |
| --------------------- | ----------------------- |
| Ends function         | Pauses function         |
| Gives one final value | Gives values one by one |
| Normal function       | Generator function      |

**SYNTAX****:**

```
def function_name():
      parguments   yield value
```

**EXAMPLE:**

```
def genrator():
    yield 1
    yield 2
    yield 3

gen= genrator()
print(next(gen))
print(next(gen))
print(next(gen))

```


# DECORATOR:

its a function  and extern   its functionality and return the modifiyed function with externded  functionality

the main objective of the decorator  is for improving the  functionality of exiting function without changing the original function

**SYNTAX:**

```
def decorator function_name(arguments):     ##inputs 

          def outputfunction_name(arguments):
                    externded  function statement 
          return output function_name 
def  function_name(arguments):
          function statement block
function_name(argumrnts)
```
