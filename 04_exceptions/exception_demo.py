# try:
#     print("================================")
#     print(my_name)
#     print("================================")
# except NameError as e:      # "as e"可以输出异常信息
#     print("程序运行出错了，请联系管理员 ~ ；异常信息：",e)


# try:
#     print("================================")
#     # print(my_name)
#     # print(1/0)
#     # print("ABC"[10])
#     print("ABC".hello)
#     print("================================")
# except NameError as e:  # "as e"可以输出异常信息
#     print("名字不存在,请检查变量和或函数名字：:异常信息:",e)
# except ZeroDivisionError as e:
#     print("0不能做被除数,异常信息:",e)
# except IndexError as e:
#     print("索引错误，异常信息:",e)
# except Exception as e:  # 保底项，捕获所有异常
#     print("程序出错,请联系管理员")
# finally:  # 无论程序是否正常运行，这段Python代码都会正常运行
#     print("资源释放 ~")


# 异常的传递

# def fun1():
#     print("fun1 ... runing ...")
#     fun2()

# def fun2():
#     print("fun2 ... runing ...")
#     fun3()

# def fun3():
#     print("fun3 ... runing ...")
#     print(my_color)

# if __name__ == "__main__":
#     try:
#         fun1()
#     except Exception as e:
#         print("程序出现错误,请联系管理员,错误信息:",e)




