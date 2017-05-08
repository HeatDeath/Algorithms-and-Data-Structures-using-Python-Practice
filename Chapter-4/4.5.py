def toStr(n,base):
    convertString = "0123456789ABCDEF"

    #我们检查基本情况，其中 n 小于我们要转换的基数。
    #当我们检测到基本情况时，我们停止递归，并简单地从 convertString 序列返回字符串。
    if n < base:
        return convertString[n]

    #我们满足第二和第三定律 - 递归调用和减少除法问题大小。
    else:
        return toStr(n//base, base) + convertString[n%base]

print(toStr(1453, 16))
