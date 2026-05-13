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

