class HashTable:
    def __init__(self):
        # HashTable 的初始大小已经被选择为 11,大小是质数，使得冲突解决算法尽可能的高效
        self.size = 11
        # slots[] 储存key
        self.slots = [None]*self.size
        # data[] 储存value
        self.data = [None]*self.size

    # put 函数,用于给 key-value 找到合适的位置，并将其插入进去
    def put(self, key, data):
        hashvalue = self.hashfunction(key, len(self.slots))

        # 当 hashvalue 对应的槽为空时，将 key 和 data 分别插入 slots[] 和 data[] 中
        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] =data

        else:
            # 如果非空槽已经包含了 key ，则将以前的 data 替换为新的 data
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data


            else:
                # 使用 rehash() 函数重新计算 hashvalue(nextslot)，即下一个空槽的位置
                nextslot = self.rehash(hashvalue, len(self.slots))

                # 在找到空槽或包含 key 的非空槽之前，迭代 rehash() 函数
                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot, len(self.slots))

                # 找到空槽，插入 key 和 data
                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data

                # 找到包含 key 的非空槽，更新data
                else:
                    self.data[nextslot] = data

    # hashfunction 函数，用于首次计算 hashvalue
    def hashfunction(self, key, size):
        return key % size

    # rehash 函数，用于解决冲突，在发生冲突时再次计算新 hashvalue
    def rehash(self, oldhash, size):
        return (oldhash + 1) % size

    # get函数，用于通过 key 来查找对应的 value
    def get(self, key):

        #使用 hashfunction() 根据 key 来计算查找的起始槽(startslot)
        startslot = self.hashfunction(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot


        while self.slots[position] != None and not found and not stop:

            # 当前槽中的 key 为想要查找的 key 时
            if self.slots[position] == key:
                found = True
                data = self.data[position]

            else:
                position = self.rehash(position, len(self.slots))
                # 当返回起始槽 startsplot 时，终止
                if position == startslot:
                    stop = True

        return data

    # 重载 __getitem__() 和 __stiitem__() 方法，以允许使用[]访问
    # 这意味着一旦创建了 HashTable，索引操作符将可用
    def __getitem__(self, key):
        return  self.get(key)

    def __setitem__(self, key, data):
        return self.put(key, data)

H = HashTable()
H[54] = "cat"
H[26] = "dog"
H[93] = "lion"
H[17] = "tiger"
H[77] = "bird"
H[31] = "cow"
H[44] = "goat"
H[55] = "pig"
H[20] = "chicken"
print(H.slots)
print(H.data)

