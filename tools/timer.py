from time import time

class Timer:
    starting_time = 0

    @staticmethod
    def start():
        Timer.starting_time = time()

    @staticmethod
    def stop(prefix = "Time: "):
        print prefix + str(round(time() - Timer.starting_time, 3)) + "s"
