"""Tests the backend code of Another-CPS-Tester"""

import unittest
from time import sleep
from src.backend import BackendCPSTester

class TestCPSTester(unittest.TestCase):
    """Manages the tests of the backend code of Another-CPS-Tester"""
    def __init__(self, methodName = "runTest"):
        super().__init__(methodName)

        self.is_called = False


    def setUp(self):
        """Setup runs before each test"""

        def cb(_):
            self.is_called = True

        self.cps_tester = BackendCPSTester(cb)

    def test_addclick(self):
        """Test add one click"""
        self.cps_tester.add_click()
        self.assertEqual(self.cps_tester.current_clicks, 1)

    def test_noclick(self):
        """Test if no click"""
        self.assertEqual(self.cps_tester.current_clicks, 0)

    def test_multipleclicks(self):
        """Tests if clicked 5 times"""
        for _ in range(0, 5):
            self.cps_tester.add_click()

        self.assertEqual(self.cps_tester.current_clicks, 5)

    def test_default_duration(self):
        """Test if the default test duration is 5"""
        self.assertEqual(self.cps_tester.config_test_duration, 5)

    def test_test_duration_false(self):
        """Tests if the time is up after only 1 second"""
        self.cps_tester.start()
        sleep(1)
        self.assertFalse(self.cps_tester.is_time_up())

    def test_test_duration_true(self):
        """Tests if the time is up after 5 seconds"""
        self.cps_tester.start()
        sleep(5)
        self.assertTrue(self.cps_tester.is_time_up())

    def test_timer_is_called_before_called(self):
        """Tests is_called is False before called"""
        self.assertFalse(self.is_called)

    def test_timer_is_called_1_sec_after_called(self):
        """Tests is_called is True 1 sec after called"""
        self.cps_tester.start()
        sleep(1)
        self.assertTrue(self.is_called)

    def test_timer_stops_after_time_up(self):
        """Tests if the timer stops after the test duration ends"""
        self.cps_tester.start()
        sleep(self.cps_tester.config_test_duration + 0.01)
        self.assertTrue(self.cps_tester.is_time_up())

    def test_callback_function_called_periodically(self):
        """Tests if the callback function is called multiple times during the test duration"""
        call_count = 0

        def cb(_):
            nonlocal call_count
            call_count += 1

        self.cps_tester = BackendCPSTester(cb)
        self.cps_tester.start()
        sleep(1)
        self.assertGreater(call_count, 1)

    def test_click_count_persists_after_timer_ends(self):
        """Tests if the click_count variable still exists after the timer ends"""
        self.cps_tester.start()
        self.cps_tester.add_click()
        self.cps_tester.add_click()
        sleep(self.cps_tester.config_test_duration+0.01)
        self.assertEqual(self.cps_tester.current_clicks, 2)

    def test_custom_test_duration(self):
        """Tests if a custom test time work correctly"""
        self.cps_tester.config_test_duration = 3
        self.cps_tester.start()
        self.assertFalse(self.cps_tester.is_time_up())
        sleep(3.1)
        self.assertTrue(self.cps_tester.is_time_up())
