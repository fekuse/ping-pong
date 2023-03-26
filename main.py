from pygame import *

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
