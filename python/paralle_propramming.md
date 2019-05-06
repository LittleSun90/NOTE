#Python并发编程
##多线程编程-threading模块
###实现线程
######实例化Thread类实现
```Python
# target 当线程启动时执行的函数
# name 线程的名字，默认会分配一个统一的名字Thread-N，也可以通过t.setName(name)设置
# args 传递给target函数的参数，要使用tuple类型
# kwargs 传递给target函数的参数，要使用dict类型
# daemon 后台线程，不阻塞主线程，主线程退出依然会被中止，也可以通过t.setDaemon(True)设置
t = threading.Thread(['group=None', 'target=None', 'name=None', 'args=()',  
    'kwargs=None', '*', 'daemon=None'],)

# 启动线程
t.start()

# 主线程等待子线程运行结束
t.join()

# 获取子线程名称
t.getName()

# 判断子线程存活状态
t.is_alive()

# 判断子线程是否为后台线程
t.isDaemon()
```
######Thread子类实现
```Python
# 定义Thread子类
# 继承扩展Thread类的__init__方法
# 覆写Thread类的run方法
import threading


class Mythread(threading.Thread):
    def __init__(self,
            group=None, target=None, name=None, args=(),
            kwargs=None, *, daemon=None):  # noqa
        super().__init__(group=group, target=target, name=name, daemon=daemon)
        self.args = args
        self.kwargs = kwargs

    def run(self):
        print('running with %s and %s', self.args, self.kwargs)
```
###同步机制
######信号量 Semaphore
```Python
# 信号量是一个内部数据，用于标明当前的共享资源可以允许的并发读取数
# 初始化信号量
# value信号量内部值初始大小，默认为1（互斥量），不可小于0.
# value设置为0，则类似Lock，用于线程同步
sema = threading.Semaphore(value=1)  

# 获取信号量，信号量内部值减1，如果内部值为负则挂起线程，等待信号量释放
sema.acquire()

# 释放信号量，信号量内部值加1
# TODO: 确定先释放会怎样
sema.release()

```

