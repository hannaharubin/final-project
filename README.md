# final-project 
# 6/10/25
import random
import uvage
camera = uvage.Camera(800, 600)
<<<<<<< HEAD

game_over = False
score = 0

#images

run_image = "run.png"
fly_image = "fly.png"
obstacle_image = "cat.png" 

player_icon = uvage.from_image(100, 500, run_image)
player_vy = 0
gravity = 1
jumping = False
max_jumps = 3  #  double jump

obstacle_speed = 5
obstacle = uvage.from_image(900, 500, obstacle_image)  
obstacle.scale_by(0.3)  # reduce size if needed

def tick():
    global game_over, score, player_vy, jumping, jump_count

    camera.clear("light blue")

    if not game_over:
        if uvage.is_pressing("up arrow") and jump_count < max_jumps:
            player_vy = -10
            jump_count += 1
            jumping = True
            jump_count = 0

        player_vy += gravity
        player_icon.y += player_vy

        if player_icon.y < 50:
            player_icon.y = 50
            player_vy = 0

        # Stay on ground
        if player_icon.y >= 500:
            player_icon.y = 500
            player_vy = 0
            jumping = False
            jump_count = 0

        # Update image
        player_icon.image = fly_image if jumping else run_image

        # Move obstacle
        obstacle.x -= obstacle_speed
        if obstacle.x < -50:
            obstacle.x = 850
            score += 1

        # player_icon".touches(obstacle)" is important & the only way i could find to check for collision
        if player_icon.touches(obstacle):
            game_over = True

        # Draw game elements
        camera.draw(player_icon)
        camera.draw(obstacle)
        camera.draw(uvage.from_text(80, 50, f"Score: {score}", 30, "black"))
    else:
        camera.draw(uvage.from_text(400, 300, "Game Over", 60, "red"))

    camera.display()
uvage.timer_loop(30, tick)

=======

Hey everyone this is juliaaaaa
heyyy queen
>>>>>>> 24a70c772ba740d739656c63bb1d717eb4e7dec6
>>>>>>> 
