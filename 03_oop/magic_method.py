# 魔法方法是指Python中提供的以双下划线开头和结尾的特殊方法，用于定义类的特殊行为，比如：__init__。
# 魔法方法是不需要我们主动调用的，Python会在合适的时机主动调用。

# 魔法方法                          描述
# __init___                     初始化方法
# ___str___                     字符串表示的方法
# __eq__                        比较两个对象是否相等（equal）
# __lt__,__le__,__gt__,__ge__   支持比较两个对象的大小（小于less than），小于等于（less than or equal），大于（greater than），大于等于（greater than orequal）


# class Car:
#     def __init__(self,brand,name,price):
#         self.brand = brand
#         self.name = name
#         self.price = price
# c1 = Car("BMW","X5",500000)
# c2 = Car("BMW","X5",500000)

# print(c1 == c2)  # 直接输出为 False，因为 c1 和 c2 里面存的是他们各自的地址。
# print(c1 < c2)  # 所以这一行也会报错，因为 "<" 不能比较两个地址。


class Car:
    def __init__(self,brand,name,price):
        self.brand = brand
        self.name = name
        self.price = price
    def running(self):
        print(f"{self.brand} {self.name} 正在高速行驶...")
    def __str__(self):
        return f"{self.brand} {self.name} {self.price}"
    def __eq__(self,other):
        return self.brand == other.brand and self.name == other.name and self.price == other.price
    def __lt__(self,other):
        return self.price < other.price
c1 = Car("BMW","X5",500000)
c2 = Car("BMW","X5",500000)

print(c1 == c2)
print(c1 < c2)