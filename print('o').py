from pygame import *
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))    
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y 
        self.width = width
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Rocket1(GameSprite):
    def update1(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 400:
            self.rect.y += self.speed
    def update2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 400:
            self.rect.y += self.speed

win_height = 500
win_width = 500
window = display.set_mode((win_width, win_height))
background = [100, 100, 100]
display.set_caption("Ping-Pong")
#window.fill(background)
rocket1 = Rocket1('ракетка.png', 350, 200, 3, 200, 100)
rocket2 = Rocket1('ракетка.png', -50, 200, 3, 200, 100)
#window.blit(0, 0)
clock = time.Clock()
game = True
while game:
    window.fill(background)
    rocket1.reset()
    rocket1.update1()
    rocket2.reset()
    rocket2.update2()

    for e in event.get():
       if e.type == QUIT:
          game = False
    clock.tick(60)
    display.update()
