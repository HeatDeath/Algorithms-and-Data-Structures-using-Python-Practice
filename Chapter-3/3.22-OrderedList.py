class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

class OrderdList:
    def __init__(self):
        self.head = None

        # isEmpty() 检查列表是否为空。它不需要参数，并返回布尔值。

    def isEmpty(self):
        return self.head == None

        # add(item) 向列表中添加一个新项。它需要 item 作为参数，并不返回任何内容。假定该 item 不在列表中。

    def add(self, item):
        # 链表的每项必须驻留在节点对象中
        temp = Node(item)

        # 更改新节点的下一个引用以引用旧链表的第一个节点
        temp.setNext(self.head)

        # 修改链表的头以引用新节点
        self.head = temp

        # size（）返回列表中的项数。它不需要参数，并返回一个整数。

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current != None and not  stop:
            if current.getData() == item:
                found = True

            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()

        return found


    def add(self, item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current =current.getNext()

        temp = Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp

        else:
            temp.setNext(current)
            previous.setNext(temp)
