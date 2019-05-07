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
######锁 Lock
```Python
# 互斥，共享资源可允许的并发读取数为1

# 初始化锁
lock = threading.Lock()

# 获取锁 acquire(blocking=True, timeout=-1) -> bool
# 如果已被获取，则挂起线程，等待锁释放
# 只传一个参数的时候，如果传入的参数为假，获取锁失败不会被挂起阻塞
lock.acquire()

# 释放锁
# 释放前状态为unlocked，则会抛RuntimeError
lock.release()
```
######可重入锁 RLock
```Python
# 对比Lock：
# 1. 谁拿到谁释放。如果线程A拿到锁，线程B无法释放这个锁，只有A可以释放
# 2. 同一线程可以多次拿到该锁，即可以acquire多次
# 3. acquire多少次就必须release多少次，只有最后一次release才能改变RLock的状态为unlocked

# 主要用于在类外保证线程安全，但又要类内使用同样方法时

# 初始化可重复锁
rlock = threading.RLock()

# 获取锁 acquire(blocking=True) -> bool
rlock.acquire()

# 释放锁
# 只有当前线程拥有锁才能调用这个方法
# 如果锁被释放后调用这个方法，会引起RuntimeError异常
rlock.release()
```
######信号量 Semaphore
```Python
# 信号量是一个内部数据，用于标明当前的共享资源可以允许的并发读取数

# 初始化信号量
# value信号量内部值初始大小，默认为1（互斥量，类似Lock），不可小于0
# value设置为0，用于线程同步
sema = threading.Semaphore(value=1) 

# 获取信号量，信号量内部值减1，如果进入时内部值等于0则挂起线程，等待信号量释放(内部值重新大于0)
# acquire(self, blocking=True, timeout=None)
sema.acquire()

# 释放信号量，信号量内部值加1
# 多次调用可能导致信号量内部值超过初始值，导致资源虚增
sema.release()


# BoundedSemaphore 有界信号量
# 有界信号量通过检查以确保它当前的值不会超过初始值，如果超过了初始值，将会引发ValueError异常
```
######条件 Condition
```Python

# wait

# notifyAll()

```

