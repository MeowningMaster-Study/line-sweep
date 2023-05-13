import heapq
from point import Point
from plot import plot_result

class Event:
    def __init__(self, x, segment, left=True):
        self.x = x
        self.segment = segment
        self.left = left
    
    def __lt__(self, other):
        return self.x < other.x
    
class Segment:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __lt__(self, other):
        return self.p1 < other.p1
    
    def det(self):
        return self.p1.x * self.p2.y - self.p1.y * self.p2.x
    
    def intersection(self, other):
        xdiff = Point(self.p1.x - self.p2.x, other.p1.x - other.p2.x)
        ydiff = Point(self.p1.y - self.p2.y, other.p1.y - other.p2.y)

        div = Segment(xdiff, ydiff).det()
        if div == 0:
            return None

        d = Point(self.det(), other.det())
        x = Segment(d, xdiff).det() / div
        y = Segment(d, ydiff).det() / div
        return Point(x, y)

    
def bentley_ottmann(segments):
    events = []
    for segment in segments:
        events.append(Event(segment.p1.x, segment))
        events.append(Event(segment.p2.x, segment, False))
    events.sort()
    
    queue = []
    intersections = []
    for event in events:
        if event.left:
            for other in queue:
                intersection = event.segment.intersection(other)
                if intersection:
                    heapq.heappush(intersections, intersection)
            heapq.heappush(queue, event.segment)
        else:
            queue.remove(event.segment)
        
    return intersections

def main():
    segments = [
        Segment(Point(1, 1), Point(5, 5)),
        Segment(Point(2, 3), Point(6, -1)),
        Segment(Point(1, 2), Point(7, 2)),
        Segment(Point(4, 1), Point(4, 5)),
    ]
    intersections = bentley_ottmann(segments)
    print("Intersections found:")
    for point in intersections:
        print(point)

    plot_result(segments, intersections)

if __name__ == "__main__":
    main()
