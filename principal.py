import pygame
import math

class Enemy(pygame.sprite.Sprite):
    def __init__(self, waypoints, hp, speed):
        super().__init__()
        self.waypoints = waypoints
        self.pos = pygame.math.Vector2(waypoints[0])
        self.target_index = 1
        self.speed = speed
        self.hp = hp

        #Grafico basico (un circulo o cuadrado rojo)
        self.image = pygame.Surface((24, 24))
        self.image.fill((220, 50 ,50))
        self.rect = self.image.get_rect(center=self.pos)

    def update(self):
        if self.target_index < len(self.waypoints)
            target = pygame.math.Vector2(self.waypoints[self.target_index])
            movement = target - self.pos
            distance = movement.length()

            if distance >= self.speed:
                self.pos += movement.normalize() * self.speed
            else:
                self.pos = target
                self.target_index += 1

            self.rect.center = self.pos
        else:
            # Llego al final del camino: restar vida al jugador y eliminar enemigo
            self.kill()

class Tower(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.pos = pygame.math.Vector2(x, y)
        self.range = 150
        self.cooldown = 60 #Frames entre disparos(1 segundos a 60 FPS)
        Self.timer = 0

        self.image = pygame.Surface((32, 32))
        self.image.fill((50, 150, 220))
        self.rect = self.image.get_rect(center=self)
