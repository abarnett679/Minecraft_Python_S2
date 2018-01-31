def getWoolState(color):
    if color == "pink":
        blockState = 6

colorString = input("Enter a block color: ")
state = getWoolState(colorString)

pos = mc.player.getTilePos()
mc.setBlock(pos.x, pos,y, pos.z, 35, state
