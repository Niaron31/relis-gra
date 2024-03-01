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
        global lost
        self.rect.x += self.speed
        if self.rect.x > 345: 
            self.rect.x = 0 
            self.rect.y = randint(200, 400)
            lost = lost + 1
class Titan_left(GameSprite):
    def update(self):
        global lost
        self.rect.x -= self.speed
        if self.rect.x < 830: 
            self.rect.x = 1175  
            self.rect.y = randint(200, 400)
            lost = lost + 1

class Titan_top(GameSprite):
    def update(self):
        global lost
        self.rect.y += self.speed
        if self.rect.y > 205: 
            self.rect.x = randint(380,830)  
            self.rect.y = 0
            lost = lost + 1

class Titan_down(GameSprite):
    def update(self):
        global lost
        self.rect.y -= self.speed
        if self.rect.y < 470: 
            self.rect.x = randint(380,830)  
            self.rect.y = 675
            lost = lost + 1

class Lightning():
    def __init__(self, player_image , player_x , player_y, size_x, syze_y, player_speed): 
        sprite.Sprite.__init__(self) 
        self.image = transform.scale(image.load(player_image),(size_x , syze_y))  
        self.speed = player_speed 
        self.rect = self.image.get_rect() 
        self.rect.x = player_x 
        self.rect.y = player_y 
        self.animatedd = False
        self.count = 0
    def reset (self): 
        window.blit(self.image,(self.rect.x , self.rect.y))
    def update(self):
        keys = key.get_pressed()
        if keys[K_a]:
            self.animatedd = True
        else: 
            self.animatedd = False

    def animated(self):
        if self.animatedd:
            self.count = (self.count + 1) % len(lightning)  
            window.blit(lightning[self.count], (self.rect.x, self.rect.y))
        else:
            self.count = 0
            window.blit(lightning[self.count], (self.rect.x, self.rect.y))



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
lightning = [image.load('lightning_1.png'), image.load("lightning_2.png"),image.load("lightning_3.png"),image.load('lightning_4.png'),image.load('lightning_5.png'),image.load('lightning_6.png'),image.load('lightning_7.png'),image.load("lightning_8.png"),image.load("lightning_9.png")]
lightnings = Lightning('lightning_1.png', 100, 100, 50, 100, None)
font.init()
font1 = font.Font(None,36)
font2 = font.Font(None,56)

lost = 0
score = 0
while game:
    for e in event.get(): 
        if e.type == QUIT: 
            game = False 
    if not finish:
        losting = font1.render('Пропущено: ' + str(lost), 1, (255, 255, 255))
        killed = font1.render('Вбито: ' + str(score), 1, (255,255,255))
        window.blit(background, (0, 0))
        window.blit(losting,(10,20))
        window.blit(killed,(10,60))
        over_los = font2.render('Ти програв:',1,(144,30,45))
        olimp.reset()
        
        titans_right.update()
        titans_right.draw(window) 
        
        titans_left.update()
        titans_left.draw(window)
        
        titans_top.update()
        titans_top.draw(window)
        
        titans_down.update()
        titans_down.draw(window)

        lightnings.update()
        lightnings.animated()       
        if lost >= 3:
            window.blit(over_los,(500,300))
            finish = True

    display.update() 
 
    time.delay(50)
