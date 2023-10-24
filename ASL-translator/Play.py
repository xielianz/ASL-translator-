import pygame
import sys
from pygame.locals import *

# Initialize Pygame
pygame.init()

WIDTH, HEIGHT = 1280, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Play Screen")

play_screen = True  # We start on the Play screen

image_dict = {
    "A": pygame.image.load("ASL-translator/play_images/A.png"),
    "B": pygame.image.load("ASL-translator/play_images/B.png"),
    "C": pygame.image.load("ASL-translator/play_images/C.png"),
    "D": pygame.image.load("ASL-translator/play_images/D.png"),
    "E": pygame.image.load("ASL-translator/play_images/E.png"),
    "F": pygame.image.load("ASL-translator/play_images/F.png"),
    "G": pygame.image.load("ASL-translator/play_images/G.png"),
    "H": pygame.image.load("ASL-translator/play_images/H.png"),
    "I": pygame.image.load("ASL-translator/play_images/I.png"),
    "J": pygame.image.load("ASL-translator/play_images/J.png"),
    "K": pygame.image.load("ASL-translator/play_images/K.png"),
    "L": pygame.image.load("ASL-translator/play_images/L.png"),
    "M": pygame.image.load("ASL-translator/play_images/M.png"),
    "N": pygame.image.load("ASL-translator/play_images/N.jpg"),
    "O": pygame.image.load("ASL-translator/play_images/O.png"),
    "P": pygame.image.load("ASL-translator/play_images/P.png"),
    "Q": pygame.image.load("ASL-translator/play_images/Q.png"),
    "R": pygame.image.load("ASL-translator/play_images/R.png"),
    "S": pygame.image.load("ASL-translator/play_images/S.png"),
    "T": pygame.image.load("ASL-translator/play_images/T.png"),
    "U": pygame.image.load("ASL-translator/play_images/U.png"),
    "V": pygame.image.load("ASL-translator/play_images/V.png"),
    "W": pygame.image.load("ASL-translator/play_images/W.png"),
    "X": pygame.image.load("ASL-translator/play_images/X.png"),
    "Y": pygame.image.load("ASL-translator/play_images/Y.png"),
    "Z": pygame.image.load("ASL-translator/play_images/Z.png"),
}

current_letter = "A"  # Start with letter "A"

def change_letter(key):
    global current_letter
    if key in image_dict:
        current_letter = key

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.unicode.isalpha():
                change_letter(event.unicode.upper())

    if play_screen:
        # Display the Play screen with the current letter's image
        screen.fill((255, 255, 255))
        image = image_dict.get(current_letter, pygame.Surface((100, 100)))
        image_rect = image.get_rect()
        image_rect.center = (WIDTH // 2, HEIGHT // 2)  # Center the image on the screen
        screen.blit(image, image_rect)
        pygame.display.flip()
