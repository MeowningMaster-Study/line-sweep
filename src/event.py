from enum import Enum
from point import Point

from segment import Segment


class EventType(Enum):
    BEGIN = 0
    END = 1
    INTERSECTION = 2


class Event:
    def __init__(self, point: Point, segment: Segment, type: EventType):
        self.point = point
        self.segment = segment
        self.type = type

    def __lt__(self, other: "Event"):
        return self.point.x < other.point.x
