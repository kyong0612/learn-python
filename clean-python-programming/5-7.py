spam = []
for number in range(100):
    if number % 5 != 0:
        spam.append(number)

print(spam)

# 1 liner
spam = [str(number) for number in range(100) if number % 5 != 0]
print(spam)

# nested for loop
nestedList = [[0, 1, 2, 3], [4], [5, 6], [7, 8, 9]]
flatList = []
for sublist in nestedList:
    for num in sublist:
        flatList.append(num)

print("flatList", flatList)
