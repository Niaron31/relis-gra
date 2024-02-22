from typing import Any
from pygame import * 
from pygame.sprite import Group
from random import randint 
win_width = 1200 
win_height = 700 
#звук 
mixer.init() 
#fon
window = display.set_mode((win_width, win_height)) 
display.set_caption("Save of Olimp")
fon = 'background.jpg'
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
class Titan_right(GameSprite):
    def update(self):
        self.rect.x += self.speed
titan_right = Titan_right("titan.png", 0, randint(200, 300),25,25,2)
olimp = GameSprite("olimp_5.png", 370, 220, 460, 240, None)        
game = True
finish = False
while game:
    for e in event.get(): 
        if e.type == QUIT: 
            game = False 
    if not finish:
        window.blit(background, (0, 0))
        titan_right.update()
        titan_right.reset() 
        olimp.reset()
    display.update() 
 
    time.delay(50)