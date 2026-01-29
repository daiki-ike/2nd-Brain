import pyautogui
import time
import os
from datetime import datetime

def capture_region(region, output_path=None):
    """
    Captures a region of the screen.
    region: (left, top, width, height)
    output_path: If provided, saves the image to this path.
    Returns: PIL Image object
    """
    try:
        screenshot = pyautogui.screenshot(region=region)
        if output_path:
            screenshot.save(output_path)
            print(f"[Capture] Saved to {output_path}")
        return screenshot
    except Exception as e:
        print(f"[Error] Capture failed: {e}")
        return None

def select_region():
    """
    Interactive region selection.
    (This is a simple placeholder. In a full GUI, we'd use a selection tool.
    For CLI, we might ask user to hover mouse.)
    """
    print("Move mouse to TOP-LEFT corner of the book content and press Enter...")
    input()
    x1, y1 = pyautogui.position()
    print(f"Top-Left caught: ({x1}, {y1})")
    
    print("Move mouse to BOTTOM-RIGHT corner and press Enter...")
    input()
    x2, y2 = pyautogui.position()
    print(f"Bottom-Right caught: ({x2}, {y2})")
    
    width = x2 - x1
    height = y2 - y1
    
    if width <= 0 or height <= 0:
        print("[Error] Invalid region selected.")
        return None
        
    return (x1, y1, width, height)
