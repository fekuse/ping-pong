from pygame import *

class GameSprite (sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (wight, height)) #BMеCT
        self.speed= player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
   #метод для управления спрайтом стрелками клавиатуры
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 480:
            self.rect.y += self.speed
 #метод "выстрел" (используем место игрока, чтобы создать там пулю)
    def update_r(self):
        keys = key.get_pressed() 
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 480:
            self.rect.y += self.speed



#создаём окошко
win_width = 600
win_height = 500
back = (200,255,251)
display.set_caption("Shooter")
window = display.set_mode((win_width, win_height))
window.fill(back)
#создаём спрайты
#основной цик
racket1 = Player("racket.png", 30, 200, 4, 50, 150)
racket2 = Player("racket.png", 520, 200, 4, 50, 150)
ball = GameSprite("ball.png", 200,200,4,50,50)
game = True #флаг сбрасывается кнопкой закрытия окна
finish = False

clock = time.Clock()

speed_x = 3
speed_y = 3

while game:
   #событие нажатия на кнопку Закрыть
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.fill(back)
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1

        if ball.rect.y > win_height-50 or  ball.rect.y < 0: 
            speed_y *= -1

        racket1.reset()
        racket2.reset()
        ball.reset()


    display.update()
    clock.tick(60)
