#coding=UTF-8
#明文长度4密钥长度8密钥轮数14

#s盒
sbox=[0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16]
#十六进制输出方式：print("%x"%(sbox[0][1]))

#逆s盒
inv_sbox=[0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB,0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB,0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E,0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25,0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92,0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06,0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B,0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73,0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E,0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B,0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4,0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F,0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF,0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61,0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D]

#列混合的常数矩阵
mix=[0x02,0x03,0x01,0x01],[0x01,0x02,0x03,0x01],[0x01,0x01,0x02,0x03],[0x03,0x01,0x01,0x02]

#列混合的常数矩阵
inv_mix=[0x0e,0x0b,0x0d,0x09],[0x09,0x0e,0x0b,0x0d],[0x0d,0x09,0x0e,0x0b],[0x0b,0x0d,0x09,0x0e]

#初始化Rcon轮常数二维数组
rcon=[0x01,0x02,0x04,0x08,0x10,0x20,0x40,0x80,0x1b,0x36]

#行移位
def shiftrows(a):
    for i in range(1,4):
        if(i==1):
            j=a[i][0];
            a[i][0]=a[i][1];
            a[i][1]=a[i][2];
            a[i][2]=a[i][3];
            a[i][3]=j;
        if(i==2):
            j=a[i][0];
            b=a[i][1];
            a[i][0]=a[i][2];
            a[i][1]=a[i][3];
            a[i][2]=j;
            a[i][3]=b;
        if(i==3):
            j= a[i][3];
            a[i][3]=a[i][2];
            a[i][2]=a[i][1];
            a[i][1]=a[i][0];
            a[i][0]=j;
    return a

#逆行移位
def inv_shiftrows(a):
    for i in range(1,4):
        if(i==1):
            j=a[i][3];
            a[i][3]=a[i][2];
            a[i][2]=a[i][1];
            a[i][1]=a[i][0];
            a[i][0]=j;
        if(i==2):
            j=a[i][0];
            b=a[i][1];
            a[i][0]=a[i][2];
            a[i][1]=a[i][3];
            a[i][2]=j;
            a[i][3]=b;
        if(i==3):
            j=a[i][0];
            a[i][0]=a[i][1];
            a[i][1]=a[i][2];
            a[i][2]=a[i][3];
            a[i][3]=j;
    return a

#列混合
def mixcolumns(a,mix):
    temp=[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]
    d=[0x80,0x1B,0x02]
    for m in range(0,4):
        for i in range(0,4):
            for j in range(0,4):
                if(mix[i][j]==1):
                    temp[i][m]=a[j][m]^temp[i][m]
                elif(mix[i][j]==2):
                    if(a[j][m]<d[0]):
                        temp[i][m]=(mix[i][j]*a[j][m])^temp[i][m]
                    else:
                        k=a[j][m]^d[0]
                        temp[i][m]=((mix[i][j]*k)^d[1])^temp[i][m]
                else:
                    if(a[j][m]<d[0]):
                        temp[i][m]=((a[j][m]*d[2])^a[j][m])^temp[i][m]
                    else:
                        k=a[j][m]^d[0]
                        temp[i][m]=(((k*d[2])^d[1])^a[j][m])^temp[i][m]
    for i in range(0,4):
        for j in range(0,4):
            a[i][j]=temp[i][j]
    return a

