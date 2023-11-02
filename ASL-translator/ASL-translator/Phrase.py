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
pygame.display.set_caption("Baisc Phrase Testing")
# Load images and corresponding words
image_word_pairs = {
    "goodbye": pygame.image.load("ASL-translator/play_images/Goodbye.jpg"),
    "hello": pygame.image.load("ASL-translator/play_images/Hello.jpg"),
    "please": pygame.image.load("ASL-translator/play_images/please.jpg"),
    "what": pygame.image.load("ASL-translator/play_images/what.jpg"),
    "yes": pygame.image.load("ASL-translator/play_images/yes.jpg"),
    "no": pygame.image.load("ASL-translator/play_images/no.jpg"),
}

# Load images and corrensponding words with hints
image_word_hint_pairs = {
    "goodbye": {"image": pygame.image.load("ASL-translator/play_images/Goodbye.jpg"), "hint": "This word starts with the letter G"},
    "hello": {"image": pygame.image.load("ASL-translator/play_images/Hello.jpg"), "hint": "This word starts with the letter H"},
    "please": {"image": pygame.image.load("ASL-translator/play_images/please.jpg"), "hint": "This word starts with the letter P"},
    "what": {"image": pygame.image.load("ASL-translator/play_images/what.jpg"), "hint": "This word starts with the letter W"},
    "yes": {"image": pygame.image.load("ASL-translator/play_images/yes.jpg"), "hint": "This word starts with the letter Y"},
    "no": {"image": pygame.image.load("ASL-translator/play_images/no.jpg"), "hint": "This word starts with the letter N"},
}

# Set up the font
font = pygame.font.Font("ASL-translator/assets/font.ttf",36)
large_font = pygame.font.Font("ASL-translator/assets/font.ttf", 68)
small_font = pygame.font.Font("ASL-translator/assets/font.ttf", 33) 

GPIO.output(LED_PIN_RIGHT, GPIO.LOW)
GPIO.output(LED_PIN_WRONG, GPIO.LOW)

# Select a random word from the list
current_word, current_image = random.choice(list(image_word_pairs.items()))

# Track the user's input and score
user_input = ""
current_streak = 0
highest_streak = 0
wrong_message = ""
wrong_message_time = 0
hint_message = ""

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
                if user_input.lower() == "hint":
                    # shows hint for current phrase
                    hint_message = image_word_hint_pairs[current_word]["hint"]
                    hint_message_request = "Hint: {}".format(hint_message)
                    wrong_message_time = pygame.time.get_ticks()
                    user_input = "" # Reset user input after displaying the hint
                # Check if the user's input matches the current word
                elif user_input.lower() == current_word:
                        current_streak += 1
                        if current_streak > highest_streak:
                            highest_streak = current_streak
                        user_input = ""  # Reset user input on correct answer
                        hint_message = "" # Reset the hint message on correct answer
                        GPIO.output(LED_PIN_RIGHT, GPIO.HIGH)
                        pygame.time.delay(500)
                        GPIO.output(LED_PIN_RIGHT, GPIO.LOW)
                        current_word, current_image = random.choice(list(image_word_hint_pairs.items()))
                        # Select a new random word and image
                        current_word, current_image = random.choice(list(image_word_pairs.items()))
                else:
                    current_streak = 0
                    user_input = ""
                    wrong_message = "Wrong, Try Again"
                    wrong_message_time = pygame.time.get_ticks()
                    GPIO.output(LED_PIN_WRONG, GPIO.HIGH)
                    pygame.time.delay(500)
                    GPIO.output(LED_PIN_WRONG, GPIO.LOW)

    screen.fill((255, 255, 255))

    # Display the current image
    image_rect = current_image.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
    screen.blit(current_image, image_rect)

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

    # Display the hint message if available
    if hint_message:
        hint_text = small_font.render(hint_message, True, (255, 0, 0))
        screen.blit(hint_text, (WIDTH // 2 - 550, HEIGHT // 2 + 30))
    else:
        hint_message = ""


    pygame.display.flip()

GPIO.cleanup()    

pygame.quit()
sys.exit()
