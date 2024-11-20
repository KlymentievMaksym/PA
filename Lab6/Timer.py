import time


class Timer:
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.time_used = time.time() - self.start

    def __str__(self):
        return str(self.time_used)
