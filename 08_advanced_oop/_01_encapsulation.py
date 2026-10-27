# 封装就是把数据(属性)和操作数据的函数(方法)捆绑在一起,形成一个独立的单元(类),并隐藏内部的实现细节,只对外暴露必要的功能(方法)。
# 私有:私有的属性和方法只能在类的内部使用;Python中并没有真正的私有机制,约定在私有属性名和方法名前加 __ (两个下划线)。

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

if __name__ == '__main__':
    car = Car(brand='Audi',model='A6',color='黑色',owner='张三') # 创建实例对象（实例化）
    # car.start()
    # car.run()
    # car.stop()
    # print(car.color)
    # car.get_owner()

    print(car._Car__owner) # 强制访问
    car._Car__control() # 强制访问


