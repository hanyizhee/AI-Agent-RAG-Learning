"""
函数进阶学习
日期:2026-08-19

学习内容:
1.变量作用域(global关键字)
2.传参方式(位置参数、关键字参数)
3.默认参数(缺省参数)
4.不定长参数(*args and **kwargs)
5.参数类型（函数作为参数）
6.匿名函数(lambda表达式)
7.案例1(递归)
8.案例2:电商总金额计算系统
"""
#=========================== 变量的作用域 ===========================#
# 变量的作用域：指的是变量的作用范围（表示这个变量在哪里可以使用，在哪不能用）

# num = 100                   # 全局变量：在函数之外定义，称之为全局变量，在整个文件中（包括函数内）都可以使用（通常定义在文件的顶部）。
# 定义函数
# def circle_area(r):         # r也为局部变量
#     pi = 3.14               # 局部变量：在函数内部定义的变量，称之为局部变量，只能在该函数内部使用，外部无法访问（函数执行完毕后，会自动销毁其内部局部变量）
#     area = pi * r * r       # 局部变量
#     return area

# count = 0                   # 全局变量
# #调用函数
# c_area = circle_area(10)    # 全局变量
# print(c_area)
# print("num =", num)


#------------------- global关键字 -------------------#

# num1 = 1              # 全局变量：num1

# def fun1():           # 定义函数
#     global num1       # global关键字：使用全局变量 num1
#     num1 = 100        # 修改全局变量的值
#     print(num1)       # 输出 num1

# fun1()                # 调用函数
# print(num1)           # 测试全局变量 num1 是否还为1


#~~~~~~~~~~~~~ 调试开关(global使用场景) ~~~~~~~~~~~~~#

# debug_mode = False

# def enable_debug_mode():      # 定义函数头
#     global debug_mode         # global关键字:声明要修改的变量为全局变量
#     debug_mode = True
#     print("调试模式已开启")

# def disable_debug_mode():
#     global debug_mode
#     debug_mode = False
#     print("调试模式已关闭")


#=========================== 函数传参方式 ===========================#
# 函数传参方式：在调用函数时，传递实参的方式

#------------------- 1.位置参数 -------------------#
# 位置参数：调用函数时根据函数定义时的位置来传递参数

# def reg_stu(name,age,gender,city):
#     print(f"注册成功,姓名:{name},年龄:{age},性别:{gender},城市:{city}")
#     return {"name": name,"age": age,"gender": gender,"city": city}

# stu = reg_stu("张三",18,"男","北京")
# print(stu)

# 要求：调用函数时参数顺序与定义函数时参数顺序完全一致


#------------------ 2.关键字参数 ------------------#
# 关键字参数：是指调用函数时以函数定义时形参名称作为关键字，以“键=值”的形式来传递参数（不要求顺序）。

# def reg_stu(name,age,gender,city):
#     print(f"注册成功,姓名:{name},年龄:{age},性别:{gender},城市:{city}")
#     return {"name": name,"age": age,"gender": gender,"city": city}

# stu1 = reg_stu(name = "张三",age = 18,gender = "男",city = "北京")
# print(stu1)
# stu2 = reg_stu(gender = "男",name = "王武",city = "上海",age = 22)
# print(stu2)
# stu3 = reg_stu("赵四",28,city = "上海",gender = "男")  # 前面为位置参数，后面为关键字参数
# print(stu3)

# 要求：如果位置参数与关键字参数混用，关键字参数必须在位置参数之后（关键字参数之间，没有顺序要求）


#=========================== 函数默认参数 ===========================#
# 默认参数也叫缺省参数，用于在定义参数时，为参数提供默认值，调用参数时，可以不传递有默认值的参数。

# def reg_stu(name,age,gender,city = "北京"):
#     print("注册成功,姓名:{name},年龄{age},性别{gender},城市:{city}")
#     return {"name": name,"age": age,"gender": gender,"city": city}

# stu = reg_stu("张三",18,"男")
# print(stu)

# stu = reg_stu("赵四",22,"男","深圳")
# print(stu)

# 注意：默认参数必须放在没有默认值的参数列表的后面，一个函数是可以在定义时可以设置多个默认参数的。
# 注意: 函数调用时，如果为默认参数传递了值，则会修改默认参数的值；如果没有传递参数，则直接使用默认值


#=========================== 函数不定长参数 ===========================#

