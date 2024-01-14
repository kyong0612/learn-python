class SomeClass:
    def __eq__(self, __value: object) -> bool:
        if __value is None:
            return True


spam = SomeClass()
print(spam == None)
print(spam is None)
