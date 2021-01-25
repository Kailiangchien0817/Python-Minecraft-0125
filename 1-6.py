from mcpi.minecraft import Minecraft 
LC = Minecraft.create()

LC.postToChat("I'm watching you")

while True:
    x,y,z=LC.player.getTilePos()
    LC.postToChat("X:"+str(x)+"Y:"+str(y)+"Z"+str(z))