animals = ["cat", "dog", "moose"]
# not good
print("not good")
for i in range(len(animals)):
    print(i, animals[i])

print("good")
for i, animal in enumerate(animals):
    print(i, animal)

for animal in animals:
    print(animal)
