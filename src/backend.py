"""Backend code for Another-CPS-Tester"""
from threading import Timer
from time import time
from typing import Callable

class BackendCPSTester:
    """Manages all backend code for Another-CPS-Tester"""
    def __init__(self, callback_function_external: Callable[[], None]):
        self.current_clicks = 0
        self.config_test_duration = 5 #seconds
        self.start_time = time()
        self.end_time = self.start_time + self.config_test_duration

        self.callback_function_external = callback_function_external
        self.timer = Timer(0.01, self.callback_function)

    def add_click(self):
        """Adds a click"""
        self.current_clicks += 1

    def start(self):
        """Starts the test timer"""
        self.start_time = time()
        self.end_time = self.start_time + self.config_test_duration

        self.timer.start()

    def is_time_up(self):
        """Checks if test duration has elapsed"""
        return time() >= self.end_time

    def callback_function(self):
        """A callback function that runs every hundredth of a second"""
        if self.is_time_up():
            self.timer.cancel()

        self.callback_function_external()
