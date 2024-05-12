#создай игру "Лабиринт"!
from pygame import *
win_width = 600
win_height = 800
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self): 
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x >5 :
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < win_height - 80:
            self.rect.x += self.speed
        if keys[K_w] and self.rect.x > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_width - 80:
            self.rect.y += self.speed

class Enemy(GameSprite):
    direction = "left"
    def update(self):
        if self.rect.x <= win_height - 230:
            self.direction = "right"
        if self.rect.x >= win_height - 85:
            self.direction = "left"
        if self.direction == "left":
            self.rect.x -=self.speed
        else:
            self.rect.x +=self.speed

class Wall(sprite.Sprite):
    def __init__(self, color1, color2, color3, wall_y, wall_x, wall_height, wall_width):
       super().__init__()
       self.color1 = color1
       self.color2 = color2
       self.color3 = color3
       self.width = wall_width
       self.height = wall_height
       self.image = Surface((self.width, self.height))
       self.image.fill((color1, color2, color3))
       self.rect = self.image.get_rect()
       self.rect.x = wall_x
       self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
#создай окно игры
window = display.set_mode((win_height, win_width))
display.set_caption("Лабиринт")
#задай фон сцены
background = transform.scale(image.load("background.jpg"), (win_height, win_width))
player = Player(("hero.png"), 10, 420, 4)
cyborg1 = Enemy(("cyborg.png"), win_height - 80, win_width - 220, 2)
final = GameSprite(("treasure.png"), win_height - 120, win_width - 80, 0)
wall1 = Wall(68, 207, 95, 100, 0, 10, 800)
wall2 = Wall(68, 207, 95, 300, 150, 600, 10)
wall3 = Wall(68, 207, 95, 100, 340, 300, 10)
wall4 = Wall(68, 207, 95, 300, 500, 600, 10)
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
finish = False
game = True
clock = time.Clock()
FPS = 80
money = mixer.Sound("money.ogg")
kick = mixer.Sound("kick.ogg")
font.init()
font = font.Font(None, 70)
win = font.render("Молодец!", True, (255, 215, 0))
lose = font.render("Проиграл!", True, (240, 55, 14))



while game:
    window.blit(background, (0,0))
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        player.update()
        player.reset()
        cyborg1.update()
        cyborg1.reset()
        final.reset()
        wall1.draw_wall()
        wall2.draw_wall()
        wall3.draw_wall()
        wall4.draw_wall()
    if sprite.collide_rect(player, final):
        window.blit(win, (200, 200))
        finish = True
        money.play()
    if sprite.collide_rect(player, cyborg1)  or sprite.collide_rect(player, wall1) or sprite.collide_rect(player, wall2) or sprite.collide_rect(player, wall3) or sprite.collide_rect(player, wall4):
        window.blit(lose, (200, 200))
        finish = True
        kick.play()
        
    display.update()
    clock.tick(FPS)
    