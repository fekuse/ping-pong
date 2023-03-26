from pygame import *

class Player(GameSprite):
   #метод для управления спрайтом стрелками клавиатуры
   def update_1(self):
        keys = key.get_pressed()
        if keys[K_W] and self.rect.y > 5:
            self.rect.y -= self.speed
 #метод "выстрел" (используем место игрока, чтобы создать там пулю)
    def update_r(self):
    keys = key.get_pressed() 
    if keys[K_UP] and self.rect.y > 5:
        self.rect.y -= self.speed

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

#создаём окошко
win_width = 700
win_height = 500
back = (200,255,251)
display.set_caption("Shooter")
window = display.set_mode((win_width, win_height))
window.fill(back)
#создаём спрайты
#основной цикл игры:
run = True #флаг сбрасывается кнопкой закрытия окна
while run:
   #событие нажатия на кнопку Закрыть
    for e in event.get():
        if e.type == QUIT:
            run = False
    display.update()
