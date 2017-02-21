print("请输入需要解密的密文：")
string=input("")
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
