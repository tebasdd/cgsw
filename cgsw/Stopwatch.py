import datetime
from builtins import property


class StopWatch:
    __running = False
    __running_since = None
    __dt_prev = 0.

    @property
    def is_running(self):
        return self.__running

    @property
    def elapsed(self):
        dt = self.__dt_prev
        if self.__running:
            dt += StopWatch.now() - self.__running_since
        return dt

    @staticmethod
    def now():
        return datetime.datetime.now().timestamp()

    def run(self):
        if not self.__running:
            self.__running = True
            self.__running_since = StopWatch.now()

    def stop(self):
        if self.__running:
            self.__dt_prev += StopWatch.now() - self.__running_since
            self.__running = False
            self.__running_since = None

    def reset(self):
        self.__running = False
        self.__running_since = None
        self.__dt_prev = 0.
