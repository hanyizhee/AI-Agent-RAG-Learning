class Goods:
    def __init__(self,name,price,quantity):         # 初始化方法
        self.name = name                            # 这里前面要写 self 而不是 Goods
        self.price = price
        self.quantity = quantity

    def __str__(self):                              # 设置返回值，防止输出地址
        return f"商品名称:{self.name} 商品价格:{self.price} 商品数量:{self.quantity}"  # return 后不加括号

class SpCManagement:
    def __init__(self):
        self.shopping_cart = []     # 设置一个列表，存放购物车信息

    def add_shopping_cart(self):
        name = input("请输入商品名称: ")
        price = int(input("请输入商品价格: "))
        quantity = int(input("请输入商品数量: "))
        goods = Goods(name,price,quantity)          # goods（中间变量）接收的是用 Goods 类创建出来的、带有 name、price、quantity 三个属性的对象
        self.shopping_cart.append(goods)

    def modify_cart(self):
        name = input("请输入要修改的商品: ")
        for goods in self.shopping_cart:
            if goods.name == name:
                price = int(input("请输入商品价格: "))
                quantity = int(input("请输入商品数量: "))
                goods = Goods(name,price,quantity)
                return
        print("未找到要修改的商品")

    def delete_cart(self):
        name = input("请输入要删除的商品: ")
        for goods in self.shopping_cart:
            if goods.name == name:
                self.shopping_cart.remove(goods)            # 删除列表中的这个 goods (Goods类型的对象)
                print("商品删除完毕")
                return
        print("要删除的物品不存在")

    def view_cart(self):
        for items in self.shopping_cart:
            print(items)
    def open_SpCManagement(self):
        print("欢迎使用购物车管理系统")

        while True:
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # ")
            print("# 1.添加购物车  2.修改购物车  3.删除购物车  4.查询购物车  5.退出购物车 #")
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # ")

            choice = input("请输入 1-5 实现您要实现的功能: ")
            try:
                match choice:       # 不能写case
                    case "1":
                        self.add_shopping_cart()
                    case "2":
                        self.modify_cart()
                    case "3":
                        self.delete_cart()
                    case "4":
                        self.view_cart()
                    case "5":
                        print("成功退出购物车管理系统")
                        break
                    case _:
                        print("请选择 1-5 之间的菜单功能!")
            except ValueError:
                print("输入的数据有问题,请重新输入!!!")
            except Exception:
                print("程序运行出错了,请重新选择 ~")
# 测试
if __name__ == "__main__":
    Shopping_Cart = SpCManagement()
#     a.add_shopping_cart()       # 如果直接打印列表本身，输出的是列表中对象的内存地址，而不是对象的具体属性内容    

#     a.modify_cart()
#     a.delete_cart()
#     for items in a.shopping_cart:   # for 遍历列表，逐个取出对象并打印其内容
#         print(items)            # 输出的时候调用 items 对象的 __str__ 方法，返回一个字符串并显示到屏幕上
Shopping_Cart.open_SpCManagement()

