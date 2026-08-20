def log_separator1():
    print("-" * 30)

def log_separator2():
    print("+" * 30)

def log_separator3():
    print("#" * 30)

def log_separator4():
    print("*" * 30)

# 测试函数
# __name__：Python中内置的变量，表示当前模块的名字（直接运行当前模块，__name__的值为"__main__"）;当该模块导入时，__name__的值就是模块名。
print(__name__)  
if __name__ == "__main__":  #导入时不会执行下列语句
    log_separator1()