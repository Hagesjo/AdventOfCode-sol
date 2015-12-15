class Deer:
    def __init__(self, speed, flytime, rest):
        self.speed = speed
        self.flytime = flytime
        self.rest = rest
        self.distance = 0
        self.points = 0
        self.generator = self.move_generator()

    def move_generator(self):
        while True:
            for i in range(self.flytime, 0, -1):
                self.distance += self.speed
                yield self.distance
            for i in range(self.rest, 0, -1):
                yield self.distance

deers = []

with open('input') as f:
    for line in f:
        _, _, _, speed, _, _, flytime, _, _, _, _, _, _, rest, _ = line.split()
        deers.append(Deer(*map(int, [speed,flytime,rest])))
    for i in range(2503):
        maxd = max(map(lambda x: next(x.generator), deers))
        for deer in deers:
            if deer.distance == maxd:
                deer.points += 1

    print max(map(lambda x: x.points, deers))
