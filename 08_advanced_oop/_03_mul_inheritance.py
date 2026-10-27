# 多继承指的是一个子类,同时继承了多个父类的情况(会将多个父类中的非私有的属性和方法都继承下来)。
# 当一个类继承了多个父类时,默认优先使用第一个父类中的同名属性或方法,可以使用 类名 .__ mro __ 属性 或 类名.mro()方法查看调用顺序。
class Car: # Car是一个类
    def __init__(self,brand,model,color,owner): # 初始化方法（局部形参,只能在实例方法中用）,self是实例对象
        self.brand = brand # 品牌（公有实例属性）
        self.model = model # 型号（公有实例属性）
        self.color = color # 颜色（公有实例属性）
        self.__owner = owner # 所有者（私有实例属性），私有属性不能被外部直接调用，但是如果被公有方法调用，会被输出，并且私有属性可以被类内方法直接调用

    def start(self):  # 启动
        print(f'{self.brand} {self.model} 正在启动 ... ')

    def run(self):  # 行驶
        print(f'{self.brand} {self.model} 正在行驶 ... ')

    def stop(self):  # 停止
        print(f'{self.brand} {self.model} 停止行驶 ... ')

    def charge(self):
        print(f'{self.brand} {self.model} 正在补充燃料 ... ')

    def __control(self):
        print(f'{self.brand} {self.model} 正在被 {self.__owner} 驾驶 ... ')

    def get_owner(self):
        return self.__owner

# 华为智驾
class HuaweiAiDriving:
    """华为AI智能驾驶"""
    def __init__(self,version="V1.0"):
        self.version = version
    def run(self):
        print(f'使用华为Ai智能驾驶系统{self.version}正在行驶...')

# 问界汽车
class WenjieCar(Car,HuaweiAiDriving):
    def __init__(self,brand,model,color,owner,version="V1.0"): # 如果有形参少传，就会报错，除非在父类定义的时候设置默认值
        Car.__init__(self,brand,model,color,owner)
        HuaweiAiDriving.__init__(self,version)
    def run(self):
        Car.run(self)
        HuaweiAiDriving.run(self)





# MRO: Method Resolution Order (方法解析顺序)
if __name__ == '__main__':
    c = WenjieCar("BMW","X5","黑色","张三")
    # print(WenjieCar.__mro__) # 返回一个元组
    # print(WenjieCar.mro()) # 返回一个列表
    print(c.__dict__)
    c.run()