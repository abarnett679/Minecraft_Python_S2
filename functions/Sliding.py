from mcpi.minecraft import Minecraft
mc = Minecraft.creat()

import random
import time

while True:
    x += random.uniform(-0.2, 0.2)
    z +=
    y = mc.getHeight(x, z)

    mc.player.setPos(x, y, z)
    time.sleep(0.1)
