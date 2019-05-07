#!/usr/bin/env python
# -*- coding:utf-8 -*-

import threading
import time


def hello(n, sema):
    sema.acquire()
    print('call thread　{0}'.format(n))
    # sema.release()


# 信号量管理表示realse()调用数减去acquire()调用数加上去一个初始值的计数器　　1　-　5　+　0　＝　-4　
sema = threading.Semaphore(value=1)
# sema = threading.BoundedSemaphore(value=1)
# sema.release()
sema.release()
sema.release()
sema.release()
workers = 5
for n in range(workers):
    t = threading.Thread(target=hello, args=(n+1, sema, ))
    t.start()

time.sleep(3)
print('start thread')
