

print("Welcome to our Cafè")

menu = ["Espresso", "Cappuccino", "Latte", "Americano"] # list
prices = (3.0, 4.5, 5.0, 3.5) # tuple
availableSizes = {"Small", "Medium", "Large"} # set

orders = [] # list
orderInfo = {} # dictionary

print("\n today's menu:")
for i, item in enumerate(menu):
    print(f"{i+1}. {item} -$ {prices[i]}")

choice = int(input("Please select an option(1-4): "))

if 1 <= choice <= len(menu):
    coffee = menu[choice -1]
else:
    print("Invalid option")
    exit()

# choose a valid size
size = input(f"Please select a size of {coffee}) {', '.join(availableSizes)}: ")
if size not in availableSizes:
    print("Invalid size")
    exit()

# add something
addMilk = input(f"would you like to add milk? (Y/N): ").lower()
addSuger = input(f"would you like to add suger? (Y/N): ").lower()

# invoice
price = prices[choice-1]
if addMilk == "y":
    price += 0.5
if addSuger == "y":
    price += 0.2

orderInfo = {
    "coffee": coffee,
    "size": size,
    "Add Milk": addMilk,
    "Add Suger": addSuger,
    "Price": price
}

orders.append(orderInfo)
print("\nYour order:")
for key, value in orderInfo.items():
    print(f"{key.capitalize()}: {value}")

print(f"\nTotal Price: {price:.2f}")
print("Thanks you! You will be noticed, when your coffee is ready..")

