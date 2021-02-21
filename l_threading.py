import threading


def f(i):
    print(' i am from a thread, num= %d \n' % i)


def main():
    for i in range(1, 10):
        t = threading.Thread(target=f, args=(i,))
        t.setDaemon(True)

        t.start()


if __name__ == "__main__":
    main()
