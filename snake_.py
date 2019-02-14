import arcade
from models import World

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


class ModelSprite(arcade.Sprite):
    def __init__(self, *args, **kwargs):
        self.model = kwargs.pop('model', None)

        super().__init__(*args, **kwargs)

    def sync_with_model(self):
        if self.model:
            self.set_position(self.model.x, self.model.y)

    def draw(self):
        self.sync_with_model()
        super().draw()


class SnakeSprite:
    def __init__(self, snake):
        self.snake = snake
        self.block_sprite = arcade.Sprite('images/block.png')

    def draw(self):
        for x, y in self.snake.body:
            # เพิ่มโค้ดที่วาด self.block_sprite ลงตำแหน่ง (x,y) หลักๆ คือให้ set_position ก่อน แล้วค่อย draw
            self.block_sprite.set_position(x,y)
            self.block_sprite.draw()


class SnakeWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)


        self.world = World(SCREEN_WIDTH, SCREEN_HEIGHT)

        # self.snake_sprite = arcade.Sprite('images/block.png')
        # we use class Model sprite instead for collect image data.
        # self.snake_sprite = ModelSprite('images/block.png',
        #                                 model=self.world.snake)
        # self.snake_sprite.set_position(300, 300)
        self.snake_sprite = SnakeSprite(self.world.snake)
        arcade.set_background_color(arcade.color.BLACK)
    # create update for update in world class.
    def update(self, delta):
        self.world.update(delta)


    # draw sprite
    def on_draw(self):
        arcade.start_render()
        self.snake_sprite.draw()

    def on_key_press(self, key, key_modifiers):
        self.world.on_key_press(key, key_modifiers)

def main():
    window = SnakeWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.set_window(window)
    arcade.run()

if __name__ == '__main__':
    main()