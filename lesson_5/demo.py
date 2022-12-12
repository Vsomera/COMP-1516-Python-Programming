fruits = ["apples", "banana", "cherry", "peach"] # tuples

print(type(fruits))
print(fruits[1])
fruits = list(fruits)
print(fruits)
fruits = tuple(fruits)
print(fruits)
print(fruits[2:20])

i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1

for fruit in fruits:
    print(fruit)

fruits = ["apple", "banana", "peach", "grape"]
print(fruits[2])
print(fruits[2:20])

fruits.append("orange", "mandarin")
print(fruits)
