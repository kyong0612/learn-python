print("bad")
try:
    fileObj = open("clean-python-programming/ref.md", "r")
    eggs = 42 / 0
    fileObj.close()
except:
    print("An error occurred")


print("good")
with open("clean-python-programming/ref.md", "r") as fileObj:
    print(fileObj.read())
