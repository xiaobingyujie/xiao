
#厨师类
class Cookers:
    __name=None
    __age=None
    def setName(self,name):
        self.__name=name
    def getName(self):
        return self.__name

    def setAge(self,age):
        self.__age=age
    def getAge(self):
        return self.__age

    def cook(self):
        pass

#定义厨师的子类
class Cooker1(Cookers):#继承父类Cooker
    # 无返回值的无参数的炒菜的方法
    def chao(self):
        pass

# 定义厨师的子类的子类（孙子类）
class Cooker1_1(Cooker1):#继承父类Cooker1
    # 重写所有父类的方法，每个方法的内容只需打印一句话描述方法的功能即可
    def cook(self):
        super().cook()
        print(self.getName(),"正在煮饭")
    def chao(self):
        super().chao()
        print(self.getName(), "正在炒菜")

#初始化Cooker1_1类
c=Cooker1_1()
#使用厨师的孙子类调用setName()和setAge()方法赋值
c.setName("肖冰玉洁")
c.setAge("22")
#使用厨师的孙子类调用getName(),getAge()方法输出值
print(c.getName(),c.getAge())
#使用厨师的孙子类调用chao()和cook()方法
c.chao()
c.cook()

'''
# 人：年龄，性别，姓名。
class Person:
    __name=None
    __age=None
    __sex=None

    def __init__(self,name,age,sex):
        self.__name = name
        self.__age = age
        self.__sex = sex

    def setName(self, name):
        self.__name = name
    def getName(self):
        return self.__name

    def setAge(self, age):
        self.__age = age
    def getAge(self):
        return self.__age

    def setSex(self,sex):
        self.__sex=sex
    def getSex(self):
        return self.__sex

# ii.工人类
class Worker(Person):
    def __init__(self,name,age,sex):
        super().__init__(name,age,sex)#继承父类Person的，姓名，年龄，性别
    # 行为：干活。
    def work(self):
        print(self.getName(),"正在干活")

# iii.学生类
class Student(Person):
    #定义一个学号属性
    __studerNum=None
    def __init__(self,name,age,sex,studerNum):
        super().__init__(name,age,sex)#继承父类Person的，姓名，年龄，性别
        self.__studerNum=studerNum

    # 行为：唱歌。
    def study(self):
        print(self.getName(),"正在学习")

    # 行为：唱歌。
    def song(self):
        print(self.getName(),"正在唱歌")

#初始化Workers类，用构造方法传值
w=Worker("xiao","22","女")
#使用工人类调用work()方法
w.work()
#初始化Student类，用构造方法传值
s=Student("xiao","22","女","123456")
#使用学生类调用song()方法
s.song()
#使用学生类调用study()方法
s.study()

'''


