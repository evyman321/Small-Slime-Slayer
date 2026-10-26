from assets.Code import Settings, Object, Tree, NPC
    
Objects = []
def setObjects(screen):
    global Objects
    Objects.append(Tree.Tree(40*Settings.TILESIZE, 52*Settings.TILESIZE))
    Objects.append(Tree.Tree(76*Settings.TILESIZE, 110*Settings.TILESIZE))
    Objects.append(NPC.NPC(62*Settings.TILESIZE, 68*Settings.TILESIZE, screen))
