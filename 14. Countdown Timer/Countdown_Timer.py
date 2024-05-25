import time


def countdown(seconds):
    print("The Countdown Timer Started!")
    for i in range(seconds, 0, -1):
        print(i)
        time.sleep(1)
    print("Times Up!")


countdown(10)
