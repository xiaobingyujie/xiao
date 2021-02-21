'''
class Watercup:
    __height=0
    __vt=0
    __color=""
    __tom=""
    def setHeight(self,height):
        if height<0:
            print("输入非法！")
        else:
            self.__height=height
    def getHeight(self):
        return self.__height

    def setVt(self,vt):
        if vt<0:
            print("输入非法！")
        else:
            self.__vt=vt
    def getVt(self):
        return self.__vt

    def setColor(self,color):
        self.__color=color
    def getColor(self):
        return self.__color

    def setTom(self,tom):
        self.__tom=tom
    def getTom(self):
        return self.__tom

    def deposit(self,many):
        if many>self.__vt:
            print("输入非法！")
        else:
            print("这个水杯能存放",many,"毫升液体")
w=Watercup()
w.setHeight(10)
w.setVt(200)
w.setColor("透明")
w.setTom("玻璃")
w.deposit(100)
print("这个杯子，高度为",w.getHeight(),"容积为",w.getVt(),"的",w.getColor(),w.getTom(),"水杯")
'''
class Computer:
    __size=""
    __money=""
    __cpu=""
    __meory=""
    __time=""
    def setSize(self,size):
        self.__size=size
    def getSize(self):
        return self.__size

    def setMoney(self,money):
        self.__money=money
    def getMoney(self):
        return self.__money

    def setCpu(self,cpu):
        self.__cpu=cpu
    def getCpu(self):
        return self.__cpu

    def setMeroy(self,meroy):
        self.__meory=meroy
    def getMeroy(self):
        return self.__meory

    def setTime(self,time):
        self.__time=time
    def getTime(self):
        return self.__time

    def dazi(self):
        print("笔记本电脑正在打字！")
    def playGame(self,game):
        print("正在打"+game+"游戏。")
    def watch(self):
        print("正在看视频。")
c=Computer()
c.setSize("14寸")
c.setMoney("5000$")
c.setCpu("888")
c.setMeroy("568G")
c.setTime("14h")
c.playGame("植物大战僵尸")
print("这个电脑，内存有"+c.getSize()+"，cup是"+c.getCpu()+"，内存"+c.getMeroy()+"，待机时长"+c.getTime()+"，价格为"+c.getMoney())