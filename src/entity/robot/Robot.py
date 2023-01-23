import pygame

from constant.constants import BLOCK_SIZE


class Robot:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.current_battery = 200
        self.max_battery = 1000
        self.battery_bar_length = 400
        self.battery_ratio = self.max_battery / self.battery_bar_length

    def update(self, display):
        self.basic_battery(display)

    def dying_damage(self, amount):
        self.current_battery = max(0, self.current_battery - amount)

    def get_battery(self, amount):
        self.current_battery = min(self.max_battery, self.current_battery + amount)

    def basic_battery(self, display):
        pygame.draw.rect(display, self.get_battery_color(self.current_battery),
                         (10, 10, self.current_battery / self.battery_ratio, 25))
        pygame.draw.rect(display, (255, 255, 255), (10, 10, self.battery_bar_length, 25), 4)

    def get_battery_color(self, battery):
        if battery < self.max_battery // 3:
            return (255, 0, 0)
        if battery > self.max_battery // 3 * 2:
            return (127, 255, 0)
        return (255, 255, 0)

    def main(self, display):
        pygame.draw.rect(display, (105, 105, 105),
                         ((self.x - 1) * BLOCK_SIZE, (self.y - 1) * BLOCK_SIZE, 3 * BLOCK_SIZE, 3 * BLOCK_SIZE))
        pygame.draw.rect(display, (0, 0, 0), (self.x * BLOCK_SIZE, self.y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))