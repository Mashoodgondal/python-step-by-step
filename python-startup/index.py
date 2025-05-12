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
# numbers = [10, 20, 30, 40, 50]
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
# ===========remove arrording ot condition=========
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

# ============Find dogs years using human years============

# dog_years = 7.18
# age =  int(input("Enter an age in calendar years: "))
# total = age * dog_years
# print("That's"+ str(total) +"in dog years!")

# ========Print random number in dice===========
import random
sides = int(input("How many sides does your dice have? "))
roll = random.randint(1, sides)
print("Your roll is ", roll)