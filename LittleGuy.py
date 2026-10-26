import pygame
import sys
from assets.Code import Settings, worldMap, TileManager, ObjectHandler, EnemyHandler, Player, DialogueHandler

pygame.init()

screen = pygame.display.set_mode((Settings.SCREEN_WIDTH, Settings.SCREEN_HEIGHT))

entities = []
player = Player.Player(entities)
enemyHandler = EnemyHandler.EnemyHandler()
ObjectHandler.setObjects(screen)
entities += [obj for obj in ObjectHandler.Objects]
entities.append(player)
clock = pygame.time.Clock()
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

    screen.fill('black')
    
    screenX = 0
    screenY = 0
    for i in worldMap.worldMap:
        for j in i:
            screen.blit(TileManager.Tiles[j], (Settings.WorldMapStartingX + screenX, Settings.WorldMapStartingY + screenY))
            screenX += Settings.TILESIZE
        screenX = 0
        screenY += Settings.TILESIZE

    for entity in entities:
        if entity:
            entity.update()
        else:
            entities.remove(entity)
        
    entities.sort(key=lambda entity: entity.worldY + entity.image.get_height())
    for entity in entities:
        if entity:
            entity.draw(screen)

    player.drawHealthBar(screen)
    killCounter = Settings.DIALOGUE_FONT.render(f"Kills:{player.kills}", False, (200, 200, 200))
    screen.blit(killCounter, (10, 10))
    for bullet in player.bullets:
        bullet.update()
        bullet.draw(screen)

    if player.win:
        DialogueHandler.drawDialogueScreen(screen, ["Well Done!", "You Succeeded!", "I Never Believed In You!", "No One Did!", "I'm Sorry!", "I Had Underestimated You!"])
        run = False
        pygame.quit()
        sys.exit()
        
    elif player.lose:
        DialogueHandler.drawDialogueScreen(screen, ["I Knew It!", "I Knew That U Would Never\n Amount To Anything In Life!", "And Now, You Have Died!", "I Tried To Warn You!", "Goodbye!"])
        run = False
        pygame.quit()
        sys.exit()

    enemyHandler.spawnNewEnemy(entities, player)
    pygame.display.update()
    clock.tick(Settings.FPS)
