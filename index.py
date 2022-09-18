from pygame import mixer
from tkinter import *

# snipet for the GUI

root = Tk()
root.geometry("600x300")

mixer.init()
mixer.music.load("filename.mp3")


def pause():
    mixer.music.pause()


def play():
    mixer.music.play()


def resume():
    mixer.music.unpause()


Label(root, text="Welcome to simvic mp3 player", font="lucidia 20 bold").pack()
Button(text="Play", command=play).place(x=200, y=100)
Button(text="Pause", command=pause).place(x=250, y=100)
Button(text="Resume", command=resume).place(x=310, y=100)
Button(text="Quit", command=quit).place(x=380, y=100)

root.mainloop()


# Cod for the simple program


import pygame
from pygame import mixer

pygame.init()
mixer.init()
screen = pygame.display.set_mode((600, 400))
mixer.music.load("filename.mp3")
mixer.music.play()

print("Press 'p' to pause 'r' to resume")
print("Press 'q' to quit")
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                mixer.music.pause()
            if event.key == pygame.K_r:
                mixer.music.unpause()
            if event.key == pygame.K_q:
                running = False
quit()