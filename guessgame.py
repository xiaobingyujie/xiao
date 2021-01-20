import random
import time
num = random.randint(1,100)
counter=0
while True:
    if counter>=3:
        print("三次没猜中，系统锁定五秒！")
        f=1
        while f<=5:
            print(".",end="")
            time.sleep(1)
            f=f+1
    counter=counter+1
    print()
    n=input("请输入您猜的数字！")
    n=int(n)
    if n>num:
        print("大了！")
    elif n<num:
        print("小了！")
    else:
        print("恭喜您猜对了！您共用了：",counter,"次！")
        break