from mcpi.minecraft import Minecraft 
import time
LC = Minecraft.create()

x=200
y=200
z=100

LC.player.setTilePos(x,y,z)
time.sleep(2)

x=x-50
y=y-50

LC.player.setTilePos(x,y,z)
time.sleep(2)

x=x-50
y=y-50

LC.player.setTilePos(x,y,z)
