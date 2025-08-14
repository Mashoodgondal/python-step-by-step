# for i in range(5):
#     print(i)

# MARS_GRAVITY= 0.38
# earth_weight=input("Enter earth weight in kg: ")
# earth_weighted= float(earth_weight)
# mars_weight= earth_weighted * MARS_GRAVITY
# print(f"mars weight: {mars_weight}")

# =========== Ratio on other planets ============


# earth_weight = input("Enter Earth weight  ")
# earth_weight= float(earth_weight)
# gravity_ratios={
#     "Mercury": 0.38,
#         "Venus": 0.91,
#         "Mars": 0.38,
#         "Jupiter": 2.34,
#         "Saturn": 1.06,
#         "Uranus": 0.92,
#         "Neptune": 1.19,
#         "Pluto": 0.06
# }
# print("Weight of the object on other planets:")
# for planet,ratio in gravity_ratios.items():
#     planet_weight = earth_weight * ratio
#     print(f"{planet}:{planet_weight:.3f}kg")

# =============== if Statement ============
# age =10
# if age>15:
#     print("you are audult")
# else:
#     print("you are not audult")

# ================for loop=================

# arr = [2,4,5,6,4]

# for num in arr:
#     square = num * num

#     print(f"Squire of the {num} is: {square}")


# Define an array (list)
# numbers = [10, 20, 40, 30, 50]
# ===========remove element==========
# numbers.remove(20)
# print("remove one element",numbers)
# ==============add element===========
# numbers.append(70)
# print("addition of new number", numbers)
# ===============length of array=======
# print("here is the length of array: ", len(numbers))
# =================sum of the elements in array=======
# print("here is the sum of all numbers:" , sum(numbers))
# ================print all elements==============
# print("All numbers:", numbers)
# ===========remove accordign to condition=========
# numbers.pop(3)
# print("remove last element" , numbers)
# ============insert element============
# numbers.insert(4,80)
# print("print after insertion:" , numbers)
# ============clear all elements========
# numbers.clear()
# print("crear array", numbers)
# =========find index =====
# numbers.index(20)
# print("index of the number is " , numbers.index(20))
# =========sort array ==========
# numbers.sort()
# print(numbers)
# =========sort in reversed==========
# numbers.sort(reverse=True)
# print(numbers)
# ===========reverse array=========
# numbers.reverse()
# print(numbers)

# ============Find dogs years using human years============

# dog_years = 7.18
# age =  int(input("Enter an age in calendar years: "))
# total = age * dog_years
# print("That's"+ str(total) +"in dog years!")

# ========Print random number in dice===========
# import random
# sides = int(input("How many sides does your dice have? "))
# roll = random.randint(1, sides)
# print("Your roll is ", roll)

# ========== judge using color and adjecent========

# color = input("A color: ")
# adjective = input("An adjective: ")
# goal= input("A goal you would like to achieve:")
# if color=='blue' and adjective=='smelly' and goal=='eat fewer bugs':
#         # print("A color: ", color)
#         # print("An adjective: ", adjective)
#     print("At dawn the sky turned blue, and the air felt smelly. I decided today I will finally eat fewer bugs.")
# if color=='pink' and adjective=='friendly' and goal=='learn to code':
#         # print("A color: ", color)
#         # print("An adjective: ", adjective)
#     print("At dawn the sky turned pink, and the air felt friendly. I decided today I will finally learn to code.")

# ===============Multiply nummber======

# number = int(input("Enter a number "))
# while number < 100:
#     new_num= number * 2
#     print(new_num)
#     number = new_num

# ===========Game to guess secret number==========
# import random
# sceret_number = random.randint(1, 10)
# guess = int(input("Enter your guess number between(1,10): "))
# while guess != sceret_number:
#     if guess< sceret_number:
#         print("you are too low Try again")
#     else:
#         print("You are too high Try again")
#     guess= int(input("Enter again"))    

# print("congrants you are correct You'r number is ",sceret_number)

# ============ Round Game=============
# import random
# round_number = 0
# for i in range(6):
#     print("New institutoin")
#     num1= random.randint(1,99)
#     num2 = random.randint(1,99)
#     sum = num1 + num2
#     print(f"what is {num1} + {num2}? ")
#     use_input = int(input("Your answer: "))
#     if use_input == sum:
#         round_number += 1
#         print("Corrected")
#         print(f"you gotten {round_number} corrected")
#     else:
#         round_number = 0
#         print("wrong answer")
#         print(f"Expected answer is {sum}")

# =========== Number guess Game============
    
# import random
# # Random number between 1 and 100
# secret_number = random.randint(1, 100)
# attempts = 0

# # While loop for the guessing game
# while True:
#     guess = input("Guess a number between 1 and 100 (or type 'exit' to quit): ")
    
#     if guess.lower() == 'exit':
#         print("Thanks for playing! The number was:", secret_number)
#         break
    
#     if not guess.isdigit():
#         print("Please enter a valid number!")
#         continue

#     guess = int(guess)
#     attempts += 1

#     if guess < secret_number:
#         print("Too low! Try again.")
#     elif guess > secret_number:
#         print("Too high! Try again.")
#     else:
#         print(f"🎉 Congratulations! You guessed it in {attempts} attempts.")
#         break


# =================Remove duplicates from a sorted array (in-place).===========

# array= [2,5,6,7,6,5,4,3,2]
# newarr = list(set(array))
# print(newarr)


# ===> second method <=====
# duplicate =[]
# for i in array:
#     if i not in duplicate:
#         duplicate.append(i)
# print(duplicate)

# Do some extra for success that is mendotory


