import pyautogui
import time
import random

def turn_next_page():
    """
    Simulates pressing the Right Arrow key to turn pages.
    Includes random variability to mimic human behavior.
    """
    # Press Right Arrow
    pyautogui.press('right')
    print("[Nav] Turned page.")

def wait_human_like(base_delay=1.0):
    """
    Waits for a base delay plus some random variance.
    """
    variance = random.uniform(0.5, 2.0)
    total_wait = base_delay + variance
    print(f"[Wait] Sleeping for {total_wait:.2f}s...")
    time.sleep(total_wait)
