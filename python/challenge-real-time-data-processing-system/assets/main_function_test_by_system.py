import sys

sys.path.append("/home/labex/project")

import unittest, time
from unittest.mock import patch

from main_function import main


class TestMainFunctionAndStoppingMechanism(unittest.TestCase):
    def test_main_graceful_stop(self):
        # Set a short duration for the test
        duration = 1

        # Use a context manager to patch the time.sleep function in the solution module
        with patch("time.sleep", side_effect=InterruptedError) as mock_sleep:
            start_time = time.time()

            try:
                main()
            except InterruptedError:
                # Ensure the main function was stopped by the KeyboardInterrupt
                self.assertTrue(mock_sleep.called)

            elapsed_time = time.time() - start_time

            # Check if the test duration is within an acceptable range
            self.assertTrue(duration - 1 <= elapsed_time <= duration + 1)


if __name__ == "__main__":
    unittest.main()
