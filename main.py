import math
import time
import pyautogui


def move_cursor_in_circle(radius):
    start_x, start_y = pyautogui.position()  # Get current cursor position

    angle = 0
    while True:
        x = int(start_x + radius * math.cos(angle))
        y = int(start_y + radius * math.sin(angle))
        pyautogui.moveTo(x, y, duration=0.1)  # Move cursor to the calculated position
        angle += 0.1
        time.sleep(0.01)  # Adjust speed of the movement


radius = 100

move_cursor_in_circle(radius)
