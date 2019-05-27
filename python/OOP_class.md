#Python面向对象
##面向对象编程
###面向对象基本概念
面向对象编程(Object Oriented Programming - OOP)是一种程序设计思想，OOP把对象作为程序的基本单元，一个对象可能包含了数据、属性和操作数据的方法。

Python中一切皆对象。

类和对象

继承、封装和多态

属性和方法

覆盖

重载：Python不支持同一个函数多种定义，可基于动态类型和缺省参数解决参数类型和个数不一致的问题。


###Python中的类
####类的定义

```Python
# Python2中，默认类都为经典类，经典类需要显示继承object
# 默认类名首字母大写，实例名全小写
class A：
    pass

class B(object):
    pass

# 继承类
class A(B):
    pass

# Python3中，默认类都为新式类
```

####经典类和新式类的区别
- 定义实现不一样
- 新式类中类和类型合并，__class__和type()得到统一
- 继承方法顺序（Method Resolution Order-MRO），新式类采用C3广度优先算法，经典类使用深度优先
- 新式类具有更多的高级工具（特性property，描述符，__slots__等）


####特性property

@property是将一个实例方法变成同名属性，支持.调用。常用于将方法装换成只读属性和参数校验等场景



