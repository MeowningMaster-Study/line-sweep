import bisect
from avl_tree import AVLTree
from typing import Any
from event import Event, EventType
from point import Point
from plot import plotResult
from segment import Segment


def indexInList(index: int, list: list[Any]):
    return index > 0 and index < len(list)


def bentleyOttmann(segments: list[Segment]):
    events: list[Event] = []
    for segment in segments:
        events.append(Event(segment.p1, segment, EventType.BEGIN))
        events.append(Event(segment.p2, segment, EventType.END))
    events = sorted(events)

    activeSegments = AVLTree()
    intersections: list[Point] = []

    def processIntersection(segment1: Segment, segment2: Segment):
        intersection = segment1.intersection(segment2)
        if intersection:
            intersections.append(intersection)

    for event in events:
        if event.type == EventType.BEGIN:
            index = bisect.bisect_left(activeSegments, event.segment)
            activeSegments.insert(index, event.segment)
            if indexInList(index - 1, activeSegments):
                processIntersection(event.segment, activeSegments[index - 1])
            if indexInList(index + 1, activeSegments):
                processIntersection(event.segment, activeSegments[index + 1])
        elif event.type == EventType.END:
            activeSegments.remove(event.segment)
        elif event.type == EventType.INTERSECTION:
            # todo
            pass
        else:
            raise Exception("Unknown event type")

    return intersections


def main():
    segments = [
        Segment(Point(1, 1), Point(5, 5)),
        Segment(Point(2, 3), Point(6, -1)),
        Segment(Point(1, 2), Point(7, 2)),
        Segment(Point(4, 1), Point(4, 5)),
        Segment(Point(0, 0), Point(5, 1)),
    ]
    intersections = bentleyOttmann(segments)
    print("Intersections")
    for point in intersections:
        print(point)

    plotResult(segments, intersections)


if __name__ == "__main__":
    main()
