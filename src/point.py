import math


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __lt__(self, other: "Point"):
        if self.x != other.x:
            return self.x < other.x
        else:
            return self.y < other.y

    def __eq__(self, other: "Point"):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"[{self.x}, {self.y}]"

    def __hash__(self):
        return hash((self.x, self.y))

    def __add__(self, other: "Point"):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Point"):
        return Point(self.x - other.x, self.y - other.y)

    def cross(self, other: "Point"):
        return self.x * other.y - self.y * other.x

    def norm(self):
        return math.sqrt(self.x**2 + self.y**2)
