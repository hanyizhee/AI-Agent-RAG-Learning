# Python 函数学习笔记

> 记录我从零开始学习 Python 函数的完整过程

---

## 📚 学习内容

### 第1天：函数基础（basic.py）
- ✅ 函数介绍
- ✅ 函数定义（`def`）
- ✅ 函数参数与返回值（`return`）
- ✅ 函数说明文档（docstring）
- ✅ 函数嵌套应用
- ✅ 案例练习

### 第2天：函数进阶（advanced.py）
- ✅ 变量作用域（`global` 关键字）
- ✅ 传参方式（位置参数、关键字参数）
- ✅ 默认参数（缺省参数）
- ✅ 不定长参数（`*args` 和 `**kwargs`）
- ✅ 参数类型（函数作为参数）
- ✅ 匿名函数（`lambda` 表达式）
- ✅ 案例1：递归函数
- ✅ 案例2：电商总金额计算系统

### 第3天：模块与类型注解（module_intro.py）

- ✅ 类型注解
  - 变量类型注解（`name: str = "张三"`）
  - 函数参数类型注解（`def greet(name: str) -> str:`）
  - 函数返回值类型注解（`-> str`）
  - 类型推断（编辑器自动识别类型）
- ✅ 模块介绍
  - 什么是模块（`.py` 文件）
  - 模块的作用（代码复用、命名空间隔离）
- ✅ 导入模块的方式
  - `import module`（导入整个模块）
  - `from module import func`（导入特定功能）
  - `import module as alias`（起别名）
  - `from module import *`（导入所有，不推荐）
- ✅ 自定义模块
  - 创建 `.py` 文件作为模块
  - 模块中的全局变量与函数
  - `if __name__ == "__main__"` 的作用
- ✅ 模块包（Package）
  - 包的概念（包含 `__init__.py` 的文件夹）
  - 包的作用（组织多个模块）
  - 包的导入方式（`from package import module`）

---

## 🚀 如何运行

```bash
# 运行基础练习
python functions/basic.py

# 运行进阶练习
python functions/advanced.py
```

---

## 📁 项目结构

```
practice/
├── README.md                  # 项目说明文档（中文）
├── LICENSE                    # 开源许可协议
├── .gitignore                 # Git 忽略文件配置
├── modules/                   # 模块学习模块
|   ├── utils                  # 工具包
|   ├── module_intro           # 模块内容介绍
|   └── module.test            # 模块内容测试
└── functions/                 # 函数学习模块
    ├── basic.py               # 函数基础
    └── advanced.py            # 函数进阶
```

---

## 📅 学习进度

☑ 第1天：函数基础（2026-08-18）
☑ 第2天：函数进阶（2026-08-19）
☑ 第3天：类型注解与模块（2026-08-20）
☐ 第4天：待解锁 ~

---

## 💡 学习心得

每天进步一点点，坚持带来大改变！

---

## 📝 提交记录

| 日期 | 内容 | 提交信息 |
|------|------|---------|
| 2026-08-18 | 完成函数基础学习 | `feat: 初始化 basic.py` |
| 2026-08-19 | 完成函数进阶学习 | `feat: 新增 advanced.py` |
| 2026-08-20 | 完成类型注解与模块学习 | `feat: 学习模块导入、自定义模块及 utils 包的 __init__.py 配置` |