#逆列混合
def inv_mixcolumns(a,inv_mix):
    temp=[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]
    d=[0x80,0x1B,0x02,0x0e,0x0b,0x0d,0x09]
    for m in range(0,4):
        for i in range(0,4):
            for j in range(0,4):
                e=a[j][m]
                y=a[j][m]
                if(inv_mix[i][j]==d[3]):
                    for n in range(0,3):
                        if(y<d[0]):
                            y=y*d[2]
                        else:
                            k=y^d[0]
                            y=(k*d[2])^d[1]
                        if(n==0):
                            p=y
                        elif(n==1):
                            q=y
                        else:
                            x=y
                    temp[i][m]=p^q^x^temp[i][m]
                if(inv_mix[i][j]==d[4]):
                    for n in range(0,3):
                        if(y<d[0]):
                            y=y*d[2]
                        else:
                            k=y^d[0]
                            y=(k*d[2])^d[1]
                        if(n==0):
                            q=y
                        if(n==2):
                            x=y
                    temp[i][m]=e^q^x^temp[i][m]
                if(inv_mix[i][j]==d[5]):
                    for n in range(0,3):
                        if(y<d[0]):
                            y=y*d[2]
                        else:
                            k=y^d[0]
                            y=(k*d[2])^d[1]
                        if(n==1):
                            q=y
                        if(n==2):
                            x=y
                    temp[i][m]=e^q^x^temp[i][m]
                if(inv_mix[i][j]==d[6]):
                    for n in range(0,3):
                        if(y<d[0]):
                            y=y*d[2]
                        else:
                            k=y^d[0]
                            y=(k*d[2])^d[1]
                    temp[i][m]=e^y^temp[i][m]
    for i in range(0,4):
        for j in range(0,4):
            a[i][j]=temp[i][j]
    return a

#字节替代
def subbytes(a,sbox):
    for i in range(0,4):
        for j in range(0,4):
            a[i][j]=sbox[a[i][j]]
    return a

#逆字节替代
def inv_subbytes(a,inv_sbox):
    for i in range(0,4):
        for j in range(0,4):
            a[i][j]=inv_sbox[a[i][j]]
    return a

#密钥扩展
def keyexpansion(a,key):
    w=[0,0,0,0]
    r=[0,0,0,0]
    q=[0,0,0,0]
    for i in range(0,4):
        for j in range(0,4):
            temp[i][j]=roundkey[i][j]
    for i in range(4,68):
        a=i-4
        b=i-1
        if(i%4!=0):#i不是4的倍数
            for j in range(0,4):
                q[j]=temp[j][a]^temp[j][b]
            for y in range(0,4):
                temp[y][i]=q[y]
        else:
            for x in range(0,4):
                w[x]=temp[x][b]
            n=w[0]#左移一位
            w[0]= w[1]
            w[1]= w[2]
            w[2]= w[3]
            w[3]=n
            for j in range(0,4):
                w[j]=sbox[w[j]]#字节替代
           # w[0]= rcon[(i-4)/4]^w[0]
            for m in range(0,4):
                r[m]=temp[m][a]^w[m]
            for y in range(0,4):
                temp[y][i]=r[y]
    return temp

#获取轮密钥
def getroundkey(temp,n):
    for i in range(0,4):
        for j in range(0,4):
            roundKey[i][j]=temp[i][j+4*n];
    return roundkey

#轮密钥操作
def addroundkey(a,key):
    roundkey=[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]
    rcon=[0x01,0x02,0x04,0x08,0x10,0x20,0x40,0x80,0x1b,0x36]#Rcon轮常数二维数组
    for i in range(0,4):
        for j in range(0,4):
            roundkey[i][j]=rcon[i+j]+key[i][j]
    for i in range(0,4):
        for j in range(0,4):
            a[i][j]=a[i][j]^roundkey[i][j]
    return a,key
#加密函数
def encrypt(a,key):
    addroundkey(a,key)#轮密钥加
    for n in range(1,15):
        if(n==14):
            subbytes(a,sbox)#字节替代
            shiftrows(a)#行移位
            addroundkey(a,key)#轮密钥加
        else:
            subbytes(a,sbox)#字节替代
            print('第',n,'轮字节替代结果为：')
            for i in range(0,4):
                print('[',end=' ')
                for j in range(0,4):
                        print('%02x'%(a[i][j]),end=' ')
                print(']',end='')
            print()
            shiftrows(a)#行移位
            print('第',n,'轮行移位结果为：')
            for i in range(0,4):
                print('[',end=' ')
                for j in range(0,4):
                        print('%02x'%(a[i][j]),end=' ')
                print(']',end='')
            print()
            mixcolumns(a,mix)#列混合
            print('第',n,'轮列混合结果为：')
            for i in range(0,4):
                print('[',end=' ')
                for j in range(0,4):
                        print('%02x'%(a[i][j]),end=' ')
                print(']',end='')
            print()
            addroundkey(a,key)#轮密钥加
            print('第',n,'轮轮密钥加结果为：')
            for i in range(0,4):
                print('[',end=' ')
                for j in range(0,4):
                        print('%02x'%(a[i][j]),end=' ')
                print(']',end='')
            print()
    return a,key

