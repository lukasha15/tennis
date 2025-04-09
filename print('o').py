from pygame import *
win_height = 500
win_width = 500
window = display.set_mode((win_width, win_height))
background = [100, 100, 100]
display.set_caption("Ping-Pong")
window.fill(background)
#window.blit(0, 0)
clock = time.Clock()
game = True
while game:
    for e in event.get():
       if e.type == QUIT:
          game = False
    clock.tick(60)
    display.update()