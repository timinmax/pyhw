class Car:
    speed = 0
    color = None
    name = ''
    is_police = False

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'The {self.color} {self.name} is running')

    def stop(self):
        self.speed = 0
        print(f'The {self.color} {self.name} stopped')

    def turn(self, direction):
        print(f'The {self.color} {self.name} turned {direction}')

    def show_speed(self):
        return f'The {self.color} {self.name} speed is {self.speed}'


class TownCar(Car):
    speed_limit = 60

    def __init__(self, *args, **kwargs):
        super(TownCar, self).__init__(*args, **kwargs, is_police=False)

    def show_speed(self):
        return f'{super().show_speed()} {"[overspeed]" if self.speed > TownCar.speed_limit else ""}'


class WorkCar(Car):
    speed_limit = 40

    def __init__(self, *args, **kwargs):
        super(WorkCar, self).__init__(*args, **kwargs, is_police=False)

    def show_speed(self):
        return f'{super().show_speed()} {"[overspeed]" if self.speed > WorkCar.speed_limit else ""}'


class SportCar(Car):

    def __init__(self, *args, **kwargs):
        super(SportCar, self).__init__(*args, **kwargs, is_police=False)


class PoliceCar(Car):

    def __init__(self, *args, **kwargs):
        super(PoliceCar, self).__init__(*args, **kwargs, is_police=True)


town_car = TownCar(61, 'red', 'cts')
print(town_car.show_speed())
print(town_car.is_police)  # False
town_car.turn('Left')

work_car = WorkCar(41, 'grey', 'van')
print(work_car.show_speed())

police_car = PoliceCar(80, 'blue', 'crown')
print(police_car.show_speed())
print(police_car.is_police)  # True
