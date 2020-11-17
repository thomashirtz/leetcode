import math
import random


class Solution:
    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self):
        theta = random.uniform(0, 2 * math.pi)
        distance = self.radius * random.random() ** (1/2)
        return self.x_center + distance * math.cos(theta), self.y_center + distance * math.sin(theta)