#解密函数
def decrypt(a,key):
    r=[0,13,12,11,10,9,8,7,6,5,4,3,2,1]
    m=14
    addroundkey(a,key)#轮密钥加
    for n in range(1,15):
        if(n==14):
            inv_shiftrows(a)#逆行移位
            inv_subbytes(a,inv_sbox)#逆字节替代
            m=0
            addroundkey(a,key)#轮密钥加
        else:
            inv_shiftrows(a)#逆行移位
            print('第',n,'轮逆行移位结果为：')
            for i in range(0,4):
                print('[',end=' ')
                for j in range(0,4):
                        print('%02x'%(a[i][j]),end=' ')
                print(']',end='')
            print()
            inv_subbytes(a,inv_sbox);#逆字节替代
            print('第',n,'轮逆字节替代结果为：')
            for i in range(0,4):
                print('[',end=' ')
                for j in range(0,4):
                        print('%02x'%(a[i][j]),end=' ')
                print(']',end='')
            print()
            m=r[n]
            addroundkey(a,key);#轮密钥加
            print('第',n,'轮轮密钥加结果为：')
            for i in range(0,4):
                print('[',end=' ')
                for j in range(0,4):
                        print('%02x'%(a[i][j]),end=' ')
                print(']',end='')
            print()
            inv_mixcolumns(a,inv_mix);#逆列混合
            print('第',n,'轮逆列混合结果为：')
            for i in range(0,4):
                print('[',end=' ')
                for j in range(0,4):
                        print('%02x'%(a[i][j]),end=' ')
                print(']',end='')
            print()
    return a,key

#主函数
print("请输入明文：（16位字符）")#明文处理开始
#string=input("")
string='2222222222222222'
a = []
tmp = []
for i in range(len(string)):#字符串转为数组
	if i % 4 == 0 and i is not 0:
		a.append(tmp)
		tmp = []
	tmp.append(string[i])

a.append(tmp)
print('')
for i in range(0,4):#字符转为ASCII码
    for j in range(0,4):
        a[i][j]=ord(a[i][j])
print('\n\n产生的明文数组为：')
for i in range(0,4):#10进制转为16进制 
    print('[',end=' ')
    for j in range(0,4):
        print('%02x'%(a[i][j]),end=' ')
    print(']',end='')
print()

print("请输入密钥：（32位字符）")#密钥处理开始
#k=input("")
k='qwertyuiopasdfghjklzxcvbnm123456'
key = []
tmp2 = []
for i in range(0,len(k),2):#字符串转为数组
	if i % 8 == 0 and i is not 0:
		key.append(tmp2)
		tmp2 = []
	tmp2.append(k[i])

key.append(tmp2)
print('')
for i in range(0,4):#字符转为ASCII码
    for j in range(0,4):
        key[i][j]=ord(key[i][j])
print('\n\n产生的密钥数组为：')
for i in range(0,4):#10进制转为16进制 
    print('[',end=' ')
    for j in range(0,4):
        print('%02x'%(key[i][j]),end=' ')
    print(']',end='')
print()
print('\n\n请输入任意值进行加密')
test=input()

temp=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
w=[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]
#keyexpansion(key,sbox,temp)
encrypt(a,key)
print('\n\n最终加密结果：')
for i in range(0,4):
    print('[',end=' ')
    for j in range(0,4):
        print('%02x'%(a[i][j]),end=' ')
    print(']',end='')
print()
print('\n\n输入任意值进行解密：')
test=input()
decrypt(a,key)
print('\n\n最终解密数组为：')
for i in range(0,4):
    print('[',end=' ')
    for j in range(0,4):
        print('%02x'%(a[i][j]),end=' ')
    print(']',end='')
print()
print('\n\n最终解密结果为：')
for i in range(0,4):
    for j in range(0,4):
        a[i][j]=chr(a[i][j])
for i in range(0,4):
    for j in range(0,4):
        print(a[i][j],end='')
print()
