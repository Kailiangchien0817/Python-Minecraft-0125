from mcpi.minecraft import Minecraft 
LC = Minecraft.create()

x=200
y=100
z=300

LC.player.setTilePos(x,y,z)

y=150

#time.sleep(2)
LC.player.setTilePos(x,y,z)
#time.sleep(2)

y=200

LC.player.setTilePos(x,y,z)
