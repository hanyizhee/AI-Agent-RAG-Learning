class Student:  # 定义"Student"类
    def __init__(self,name,chinese,math,english):  # 初始化方法
        self.name = name  # 学生的姓名
        self.chinese = chinese   # 学生的语文成绩
        self.math = math         # 学生的数学成绩
        self.english = english   # 学生的英语成绩

    def __str__(self):  # 定义打印对象时显示的内容
        return f"姓名:{self.name} 语文: {self.chinese} 数学: {self.math} 英语: {self.english}"
    
    # 修改学生成绩

    def updata_score(self,chinese = None,math = None,english = None):
        if chinese is not None: 
            self.chinese = chinese
        if math is not None: 
            self.math = math
        if english is not None: 
            self.english = english

# 测试

if __name__ == "__main__":
    s1 = Student("王林",90,88,92)
    # print(s1)                   # 原始分数

# s1.update_score(english = 100)  # 修改英语分数为 100
# print(s1)                       # 输出修改后的分数


# 教务管理系统

class EduManagement:
    system_version = "1.0"
    system_name = "教务管理系统"

    def __init__(self):  # 初始化方法
        self.student_list = []  # 列表，记录的是在校学生的成绩信息

    # 添加学生成绩
    def add_student(self):
        name = input("请输入学生姓名: ")

        # 判断学生是否存在，如果存在，则添加失败（不能重复添加）
        for s in self.student_list:
            if s.name == name:
                print("该学生已存在，添加失败!")
                return
            
        chinese = int(input("请输入学生语文成绩: "))
        math = int(input("请输入学生数学成绩: "))
        english = int(input("请输入学生英语成绩: "))

        # 判断分数是否在 1-100 之间
        if 0 <= chinese <=100 and 0 <= math <=100 and 0 <= english <=100:
            stu = Student(name,chinese,math,english)
            self.student_list.append(stu)
            print("学生信息添加成功 ~")
        else:
            print("各科成绩必须在 1-100 之间!")


    # 修改学生成绩

    def updata_student(self):
        name = input("请输入要修改的学生姓名: ")
        for s in self.student_list:
            if s.name == name:
                print(f"当前成绩{s}")

            # 修改成绩
            chinese = int(input("请输入学生语文成绩: "))
            math = int(input("请输入学生数学成绩: "))
            english = int(input("请输入学生英语成绩: "))

            # 判断分数是否在 0-100 之间
            if 0 <= chinese <=100 and 0 <= math <=100 and 0 <= english <=100:
                s.updata_score(chinese,math,english)
                print(f"成绩修改成功 ~")
                print(f"修改后的成绩为: {s}")
                return
            else:
                print("各科成绩必须在 1-100 之间!")
                return
            print("修改完成!")  # 如果上面不写 return 这里就会被打印
        print("未找到该学生，修改失败 !")  # 与 for 齐平，如果没有进入 if 判断，就输出这句话


    # 删除学生成绩

    def delete_student(self):
        name = input("请输入要删除的学生姓名: ")
        for s in self.student_list:
            if s.name == name:
                self.student_list.remove(s)
                print("学生信息删除完毕 ~")
                return
        print("未找到学生，删除失败 !")   
    
    # 查询指定学生成绩
    def query_student(self):
        name = input("请输入要查询的学生姓名: ")
        for s in self.student_list:
            if s.name == name:
                print(f"学生信息:{s}")
                return
        print("未找到学生 !")
    # 展示所有学生信息
    def list_student(self):
        for s in self.student_list: 
            print(s)


# 运行系统
    def run(self):
        print(f"欢迎使用教务管理系统 V{EduManagement.system_version}")
    
        while True:
            print()
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            print("# 1.添加学生  2. 修改学生  3.删除学生  4.查询指定学生  5.查询所有学生  6.退出系统 #")
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
    
    
            choice = input("请选择您要执行的操作，输入 1-6: ")
            match choice:
                case "1":
                    self.add_student()
                case "2":
                    self.updata_student()
                case "3":
                    self.delete_student()
                case "4":
                    self.query_student()
                case "5":
                    self.list_student()
                case "6":
                    print("Bye ~")
                    break
                case _:
                    print("请选择 1-6 之间的菜单功能!")


# 测试
if __name__ == "__main__":
    edu_management = EduManagement()
    edu_management.run()

