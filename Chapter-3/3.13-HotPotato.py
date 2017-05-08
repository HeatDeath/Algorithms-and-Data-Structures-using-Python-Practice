class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

def hotPotato(namelist,num):
    simqueue = Queue()

    for name in namelist:
        simqueue.enqueue(name)

    #当幸存人数>1时，这个过程持续下去
    while simqueue.size() > 1:

        #模拟报数过程，队首的人即为被裁决之剑指向人
        #约瑟夫环的裁决之剑持续转动，当约瑟夫环的裁决之剑停止转动时，被指向的那个狗带
        for i in range(num):
            #约瑟夫环的裁决之剑转动了一个单位
            simqueue.enqueue(simqueue.dequeue())

        #约瑟夫环中狗带的人
        simqueue.dequeue()

    #约瑟夫环最后幸存的人的名字
    return simqueue.dequeue()

print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))