# Python模块(module):一个.py文件就是一个模块,模块是Python程序的基本组织单位。在模块中可以定义变量、函数、类,以及可执行代码。

#=========================== 导入模块 ===========================#

#------------------ 模块导入方式 ------------------#
# 在使用模块中提供的功能之前，必须得先导入，再使用。

# 导入模块的具体语法如下：

# 导入形式                                  代码案例                            调用方式                调用方式

# import 模块名                         import random,os                    模块名.功能名       random.dandint(10,100)
# import 模块名 as 别名                 import random as rd                 别名，功能名        rd.radint(10,100)
# from 模块名 import 功能名 as 别名     from random import randint as rint      别名                rint(10,100)
# from 模块名 import *                  from random import *                    功能名          randint(10,100)


#------------------ 模块导入示例 ------------------#

# 1.导入模块 --> 调用方式：模块名.功能名 / 别名.功能名

# import random
# for i in range(10):
#     print(random.randint(1,100))

# import random as rd
# for i in range(10):
#     print(rd.randint(1,100))

# 2.导入模块中的功能 --> 调用方式：功能名 / 别名

# from random import randint
# for i in range(10):
#      print(randint(1,100))

# from random import randint as rd
# for i in range(10):
#      print(rd(1,100))


#=========================== 自定义模块 ===========================#
# 当开发一些复杂的项目，为了让项目结构更清晰，更便于项目的维护管理及代码的复用，可能会把一个项目分成若干个模块。

# 注意：每一个python文件都可以作为一个模块，模块的名字就是文件名字（建议使用python标识符定义，规范命名）

# __all__是一个模块级别的特殊变量，用于指定 from 模块名 import * 时会导入哪些功能（*通配了哪些功能）。 
# __all__ = ["log_separator1","log_separator2"]  

# 常量（不会发生变化的数据 ； 常亮的名称为全部大写）
# PI = 3.14
# NAME = "韩艺哲"

# 函数

# def log_separator1():
#     print("-" * 30)

# def log_separator2():
#     print("+" * 30)

# def log_separator3():
#     print("#" * 30)

# def log_separator4():
#     print("*" * 30)

# 测试函数
# __name__：Python中内置的变量，表示当前模块的名字（直接运行当前模块，__name__的值为"__main__"）;当该模块导入时，__name__的值就是模块名。
# print(__name__)  
# if __name__ == "__main__":  #导入时不会执行下列语句
#     log_separator1()
 

#=========================== 软件包（package） ===========================#
# 包：本质就是一个文件夹，该文件夹中可以包含若干 Python 模块（.py文件），文件夹下还包含了一个__init__.py。
# 作用：模块文件较多时，用来管理多个模块。（包的本质也是一个模块）

#------------------ 模块导入方式 ------------------#
# 在使用模块中提供的功能之前，必须得先导入，再使用。

# 导入包的具体语法如下：

# 导入形式                                  代码案例                                    调用方式                调用方式

# import 包名.模块名                import utils.module_intro                       包名.模块名.功能名      utils.module_intro.log_separator1()  
# from 包名 import 模块名           from utils import module_intro                  模块名，功能名          module_intro.log_separator1()
# from 包名 import *                from utils import *                             模块名，功能名          module_intro.log_separator1()
# from 包名.模块名 import 功能名    from utils.module_intro import log_separator1       功能名              log_separator1()
# from 包名.模块名 import *         from utils.module_intro import *                    功能名              log_separator1()  