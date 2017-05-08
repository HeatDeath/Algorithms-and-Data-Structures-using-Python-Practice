from timeit import Timer

popzero = Timer("x.pop(0)",
                       "from __main__ import x")
popend = Timer("x.pop()",
                      "from __main__ import x")

x = list(range(2000000))
print('从列表头部pop元素：',popzero.timeit(number=1000))


x = list(range(2000000))
print('从列表尾部pop元素：',popend.timeit(number=1000))
