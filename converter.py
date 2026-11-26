# Celsius to Fahrenheit converter test (no input)

# The conversion function
def c_to_f(celsius):
    fahrenheit=celsius*9/5+32
    return fahrenheit

# Test values
print(c_to_f(100))
print(c_to_f(0))
print(c_to_f(-40))
print(c_to_f(-10))

# Test table for celsius converter
# Input / Expected / Output / Pass
#  100  / 212.0    / 212.0  / Yes
#  0    / 32.0     / 32.0   / Yes
# -40   / -40.0    / -40.0  / Yes
# -10   / 14.0     / 14.0   / Yes