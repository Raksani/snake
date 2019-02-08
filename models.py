# for show snake
class Snake:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y

    # snake moves along in x+5 unit, if x direction is more than window width then reset to zero. And
    def update(self, delta):
        if self.x > self.world.width:
            self.x = 0
        self.x += 5

# for collect game data
class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.snake = Snake(self, width // 2, height // 2)

    def update(self, delta):
        self.snake.update(delta)