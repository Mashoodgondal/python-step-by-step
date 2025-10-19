# In Python, a string is a sequence of characters enclosed in quotes. You can use:

# Single quotes 'hello'

# Double quotes "hello"


# string = 'my name is mashood ali'
# print(string)
# ========upercase========
# print(string.upper())
# ===========capitalize===========
# print(string.capitalize())
# ========title========
# print(string.title())
# =======Replace=======
# print(string.replace("mashood","ahmad"))
# ===========length=====
# print(len(string))

# ==========check word is available or not ==========

# print("ali" in string)

# ============string formation========

# name = "Ali"
# age = 25

# # Using f-strings (recommended)
# print(f"My name is {name} and I am {age} years old.")

# # Using format()
# print("My name is {} and I am {} years old.".format(name, age))


# name = "Ali"
# age = 25

# # Using f-strings (recommended)
# print(f"My name is {name} and I am {age} years old.")

# # Using format()
# print("My name is {} and I am {} years old.".format(name, age))

# =============remove duplicate in string===========
# def remove_duplicate(s):
#     result=""
#     for char in s:
#         if char not in result:
#             result += char
#     return result
# print(remove_duplicate("banana"))

# ==========count vowevels===========

# def count_vovels(s):
#     vowels="aeiouAEIOU"
#     # return sum(1 for char in s if char in vovels)
#     count = 0
#     for char in s:
#      if char in vowels:
#         count += 1
#     return count
# vowels = str(input("Enter a string: "))
# print(count_vovels(vowels))


# =========reverse strign==============
# def reverse_string(s):
#     reversed_str = ""
#     for char in s:
#         reversed_str = char + reversed_str  # prepend each character
#     return reversed_str

# print(reverse_string("hello"))

 
# =============Find frequency of each charcter in string=============

# Take input from user
# input_string = input("Enter a string: ")

# char_fre={}
# for char in input_string:
#     if char in char_fre:
#         char_fre[char] += 1
#     else:
#         char_fre[char] = 1

# print("Frequency of all characters is")
# for char in char_fre:
#     print(f"{char} : {char_fre[char]}")
            
# ==========Check for Palindrome==============

# str = str(input("Enter a string: "))

# # print(reversed(str))
# reverse = ''
# for char in str:
#     reverse = char + reverse
    
# if reverse == str:
#     print("true")
# else:
#     print("false")



# ===================Remove Duplicate Characters===========

# string = str(input("Enter a string: "))
# second= ''
# for char in string:
#     if char not in second:
#         second +=char
     
# print(second)


# =============Most Frequient character=================

# string = input("Enter a string: ")
# # Remove spaces
# string = string.replace(" ", "")
# frequency={}

# for char in string:
#     if char in frequency:
#         frequency[char] +=1
#     else:
#         frequency[char] = 1

# print(string)
# most_frequent = max(frequency,key=frequency.get)
# count = frequency[most_frequent]
# print("Mosr frequent character is: ", most_frequent , "it appears: " , count, " times")

# ============Remove Duplicates============

# string= str(input("Enter any string: "))
# duplicate=''
# seen = set()
# for char in string:
#     if char in seen:
#         duplicate+=char
#         seen.add(char)
# print("you are great")
# print(duplicate)

# ===========find second largest in array================

# arr = [2,4,6,7,8,6,8,9,6]
# def second_largest(arr):
#     unique =list(set(arr))
#     unique.sort(reverse=True)
#     return unique[1]
# print(second_largest(arr))

# ============third largest ===============

# arr = [2,4,6,7,8,6,8,9,6]
# def second_largest(arr):
#     unique =list(set(arr))
#     unique.sort(reverse=True)
#     return unique[2]
# print(second_largest(arr))

# ===================Find maximum number in array=============
# arr = [2,4,5,6,7,5,4,3,2,2,4,5]
# newarr =list(set(arr))
# newarr.sort(reverse=True)
# print(newarr[0])



# ======STRING SORTING METHODS

fruit=['apple','mengo','manana','orange']
fruit.sort(key=str.lower)
print(fruit)











fruit=['apple','mengo','manana','orange']
fruit.sort(key=str.lower)
print(fruit)
fruit=['apple','mengo','manana','orange']
fruit.sort(key=str.lower)
print(fruit)
