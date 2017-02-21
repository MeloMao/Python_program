#my vacation first prgarm
print("请输入需要加密的明文：")
string=input("")
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
