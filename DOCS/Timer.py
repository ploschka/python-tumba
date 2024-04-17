from time import time


class Timer:
    def __init__(self, title: str):
        self.title = title
        self.start = time()

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(self.title, ":", time() - self.start)