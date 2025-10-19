# list, tuple, set, dictionary, and their most used methods

# create list
fruit = ["apple", "banana", "cherry", "orange"]
number = [1, 2, 3, 4, 5, 6, 7, 8]
mixed = [1, 'hello', 3.14, True]

print(fruit)
print("*************************")

fruit.append("watermelon")
print(fruit)
print("*************************")

fruit.insert(0, "grape")
print(fruit)
print("*************************")
fruit.remove("watermelon")
print(fruit)
print("*************************")

last = fruit.pop() # it removes the last item
print(last)
print(fruit)
print("*************************")

# create tuple
coordinates = (10,20)
colors = ("red", "white", "blue")
singleTuple = (5,)

numbers = (1, 2, 3, 2, 4, 2)

count = numbers.count(2)
print(count)
print(numbers)
print("*************************")

index = numbers.index(3)
print(index)
print("*************************")

length = len(numbers)
print(length)
print("*************************")

# create set
uniqueNumbers = {}

fruitsSet = {"apple","banana","cherry",}
print(fruitsSet)
print("*************************")

emptySet = set()

numbersSet = {1, 2, 3, 4, 3, 2, 1}
print(numbersSet)
print("*************************")

a = {1, 2, 3, 4, 5}
b = {5, 6, 7, 8, 9}


# union = a.union(b)
union = a | b
print(union)
print("*************************")

# intersection = a.intersection(b)
intersection = a & b
print(intersection)
print("*************************")

# difference = a.difference(b)
difference = a - b
print(difference)
print("*************************")

# dictionary NOTE: the most important thing is the value key can be anything.
person = {
    'name': "Ehmet",
    'age': 30,
    'city': "Aksu"
}
print(person['name'])
print("*************************")

person['job'] = "QML Engineer"

keys = person.keys()
print(keys)
print("*************************")

items = person.items()
print(items)
print("*************************")

remove = person.pop('age')
print(remove)
print(items)
print("*************************")

# create function/method
def hello(name):
    return f"Hello, {name}!!"

call = hello("Ehmet")
print(call)
print("*************************")

def calculater():
    print("Select an operation: ")
    print("1. add")
    print("2. subtract")
    print("3. multiply")
    print("4. divide")

    choice = input("Enter your choice (1/2/3/4): ")
    if choice not in ("1", "2", "3", "4"):
        print("Invalid choice")
        return

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    if choice == "1":
        print(f"Result: {num1 + num2}")
    elif choice == "2":
        print(f"Result: {num1 - num2}")
    elif choice == "3":
        print(f"Result: {num1 * num2}")
    elif choice == "4":
        print(f"Result: {num1 / num2}")
    else:
        print("Invalid choice")


calculater()