# 在类中定义实例方法时，定义语法与之前学习的函数定义的方式是一致的。

class Car:
    def __init__(self,brand,name,price):
        self.brand = brand
        self.name = name
        self.price = price
    def running(self):
        print(f"{self.brand} {self.name} 正在高速行驶...")
    def total_cost(self,discount,rate = 0.1):
        return self.price * discount + self.price * rate

c1 = Car("BMW","X5",500000)
total_price = c1.total_cost(0.9,0.1)
print(f"提车总价为:{total_price:.0f}")

total_price = c1.total_cost(0.9)  # 与上述语法输出一致，因为给 rate 定义了初始值。
print(f"提车总价为:{total_price:.0f}")

c1.running()
