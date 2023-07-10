from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_im, player_cor, size, player_speed = 5):
        super().__init__()
        self.image = transform.scale(image.load(player_im), size)
        self.rect = self.image.get_rect()
        
        self.cor_x, self.cor_y = player_cor[0], player_cor[1]
        self.speed = player_speed

        self.rect.x = self.cor_x
        self.rect.y = self.cor_y
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_right(self):
        keys = key.get_pressed()

        if keys[K_UP]:
            if self.rect.y > 20:
                self.rect.y -= self.speed
        elif keys[K_DOWN]:
            if self.rect.y < 380:
                self.rect.y += self.speed

    def update_left(self):
        keys = key.get_pressed()

        if keys[K_w]:
            if self.rect.y > 20:
                self.rect.y -= self.speed
        elif keys[K_s]:
            if self.rect.y < 380:
                self.rect.y += self.speed
"""
class Ball(GameSprite):
    def update(self):
        pass
"""

window = display.set_mode((700, 500))
display.set_caption("Pong")

left_player  = Player("pl.png", (20,  200), (10, 100), 10)
right_player = Player("pl.png", (670, 200), (10, 100), 10)



clock = time.Clock()
FPS = 30

game = True
while game:
    window.fill((25,25,100))

    left_player.reset()
    right_player.reset()

    left_player.update_left()
    right_player.update_right()

    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(FPS)