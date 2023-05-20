from enum import Enum
from typing import Union
from point import Point

from segment import Segment


class EventType(Enum):
    BEGIN = 0
    END = 1
    INTERSECTION = 2


class Event:
    def __init__(
        self,
        point: Point,
        segment: Union[Segment, tuple[Segment, Segment]],
        type: EventType,
    ):
        self.point = point
        self.segment = segment
        self.type = type

    def __lt__(self, other: "Event"):
        if self.point.x == other.point.x:
            if self.type == EventType.INTERSECTION:
                return True
            return self.point.y < other.point.y
        return self.point.x < other.point.x
