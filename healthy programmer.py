
# 9am - 5pm
# Water - water.mp3 (3.5 litres) - Drank - log - Every 40 min
# Eyes - eyes.mp3 - every 30 min - EyDone - log - Every 30 min
# Physical activity - physical.mp3 every - 45 min - ExDone - log
# Rules
# Pygame module to play audio
print("Welcome to healthy Program")
from pygame import mixer
from datetime import datetime
from time import time
def musiconloop(file,stopper):
    mixer.init()
    mixer.music.load("F:\\new.mp3")
    mixer.music.play()
    while True:
        a = input()
        if a==stopper:
            mixer.music.stop()
            print("music has been stopped!!!")
            break
def log(msg):
    with open("mylogs.txt","a") as f:
        f.write(f"{msg} : {datetime.now() } \n")
if __name__ == '__main__':
   # musiconloop("water.mp3","stop")
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    watersecs = 10*60 # minutes
    eyesecs = 20*60   # minutes
    exesecs = 30*60   # minutes
    while True:
        if time() - init_water>watersecs:
            print("water drinking time!!!","Type drank to stop the alarm")
            musiconloop("water.mp3","drank")
            log("water drank at")
        if time() - init_eyes>eyesecs:
            print("eyes washing time!!!","Type washed to stop the alarm")
            musiconloop("eyes.mp3","washed")
            log("eyes washed at")
        if time() - init_exercise>exesecs:
            print(" exercise time!!!","Type done to stop the alarm")
            musiconloop("exercise.mp3","done")
            log("exercise done at")




