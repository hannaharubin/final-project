import uvage
import random

# Setup
camera = uvage.Camera(800, 600)
game_over = False
score = 0

# Images
run_image = "run.png"
fly_image = "fly.png"
ground = "ground.png"


# Player
player_icon = uvage.from_image(150, 400, run_image)
player_vy = 0
gravity = 1
jumping = False
max_jumps = 3  #  double jump

# Obstacle
ground_speed = 5
ground.x = 0
border1 = 0
border2 = 0


def tick():
    global game_over, score, player_vy, jumping
    global player_icon
    global ground
    global ground_speed
    global ground1, ground2
    global border1
    global border2
    camera.clear("white")


    while not game_over:
        player_icon.yspeed += 1 # The += 1 represents gravity adding downwards speed every tick; positive y means downward direction
        if player_icon.y == 400:
            player_icon.yspeed = 0 # This stops us from falling through the floor
            if uvage.is_pressing("up arrow"): # Check if we should jump
                player_icon.yspeed = - 15
        player_icon.move_speed() # THIS IS REALLY IMPORTANT, or the walker won't move based on its speed
        ground.x-=1
        border1.x-=1
        if border1.x <= -800:
            border1.x = 800
        if ground.x <= -800:
            ground.x = 800


        
    
            
            

        # Move obstacle
      #  obstacle.x -= obstacle_speed
      #  if obstacle.x < -50:
      #      obstacle.x = 850
      #      score += 1

        # player_icon".touches(obstacle)" is important & the only way i could find to check for collision
     #   if player_icon.touches(obstacle):
      #      game_over = True

        # Draw game elements
        camera.draw(player_icon)
        camera.draw(ground1)
        camera.draw(ground2)
        camera.draw(uvage.from_text(80, 50, f"Score: {score}", 30, "black"))
    else:
        camera.draw(uvage.from_text(400, 300, "Game Over", 60, "red"))

    camera.display()

uvage.timer_loop(30, tick)