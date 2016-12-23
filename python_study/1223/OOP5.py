#! /usr/bin/env python
# Author: CDP
# email: dapeng_chang@163.com

"""
python中的特殊成员(泛指两边有两个下划线的成员)：
1、 __doc__      表示类的描述信息
2、 __module__   表示当前操作的对象在哪个模块
3、 __class__    表示当前操作的对象的类是什么
4、 __init__     构造方法
5、 __del__      析构方法

6、 __call__     对象后面加括号，触发执行
注：构造方法的执行是由创建对象触发的，即：对象 = 类名()；
但对于__call__方法的执行，是由对象后加括号触发的，即：对象()或 类名()()
（后面使用类名的调用方式，同时会先调用构造函数，最后调用析构函数）

7、 __str__      当我们打印对象时，调用

8、 __dict__     获取 对象 或者 类 中封装的数据

"""


class Foo(object):
    """
    这里是类的注释
    """
    NAME = "cdp"
    AGE = 25


    # 构造方法，创建对象时，自动执行
    # -------------------------
    def __init__(self, love, hate):
        self.love = love
        self.hate = hate
        print("这里是构造函数")



    # 析构方法，对象销毁时，自动执行（一般不用自定义）
    # ------------------------------------------
    def __del__(self):
        print("这里是析构函数")



    # 使用对象()方式时，调用
    # --------------------
    def __call__(self, *args, **kwargs):
        print("对象后面加括号执行", "\n")


    # 打印对象时，调用
    # --------------
    def __str__(self):
        return "这是这个对象的说明。。。。。。"



# 调用构造方法，对象销毁时调用析构方法
obj = Foo("奋斗", "懒惰")



# 查看类的文档
print(obj.__doc__)

# 查看对象属于的类
print(obj.__class__)

# 查看对象所在的模块
print(obj.__module__, "\n")


# 调用__call__ 方法
obj()
Foo("奋斗", "懒惰")()
print()


# 查看对象
print(obj, "\n")


# 查看对象中封装的所有字段
print(obj.__dict__)
# 查看类中封装的所有字段
print(Foo.__dict__)


print()

