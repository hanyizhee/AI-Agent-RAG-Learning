# 多态是指同一个方法,具有不同的形态、行为、表现。

class Car:
    def __init__(self, brand, model, color, owner):
        self.brand = brand
        self.model = model
        self.color = color
        self.__owner = owner

    def start(self):
        print(f"{self.brand} {self.model} 正在启动...")
    def run(self):
        print(f'{self.__owner} : {self.brand} {self.model} 正在行驶...')
    def stop(self):  # @it
        print(f'{self.brand} {self.model} f#itirat ... ')
    def get_owner(self):
        return self.__owner[0:1] + " ** "
    def charge(self):
        print(f'{self.brand} {self.model} 正在补充燃料... ')

# 燃油车
class FuelCar(Car):
    def charge(self):
        print(f'{self.brand} {self.model} 正在加油... ')

# 电车
class ElectricCar(Car):
    def charge(self):
        print(f'{self.brand} {self.model} 正在充电...')


# 补充燃料函数
def handle_charge(car: Car): # 函数参数类型声明 --- 指定的是父类型
    car.charge()

# 测试代码
if __name__ == '__main__':
    handle_charge(FuelCar(brand="BMW", model="X5", color="黑色", owner="张三"))
    handle_charge(ElectricCar(brand="BYD", model="汉", color="黑色", owner="张三"))