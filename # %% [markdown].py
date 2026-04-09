# %% [markdown]
# 1)GiventwointegersNandMasinputs,printarectangleofN*Mstars.Forexample,ifN=3,M=4thenpatternwillbelike
# 

# %%

N, M = 3, 4
for _ in range(N):
    print("*" * M)


# %% [markdown]
# 2.# Count factors of N
# 

# %%

N = 6
count = sum(1 for i in range(1, N+1) if N % i == 0)
print(count)  


# %% [markdown]
# #3.prime are not 
# 

# %%

A = 17
is_prime = all(A % i != 0 
               for i in range(2, int(A**0.5)+1)) and A > 1
print(" is a Prime" if is_prime else "Not Prime")


# %% [markdown]
# 5.LCM
# 

# %%
import math
A, B = 12, 15
lcm = abs(A*B) // math.gcd(A, B)
print(lcm) 


# %% [markdown]
# 6.calculate and print thesum of the digiT sof the number N.
# 

# %%
N= 12345
digit_sum = sum(int(digit) for digit in str(N)) 
print(digit_sum)   


# %% [markdown]
# 7. integer N,Check the give nnumber is a Armstrong Number or not    

# %%
N=193 
num_str = str(N)
num_digits = len(num_str)           
armstrong_sum = sum(int(digit)**num_digits for digit in num_str)
if armstrong_sum == N:              

    print(f"{N} is an Armstrong number.")           

else:
    print(f"{N} is not an Armstrong number.")       





# %%


# %% [markdown]
# 8)GivenanumberA.Return1ifitisaperfectsquareotherwise,return0.Example:4isaperfectsquare,1001isnotaperfect
# 

# %%
# perfect square returns true if the number is a perfect square, otherwise false
def perfect_square(n):  
    if n < 0:
        return False
    root = int(n**0.5)
    return root * root == n                         
N = 16
if perfect_square(N):           

    print(f"{N} is a perfect square.")  

else:
    print(f"{N} is not a perfect square.")          




                    

# %% [markdown]
# 9.Given a sorted integer array A, and an integer B. Find the first and last 
# index of B in A. 
# A = [-2, -2, 4, 4, 8, 9] 
# B = 4 
# Output : C = [2, 3] 
# A = [1, 9, 9, 9, 10, 21] 
# B = 9 
# Output : C = [1, 3] 
# 

# %%
 
def find_first_last(A, B):
    first = -1
    last = -1
    for i in range(len(A)):
        if A[i] == B:
            if first == -1:
                first = i
            last = i
    return [first, last]
A = [1, 2, 3, 4, 2, 5]
B = 2       
print(find_first_last(A, B))



# %% [markdown]
# 10) You are given an integer array A and an integer B. 
# You are required to return the count of pairs having sum equal to B. 
# Note : i!=j(Pair Number indexes should not be same) 
# A = [1,2,3,2,1]   B = 5 
# Output : 2 
# A = [1,1,1]   B = 2 
# Output : 3 
# 

# %%

def count_pairs_with_sum(A, B):
    count = 0
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            if A[i] + A[j] == B:
                count += 1
    return count    
A = [1,2,3,2,1]
B = 4

print(count_pairs_with_sum(A, B))   


# %% [markdown]
# 30)  Implement a simple calculator using React, that adds two numbers 
# entered by the user.
# 

# %%
## calculator for user inputed numbers only addition 
def calculator():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 + num2
    print(f"The sum of {num1} and {num2} is: {result}") 





# %% [markdown]
# 11) You are given an integer array A. Now your task is to find the inverse of A. 
# Now, the inverse of the array is A will be an array in which we change the 
# positions of the values as their indices and indices as values. 
# So, array A = [2, 0, 1] - Now 2 is at index 0. So, place 0 at index 2. - 0 is at index 1. So, place 1 at index 0. - 1 is at index 2. So, place 2 at index 1. 
# So, the inverse of A will be [1, 2, 0]

# %%
def inverse_array(A):
    n = len(A)
    inverse = [0] * n
    for i in range(n):
        inverse[A[i]] = i
    return inverse  
A = [2, 0, 1]
print(inverse_array(A)) 



# %% [markdown]
# #12) Given a 2D integer array C[][] of A rows and B columns. Return an integer array of size B that represents the sums of the columns of the 2D array C. 
# 
# 

# %%




def column_sums(C):
    if not C:
        return []
    num_cols = len(C[0])
    sums = [0] * num_cols
    for row in C:
        for j in range(num_cols):
            sums[j] += row[j]
    return sums 
C = [[4, 1], [1, 3], [6, 2]]
print(column_sums(C))   


# %% [markdown]
# 15) Write a program that returns the list of elements that are present in the 
# given list and are divisible by 5 and 7.  
# Note : Use ArrayList.  
# Input : A = [5, 7, 70, 50, 35] 
# Output : [70, 35]
# 

# %%
#15) Write a program that returns the list of elements that are present in the given list and are divisible by 5 and 7.  Note : Use ArrayList.  Input : A = [5, 7, 70, 50, 35] Output : [70, 35]

def divisible_by_5_and_7(A):
    result = []
    for num in A:
        if num % 5 == 0 and num % 7 == 0:
            result.append(num)
    return result
A = [5, 7, 70, 50, 35]
print(divisible_by_5_and_7(A))
    

# %% [markdown]
# 18)  Write a program to find if a string is a palindrome using OOP principles in

# %%
#18)  Write a program to find if a string is a palindrome using OOP principles in

class PalindromeChecker:
    def __init__(self, string):
        self.string = string

    def is_palindrome(self):
        cleaned_string = ''.join(self.string.split()).lower()
        return cleaned_string == cleaned_string[::-1]   
string = "A man a plan a canal Panama"
checker = PalindromeChecker(string) 
print(checker.is_palindrome())



