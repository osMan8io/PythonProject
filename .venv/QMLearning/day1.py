a = 10
b = 3.5
c = 'Hello'
d = True

print(type(a))
print(type(b))
print(type(c))
print(type(d))


# loop forLoop WhileLoop
fruits = ['apple', 'banana', 'orange']
print(type(fruits))

for fruit in fruits:
    print(fruit)

# range function
print('out 1 to 5: ')

for i in range(1, 6):
    print(i)

# while loop
count = 5
print('result: ')

while count > 0:
    print(count)
    count -= 1

# continue and break
for i in range(1, 6):
    print(i)
    if i == 3:
        print('continue')
        continue
    if i <= 1:
        print('break')
        break

# list can include all data types and can change the data, accepts same value
numbers = [1, 2, 3, 4, 5]
fruits = ['apple', 'banana', 'orange', 2, 3.14, True]
print(numbers)
print(fruits)

# tuple can not change the data, accepts same value
nums = (1, 1, 3, 4, 5,)
print(nums)

# set does not accept same value and the data is not fixed, useful operations like add/remove
cars = {"Ford", "Toyota", "Audi", "Audi"}
years = {1990, 1990, 1992, 1998}
print(cars)
print(years)

cars.add("BMW")
cars.remove("Ford")
print(cars)

set1 = {1, 2, 3, 4,}
set2 = {4, 5, 6, 7,}

# union = set1 | set2
union = set1.union(set2)
print(union)

# intersection = set1 & set2
intersection = set1.intersection(set2)
print(intersection)