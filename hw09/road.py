class Road:
    _length = 0
    _width = 0

    def __init__(self, length=0, width=0):
        self._length = length
        self._width = width

    def calc_asphalt_volume(self, height=1, asphalt_per_unit=25):
        return self._length * self._width * asphalt_per_unit * height / 1000


test_road = Road(5000, 20)
print(test_road.calc_asphalt_volume(5))
