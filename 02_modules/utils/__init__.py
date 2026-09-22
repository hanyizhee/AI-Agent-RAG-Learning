# 描述包信息
from . import my_fun  #"."的意思是从本文件夹找
from . import my_var

# __all__是一个模块级别的特殊变量，用于指定 from 模块名 import * 时会导入哪些功能（*通配了哪些功能）。 
__all__ = ["my_fun","my_var"]