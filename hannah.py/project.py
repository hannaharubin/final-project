# 6/10/25 Hannah Rubin
import random
import uvage
image_number=0
walker_image=uvage.load_sprite_sheet("run.png")
fly_image=uvage.load_sprite_sheet("fly.png")
background=uvage.display.set_mode((800,600))
def tick():
    if uvage.is_pressing("up"):
        image_number+=1
    player_icon.image=fly_image
    if uvage.is_pressing("down"):
        image_number+=1
    player_icon.image=fly_image