def anagramSolution1(s1,s2):
    #将字符串s2转换为一个list
    alist = list(s2)

    #初始化s1的指针pos1=0
    pos1 = 0

    #是否在s2字符串中找到s1字符串中的【所有字符】的标记stillOK
    stillOK = True

    #当指针pos1还未移动到s1结尾，且在遍历s2时能找到s1中的字符
    while pos1 < len(s1) and stillOK:
        #初始化s2的指针pos2=0
        pos2 = 0
        #是否在s2字符串中找到s1字符串中的【单个字符】的标记found
        found = False
        while pos2 < len(alist) and not found:
            #如果在遍历s2字符串的时候找到了s1中的字符，则found=true
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 = pos2 + 1

        #如果找到，将在s2中找到且存在于s1中的字符时，将s2中的字符变为None
        if found:
            alist[pos2] = None
        #如果没找到，stillOK=false
        else:
            stillOK = False

        #s1中的位置指针pos1移动到下一个位置
        pos1 = pos1 + 1

    return stillOK

print(anagramSolution1('abcd','acfdffffb'))