#------------------ 位置参数 *args --> 元组 ------------------#

# def calc_data(*args):
#     min_data = min(args)
#     max_data = max(args)
#     avg_data = sum(args) / len(args)
#     return min(args),max(args),round(avg_data,1)

# data = calc_data(10,20,30,40,50)
# print(data)

# 注意：传递的所有匹配的位置参数都会被args变量收集，这些参数会合并封装为一个元组，args是一个元组类型（注意不会封装关键字类型）
# 注意：args只是约定俗成的变量名，并不是关键字，这里可以使用任何合法的变量名（如*data）


#------------------ 关键字参数 **kwargs --> 字典 ------------------#

# def calc_data(*args,**kwargs):
#     min_data = min(args)
#     max_data = max(args)
#     avg_data = sum(args) / len(args)
#     if kwargs.get("round") is not None:
#         avg_data = round(avg_data,1)
#     if kwargs.get("print"):
#         print(f"最大值为:{max_data},最小值为: {min_data},平均值为: {avg_data}")

#     return min_data,max_data,avg_data

# print(calc_data(100,400,300,0.2,round = 1,print = False))


#=========================== 函数参数类型（函数作为参数） ===========================#
# 普通参数：数字、布尔、字符串、列表、元组、集合、字典等。
# 特殊参数：函数。

# # 加
# def add(x,y):
#     return x + y

# # 减
# def subtract(x,y):
#     return x - y

# # 乘
# def multiply(x,y):
#     return x * y

# # 除
# def divide(x,y):
#     return x / y

# # 计算
# def calc(x,y,oper):
#     return oper(x,y)

# print(calc(10,20,add))


#=========================== 匿名函数（lambda表达式） ===========================#

#lambda 参数列表：函数体

# out_line = lambda : print('----------')
# add = lambda x,y:x + y

# out_line()
# print(add(2,3))

# 注意：函数逻辑比较简单（单行表达式）且只在一个地方使用时，可以考虑使用匿名函数，简化书写（通常作为高阶函数的参数使用）。
# 注意：匿名函数中可以返回结果，也可以不返回结果。返回结果时，不需要写return，表达式的运行结果就是要返回的结果。


# 题目：按照每个元素的字符个数，从小到大排序

# data_list = ["C++","C","Python","Jack","PHP","Java","Go","TavaScript","Rust"]

# data_list.sort(key = lambda item : len(item))  # 匿名函数典型应用案例
# print(data_list)

# data_list.sort(key = lambda item : len(item),reverse = True)
# print(data_list)


#=========================== 案例1 ===========================#
#定义一个函数，根据传入的的数字，计算该数字阶乘的结果。

# 正常做法

# def factorial(num):
#     result = 1
#     for i in range(1,num+1):
#         result *= i
#     return result

# print(factorial(4))

# 递归调用：指的是在函数中自己调用自己的情况 -----> 一定得有终结点

# def jc(n):
#     if n == 1:
#         return 1
#     else :
#         return n * jc(n - 1)
# print(jc(4))


#=========================== 案例2 ===========================#
"""
定义一个函数，用于根据传入的一批商品信息(商品名、价格、数量)、优惠(优惠券、积分抵扣)、运费信息计算订单的总金额。
具体规则如下：
    优惠券需要商品金额满5000才可以使用,且优惠券金额不能超过商品总价。
    积分抵扣需要商品总金额满5000才可以使用,100积分抵扣1元(且抵扣金额不能超过商品总价，积分只能整百抵扣)。
"""

# def calc_final_amount(*args,coupon_discount,points,shipping_fee):
#     """_summary_

#     Args:
#         coupon_discount (int): 优惠券抵扣
#         points (int): 积分
#         shipping_fee (float): 运费信息
#         points_deduction: 积分抵扣

#     Returns:
#         float: 优惠完总金额
#     """
#     total_price = [goods[1] * goods[2] for goods in args]
#     subtotal = sum(total_price)
#     points_deduction = points // 100
#     total_discount = 0
#     if subtotal >= 5000:
#         total_discount += min(coupon_discount,subtotal)
#         total_discount += min(points_deduction,subtotal)
#     total_discount = min(total_discount,subtotal)
#     final_amount = subtotal - total_discount + shipping_fee

#     return final_amount

# print(calc_final_amount(("白菜",1000,6),("土豆",500,2),coupon_discount = 200,points = 40000,shipping_fee = 200))








