# 属性分为：
# 实例属性：实例属性属于每个具体对象的属性，每个对象都是独立的。（各个对象特有的数据）
# 类属性：类属性是属于类本身的属性，所有实例共享的。（所有对象共享的数据或配置）

#=========================== 实例属性 与 类属性 ===========================#

class Car:
    # 类属性
    wheel = 4
    tax = 0.1
    discount = 0.9
    def __init__(self,brand,name,price):
        # 实例属性
        self.brand = brand
        self.name = name
        self.price = price
        self.wheel = 5
    def running(self):
        print(f"{self.brand} {self.name} 正在高速行驶...")
    def total_price(self):
        return Car.tax * self.price + self.price * Car.discount
    
c1 = Car("BMW","X5",500000)

print(f"{c1.total_price():.0f}")  # 保留 0 位小数，必须用 f-string 语句
print(Car.wheel)  # 通过类名来访问类属性，会先查找类属性
print(c1.wheel)  # 通过实例对象，查找属性时，会先查找实例属性；实例属性不存在，再查找类属性