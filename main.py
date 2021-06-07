import pyautogui, sys
import keyboard
from time import sleep
from os import system


def menu():
    print("Valid choices: ")
    print("Record strokes - r")
    print("Apply strokes - a")
    print("Exit - e")
    print()


system("clear")
menu()
dng = True
while dng:
    choice = input()
    if choice == "e":
        print("Exited")
        break
    elif choice == "r":
        pos = []
        print("press w for recording a position")
        while True:
            if keyboard.is_pressed('w'):
                x, y = pyautogui.position()
                pos.append([x, y])
                print()
                sleep(0.5)
            if keyboard.is_pressed('del'):
                print()
                print(len(pos))
                for i in pos:
                    print("{}, {}".format(i[0], i[1]))
                dng = False
                break
    elif choice == "a":
        print("Input the coordinates: ")
        coords = []
        l = int(input())
        for i in range(l):
            ln = list(map(int, input().split(", ")))
            coords.append(ln)
        print("press q to start drawing...")
        while True:
            if keyboard.is_pressed('q'):
                for c in coords:
                    pyautogui.moveTo(c[0], c[1])
                    # pyautogui.click(x=c[0], y=c[1])
                break
        dng = False
    else:
        menu()
