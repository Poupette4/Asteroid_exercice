import pygame
import random
from logger import log_event
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen,"white",self.position,self.radius,LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self) -> None:
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")
        new_angle = random.uniform(20, 50)
        velocity_1 = self.velocity.rotate(new_angle)
        velocity_2 = self.velocity.rotate(-new_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        new_asteroid_1 = Asteroid(self.position.x,self.position.y,new_radius)
        new_asteroid_2 = Asteroid(self.position.x,self.position.y,new_radius)

        new_asteroid_1.velocity = velocity_1 * 1.2
        new_asteroid_2.velocity = velocity_2 * 1.2
