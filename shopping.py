# Simple shopping list

# This is me training myself to write from pseudocode to python, read shopping_pseudocode.txt for the pseudocode

# The shopping list (builds as items are added)
shop_list=[]

# Function adds a new item to the shopping list
def add_item():
    new=input("add item: ")
    shop_list.append(new)
    print(f"{new} has been added")

# Function shows whats in the list in order
def show_list():
    for i in range(len(shop_list)):
        print(f"{i+1}. {shop_list[i]}")
    if shop_list==[]:
        print("Nothing in list")

# Function tells user how much items they have in the shopping list
def quantity():
    count=len(shop_list)
    if count==1:
        print(f"{count} item")
    else:
        print(f"{count} items")

# The loop below uses the users input to decide which functions above to use
while True:
    inp=input("1. Add item   2. Show items   3. Count items   4. Quit      ")
    if inp=="1":
        add_item()
    elif inp=="2":
        show_list()
    elif inp=="3":
        quantity()
    elif inp=="4":
        break
    else:
        print("Invalid key")

# When loop breaks below is whats printed
print("Goodbye")

# |       Input                        |        Expected                               |          Output                               | Pass  |
# | ================================== | ============================================= | ============================================= | ===== |
# | 1, then "milk"                     | milk has been added                           | milk has been added                           | Yes   |
# | 2 (after milk)                     | 1. milk                                       | 1. milk                                       | Yes   |
# | 2 on an empty list                 | Nothing in list                               | Nothing in list                               | Yes   |
# | 3                                  | 0 items                                       | 0 items                                       | Yes   |
# | 7                                  | Invalid key                                   | Invalid key                                   | Yes   |
# | 1, then milk then 1 again and eggs | milk has been added       eggs has been added | milk has been added       eggs has been added | Yes   |
# | 1, then milk, then 3               | milk has been added                    1 item | milk has been added                    1 item | Yes   |