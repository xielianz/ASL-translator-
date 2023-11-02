import pygame, sys
import Button
from pygame.locals import *
import os


pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("ASL-translator/assets/Background.png")

def get_font(size):
    return pygame.font.Font("ASL-translator/assets/font.ttf",size)

def play():
	path_to_file = os.path.join("ASL-translator", "Play.py")
	os.system('python "{}"'.format(path_to_file))
     
def testing():
	path_to_file = os.path.join("ASL-translator", "Testing.py")
	os.system('python "{}"'.format(path_to_file))

LEARN_BUTTON = None

# Learn screen
def learn(): 
    pygame.display.set_caption("Learn")

    while True:
        LEARN_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        LEARN_TEXT = get_font(45).render("ASL Translator", True, (225,225,225))
        LEARN_RECT = LEARN_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(LEARN_TEXT, LEARN_RECT)

        LEARN_BACK = Button(image=None, pos=(640, 460),
                           text_input ="BACK", font=get_font(75), base_color=(225,225,225), hovering_color=(215,252,212))
        
        LEARN_BACK.changeColor(LEARN_MOUSE_POS)
        LEARN_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if LEARN_BACK.checkForInput(LEARN_MOUSE_POS):
                    main_menu()
                if LEARN_BUTTON.checkForInput(LEARN_MOUSE_POS):
                    play()

        pygame.display.update()


# testing menu
def test():
    while True:
        TEST_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        TEST_TEXT = get_font(45).render("This is the TESTING screen.", True, "Black")
        TEST_RECT = TEST_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(TEST_TEXT, TEST_RECT)

        TEST_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color=(0,0,0), hovering_color=(215,252,212))

        TEST_BACK.changeColor(TEST_MOUSE_POS)
        TEST_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if TEST_BACK.checkForInput(TEST_MOUSE_POS):
                    main_menu()
                if TEST_BUTTON.checkForInput(TEST_MOUSE_POS):
                    testing()

        pygame.display.update()

# main menu screen
def main_menu():
    pygame.display.set_caption("Menu")

    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(80).render("ASL-TRANSLATOR", True, (182,143,64))
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        LEARN_BUTTON = Button(image=pygame.image.load("ASL-translator/assets/Learn Rect.png"), pos=(640,250),
                            text_input="LEARN", font=get_font(75), base_color=(215,252,212), hovering_color=(225,225,225))
        TEST_BUTTON = Button(image=pygame.image.load("ASL-translator/assets/Testing Rect.png"), pos=(640,400),
                            text_input="TESTING", font=get_font(75), base_color=(215,252,212),hovering_color=(225,225,225))
        QUIT_BUTTON =  Button(image=pygame.image.load("ASL-translator/assets/Quit Rect.png"), pos=(640,550),
                            text_input="SIGN", font=get_font(75), base_color=(215,252,212),hovering_color=(225,225,225))
        
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [LEARN_BUTTON, TEST_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if LEARN_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if TEST_BUTTON.checkForInput(MENU_MOUSE_POS):
                    testing()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    testing()    #PlAVE HOLDER< NOT ACTUALLY TESTING!!!

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
