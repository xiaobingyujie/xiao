#使用random模块，如何产生 50~150之间的数？
'''
import random
n=random.randint(50.150)
'''
#从键盘输入任意三边，判断是否能形成三角形，若可以，则判断形成什么三角形
'''
a=float(input("请输入第一个边的值"))
b=float(input("请输入第二个边的值"))
c=float(input("请输入第三个边的值"))
if a+b>c and b+c>a and a+c>b:
    if a==b==c:
        print("这是等边三角形")
    elif a==b and b==c:
        print("这是等腰三角形")
    else:
        print("这是普通三角形")
else:
    print("这不是三角形")
'''

#有以下两个数，使用+，-号实现两个数的调换。
'''
A=input("A=")
B=input("B=")
A=int(A)
B=int(B)
A=A+B
B=A-B
A=A-B
print("A","=",A)
print("B","=",B)
'''
#实现登陆系统的三次密码输入错误锁定功能
'''
username="xiao"
userpassword="1111"
count=0
name = input("登录用户名：")
if name == username:
    # 如果密码连续输错了三次，锁定账号
    while count < 3:
        password = input("登录密码：")
        if name == username and password == userpassword:
            print("欢迎%s!" % name)
            break
        else:
            print("账号和密码不匹配")
            count += 1
    else:
        print("对不起，您的账号连续输错三次密码已被锁定，请联系管理员。")
        f = open("aaa.txt")
        f.close()
else:
    print("用户名不存在，请输入正确的用户名。")
'''
#编程实现下列图形的打印
i=1
while i<=7:
    j = 1
    while j <= 7-i:
        print('  ', end='')
        j=j+1
    k = 1
    while k <= i:
        print('  * ',end='')
        k=k+1
    print()
    i=i+1

# for i in range(0,7):
#     print("  " * (7 - i), end="")
#     print(" *  " * (i + 1))

#编程实现99乘法表的倒叙打印
'''
i=9
while i>=1:
    j=1
    while j<=i:
        print(i,"*",j,"=",j*i,"   ",end="")
        j=j+1
    print()
    i=i-1
'''
#一只青蛙掉在井里了，井高20米，青蛙白天网上爬3米，晚上下滑2米，问第几天能出来？请编程求出。
hight=20
h=0
day=0
while True:
    day=day+1
    h=h+3
    if h>=hight:
       break
    else:
        h=h-2
print("共需要",day,"天")