import pygame
import math
from assets.Code import Settings, worldMap, ObjectHandler

def checkObjects(entity, isPlayer=False):
    entityHitbox = entity.hitbox.move(Settings.WorldMapStartingX + entity.worldX, Settings.WorldMapStartingY + entity.worldY)
    entityLeftCol = math.floor((entity.worldX + entity.hitbox.left)/Settings.TILESIZE)
    entityRightCol = math.floor((entity.worldX + entity.hitbox.right)/Settings.TILESIZE)
    entityTopRow = math.floor((entity.worldY + entity.hitbox.top)/Settings.TILESIZE)
    entityBottomRow = math.floor((entity.worldY + entity.hitbox.bottom)/Settings.TILESIZE)
    tile1 = tile2 = tile3 = tile4 = 10

    match entity.direction:
        case 'D':
            entityHitbox.move_ip(0, entity.vel)
            entityBottomRow = math.floor((entity.worldY + entity.hitbox.bottom + entity.getCurrentVelY())/Settings.TILESIZE)
            tile1 = worldMap.worldMap[entityBottomRow][entityLeftCol]
            tile2 = worldMap.worldMap[entityBottomRow][entityRightCol]
        case 'DR':
            entityHitbox.move_ip(entity.vel*0.707, entity.vel*0.707)
            entityBottomRow = math.floor((entity.worldY + entity.hitbox.bottom + entity.getCurrentVelY()*0.707)/Settings.TILESIZE)
            entityRightCol = math.floor((entity.worldX + entity.hitbox.right + entity.getCurrentVelX()*0.707)/Settings.TILESIZE)
            tile1 = worldMap.worldMap[entityTopRow][entityLeftCol]
            tile2 = worldMap.worldMap[entityTopRow][entityRightCol]
            tile3 = worldMap.worldMap[entityBottomRow][entityLeftCol]
            tile4 = worldMap.worldMap[entityBottomRow][entityRightCol]
        case 'DL':
            entityHitbox.move_ip(-entity.vel*0.707, entity.vel*0.707)
            entityBottomRow = math.floor((entity.worldY + entity.hitbox.bottom + entity.getCurrentVelY()*0.707)/Settings.TILESIZE)
            entityLeftCol = math.floor((entity.worldX + entity.hitbox.left - entity.getCurrentVelX()*0.707)/Settings.TILESIZE)
            tile1 = worldMap.worldMap[entityTopRow][entityLeftCol]
            tile2 = worldMap.worldMap[entityTopRow][entityRightCol]
            tile3 = worldMap.worldMap[entityBottomRow][entityLeftCol]
            tile4 = worldMap.worldMap[entityBottomRow][entityRightCol]
        case 'U':
            entityHitbox.move_ip(0, -entity.vel)
            entityTopRow = math.floor((entity.worldY + entity.hitbox.top - entity.getCurrentVelY())/Settings.TILESIZE)
            tile1 = worldMap.worldMap[entityTopRow][entityLeftCol]
            tile2 = worldMap.worldMap[entityTopRow][entityRightCol]
        case 'UR':
            entityHitbox.move_ip(entity.vel*0.707, -entity.vel*0.707)
            entityTopRow = math.floor((entity.worldY + entity.hitbox.top - entity.getCurrentVelY()*0.707)/Settings.TILESIZE)
            entityRightCol = math.floor((entity.worldX + entity.hitbox.right + entity.getCurrentVelX()*0.707)/Settings.TILESIZE)
            tile1 = worldMap.worldMap[entityTopRow][entityLeftCol]
            tile2 = worldMap.worldMap[entityTopRow][entityRightCol]
            tile3 = worldMap.worldMap[entityBottomRow][entityLeftCol]
            tile4 = worldMap.worldMap[entityBottomRow][entityRightCol]
        case 'UL':
            entityHitbox.move_ip(-entity.vel*0.707, -entity.vel*0.707)
            entityTopRow = math.floor((entity.worldY + entity.hitbox.top - entity.getCurrentVelY()*0.707)/Settings.TILESIZE)
            entityLeftCol = math.floor((entity.worldX + entity.hitbox.left - entity.getCurrentVelX()*0.707)/Settings.TILESIZE)
            tile1 = worldMap.worldMap[entityTopRow][entityLeftCol]
            tile2 = worldMap.worldMap[entityTopRow][entityRightCol]
            tile3 = worldMap.worldMap[entityBottomRow][entityLeftCol]
            tile4 = worldMap.worldMap[entityBottomRow][entityRightCol]
        case 'R':
            entityHitbox.move_ip(entity.vel, 0)
            entityRightCol = math.floor((entity.worldX + entity.hitbox.right + entity.getCurrentVelX())/Settings.TILESIZE)
            tile1 = worldMap.worldMap[entityTopRow][entityRightCol]
            tile2 = worldMap.worldMap[entityBottomRow][entityRightCol]
        case 'L':
            entityHitbox.move_ip(-entity.vel, 0)
            entityLeftCol = math.floor((entity.worldX + entity.hitbox.left - entity.getCurrentVelX())/Settings.TILESIZE)
            tile1 = worldMap.worldMap[entityTopRow][entityLeftCol]
            tile2 = worldMap.worldMap[entityBottomRow][entityLeftCol]

    if 11 in [tile1, tile2, tile3, tile4]:
        entity.colliding = True
    
    for obj in ObjectHandler.Objects:
        objHitbox = obj.hitbox.move(Settings.WorldMapStartingX + obj.worldX, Settings.WorldMapStartingY + obj.worldY)
        if objHitbox.colliderect(entityHitbox):
            if isPlayer:
                obj.onCollision()
                if pygame.key.get_pressed()[pygame.K_e]:
                    obj.onInteraction()
                
            if obj.solid:
                entity.colliding = True

def isSpawnable(entity):
    entityLeftCol = math.floor((entity.worldX + entity.hitbox.left)/Settings.TILESIZE)
    entityRightCol = math.floor((entity.worldX + entity.hitbox.right)/Settings.TILESIZE)
    entityTopRow = math.floor((entity.worldY + entity.hitbox.top)/Settings.TILESIZE)
    entityBottomRow = math.floor((entity.worldY + entity.hitbox.bottom)/Settings.TILESIZE)
    entityHitbox = entity.hitbox.move(entity.worldX, entity.worldY)

    spawnable1 = spawnable2 = spawnable3 = spawnable4 = spawnable5 = False
    
    if entityLeftCol >= 0 and entityTopRow >= 0 and entityBottomRow < len(worldMap.worldMap):
        if entityRightCol < len(worldMap.worldMap[entityTopRow]):
            tile1 = worldMap.worldMap[entityTopRow][entityLeftCol]
            tile2 = worldMap.worldMap[entityTopRow][entityRightCol]
            tile3 = worldMap.worldMap[entityBottomRow][entityLeftCol]
            tile4 = worldMap.worldMap[entityBottomRow][entityRightCol]

            if tile1 in entity.getSpawnableTiles() and tile2 in entity.getSpawnableTiles() and tile3 in entity.getSpawnableTiles() and tile4 in entity.getSpawnableTiles():
                for obj in ObjectHandler.Objects:
                    objHitbox = obj.hitbox.move(obj.worldX, obj.worldY)
                    if objHitbox.colliderect(entityHitbox):
                        return False
                return True
    return False
