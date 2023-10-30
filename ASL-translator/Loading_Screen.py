import pygame
import sys
import Button
import os


pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("ASL-translator/assets/Background.png")

def get_font(size):
    return pygame.font.Font("ASL-translator/assets/font.ttf",size)

def play():
	path_to_file = os.path.join('ASL-translator', 'Play.py')
	os.system(f'python "{path_to_file}"')

LEARN_BUTTON = None

# Learn screen
def learn(): 
    pygame.display.set_caption("Learn")

    while True:
        LEARN_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        LEARN_TEXT = get_font(45).render("ASL Translator", True, "White")
        LEARN_RECT = LEARN_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(LEARN_TEXT, LEARN_RECT)

        LEARN_BACK = Button(image=None, pos=(640, 460),
                           text_input ="BACK", font=get_font(75), base_color="white", hovering_color="Green")
        
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
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        TEST_BACK.changeColor(TEST_MOUSE_POS)
        TEST_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if TEST_BACK.checkForInput(TEST_MOUSE_POS):
                    main_menu()

        pygame.display.update()

# main menu screen
def main_menu():
    pygame.display.set_caption("Menu")

    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        LEARN_BUTTON = Button(image=pygame.image.load("ASL-translator/assets/Learn Rect.png"), pos=(640,250),
                            text_input="LEARN", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        TEST_BUTTON = Button(image=pygame.image.load("ASL-translator/assets/Testing Rect.png"), pos=(640,400),
                            text_input="TESTING", font=get_font(75), base_color="#d7fcd4",hovering_color="White")
        QUIT_BUTTON =  Button(image=pygame.image.load("ASL-translator/assets/Quit Rect.png"), pos=(640,550),
                            text_input="SIGN", font=get_font(75), base_color="#d7fcd4",hovering_color="White")
        
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
                    learn()
                if TEST_BUTTON.checkForInput(MENU_MOUSE_POS):
                    test()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
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
