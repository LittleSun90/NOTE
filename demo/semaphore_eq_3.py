#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time
from random import random
from threading import Thread, Semaphore

sema = Semaphore(3)


def foo(tid):
    print(f'{tid} wait sema')
    sema.acquire()
    print(f'{tid} acquire sema')
    wt = random() * 2
    time.sleep(wt)
    print(f'{tid} sleep {wt}s')
    sema.release()
    print(f'{tid} release sema')


threads = []

for i in range(6):
    t = Thread(target=foo, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
