#!/usr/bin/env python
# -*- coding:utf-8 -*-

import threading
import time


class Box():
    rlock = threading.RLock()

    def __init__(self):
        self.total_items = 0

    def execute(self, n):
        # with Box.rlock:
            self.total_items += n

    def add(self):
        with Box.rlock:
            self.execute(1)
            # print(self.total_items)

    def remove(self):
        with Box.rlock:
            self.execute(-1)
            # print(self.total_items)


def adder(box, items):
    while items > 0:
        print("adding 1 item in the box")
        box.add()
        time.sleep(1)
        items -= 1


def remover(box, items):
    while items > 0:
        print("removing 1 item in the box")
        box.remove()
        time.sleep(2)
        items -= 1


if __name__ == "__main__":
    items = 5
    # item1 = 5
    # item2 = 6
    print("putting %s items in the box " % items)
    box = Box()
    # t1 = threading.Thread(target=adder, args=(box, item1))
    # t2 = threading.Thread(target=remover, args=(box, item2))
    t1 = threading.Thread(target=adder, args=(box, items))
    t2 = threading.Thread(target=remover, args=(box, items))
    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print("%s items still remain in the box " % box.total_items)
