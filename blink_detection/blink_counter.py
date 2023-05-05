"""
This module contains functions related to counting blinks.
"""

class BlinkCounter:
    def __init__(self):
        self.counter = 0

    def reset_counter(self):
        """
        Reset the blink counter.
        """
        self.counter = 0

    def increment_counter(self):
        """
        Increment the blink counter.
        """
        self.counter += 1

    def check_blink_threshold(self, threshold):
        """
        Check if the blink threshold has been reached.
        """
        return self.counter >= threshold
