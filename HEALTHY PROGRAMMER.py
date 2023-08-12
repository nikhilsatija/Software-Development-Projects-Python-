"""
Program: Assume that a programmer works at the office from 9-5 pm. We have to take care of his health and remind him three things-
1) To drink a total of 3.5-liter water after some time interval between 9-5 pm.
2) To do eye exercise after every 30 minutes.
3) To perform physical activity after every 45 minutes.

Instructions: The task is to create a program that plays mp3 audio(Use pygame module to play audio) until the programmer enters the input which implies that he has done the task.
1) For Water, the user should enter “Drank”
2) For Eye Exercise, the user should enter “EyeDone”
3) For Physical Exercise, the user should enter “ExDone”

After the user entered the input, a file should be created for every task separately, which contains the details about the time when the user performed a certain task.

My Edit:-
Drink Water -> 2-litre - after every 62 mins. of interval - 250ml glass * 8 hrs = 2l
Eye Exercise  -> after every 64 mins. of interval
Physical Activity -> after every 120 mins. of interval
"""

from pygame import mixer
from datetime import datetime
from time import time

def play_alarm(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()

    while True:
        user_input = input()
        if user_input == stopper:
            mixer.music.stop()
            break

def logs(log_msg):
    with open("Exercise-7 (HEALTHY PROGRAMMER).txt", "a") as f:
        f.write(f"{log_msg} {datetime.now()}")

if __name__ == '__main__':

    init_drink_water_time = time()
    init_eye_exercise_time = time()
    init_physical_activity_time = time()

    drink_water_time_interval = 62*60
    eye_exercise_time_interval = 64*60
    physical_activity_time_interval = 120*60

    while True:

        if time() - init_drink_water_time > drink_water_time_interval:
            print("\nDrink Water Time.\nEnter 'w' to log the time : ")
            play_alarm("PROJECT FILES/MP3/drink_water.mp3", "w")
            init_drink_water_time = time()
            logs(f"\nYou drank water at")

        if time() - init_eye_exercise_time > eye_exercise_time_interval:
            print("\nEye Exercise Time.\nEnter 'e' to log the time : ")
            play_alarm("PROJECT FILES/MP3/do_eye_exercise.mp3", "e")
            init_eye_exercise_time = time()
            logs(f"\nYou relaxed your eyes at")

        if time() - init_physical_activity_time > physical_activity_time_interval:
            print("\nPhysical Activity Time.\nEnter 'p' to log the time : ")
            play_alarm("PROJECT FILES/MP3/do_physical_activity.mp3", "p")
            init_physical_activity_time = time()
            logs(f"\nYou did Physical Activity at")