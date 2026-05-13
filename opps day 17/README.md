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

# 2. Run Time Polymorphism

## Definition

The method call is decided during the  **program execution (runtime)** .

It is achieved using:

* **Method Overriding**

```
class Animal:

    def sound(self):
        print("Animals make sounds")


class Dog(Animal):

    # Overriding
    def sound(self):
        print("Dog barks")


d = Dog()

d.sound()

```

# ABSTRACTION:

the pinomenon of the  hiding the complex implementation detailes while exposing the only

in python to acchive the abstrction we use the abstract class and abstract method

#### abstract class:

* in python abstrct class is a class that cont be implemented on any functionalitys and its decided to be a blueprint of the other classs

#### ABSTRACT METHOD :

* an abstract method in python in python is method declear the abstrct clas but doest provied the implementation  to declear in abstrct method in python we should use the decarator called @abstract method

## Real-Time Example

## ATM Machine

When you use an ATM:

* You insert card
* Enter PIN
* Withdraw money

You do NOT know:

* How server works
* How transaction happens internally

This is called abstraction
