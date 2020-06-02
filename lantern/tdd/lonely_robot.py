class Asteroid:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Robot:
    def __init__(self, x, y, direction, asteroid):
        self.x = x
        self.y = y
        self.asteroid = asteroid
        self.direction = direction
        if self.x > self.asteroid.x or self.y > self.asteroid.y:
            raise MissAsteroidError()

    def turn_left(self):
        turns = {
            "E": "N",
            "N": "W",
            "W": "S",
            "S": "E"
        }
        self.direction = turns[self.direction]

    def turn_right(self):
        turns = {
            "N": "E",
            "E": "S",
            "S": "W",
            "W": "N"
        }
        self.direction = turns[self.direction]

    def move_forward(self):
        if self.direction == "N":
            self.y += 1
        elif self.direction == "E":
            self.x += 1
        elif self.direction == "S":
            self.y -= 1
        elif self.direction == "W":
            self.x -= 1

    def move_backward(self):
        if self.direction == "N":
            self.y -= 1
        elif self.direction == "E":
            self.x -= 1
        elif self.direction == "S":
            self.y += 1
        elif self.direction == "W":
            self.x += 1


class MissAsteroidError(Exception):
    print("The robot has failed")
