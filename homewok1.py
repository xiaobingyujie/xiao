'''
# 定义一个空调类和对应的测试类
class Ch:
    __money=""
    __brand=""
    def setMoney(self,money):
        self.__money=money
    def getMoney(self):
        return self.__money

    def setBrand(self,brand):
        self.__brand=brand
    def getBrand(self):
        return self.__brand

    def open(self):
        print("空调开机了！")

    def time(self,t):
        t=str(t)
        print("空调在"+t+"分钟后自动关闭。")
c=Ch()
c.setMoney("2000元")
c.setBrand("格力空调")
print(c.getBrand()+":"+c.getMoney())
c.open()
c.time(8)
'''
'''
# 定义一个学生类和对应的测试类
class Student:
    __name=""
    __age=0

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setAge(self, age):
        if age < 0 or age > 120:
            print("年龄输入非法！")
        else:
            self.__age = age
    def getAge(self):
        return self.__age

    def Intorduce(self):
        self.__age=str(self.__age)
        print("大家好，我叫"+self.__name+"，今年"+self.__age+"岁了！")

    def compareAge(self,cage):
        cage=int(cage)
        self.__age=int(self.__age)
        if cage < 0 :
            print("年龄输入非法！")
        else:
            if cage<self.__age:
                a=str(self.__age-cage)

                print("我比我同桌小"+a+"岁！")
            elif cage>self.__age:
                b=str(cage-self.__age)
                print("我比我同桌大"+b+"岁！")
            else:
                print("我和我同桌一样大")

s=Student()
s.setAge(22)
s.setName("肖冰玉洁")
s1=Student()
s1.setName("付光旭")
n=s1.setAge(24)
s.compareAge(24)
s.Intorduce()
'''
'''
# 手机
class Person:
    __name=""
    __sex=""
    __more=0
    __brand=""
    __vt=""
    __size=""
    __time=""
    __score=0

    def setName(self, name):
        self.__name = name
    def getName(self):
        return self.__name

    def setSex(self,sex):
        self.__sex=sex
    def getSex(self):
        return  self.__sex

    def setBrand(self, brand):
        self.__brand = brand
    def getBrand(self):
        return self.__brand

    def setMore(self,more):
        self.__more=more
    def getMore(self):
        return  self.__more

    def setVt(self, vt):
        self.__vt = vt
    def getVt(self):
        return self.__vt

    def setSize(self,size):
        self.__size=size
    def getSize(self):
        return self.__size

    def setTime(self,time):
        self.__time=time
    def getTime(self):
        return self.__time

    def setScore(self,score):
        self.__score=score
    def getTime(self):
        return self.__score

    def faDuanxin(self,duanxin):
        print(duanxin)

    def daDainhua(self,m,t):
        if m==None or self.__more==0:
            print("拨打电话是失败！")
        else:
            if 10>t>0:
                self.__more=self.__more-t*1
                self.__score=self.__score+t*15
                print("话费余额为：",self.__more,"积分为：",self.__score)
            elif 10 >= t >= 20:
                self.__more = self.__more - t * 0.8
                self.__score = self.__score + t * 39
                print("话费余额为：", self.__more, "积分为：", self.__score)
            else:
                self.__more = self.__more - t * 0.65
                self.__score = self.__score + t * 48
                print("话费余额为：", self.__more, "积分为：", self.__score)

p=Person()
p.setMore(121)
p.setScore(99)
p.daDainhua(None,2)
'''
'''
# i.定义了一个学生类：属性:学号，姓名，年龄，性别，身高，体重，成绩，家庭地址，电话号码。行为：
# 学习（要求参数传入学习的时间），玩游戏（要求参数传入游戏名），编程（要求参数传入写代码的行数），数的求和（要求参数用变长参数来做，返回求和结果）
class Student:
    number=""
    name="" 
    age=0
    sex=""
    height=0
    weight=0
    score=0
    id=""
    telephone=""
    def xuexi(self,time):
        print("学习了",time,"个小时")
    def play(self,pname):
        print("玩",pname,"游戏")
    def baincheng(self,n):
        print("写了",n,"行代码")
'''

