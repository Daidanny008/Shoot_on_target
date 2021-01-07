# position to mouse.
# shooter game test.
# there are no sounds because gunshot sounds are too loud and damaging to hearing.

# run pygame.
import pgzrun 

# initializing.
import pygame
pygame.init()
pygame.display.set_caption("Gunfire Game")
WIDTH = 1200
HEIGHT = 600

# variables declaration.
count_score = 0
message = "—"

# gun image.
# photo attribution:
# <a href="https://www.vecteezy.com/"> PNGs by Vecteezy</a>
ak47 = Actor("ak47", center = (250, 300))

# adjust angle
ak47.angle -= 45

# target image.
target = Actor("target", center = (1000, 300))

def draw():
    # global screen
    # clear screen, bgcolor = white,
    # draw ak47, draw target, draw console.
    screen.clear()
    screen.fill("white")
    ak47.draw()
    target.draw()
    rect = Rect(0, 525, 1200, 75)
    screen.draw.filled_rect(rect, "white")
    screen.draw.textbox(message, rect, color = "black", center = (600, 562.5),
                        align = "center")
    
def on_mouse_down(pos):
    # global variables.
    global count_score, message
    
    # change to gunfire picture, adjust angle.
    ak47.image = "ak47_fire"
    ak47.angle = ak47.angle_to(pos)
    ak47.angle -= 45

    # determine if shot on target.
    if ak47.angle >= -49.7 and ak47.angle <= -38:
        count_score += 1
        message = ("Good shot! Your score is " + str(count_score))
    else:
        count_score -= 1
        message = ("Oof, your score is " + str(count_score))

def on_mouse_up(pos):
    # change to regular image, adjust angle.
    ak47.image = "ak47"
    ak47.angle = ak47.angle_to(pos)
    ak47.angle -= 45

def on_mouse_move(pos):
    # adjust angle.
    ak47.angle = ak47.angle_to(pos)
    ak47.angle -= 45

# update text.
pygame.display.update()

# run pygame.
pgzrun.go()
