from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time

heights = [100, 0]
count = 0

highest = 0

while count < 5:
    pos = mc.player.getTilePos()

    
    if pos.y < heights[0]:
        lowest = pos.y
    elif pos.y > heights[1]:
        highest = pos.y

    
    count += 1
    time.sleep(1)
    mc.postToChat("Time passed (seconds): " + str(count))

mc.postToChat("Lowest: " + str(lowest))
mc.postToChat("Highest: " + str(highest))
