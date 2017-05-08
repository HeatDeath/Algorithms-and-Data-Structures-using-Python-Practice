class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

def baseConverter(decNumber,base):
    remstack = Stack()
    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base

    binString =""

    digits = '0123456789ABCDEF'

    while not remstack.isEmpty():
        binString = binString + digits[remstack.pop()]

    return binString

print(baseConverter(42,16))

print(baseConverter(47,8))