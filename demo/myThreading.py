#!/usr/bin/env python
# -*- coding:utf-8 -*-

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


if __name__ == "__main__":
    for i in range(5):
        t = Mythread(args=(i,), kwargs={'a': 'A', 'b': 'B'})
        t.start()
