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
        if self.rect.x > 345: 
            self.rect.x = 0 
            self.rect.y = randint(200, 400)
class Titan_left(GameSprite):
    def update(self):
        self.rect.x -= self.speed
        if self.rect.x < 830: 
            self.rect.x = 1175  
            self.rect.y = randint(200, 400)
class Titan_top(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 205: 
            self.rect.x = randint(380,830)  
            self.rect.y = 0
class Titan_down(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 470: 
            self.rect.x = randint(380,830)  
            self.rect.y = 675

titans_right = sprite.Group() 
for i in range(1, 5): 
    titan_right = Titan_right("titan.png", 0, randint(200, 400),25,25,randint(1, 5))
    titans_right.add(titan_right)
 
titans_left = sprite.Group() 
for i in range(1, 5): 
    titan_left = Titan_left("titan.png", 1175, randint(200, 400),25,25,randint(1, 5))
    titans_left.add(titan_left) 

titans_top = sprite.Group() 
for i in range(1, 5): 
    titan_top = Titan_top("titan.png", randint(380,830), 0,25,25,randint(1, 5))
    titans_top.add(titan_top)

titans_down = sprite.Group() 
for i in range(1, 5): 
    titan_down = Titan_down("titan.png", randint(380,830), 675,25,25,randint(1, 5))
    titans_down.add(titan_down)   

olimp = GameSprite("olimp_4.png", 370, 230, 460, 240, None)        
game = True
finish = False
score = 0
while game:
    for e in event.get(): 
        if e.type == QUIT: 
            game = False 
    if not finish:
        window.blit(background, (0, 0))
        olimp.reset()
        
        titans_right.update()
        titans_right.draw(window) 
        
        titans_left.update()
        titans_left.draw(window)
        
        titans_top.update()
        titans_top.draw(window)
        
        titans_down.update()
        titans_down.draw(window)
        

        
        
    display.update() 
 
    time.delay(50)
