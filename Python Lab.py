# Welcome to the Python Lab!

# In this lab, you'll practice working with for loops, arrays (lists in Python), 
# and common array operations like appending, removing, and traversing elements.

# Let's get started!

# Part 1: For Loops

# 1.1: Print numbers from 1 to 10 using a for loop.
# Hint: Use the `range()` function.

for i in range(1, 11):
  # Your code here: Print the value of 'i', replace `pass` with your code
  print(i)

# Part 2: Arrays (Lists in Python)

# 2.1: Create an array named 'colors' with the following elements: 
# "red", "green", "blue".

colors = ["red", "green", "blue"] # Your code here: Initialize the array with the given colors


# 2.2: Print the first element of the 'colors' array.

# Your code here
print(colors[0])

# Part 3: Appending Array Elements

# 3.1: Add the color "yellow" to the end of the 'colors' array.

# Your code here
colors.append("yellow")

# 3.2: Print the 'colors' array to see the updated list.

# Your code here
print(colors)

# Part 4: Removing Array Elements

# 4.1: Remove the color "green" from the 'colors' array.
# Hint: Use the `remove()` method.

# Your code here
colors.remove("green")


# 4.2: Print the 'colors' array to see the updated list.

# Your code here
print(colors)


# Part 5: Traversing Arrays

# 5.1: Use a for loop to print each color in the 'colors' array.

for color in colors:
  # Your code here: Print the value of 'color', replace `pass` with your code
  print(color)


# Part 6: Bonus Challenges

# 6.1: Write a Python program to find the sum of all numbers in an array.
# Hint: Create a new array with numbers and use a loop to calculate the sum.

numbers = [1, 2, 3, 4, 5] 
sum = 0

# Your code here: Calculate the sum of 'numbers' array using a for loop
for number in numbers:
  sum += number

print("The sum of all numbers in the array is:", sum)


# 6.2: Write a Python program to find the largest and smallest elements in an array.
# Hint: You can use sorting or iterate through the array to find the min and max.

numbers = [5, 2, 9, 1, 7]
largest = numbers[0]  # Initialize with the first element
smallest = numbers[0] # Initialize with the first element

# Your code here: Find the largest and smallest in 'numbers' array

for number in numbers:
  if number > largest:
    # Your code here: Update the 'largest', replace `pass` with your code
    largest = number

  if number < smallest:
    # Your code here: Update the 'smallest', replace `pass` with your code
    smallest = number


print("Largest element:", largest)
print("Smallest element:", smallest)


# Great job completing the lab! 
# You've practiced essential Python concepts like for loops, arrays, and array manipulation.
# Keep experimenting and exploring to deepen your understanding.