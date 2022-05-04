"""#List Less Than Ten  
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
elder=int(input("Enter a number"))
less_list=[i for i in a if i <= elder]
print(less_list)

#  Divisors

num = int(input("Enter a number")) 
divisors=[]
for i in range(2,101):
    if num%i==0:
        divisors.append(i)
print(f'The divisors of {num} are: {divisors}')
"""
#  List Overlap
import random  
a = [random.randint(1,100)for e in range(13)]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = a+b
duplicate=[]
for i in c:
    if i not in duplicate:
        duplicate.append(i)

#duplicate=[i for i in a if i not in duplicate]
print(duplicate)