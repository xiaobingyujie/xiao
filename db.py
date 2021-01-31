import pymysql
con=pymysql.connect(host="localhost",user="root",password="123456",database="销售数据库")
cursor=con.cursor()

# sql = "insert into 顾客 values(%s,%s,%s,%s)"
# param= ['G005','蔡徐坤','男',22]
# sql = "update 顾客 set 顾客名='菜菜' where 顾客号=%s"
# param=['G001']
# sql = "delete from 顾客 where 顾客号=%s"
# param=["G005"]
sql = "select * from 顾客 where 顾客名 = %s"
param = ["菜菜"]
num=cursor.execute(sql,param)
print("影响了",num,"行数据")
con.commit()
cursor.close()
con.close()
