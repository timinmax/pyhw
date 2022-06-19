class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'I am {self.title} stationery')


class Pen(Stationery):
    def draw(self):
        print(f'I am {self.title} pen')


class Pencil(Stationery):
    def draw(self):
        print(f'I am {self.title} pencil')


class Handle(Stationery):
    def draw(self):
        print(f'I am {self.title} handle')


red_handle = Handle('red')
red_handle.draw()
green_pencil = Pencil('green')
green_pencil.draw()
blue_pen = Pen('blue')
blue_pen.draw()