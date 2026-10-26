from assets.Code import Settings, CollisionChecker, HappySlime

class EnemyHandler:
    def __init__(self):
        self.HappySlimeSpawnFrequency = Settings.FPS*5
        self.MadSlimeSpawnFrequency = Settings.FPS*15
        self.HappySlimeCounter = 0
        self.MadSlimeCounter = 0
        self.enemies = []
        self.spawned1 = False

    def spawnNewEnemy(self, entities, player):
        if not self.spawned1:
            happySlime = HappySlime.HappySlime(player)
            happySlime.worldX = player.worldX
            happySlime.worldY = player.worldY + 50
            self.spawned1 = True
            
        self.HappySlimeCounter += 1
        self.MadSlimeCounter += 1
        if self.HappySlimeCounter >= self.HappySlimeSpawnFrequency:
            happySlime = HappySlime.HappySlime(player)
            if CollisionChecker.isSpawnable(happySlime):
                entities.append(happySlime)
                self.enemies.append(happySlime)

            self.HappySlimeCounter = 0

        if self.MadSlimeCounter >= self.MadSlimeSpawnFrequency:
            pass

        for enemy in self.enemies:
            if not enemy.alive:
                self.enemies.remove(enemy)
                entities.remove(enemy)
