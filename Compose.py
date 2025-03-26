class Engine():
    def start(self):
        print('Engine has started')
    def stop(self):
        print('Engine has stopped')

class Car():
    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()

    def stop(self):
        self.engine.stop()

Car().start()
Engine().stop()
Car().stop()

my_Car = Car()

my_Car.start()
my_Car.stop()
