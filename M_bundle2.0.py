def strback(a):
    b=[]
    for i in range(0,len(a)):
        b.append(a[len(a)-i-1])
    return b
def strmove(a):
    b=[]
    for i in range(0,len(a)):
        if(i==0):
            b.append(a[len(a)-1])
        else:
            b.append(a[i-1])
    return b
def re_strmove(a):
    b=[]
    for i in range(0,len(a)):
        if(i==len(a)-1):
            b.append(a[0])
        else:
            b.append(a[i+1])
    return b
def strchange(a):
    b=[]
    if(len(a)%2==0):
        for i in range(0,len(a)):
            if(i%2==0):
                b.append(a[i+1])
            else:
                b.append(a[i-1])
    else:
        for i in range(0,len(a)-1):
            if(i%2==0):
                b.append(a[i+1])
            else:
                b.append(a[i-1])
        b.append(a[len(a)-1])
    return b
#main
print("请输入需要处理的字符串：")
a=input("")
print("输入1进行M加密，输入2进行M解密：")
y=input()
x=int(y)
if(x==1):
    for i in range(0,9):
        a=strback(a)
        a=strmove(a)
        a=strchange(a)
    print("M加密结果为:")
    for i in range(0,len(a)):
        print(a[i],end='')
    print()
else:
    for i in range(0,9):
        a=strchange(a)
        a=re_strmove(a)
        a=strback(a)
    print("M解密结果为:")
    for i in range(0,len(a)):
        print(a[i],end='')
    print()
