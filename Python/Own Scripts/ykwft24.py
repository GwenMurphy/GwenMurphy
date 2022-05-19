import time, datetime
##import pyautogui as pg

tn = datetime.datetime.now()

def one():
    tn = datetime.datetime.now()
    hr, min, sec = tn.hour, tn.minute, tn.second
    if sec == 24:
        print(f'{hr:02d}:{min:02d}:{sec:02d} - You know what\'s funnier than 24?')
    elif sec == 25:
        print(f'{hr:02d}:{min:02d}:{sec:02d} - {sec}')
        time.sleep(10)
    if sec != 24 and sec != 25:
        print(f'{hr:02d}:{min:02d}:{sec:02d}')
    time.sleep(1)
    
for d in range(1, 100):
    ##### Doing it for the meme.
    one()