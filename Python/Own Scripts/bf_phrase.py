import time

text = ""
target = "hello world"
for i in range(len(target)):
    character = " "
    while character != target[i]:
        character = ord(character) + 1
        character = chr(character)
        print(f"{text}{character}", end="\r")
        time.sleep(0.005)
    text += character
print(end="\n")
print("ACCESS GRANTED")

time.sleep(2)
print("Were in.")