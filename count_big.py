# Small function that determines wether a list of numbers is bigger then 10

# I am training my psueudocode to actual python skill (read count_big Pseudocode.txt for the pseudocode)

# The function that decides wether a number is bigger then 10 and makes a counter for each number higher then 10
def count_big(numbers):
    counter=0
    for i in range(len(numbers)):
        if numbers[i]>10:
            counter=counter+1
    return counter

# The input values:
print(count_big([4,15,20]))
print(count_big([]))
print(count_big([10,11]))

# Input   / Expected   / Output   / Pass
# 4,15,20 /    2       /    2     / Yes
# Nothing /    0       /    0     / Yes
# 10,11   /    1       /    1     / Yes