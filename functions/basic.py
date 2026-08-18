"""
函数基础学习
日期:2026-08-18

学习内容:
1.函数介绍
2.函数定义
3.函数参数与返回值
4.函数说明文档
5.函数嵌套应用
6.案例
"""



# 函数介绍
# 函数是组织好的(def打包) --> 可重复使用的(调用3次) --> 用来实现特定功能(只做加法) --> 的代码片段(不是完整程序)。

# def add(a,b):       #组织好的
#     return a + b    #特定功能:加法

# print(add(3,5))     #重复使用第1次
# print(add(10,20))   #重复使用第2次
# print(add(100,200)) #重复使用第3次




# 函数定义

# def 函数名(参数列表):
#     函数体
#     ......
#     return 返回值

# 注意；函数定义的时候并不会执行，只有在调用函数的时候，函数体的逻辑才会执行；必须先定义，再调用。

# 函数定义（示例）

# def out_line():
#     print("-------------------------------")
#     print("-------------------------------")




# 调用函数
# 函数名(参数)

# 调用函数（示例）
#out_line()




#------- 计算圆的面积 -- 半径 -------#
# def circle_area(r):  # r为形式参数，只能在函数内使用（局部变量）
#     area = 3.14 * r ** 2
#     return area

# 调用函数
# c_area = circle_area(10)  # 10为实际参数，指在函数调用时传入的参数
# print(c_area)




#------- 计算长方形的面积 -- 长，宽 -------#
# def rectangle_area(len,w):
#     """根据长方形的长度和宽度，计算长方形的面积

#     Args:
#         len (float): 长方形的长度
#         w (float): 长方形的宽度

#     Returns:
#         float: 长方形的面积
#     """
#     area = len * w
#     return area

# 调用函数
# print(rectangle_area(5,4))





#-------计算圆形的面积，周长 -- 半径-------#
#如果返回值有多个，多个返回值之间以逗号分隔 --> 多个返回值会封装到元组中 
# def circle_area_c(r):
#     """根据圆形的半径，计算圆形的面积，周长

#     Args:
#         r (float): 圆形的半径

#     Returns:
#         float: 圆的面积，圆的周长
#     """
#     pi = 3.14
#     area = pi * r ** 2
#     c = 2 * pi * r
#     return area,c

#调用函数
# al = circle_area_c(10)    #接收返回值
# print(al)                   #输出返回值
# print(type(al))             #输出返回值类型

# area,c = circle_area_c(10)  #解包操作
# print(area)
# print(c)





# 函数的嵌套调用
# 函数调用遵循栈结构，最后被调用的最先返回LIFO（Last In First Out，后进先出）

# def function_a():
#     print("a ... before")
#     function_b()
#     print("a ... after")

# def function_b():
#     print("b ... before")
#     function_c()
#     print("b ... after")

# def function_c():
#     print("c ...")

# function_a()

# print("函数调用完毕 ~")




# 案例1：定义一个函数：根据传入的底和高计算三角形面积的函数（三角形面积 = 底 * 高 / 2）
# def triangle_area(base,height):
#     """根据传入的底和高计算三角形面积

#     Args:
#         base (float): 三角形的底
#         height (float): 三角形的高
#     """
#     # 核心公式
#     area = base * height / 2
#     return area
# # 函数调用
# area = triangle_area(8,5)
# print(f"三角形的面积为:{area}")




# 案例2：定义一个函数：根据传入的字符串计算元音字母个数的函数
# def vowel_count(s):
#     """计算传入的字符串中元音字母的个数

#     Args:
#         s (str): 传入的字符串
#     """
#     vowels = []
#     for char in s:
#         if char in "aeiouAEIOU":
#             vowels.append(char)
#     return len(vowels)

# print(vowel_count("abiA"))




# 案例3：定义一个函数：根据传入的班级学员高考成绩列表中的成绩计算最高分、最低分、平均分（保留1位小数）
# def calc_cee_score_stats(scores):
#     """根据传入的班级学员高考成绩列表中的成绩计算最高分、最低分、平均分（保留1位小数）

#     Args:
#         scores (list): 高考成绩单
#     """
#     max_score = max(scores)
#     min_score = min(scores)
#     total_score = 0
#     for score in scores:
#         total_score += score
#     avg_score = total_score / len(scores)
#     avg_score = round(avg_score,1)
#     return max_score,min_score,avg_score
# max_score,min_score,avg_score = calc_cee_score_stats([100,500])
# print(f"最高分为: {max_score}")
# print(f"最低分为: {min_score}")
# print(f"平均分为: {avg_score}")




# 案例4：定义一个函数：根据传入的分数，计算对应的分数等级并返回。
# def get_level(score):
#     """_summary_

#     Args:
#         score (float): 传入的分数

#     Returns:
#         str: 返回的分数等级
#     """
#     if score > 100 or score < 0:
#         level = "无效分数"
#     elif score >= 90:
#         level = "A"
#     elif score >= 75:
#         level = "B"
#     elif score >= 60:
#         level = "C"
#     else :
#         level = "D"
#     return level
# print(f"所传入的分数相应的分数等级为{get_level(-1)}")




#定义一个函数，用于判断一个字符串是否为回文串
# def is_palindrome(s):
#     """通过这个函数，判断字符串是否为回文串

#     Args:
#         s (str): 所输入的字符串

#     Returns:
#         bool: 通过判断返回的bool值
#     """
#     return s == s[::1]
# print(is_palindrome("黄山落叶松叶落山黄"))




#根据传入的三角形三个边的边长，判定三角形的类型（等边、等腰、普通，或者不能构成三角形）
# def judge_triangle_type(side_a,side_b,side_c):
#     """根据传入三角形的三条边，判断三角形的类型

#     Args:
#         side_a (float): 三角形的第一条边
#         side_b (float): 三角形的第二条边
#         side_c (float): 三角形的第三条边

#     Returns:
#         str: 三角形的类型；等边、等腰、普通，或者不能构成三角形
#     """
#     if side_a < 0 or side_b < 0 or side_c < 0:
#         judge_triangle_type = "不能构成三角形"
#     elif side_a + side_b < side_c or side_b + side_c < side_a or side_a + side_c < side_b:
#         judge_triangle_type = "不能构成三角形"
#     elif side_a == side_b == side_c:
#         judge_triangle_type = "该三角形为等边三角形"
#     elif side_a == side_b and side_b != side_c or side_b == side_c and side_c != side_a or side_a == side_c and side_c != side_b:
#         judge_triangle_type = "该三角形为等腰三角形"
#     else :
#         judge_triangle_type = "该三角形为普通三角形"
#     return judge_triangle_type
# print(judge_triangle_type(3,4,5))


















