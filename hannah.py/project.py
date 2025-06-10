# 6/10/25 Hannah Rubin
import random
import uvage
image_number=0
run_image=uvage.load_sprite_sheet("run.png")
fly_image=uvage.load_sprite_sheet("fly.png")
background=uvage.display.set_mode((800,600))
player_icon=uvage.from_omage(600,100,run_image)
def tick():
    global image_number
    if uvage.is_pressing("up"):
        image_number+=1
    player_icon.image=fly_image
    if uvage.is_pressing("down"):
        image_number+=1
    player_icon.image=fly_image
    if uvage.is_pressing("right arrow"):
        image_number+=1
    player_icon.image=run_image
    if uvage.is_pressing("left arrow"):
    player_icon.image=run_image
    camera.draw(player_icon)

