"""Backend code for Another-CPS-Tester"""
from threading import Thread
from time import time, sleep
from typing import Callable

class InstantResult:
    """A class with all the information for the instant results"""
    def __init__(self):
        self.current_clicks = -1
        self.current_cps = -1
        self.time_left = -1

class FinalResult:
    """A class with all the information for the final results"""
    def __init__(self):
        self.total_clicks = -1
        self.total_cps = -1
class BackendCPSTester:
    """Manages all backend code for Another-CPS-Tester"""
    def __init__(self, callback_function_external: Callable[[bool], None]):
        self.current_clicks = 0
        self.config_test_duration = 5 #seconds
        self.start_time = time()
        self.end_time = self.start_time + self.config_test_duration

        self.callback_function_external = callback_function_external
        self.background_thread = Thread(target=self.background_loop, daemon=True)

    def add_click(self):
        """Adds a click"""
        self.current_clicks += 1

    def start(self):
        """Starts the test timer"""
        self.start_time = time()
        self.end_time = self.start_time + self.config_test_duration

        self.background_thread.start()

    def is_time_up(self):
        """Checks if test duration has elapsed"""
        return time() >= self.end_time

    def background_loop(self):
        """Background loop that runs every hundredths of a milisecond"""
        while not self.is_time_up():
            self.callback_function_external(self.is_time_up())
            sleep(0.01)

    def instant_calculate(self) -> InstantResult:
        """Calculates the instant results"""

    def final_calculate(self) -> FinalResult:
        """Calculates the final results"""
