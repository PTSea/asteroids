from circleshape import *
import random
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.radius = radius
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        vector_one = self.velocity.rotate(random_angle) * 1.2
        vector_two = self.velocity.rotate(-random_angle) * 1.2
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        split_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        split_asteroid_1.velocity = vector_one

        split_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        split_asteroid_2.velocity = vector_two