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

# ==========check work is available or not ==========

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
# print(count_vovels("education"))


# =========reverse strign==============
# def reverse_string(s):
#     reversed_str = ""
#     for char in s:
#         reversed_str = char + reversed_str  # prepend each character
#     return reversed_str

# print(reverse_string("hello"))

 
# =============Find frequency of each charcter in string=============

# Take input from user
input_string = input("Enter a string: ")

# Create an empty dictionary to store character frequencies
char_freq = {}

# Loop through each character in the string
for char in input_string:
    if char in char_freq:
        char_freq[char] += 1  # If already present, increment count
    else:
        char_freq[char] = 1   # If not present, initialize with 1

# Print the character frequencies
print("Character Frequencies:")
for char in char_freq:
    print(f"'{char}': {char_freq[char]}")
