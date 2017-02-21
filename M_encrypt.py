#M_encrypt, it's my first personal encrypt program .
print("请输入需要加密的明文：")
string=input("")
a=[]
b=[]
c=[]
for i in range(0,len(string)):
    a.append(string[len(string)-i-1])
print("字符反转后的结果为：")
for i in range(0,len(string)):
    print(a[i],end='')
print()
for i in range(0,len(string)):
    if(i==0):
        b.append(a[len(string)-1])
    else:
        b.append(a[i-1])
print("字符移位后的结果为：")
for i in range(0,len(string)):
    print(b[i],end='')
print()
if(len(string)%2==0):
    for i in range(0,len(string)):
        if(i%2==0):
            c.append(b[i+1])
        else:
            c.append(b[i-1])
else:
    for i in range(0,len(string)-1):
        if(i%2==0):
            c.append(b[i+1])
        else:
            c.append(b[i-1])
    c.append(b[len(string)-1])
print("奇偶互换后的结果为：")
for i in range(0,len(string)):
    print(c[i],end='')
print()
