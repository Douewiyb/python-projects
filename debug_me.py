# Debugging practice: this program has ONE bug.
# average([4, 8, 6]) should be 6.0, but it prints something else.
# Use the VS Code debugger to find out why. Don't just stare at it!

def average(numbers):
    total = 0
    for i in range(len(numbers)):
        total = total + numbers[i]
    return total / len(numbers)

print(average([4, 8, 6]))

# Solved the bug