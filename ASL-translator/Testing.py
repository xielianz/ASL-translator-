import pygame
import sys
from pygame.locals import *
import os

pygame.init()

WIDTH, HEIGHT = 1280, 720
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menu")

BG = pygame.image.load("ASL-translator/assets/Background.png")

def get_font(size):
    return pygame.font.Font("ASL-translator/assets/font.ttf", size)

def words():
    path_to_file = os.path.join("ASL-translator", "Words.py")
    os.system('python "{}"'.format(path_to_file))    

def alphabet():
    path_to_file = os.path.join("ASL-translator", "Alphabet.py")
    os.system('python "{}"'.format(path_to_file))

def phrase():
    path_to_file = os.path.join("ASL-translator", "Phrase.py")
    os.system('python "{}"'.format(path_to_file))

# Main menu screen
def main_menu():
    pygame.display.set_caption("Testing Menu")

    while True:
       

        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("TESTING", True, (182,143,64))
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        BASIC_PHRASE_BUTTON = Button(image=None, pos=(650, 575),
                            text_input="BASIC PHRASES", font=get_font(75), base_color=(225,225,225), hovering_color=(215,252,212))
        WORD_SEQUENCE_BUTTON = Button(image=None, pos=(650, 425),
                            text_input="WORD SEQUENCE", font=get_font(75), base_color=(225,225,225), hovering_color=(215,252,212))
        ALPHABET_BUTTON = Button(image=None, pos=(650, 275), 
                            text_input="ALPHABET", font=get_font(75), base_color=(225,225,225), hovering_color=(215,252,212))
        
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [BASIC_PHRASE_BUTTON, WORD_SEQUENCE_BUTTON, ALPHABET_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BASIC_PHRASE_BUTTON.checkForInput(MENU_MOUSE_POS):
                    phrase()  
                if WORD_SEQUENCE_BUTTON.checkForInput(MENU_MOUSE_POS):
                    words()
                if ALPHABET_BUTTON.checkForInput(MENU_MOUSE_POS):
                    alphabet()
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE or event.key == K_q:
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

class Button():
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)

main_menu()