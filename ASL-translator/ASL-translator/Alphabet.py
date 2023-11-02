import pygame
import sys
import random
from pygame.locals import *
import RPi.GPIO as GPIO

# Initialize Pygame
pygame.init()

GPIO.setmode(GPIO.BCM)
LED_PIN_RIGHT = 17
LED_PIN_WRONG = 18
GPIO.setup(LED_PIN_RIGHT, GPIO.OUT)
GPIO.setup(LED_PIN_WRONG, GPIO.OUT)

WIDTH, HEIGHT = 1280, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Alphabet Testing")

# Load ASL sign images for letters
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

# Set up the font
font = pygame.font.Font("ASL-translator/assets/font.ttf", 36)
large_font = pygame.font.Font("ASL-translator/assets/font.ttf", 68)

GPIO.output(LED_PIN_RIGHT, GPIO.LOW)
GPIO.output(LED_PIN_WRONG, GPIO.LOW)

current_letter = random.choice(list(image_dict.keys()))

# Track the user's input and highest streak
user_input = ""
current_streak = 0
highest_streak = 0
wrong_message = ""
wrong_message_time = 0

# Main loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.key == K_BACKSPACE:    
                # Handle backspace: remove the last character from user_input
                user_input = user_input[:-1]
            elif event.unicode.isalpha():
                user_input += event.unicode.upper()
            elif event.key == K_RETURN:
                if user_input == current_letter:
                    current_streak += 1
                    if current_streak > highest_streak:
                        highest_streak = current_streak
                    user_input = ""  # Reset user input on correct answer
                    GPIO.output(LED_PIN_RIGHT, GPIO.HIGH)
                    pygame.time.delay(500)
                    GPIO.output(LED_PIN_RIGHT, GPIO.LOW)
                    current_letter = random.choice(list(image_dict.keys()))
                else:
                    current_streak = 0
                    user_input = ""
                    wrong_message = "Wrong, Try Again"
                    wrong_message_time = pygame.time.get_ticks()
                    GPIO.output(LED_PIN_WRONG, GPIO.HIGH)
                    pygame.time.delay(500)
                    GPIO.output(LED_PIN_WRONG, GPIO.LOW)

    screen.fill((255, 255, 255))

    # Display the current letter sign
    image = image_dict.get(current_letter, pygame.Surface((300, 400)))
    image_rect = image.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
    screen.blit(image, image_rect)

    # Display the user's input
    input_text = font.render("Your Input: " + user_input, True, (0, 0, 0))
    screen.blit(input_text, (10, 10))

    # Display the current streak
    current_streak_text = font.render("Current Streak: " + str(current_streak), True, (0, 0, 255))
    screen.blit(current_streak_text, (10, 90))

    # Display the highest streak
    streak_text = font.render("Highest Streak: " + str(highest_streak), True, (0, 128, 0))
    screen.blit(streak_text, (10, 50))

    # Display the wrong message if not empty and less than one second has passed
    if wrong_message and pygame.time.get_ticks() - wrong_message_time < 1000:
        wrong_message_text = large_font.render(wrong_message, True, (255, 0, 0))
        screen.blit(wrong_message_text, (WIDTH // 2 - 550, HEIGHT // 2 + 30))
    else:
        wrong_message = ""  # Reset the wrong message if one second has passed

    pygame.display.flip()

GPIO.cleanup() 

pygame.quit()
sys.exit()
