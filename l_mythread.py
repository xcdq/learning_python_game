# import threading
# import time
# exitFlag = 0


# class myThread(threading.Thread):
#     def __init__(self, threadID, name, counter) -> None:
#         super().__init__()
#         self.threadID = threadID
#         self.name = name
#         self.counter = counter

#     def run(self) -> None:
#         # return super().run()
#         print('Starting '+self.name)
#         print_time(self.name, self.counter, 5)
#         print('Exiting '+self.name)


# def print_time(threadName, delay, counter):
#     while counter:
#         # if exitFlag:
#         #     thread.exit()
#         time.sleep(delay)
#         print("%s : %s" % (threadName, time.ctime(time.time())))
#         counter -= 1


# thread1 = myThread(1, 'Thread-1', 1)
# thread2 = myThread(2, "Thread-2", 2)
# thread1.start()
# thread2.start()
# print('Exiting Main Thread .')


# import threading
# import time
# exitFlag = 0


# class myThread(threading.Thread):
#     def __init__(self, threadID, name, counter) -> None:
#         super().__init__()
#         self.threadID = threadID
#         self.name = name
#         self.counter = counter

#     def run(self) -> None:
#         # return super().run()
#         print('Starting '+self.name)
#         threadLock.acquire()
#         print(self.name, "获得锁")
#         print_time(self.name, self.counter, 5)
#         print(self.name, '释放锁')
#         threadLock.release()
#         print('Exiting '+self.name)


# def print_time(threadName, delay, counter):
#     while counter:
#         # if exitFlag:
#         #     thread.exit()
#         time.sleep(delay)
#         print("%s : %s" % (threadName, time.ctime(time.time())))
#         counter -= 1


# threadLock = threading.Lock()
# threads = []
# thread1 = myThread(1, 'Thread-1', 1)
# thread2 = myThread(2, "Thread-2", 2)
# thread1.start()
# thread2.start()
# threads.append(thread1)
# threads.append(thread2)
# for t in threads:
#     t.join()
# print('Exiting Main Thread .')


# 定时器
import threading
import time


def func():
    print(time.ctime())


print(time.ctime())
timer = threading.Timer(5, func)  # 指定时间，函数f
timer.start()
