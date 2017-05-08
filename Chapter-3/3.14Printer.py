import random

class Printer:
    def __init__(self,ppm):
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaining = 0

    #tick()方法将内部定时器递减直到打印机设置为空闲
    def tick(self):
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    #如果当前有任务，则打印机处于忙碌状态
    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False

    #从任务页数计算所需要的时间
    def startNext(self,newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() * 60 / self.pagerate

class Task:
    def __init__(self,time):
        self.timestamp = time
        self.pages = random.randrange(1,21)

    #此时间戳将表示任务被创建并放置到打印机队列中的时间。
    def getStamp(self):
        return self.timestamp

    #随机数生成器将提供 1 到 20 页的长度
    def getPages(self):
        return self.pages

    #使用 waitTime() 方法来检索在打印开始之前队列中花费的时间。
    def waitTime(self, currenttime):
        return currenttime - self.timestamp

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

#模拟功能允许我们设置打印机的总时间和每分钟的页数
def simulation(numSeconds, pagesPerMinute):

    labprinter = Printer(pagesPerMinute)

    # PrintQueue 对象是我们现有队列 ADT 的一个实例
    printQueue = Queue()

    waitingtimes = []
    for currentSecond in range(numSeconds):

        if newPrintTask():
            task = Task(currentSecond)
            printQueue.enqueue(task)

        if (not labprinter.busy()) and (not printQueue.isEmpty()):
            nexttask = printQueue.dequeue()
            waitingtimes.append(nexttask.waitTime(currentSecond))
            labprinter.startNext(nexttask)

        labprinter.tick()

    averageWait = sum(waitingtimes)/len(waitingtimes)
    print("Average Wait %6.2f secs %3d tasks remaining."%(averageWait,printQueue.size()))

#newPrintTask 决定是否创建一个新的打印任务
def newPrintTask():
    num = random.randrange(1,181)
    if num == 180:
        return True
    else:
        False


#我们将使用每分钟五页的页面速率运行模拟 60 分钟（3,600秒）
#此外，我们将进行 10 次独立试验。
for i in range(10):
    simulation(3600, 5)



