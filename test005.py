#! usr/bin/env python3
#-*- coding:utf-8 -*-
import threading
import time

gl_num = 0

lock = threading.Lock()


# 调用acquire([timeout])时，线程将一直阻塞，
# 直到获得锁定或者直到timeout秒后（timeout参数可选）。
# 返回是否获得锁。
def Func():
    lock.acquire()
    global gl_num
    gl_num += 1
    time.sleep(1)
    print(gl_num)
    lock.release()


for i in range(10):
    t = threading.Thread(target=Func)
    t.start()