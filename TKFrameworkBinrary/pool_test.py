import os
import random
import time
from multiprocessing import Pool

class MyThread(object):
    def __init__(self, func):
        self.func = func

    def long_time_task(self, i):
        print('Run task %s (%s)...' % (i, os.getpid()))
        time.sleep(random.random() * 3)
        print(i)
        return (i, os.getpid())

    def parse_thread(self):
        print ('Parent process %s.' % os.getpid() )
        p = Pool()
        results = []
        for i in range(10):
            results.append(p.apply_async(long_time_task_wrapper,args=(self,i,)))

        # Now can get the result
        for res in results:
            print(es.get())
