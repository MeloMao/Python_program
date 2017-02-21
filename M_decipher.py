print("请输入需要解密的密文：")
string=input("")
a=[]
b=[]
c=[]
if(len(string)%2==0):
    for i in range(0,len(string)):
        if(i%2==0):
            a.append(string[i+1])
        else:
            a.append(string[i-1])
else:
    for i in range(0,len(string)-1):
        if(i%2==0):
            a.append(string[i+1])
        else:
            a.append(string[i-1])
    a.append(string[len(string)-1])
print("奇偶互换后的结果为：")
for i in range(0,len(string)):
    print(a[i],end='')
print()
for i in range(0,len(string)):
    if(i==len(string)-1):
        b.append(a[0])
    else:
        b.append(a[i+1])
print("逆字符移位后的结果为：")
for i in range(0,len(string)):
    print(b[i],end='')
print()
for i in range(0,len(string)):
    c.append(b[len(string)-i-1])
print("字符反转后的结果为：")
for i in range(0,len(string)):
    print(c[i],end='')
print()
