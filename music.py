import pygame

def play_usual_music():
    pygame.mixer.init()  # Initialize the mixer module
    pygame.mixer.music.load('C:/Users/Emir/PycharmProjects/termProject/sounds/b2.mp3')
    pygame.mixer.music.play(-1)

def play_boss_music():
    pygame.mixer.init()  # Initialize the mixer module
    pygame.mixer.music.load('C:/Users/Emir/PycharmProjects/termProject/sounds/a.mp3')
    pygame.mixer.music.play(-1)

def stop_music():
    pygame.mixer.init()  # Initialize the mixer module
    pygame.mixer.music.stop()
