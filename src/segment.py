from point import Point


class Segment:
    def __init__(self, p1: Point, p2: Point):
        self.p1 = min(p1, p2)
        self.p2 = max(p1, p2)
        self.current_y = p1.y

    def __str__(self):
        return f"<{self.p1}, {self.p2}>"

    def __lt__(self, other: "Segment"):
        return self.current_y < other.current_y

    def det(self):
        return self.p1.x * self.p2.y - self.p1.y * self.p2.x

    def intersection(self, other: "Segment"):
        # Calculate differences
        xdiff = self.p1.x - self.p2.x
        ydiff = self.p1.y - self.p2.y
        xdiff_other = other.p1.x - other.p2.x
        ydiff_other = other.p1.y - other.p2.y

        # Calculate divisor
        div = xdiff * ydiff_other - ydiff * xdiff_other

        # Check if segments are parallel or coincident
        if div == 0:
            return None

        # Calculate determinant values
        det_self = self.p1.x * self.p2.y - self.p1.y * self.p2.x
        det_other = other.p1.x * other.p2.y - other.p1.y * other.p2.x

        # Calculate intersection point
        x = (det_self * xdiff_other - xdiff * det_other) / div
        y = (det_self * ydiff_other - ydiff * det_other) / div

        # Check if intersection point lies within both segments
        if (
            min(self.p1.x, self.p2.x) <= x <= max(self.p1.x, self.p2.x)
            and min(self.p1.y, self.p2.y) <= y <= max(self.p1.y, self.p2.y)
            and min(other.p1.x, other.p2.x) <= x <= max(other.p1.x, other.p2.x)
            and min(other.p1.y, other.p2.y) <= y <= max(other.p1.y, other.p2.y)
        ):
            return Point(x, y)
        else:
            return None
