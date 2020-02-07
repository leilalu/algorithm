"""
使用Python实现单例模式

单例模式：确保某个类有且仅有一个实例

实现单例模式有5种方法：
1、使用模块
2、使用装饰器
3、使用类
4、基于__new__方法
5、基于metaclass元类的方法

"""

"""
1、使用模块
Python的模块是天然的单例模式，因为模块在第一次导入(import)时，会执行模块代码，生成.pyc文件，
在第二次导入时就会直接加载这个.pyc文件，而不会再次执行模块代码。
因此我们只需要将生成类的实例的相关函数定义在一个模块中，就可以获得一个单例的实例。

"""

# 如将下面的代码保存在文件mySingleton.py中， 要使用singleton实例时直接在其他文件中导入该文件中的对象,这个对象就是单例对象
# from mySingleton import singleton
class Singleton:
    def foo(self):
        pass


singleton = Singleton()

"""
2、使用装饰器 - @Singleton

"""


def Singleton(cls):
    _instance = {}

    def _singleton(*args, **kargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kargs)
        return _instance[cls]

    return _singleton


@Singleton
class A(object):
    a = 1

    def __init__(self, x=0):
        self.x = x


a1 = A(2)
a2 = A(3)