
# 记录了第一件服装详细信息
name1 = "衬衫"
material1="棉"
price1 = 100
quanlity1 = 'A+'
num1 = 2
unit1 = '件'

# 记录了第二件服装详细信息
name2 = "羊绒衫"
material2="羊毛"
price2 = 150
quanlity2 = 'A+'
num2 = 4
unit2 = '件'

# 记录了第三件服装详细信息
name3 = "羽绒服"
material3="鸭绒"
price3 = 1150
quanlity3= 'B+'
num3 = 1
unit3 = '件'

# 记录了第四件服装详细信息
name4 = "牛仔裤子"
material4="棉"
price4 = 170
quanlity4 = 'C+'
num4 = 18
unit4 = '条'

# 记录了第五件服装详细信息
name5 = "卫衣"
material5="羊毛"
price5 = 109
quanlity5 = 'B+'
num5 = 5
unit5 = '件'

print('-------------------------欢迎来到服装商城----------------------------')
print(' 名称         材质         价格          品质         数量        单位')
print('------------------------------------------------------------------')
print(name1,"         ",material1,"        ",price1,"        ",quanlity1,"         ",num1,"       ",unit1)
print(name2,"       ",material2,"       ",price2,"        ",quanlity2,"         ",num2,"       ",unit2)
print(name3,"       ",material3,"       ",price3,"       ",quanlity3,"         ",num3,"       ",unit3)
print(name4,"      ",material4,"        ",price4,"        ",quanlity4,"         ",num4,"      ",unit4)
print(name5,"        ",material5,"        ",price5,"        ",quanlity5,"          ",num5,"      ",unit5)
print('------------------------------------------------------------------')
print('总金额为：',(price1 * num1 + price2 * num2+ price3 * num3+ price4 * num4+ price5 * num5 ),"￥")
