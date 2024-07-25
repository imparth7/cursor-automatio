# Auto Cursor Movement Program

This Python program automates cursor movement in a circular path on your screen using the `pyautogui` library.

## Requirements
- Python 3.x (tested with Python 3.12.3 on Windows)
- `pyautogui` library

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/imparth7/cursor-automation.git
   cd cursor-automation
   ```

2. Install dependencies using pip:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Open a terminal or command prompt and navigate to the project directory (`cursor-automation`).

2. Run the `main.py` script:
   ```bash
   python main.py
   ```

3. The cursor will start moving in a circular path with a default radius of 100 pixels.

4. To stop the program, press `Ctrl+C` in the terminal or command prompt.

## Configuration

- You can adjust the radius of the circular path by modifying the `radius` variable in `main.py`.

## Notes

- Ensure your system allows Python to control the mouse cursor. Some operating systems or security settings may restrict or require special permissions for such actions.

- This program uses `pyautogui` for controlling the cursor. Make sure it is installed (`pip install pyautogui`) and compatible with your Python environment.

## License

This project is licensed under the MIT License.