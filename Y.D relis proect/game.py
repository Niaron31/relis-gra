from pygame import * 
from pygame.sprite import Group
from random import randint 
#https://drive.google.com/drive/folders/1IIxWXbRVcyO-2O2soaao2-H5idAq16_V?usp=sharing
#звук 
win_width = 1000 
win_height = 600 
mixer.init() 
#fon
window = display.set_mode((win_width, win_height)) 
display.set_caption("Ping-pong Game")
fon = 'fon5.jpg'
background = transform.scale(image.load(fon), (win_width, win_height))
class GameSprite(sprite.Sprite): 
 
    def __init__(self, player_image , player_x , player_y, size_x, syze_y, player_speed): 
        sprite.Sprite.__init__(self) 
        self.image = transform.scale(image.load(player_image),(size_x , syze_y))  
        self.speed = player_speed 
        self.rect = self.image.get_rect() 
        self.rect.x = player_x 
        self.rect.y = player_y 
    def reset (self): 
        window.blit(self.image,(self.rect.x , self.rect.y))

game = True
finish = False
while game:
    for e in event.get(): 
        if e.type == QUIT: 
            game = False 
    if not finish:
        window.blit(background, (0, 0)) 
    display.update() 
 
    time.delay(50)
