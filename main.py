from pygame import *

init()

class GameSprite(sprite.Sprite):
    def __init__(self, player_im, player_cor, size, player_speed = 5):
        super().__init__()
        self.image = transform.scale(image.load(player_im), size)
        self.rect = self.image.get_rect()
        
        self.cor_x, self.cor_y = player_cor[0], player_cor[1]
        self.speed = player_speed

        self.rect.x = self.cor_x
        self.rect.y = self.cor_y

        self.LEFT = True
    
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

window = display.set_mode((700, 500))
display.set_caption("Pong")

left_player  = Player("pl.png", (20,  200), (10, 100), 10.2)
right_player = Player("pl.png", (670, 200), (10, 100), 10.2)


ball = GameSprite("ball.png", (350, 250), (50,50))
ball_speed_x = 6
ball_speed_y = 6


left_points = 0
right_points = 0

left_win = font.SysFont("Arial", 70).render("Left Wins!", True, (255, 0, 0))
right_win = font.SysFont("Arial", 70).render("Right Wins!", True, (0, 0, 255))

clock = time.Clock()
FPS = 30

game = True
finish = False
while game:
    window.fill((170,255,255))

    if not(finish):
        ball.reset()
        left_player.reset()
        right_player.reset()


        left_player.update_left()
        right_player.update_right()


        ball.rect.x += ball_speed_x
        ball.rect.y += ball_speed_y

        if ball.rect.x > 680:
            left_points += 1
            ball.rect.x, ball.rect.y = 300, 200
            ball_speed_x *= -1

        if ball.rect.x < 10:
            right_points += 1
            ball.rect.x, ball.rect.y = 300, 200
            ball_speed_x *= -1

        if ball.rect.y > 445 or ball.rect.y < 10:
            ball_speed_y = ball_speed_y * -1
        if sprite.collide_rect(left_player, ball):
            ball_speed_x = ball_speed_x * -1
        if sprite.collide_rect(right_player, ball):
            ball_speed_x = ball_speed_x * -1


        left_pnts_text = font.SysFont("Arial", 20).render("Left Points: ", True, (255, 0, 0))
        left_pnts_counter = font.SysFont("Arial", 20).render(str(left_points), True, (255,0,0))

        right_pnts_text = font.SysFont("Arial", 20).render("Right Points: ", True, (0, 0, 255))
        right_pnts_counter = font.SysFont("Arial", 20).render(str(right_points), True, (0, 0, 255))

        window.blit(left_pnts_text, (250,10))
        window.blit(left_pnts_counter, (250,30))

        window.blit(right_pnts_text, (350,10))
        window.blit(right_pnts_counter, (350,30))

        if left_points == 5:
            finish = "Left"
        elif right_points == 5:
            finish = "Right"

    if finish == "Left":
        window.blit(left_win,(200,200))
    elif finish == "Right":
        window.blit(right_win,(200,200))

    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(FPS)

quit()
