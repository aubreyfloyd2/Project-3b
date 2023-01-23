# Author: Aubrey Floyd
# GitHub username: aubreyfloyd2
# Date: 1/23/2023
# Description: Asks user to enter a positive integers and then prints a list of all positive
#              integers that divide that number evenly, inlcuding 1 and itself in ascending order.
num_int = int(input("Please enter a positive integer: "))
print("The factors of", num_int, "are:")
for num in range(1, num_int+1):
    if num_int % num ==0:
        print(num)
