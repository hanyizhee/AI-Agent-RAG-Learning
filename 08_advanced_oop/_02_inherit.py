from _01_encapsulation import Car
class FuelCar(Car): # 所有的类都有一个父类，默认为object
    def charge(self):
        #方法一: super().方法名()
        super().charge() # 调用父类中的指定方法
        print(f'{self.brand} {self.model}正在加油...')
        #方法二:类名.方法名(self)
        Car.charge(self)
        print(f'{self.brand} {self.model}正在加油...')
class ElectricCar(Car):
    pass
if __name__ == '__main__':
    c1 = FuelCar('BMW','X5','黑色','张三')
    c1.charge()
    # c1.start()
    # c1.run()
    # c1.stop()
    # print(c1.brand)
    # print(c1.get_owner())