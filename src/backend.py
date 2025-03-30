"""Backend code for Another-CPS-Tester"""
from time import time

class BackendCPSTester:
    """Manages all backend code for Another-CPS-Tester"""
    def __init__(self):
        self.current_clicks = 0
        self.config_test_duration = 5 #seconds
        self.start_time = time()
        self.end_time = self.start_time + self.config_test_duration

    def add_click(self):
        """Adds a click"""
        self.current_clicks += 1

    def start(self):
        """Starts the test timer"""
        self.start_time = time()
        self.end_time = self.start_time + self.config_test_duration

    def is_time_up(self):
        """Checks if test duration has elapsed"""
        return time() >= self.end_time
