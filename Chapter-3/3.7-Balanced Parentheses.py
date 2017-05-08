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
'''
读取输入的只包含"([{"和")]}"的符号串
    如果是"([{"则入栈
    如果是")]}"则先检查栈是否为空，如果为空，则Not balance，否则pop()栈顶的"([{",
运行辅助匹配函数，如果不匹配，则Not balande。当遍历了符号串中的所有元素后，如果栈为空，
且balance，则符号匹配；否则，不匹配
'''
def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]

        if symbol in "([{":
            s.push(symbol)

        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top,symbol):
                    balanced = False

        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(open,close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)

print(parChecker('{{([][])}()}'))
print(parChecker('[{()]'))
