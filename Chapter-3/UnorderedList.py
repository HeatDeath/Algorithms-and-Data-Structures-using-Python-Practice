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

class UnorderList:
    def __init__(self):
        self.head = None

    #isEmpty() 检查列表是否为空。它不需要参数，并返回布尔值。
    def isEmpty(self):
        return self.head == None

    #add(item) 向列表中添加一个新项。它需要 item 作为参数，并不返回任何内容。假定该 item 不在列表中。
    def add(self, item):
        #链表的每项必须驻留在节点对象中
        temp = Node(item)

        #更改新节点的下一个引用以引用旧链表的第一个节点
        temp.setNext(self.head)

        #修改链表的头以引用新节点
        self.head = temp

    #size（）返回列表中的项数。它不需要参数，并返回一个整数。
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            cunrrent = current.getNext()

        return count

    #search(item) 搜索列表中的项目。它需要 item 作为参数，并返回一个布尔值。
    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    #remove(item) 从列表中删除该项。它需要 item 作为参数并修改列表。假设项存在于列表中。
    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True

            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()

        else:
            previous.setNext(current.getNext())

    #append(item) 将一个新项添加到列表的末尾，使其成为集合中的最后一项。
    #它需要 item 作为参数，并不返回任何内容。假定该项不在列表中
    def append(self, item):
        current = self.head
        while current.getNext() != None:
            current = current.getNext()

        temp = Node(item)
        current.setNext(temp)

    #index(item) 返回项在列表中的位置。它需要 item 作为参数并返回索引。假定该项在列表中。
    def index(self, item):
        current = self.head
        count = 0
        found = False

        while current != None and not found:
            count = count + 1
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        if found:
            return count
        else:
            return "Not found!"

    #insert(pos，item) 在位置 pos 处向列表中添加一个新项。
    #它需要 item 作为参数并不返回任何内容。假设该项不在列表中，并且有足够的现有项使其有 pos 的位置。
    def insert(self, pos, item):
        if pos > self.size() or pos < 0:
            return "Out of index!"
        current = self.head
        count = 0
        previous = None

        temp = Node(item)

        while current != None and count != pos:
            count = count + 1
            previous = current
            current = current.getNext()

        ##处理头结点为最后一个节点的情况
        if previous == None:
            self.head = temp
            temp.setNext(current)

        #处理一般情况
        else:
            previous.setNext(temp)
            temp.setNext(current)

    #pop() 删除并返回列表中的最后一个项。假设该列表至少有一个项。
    def pop_last(self):
        current = self.head
        previous = None

        #遍历到游标current指向UnorderList的尾节点
        while current != None:
            current = current.getNext()

        #处理头结点为尾节点的情况
        if previous == None:
            self.head = None

        #处理普遍情况
        else:
            previous.setNext(None)

        return current.getData()

    #pop(pos) 删除并返回位置 pos 处的项。它需要 pos 作为参数并返回项。假定该项在列表中。
    def pop_pos(self, pos):
        if pos > self.size() or pos < 0:
            return "Out of index!"

        current = self.head
        count = 0
        previous = None

        #遍历节点，直到将current游标移动到pos位置为止
        while current != None and count != pos:
            count = count + 1
            previous = current
            current = current.getNext()

        #处理头结点为尾节点的情况
        if previous == None:
            self.head = None

        #处理普遍情况
        else:
            previous.setNext(current.getNext())

        return current.getData()
