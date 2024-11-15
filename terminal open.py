import os
import subprocess
import sys

def open_terminal():
    # Check the operating system
    if sys.platform == 'win32':
        # For Windows, use 'start' command to open a new terminal window
        subprocess.run(['start', 'cmd', '/K', 'python', 'runner.py'], shell=True)
    elif sys.platform == 'darwin' or sys.platform.startswith('linux'):
        # For Linux/macOS, use 'gnome-terminal' or 'xterm' (common Linux terminal)
        # Adjust this for your preferred terminal
        subprocess.run(['gnome-terminal', '--', 'python3', 'runner.py'])
        # If 'gnome-terminal' is unavailable, try 'xterm' instead
        # subprocess.run(['xterm', '-e', 'python3', 'runner.py'])
    else:
        print("Unsupported OS. Please open a terminal manually.")

def main():
    print("Opening an interactive Lua terminal...")
    open_terminal()

if __name__ == '__main__':
    main()
