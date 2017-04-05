def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist) - 1
    while passnum > 0 and exchanges:
        exchanges = False

        for i in range(passnum):

            #当alist的剩余项不是相对有序(前一项小于下一项)的时候
            if alist[i] > alist[i+1]:

                #此时需要交换
                exchanges = True

                alist[i], alist[i+1] = alist[i+1], alist[i]

        passnum = passnum - 1

alist = [20, 30, 40, 90, 50, 60, 70, 80, 100, 110]
shortBubbleSort(alist)
print(alist)

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
shortBubbleSort(alist)
print(alist)
