# nums = [1,2,3]
# string = ["Hello", "World", "Hi"]
# import functools
# def combine(items):
#     return functools.reduce(lambda x, y: x + y, items)
# combine(nums)

# # def x, y: x + y 'reduce to a single value'
# from functools import reduce
# scores = [75, 65, 80, 95, 50]
# total = reduce(lambda a, b: a + b, scores)
# print(total)

# def check_factorial(num1):
#     #filter(x if x != ) x 
#     for i in range (1, num1):
#         list1.append(i)
#     while sum(list1) <= num1:
#         for i in range (1, num1):
#             for j in range (1,i):
#                 result *= list1[j]
#                 if list1[i] != result:
#                     del.list1[i]
#     return num1
# check_factorial(150)

# # 150
# # 1,2,149
# def check_factorial(num1):
#     fact = 
#     for i in range (num1):
#         fact *= i

#     while result < fact
#         for i in range (num1):
#             for j in range (i):
#                 result *= j
#                 list1.append(i)
        
# while summ < num1:


# MAX = 10
# # Function that returns true
# # if n is a Factorion

# def isFactorion(n) :
# 	# fact[i] will store i!
# 	fact = [0] * MAX
# 	fact[0] = 1
# 	for i in range(1, MAX):
# 		fact[i] = i * fact[i - 1]
# 	# A copy of the given integer
# 	org = n
# 	# To store the sum of factorials
# 	# of the digits of n
# 	sum = 0
# 	while n > 0 :
# 		# Get the last digit
# 		d = n % 10
# 		# Add the factorial of the current
# 		# digit to the sum
# 		sum += fact[d]
# 		# Remove the last digit
# 		n = n // 10
# 	if (sum == org):
# 		return True
# 	return False
# def check_factorian(n):
#     list10=[]
#     for i in range n:
#         if isFactorion(i):
#             list10.append(i)
#     return list10
# check_factorian(150)





# # 
# def odd(data):
#     if len(data[1:]) == 0:
#         return data
#     else:
#         return data[0] + odd(data[2:])
# odd(lll)
# lll = [5,6,2,4,3,9]

# def number(set1):
#     if len(set1) == 0:
#         return set1
#     else:
#         if str(set1[0]).isdigit():
#             return [set1[0]] +number(set1[1:])
#         else:
#             return number(set1[1:])
        
# set1=[1,2,3, "hello", 4,5]
# number(set1)

# # class Book:
# #     def assign(self, genre, title, author, year):
# #         self.genre = genres
# #         self.title = title
# #         self.author = author
# #         self.year = year

# #     def yes_no(year):
# #         if year





# MAX = 10

# def isFactorion(n) :
# 	for i in range(1, MAX):
# 		fact[i] = i * fact[i - 1]
# 	org = n
# 	sum = 0
# 	while n > 0 :
# 		d = n % 10
# 		sum += fact[d]
# 		n = n // 10
# 	if (sum == org):
# 		return True
# 	return False

# #####
# #check_factoriabn
# def isFactorion(n) :
#     digit = 10 
#     sum = 0
#     while n > 0 :
#         d = n % 10
#         sum += fact[d]
#         n = n // 10
#     if sum == input:
#         return True
#     return False

# def check_factorian(result):
#     list1 = []
#     for i in range (result+1):
#         list1.append(i)
#     list2=map(isFactorion, list1)#.index(True)
#     return [i for i, e in enumerate(list2) if e == True]

# check_factorian(2)

# # check_is_pandigital
# def is_pandigital(numb):
#     list1,list2 = [],[]
#     mull,mull2=1,1
#     while numb > 0:
#         d = numb % 10
#         list1.append(d)
#         numb = numb // 10
#     for i in range(1,len(list1)+1):
#         list2.append(i)
#     for item in list1:
#         mull *= item
#     for item in list2:
#         mull2 *= item
#     if mull == mull2:
#         return True
#     else:
#         return False

# def check_is_pandigital(result):
#     list1 = []
#     for i in range (1, result+1):
#         list1.append(i)
#     list2=map(is_pandigital, list1)#.index(True)
#     return [i+1 for i, e in enumerate(list2) if e == True]
    
# check_is_pandigital(21)


# check_is_pandigital
def is_pandigital(numb):
    list1,list2 = [],[]
    mull,mull2=1,1
    while numb > 0:
        d = numb % 10
        list1.append(d)
        numb = numb // 10
    for i in range(1,len(list1)+1):
        list2.append(i)
    for item in list1:
        mull *= item
    for item in list2:
        mull2 *= item
    if mull == mull2:
        return True
    else:
        return False

def check_is_pandigital(result):
    list1 = []
    for i in range (1, result+1):
        list1.append(i)
    list2=map(is_pandigital, list1)#.index(True)
    return [i+1 for i, e in enumerate(list2) if e == True]
    
check_is_pandigital(21)

###
import functools 
def isFactorion(n) :
    digit = 10
    fact = [0] * digit
    fact[0] = 1
    for i in range(1, digit):
        fact[i] = i * fact[i - 1]
    input = n
    sum = 0
    while n > 0 :
        d = n % 10
        sum += fact[d]
        n = n // 10
    if sum == input:
        return True
    return False

def check_factorian(result):
    list1 = []
    for i in range (result+1):
        list1.append(i)
    list2=map(isFactorion, list1)#.index(True)
    return [i for i, e in enumerate(list2) if e == True]

check_factorian(2)
