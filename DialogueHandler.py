import pygame
import sys
from assets.Code import Settings

def drawDialogueScreen(screen, texts):
    clock = pygame.time.Clock()
    for text in texts:
        screen.blit(Settings.DIALOGUE_SCREEN, (0, 0))
        screen.blit(Settings.DIALOGUE_FONT.render(text, False, (200, 200, 200)), (10, 10))
        pygame.display.update()
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        run = False
                        pygame.quit()
                        sys.exit()
                    elif event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                        run = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    run = False

            clock.tick(10)
