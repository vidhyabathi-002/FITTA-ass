# POLYMORPHISM:

> poly-many morphism - forms
>
> **Polymorphism** is a core concept in **Object-Oriented Programming** that means "many forms." It allows the same function, method, or operator to behave differently depending on the context.
>
> 2 TYPES:
>
> * COMPILE TIME
> * RUN TIME

### 1. Compile-time Polymorphism (Static)

Also called  **method overloading** .

> itsa programing technniques that allows multiple functions to have the same name but diff implementation  if   with perform method overloading
>
> python will perform method overiding because of  dynamic memory

operater overloading allows same operater to have diff meaning difending on the object operation

* Same function name
* Different parameters (type or number)

```

class Calculator:

    # Method Overloading
    def add(self, a, b, c=0):
        print(a + b + c)


c = Calculator()

c.add(10, 20)
c.add(10, 20, 30)


```
