from mcpi.minecraft import Minecraft
mc = minecraft.creat()

import time

pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z
mc.setblock(x, y - 1, z, 103)
time.sleep(10)

pos = mc.player.getPos()
x = pos.x
y = pos.y -1
z = pos.z
mc.setblock(x, y - 1, z, 103)
time.sleep(10)

pos = mc.player.getPos()
x = pos.x
y = pos.y - 1
z = pos.z
mc.setblock(x, y - 1, z, 103)
time.sleep(10)
