import arcade.key
# set up the direction
DIR_UP = 1
DIR_RIGHT = 2
DIR_DOWN = 3
DIR_LEFT = 4

DIR_OFFSET = {DIR_UP: (0, 1),
              DIR_RIGHT: (1, 0),
              DIR_DOWN: (0, -1),
              DIR_LEFT: (-1, 0)}


# for show snake
class Snake:
    # ให้งูขยับเป็นจังหวะ โดยเก็บค่าไว้ในdeltaถ้าถึงค่านึง มันจะขยับ เหมือนนับ123วิ่ง
    # move wait เลยเป็นค่าที่เราจะนับก่อนขยับ
    MOVE_WAIT = 0.2
    BLOCK_SIZE = 16

    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.wait_time = 0
        self.direction = DIR_RIGHT
        # make snake longer
        self.body = [(x, y),
                     (x - Snake.BLOCK_SIZE, y),
                     (x - 2 * Snake.BLOCK_SIZE, y)]
        self.length = 3

    def update(self, delta):
        # snake moves along in x+5 unit, if x direction is more than window width then reset to zero.
        # if self.x > self.world.width:
        #     self.x = 0
        # self.x += 5
        # เพิ่มเวลานับ เท่ากับ delta
        self.wait_time += delta
        # ถ้่านับwait time ยังน้อยกว่าเวลาที่เราจะขยับ ก็ไม่ต้องทำอะไร นับต่อไป
        if self.wait_time < Snake.MOVE_WAIT:
            return
        # snake moves along in x+16 unit, if x direction is more than window width then reset to zero. And
        if self.x > self.world.width:
            self.x = 0
        # self.x += 16
        # change to be
        # แงะไปทีละชั้น self.direction เพื่อดูว่าขึ้นหรือลงหรือซ้ายหรือขวาใส่ตำแหน่งที่Arrayตัวที่0คือตัวx และ คูณกับ blocksize เป็นระยะทางที่จะเคลื่อนที่
        self.x += DIR_OFFSET[self.direction][0] * self.BLOCK_SIZE
        self.y += DIR_OFFSET[self.direction][1] * self.BLOCK_SIZE
        self.wait_time = 0
        self.body.insert(0, (self.x, self.y))
        self.body.pop()

# for collect game data
class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.snake = Snake(self, width // 2, height // 2)

    def update(self, delta):
        self.snake.update(delta)

    def on_key_press(self, key, key_modifiers):
        # เพิ่มโค้ดตรวจสอบปุ่มและเปลี่ยนทิศทางของ self.snake
        if key == arcade.key.RIGHT:
            self.snake.direction = DIR_RIGHT
        elif arcade.key.LEFT == key:
            self.snake.direction = DIR_LEFT
        elif arcade.key.UP == key:
            self.snake.direction = DIR_UP
        elif arcade.key.DOWN == key:
            self.snake.direction = DIR_DOWN
