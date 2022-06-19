import time


class TrafficLight:

    __traffic_lights_colors = {'red': 7, 'yellow': 2, 'green': 5}

    def __init__(self):
        self.__color = 'red'

    def get_color(self):
        return self.__color

    def running(self):
        while True:
            for color in self.__traffic_lights_colors:
                self.__color = color
                print(self.get_color())
                time.sleep(self.__traffic_lights_colors[color])


tr1 = TrafficLight()
tr1.running()