# In Python, a string is a sequence of characters enclosed in quotes. You can use:

# Single quotes 'hello'

# Double quotes "hello"


string = 'my name is mashood ali'
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

def count_vovels(s):
    vovels="aeiouAEIOU"
    return sum(1 for char in s if char in vovels)
print(count_vovels("education"))