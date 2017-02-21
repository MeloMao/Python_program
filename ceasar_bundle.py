print("请输入需要处理的字符串：")
string=input("")
print("输入1进行凯撒加密，输入2进行凯撒解密：")
y=input()
x=int(y)
if(x==1):
    a=[]
    b=[]
    for i in range(0,len(string)):
        if(ord(string[i])>119):
            a.append(ord(string[i])-23)
        else:
            a.append(ord(string[i])+3)
    for i in range(0,len(string)):
        b.append(chr(a[i]))
    print("凯撒加密结果为：")
    for i in range(0,len(string)):
        print((b[i]),end='')
    print()
else:
    a=[]
    b=[]
    for i in range(0,len(string)):
        if(ord(string[i])<100):
            a.append(ord(string[i])+23)
        else:
            a.append(ord(string[i])-3)
    for i in range(0,len(string)):
        b.append(chr(a[i]))
    print("凯撒解密结果为：")
    for i in range(0,len(string)):
        print((b[i]),end='')
    print()
