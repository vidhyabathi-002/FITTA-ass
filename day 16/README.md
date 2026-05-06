# INTERVIEW QUTIONS IN OOPS CONCEPTS:

> DAY 16 FITA 

1. STUDENT DETAILES      :create a class student with constructor to intialize name aand age, display the details
2. CAR INFORMATION        :create a car with constructor to initialize brand and price , print car detailes
3. BOOK DETAILES             : create a class book  with constrector  initialize title and  author display book info
4. EMP SALARY                   :  create a class emp with constrector  initialize na,me , salary , print emp detailes
5. MOBILE PHONE              : craete  a class mobile with constrector  initialize model,price . display the mobile detailes
6. BANK ACCOUNT             : create a class bank with constrector  initialize acc_no and balance . print the account detailes
7. DOG DETAILES               : create a class dog with constrector  initialize the name of the dog and  bread
8. LAPTO[P DETAILES        :.Create a class Laptop with constructor to initialize brand and RAM size. Print Laptop details
9. TEACHER DETILES        : Create a class Teacher with constructor to initialize name and subject. Display teacher details.
10. BIKE DETAILES               : Create a class Bike with constructor to initialize model and price. Print bike details.

## CONSTRAINT SATISFACTION PROBLEM(CSP):

* is a problem where a set of variable must be assigned values that satisfy a number of constraines
* used in AI  and ML  for solving  combinatorial

## COMPONENTS OF CSP:

**1.VARIABLES(X):**
             >>>    (X={X_1,X_2.........,X_N})

    >>> EXAMPLE : subject. time slots,colors

**2.DOMINES(D):**

* each variable has a dommine  of possible values
*  (D_i={V_1,V_2.......V_K})

**3.CONSTRAINTS(C):**

* restrictions of the values  that variables can take
* can be unary,binary,or higher-order

**FORMULA:**

**REPRESENTATION:**

CSP=(X,D,C)

## TYPES OF CONSTRAINTS:

1. **unary constraint:**
   restricts one variable
   example: X!= RED
2. **BINARY CONSTRAINTS:**
   between two variable
   example: X!= Y
3. **GLOBAL CONSTARINES :**
   involve multiple variable
   example:all diff - constraints 


**CONSTRAINT GRAPS:**
               csp can be represented  using  a constraint graphs

**BASIC ALGORITHMS:**

* assining the variable
* check the constraints
* if voilation ------>backtrack
* continue untile the  sollution found
