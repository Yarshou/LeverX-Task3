from threading import Lock
from concurrent.futures import ThreadPoolExecutor

lock = Lock()
a = 0


def function(arg):
    global a
    for _ in range(arg):
        lock.acquire()
        a += 1
        lock.release()


def main():
    with ThreadPoolExecutor(max_workers=5) as executor:
        for i in range(5):
            executor.submit(function, 1000000)
    print("----------------------", a)  # ???


main()
