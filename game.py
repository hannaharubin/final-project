import uvage
import random

camera = uvage.Camera(800, 550)
game_over = False
score = 0

# Images
run_image = "run.png"
fly_image = "fly.png"
ground_image = "desert4.jpg"
obstacle_image= "cactus.png"


# Player
player_icon = uvage.from_image(150, 375, run_image)
gravity = 1
jumping = False

# Obstacles
obstacles = []
frame_count = 0
obstacle_speed = 5

obstacle = uvage.from_image(800, 410, "cactus.png")
obstacle.scale_by(0.3)
# Ground
scroll_speed = 5
speed_increase_timer = 0
scroll_x = 0
bg1 = uvage.from_image(400, 275, "desert4.jpg")
bg1.scale_by(.431)
bg2 = uvage.from_image(1200, 275, "desert4.jpg")
bg2.scale_by(.431)

# ground = uvage.from_image(400, 300, ground)  
# ground.scale_by(1)  # reduce size if needed

ground_width = bg1.width

def tick():
    global game_over, score
    global jumping, player_icon, gravity
    global scroll_x, scroll_speed
    global bg1, bg2
    global frame_count, obstacles

    camera.clear("white")

    scroll_x = (scroll_x + scroll_speed) % ground_width

    bg1.x = ground_width//2 - scroll_x
    bg2.x = (3*ground_width)//2 - scroll_x


    if not game_over:
        player_icon.yspeed += gravity # The += 1 represents gravity adding downwards speed every tick; positive y means downward direction
        frame_count+=1

        if speed_increase_timer % 600 == 0:
          scroll_speed += 0.05
          if scroll_speed > 20:
            scroll_speed = 20
      
        if player_icon.y == 375:
            player_icon.yspeed = 0 # This stops us from falling through the floor
            if uvage.is_pressing("up arrow"): # Check if we should jump
                player_icon.yspeed = - 15

        player_icon.move_speed() # THIS IS REALLY IMPORTANT, or the walker won't move based on its speed

        
      # Move obstacle
        obstacle.x -= obstacle_speed
        if obstacle.x < -50:
            obstacle.x = 850
            score += 1
     

      # player_icon".touches(obstacle)" is important & the only way i could find to check for collision
        if player_icon.touches(obstacle):
            game_over = True
    

        # Draw game elements
        camera.draw(bg1)
        camera.draw(bg2)
        camera.draw(obstacle)
        camera.draw(uvage.from_text(80, 50, f"Score: {score}", 30, "black"))
        camera.draw(player_icon)
        camera.draw(uvage.from_text(80, 50, "Score: {score}", 30, "black"))
    else:
        camera.draw(uvage.from_text(400, 300, "Game Over", 60, "red"))

    camera.display()

uvage.timer_loop(30, tick)