# ii.车类：属性：车型号，车轮数，车身颜色，车重量，油箱存储大小 。功能：跑（要求参数传入车的具体功能，比如越野，赛车）创建：法拉利，宝马，铃木，五菱，拖拉机对象
class Car:
    __brank=""
    __size=0
    __color=""
    __weigth=0
    __meory=0
    def setBrand(self, brand):
        self.__brand = brand
    def getBrand(self):
        return self.__brand

    def setSize(self,size):
        self.__size=size
    def getSize(self):
        return self.__size

    def setColor(self, color):
        self.__color = color
    def getColor(self):
        return self.__color

    def setWeight(self, weight):
        self.__weight = weight
    def getWeight(self):
        return self.__weight

    def setMeroy(self,meroy):
        self.__meory=meroy
    def getMeroy(self):
        return self.__meory
# 创建：法拉利，宝马，铃木，五菱，拖拉机对象
c1=Car()
c1.setBrand("拖拉机")
c1.setSize(6)
c1.setColor("黄色")
c1.setWeight(2)
c1.setMeroy(200)
print(c1.getBrand(),"车轮数为",c1.getSize(),"，颜色为",c1.getColor(),"，重量为",c1.getWeight(),"，油箱存储大小为",c1.getMeroy())
c2=Car()
c2.setBrand("法拉利")
c2.setSize(6)
c2.setColor("黄色")
c2.setWeight(2)
c2.setMeroy(200)
print(c2.getBrand(),"车轮数为",c2.getSize(),"，颜色为",c2.getColor(),"，重量为",c2.getWeight(),"，油箱存储大小为",c2.getMeroy())
c3=Car()
c3.setBrand("宝马")
c3.setSize(6)
c3.setColor("黄色")
c3.setWeight(2)
c3.setMeroy(200)
print(c3.getBrand(),"车轮数为",c3.getSize(),"，颜色为",c3.getColor(),"，重量为",c3.getWeight(),"，油箱存储大小为",c3.getMeroy())
c4=Car()
c4.setBrand("铃木")
c4.setSize(6)
c4.setColor("黄色")
c4.setWeight(2)
c4.setMeroy(200)
print(c4.getBrand(),"车轮数为",c4.getSize(),"，颜色为",c4.getColor(),"，重量为",c4.getWeight(),"，油箱存储大小为",c4.getMeroy())
c5=Car()
c5.setBrand("五菱")
c5.setSize(6)
c5.setColor("黄色")
c5.setWeight(2)
c5.setMeroy(200)
print(c5.getBrand(),"车轮数为",c5.getSize(),"，颜色为",c5.getColor(),"，重量为",c5.getWeight(),"，油箱存储大小为",c5.getMeroy())
'''
#iii.笔记本：属性：型号，待机时间，颜色，重量，cpu型号，内存大小，硬盘大小。  行为：打游戏（传入游戏的名称）,办公。
class Computer:
    __brank=""
    __time = ""
    __color = ""
    __size=""
    __cpu=""
    __meory=""
    __yingpan=""

    def setBrand(self, brand):
        self.__brand = brand
    def getBrand(self):
        return self.__brand
    
    def setTime(self,time):
        self.__time=time
    def getTime(self):
        return self.__time
    
    def setColor(self, color):
        self.__color = color
    def getColor(self):
        return self.__color
    
    def setSize(self,size):
        self.__size=size
    def getSize(self):
        return self.__size

    def setCpu(self,cpu):
        self.__cpu=cpu
    def getCpu(self):
        return self.__cpu

    def setMeroy(self,meroy):
        self.__meory=meroy
    def getMeroy(self):
        return self.__meory

    def setYingpan(self,pan):
        self.__yingpan=pan
    def getYingpan(self):
        return self.__yingpan

    def work(self):
        print("笔记本电脑正在办公！")

    def playGame(self, game):
        print("正在打" + game + "游戏。")
'''
'''
# iv.猴子类：属性：类别，性别，身体颜色，体重。行为：造火（要求传入造火的材料：比如木棍还是石头），学习事物（要求参数传入学习的具体事物，可以不止学习一种事物）
class Monkey:
    __type=""
    __sex=""
    __color=""
    __weight=0
    def setType(self,type):
        self.__type=type
    def getType(self):
        return  self.__type

    def setSex(self,sex):
        self.__sex=sex
    def getSex(self):
        return  self.__sex

    def setColor(self, color):
        self.__color = color
    def getColor(self):
        return self.__color
    
    def setWeight(self, weight):
        self.__weight = weight
    def getWeight(self):
        return self.__weight
    
    def zaohuo(self,cailiao):
        print("正在用",cailiao,"造火")
        
    def study(self,xx):
        print("正在学习",xx)
'''
