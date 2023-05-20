import bisect
from typing import Any
from event import Event, EventType
from point import Point
from plot import plotResult
from segment import Segment


def indexInList(index: int, list: list[Any]):
    return index >= 0 and index < len(list)


def swap_items_by_index(lst, index1, index2):
    lst[index1], lst[index2] = lst[index2], lst[index1]


def bentleyOttmann(segments: list[Segment]):
    events: list[Event] = []
    for segment in segments:
        events.append(Event(segment.p1, segment, EventType.BEGIN))
        events.append(Event(segment.p2, segment, EventType.END))
    events = sorted(events, reverse=True)

    status: list[Segment] = []
    intersections: list[Point] = []

    def processIntersection(segment1: Segment, segment2: Segment):
        intersection = segment1.intersection(segment2)
        if intersection:
            intersections.append(intersection)
            events.append(
                Event(intersection, (segment1, segment2), EventType.INTERSECTION)
            )
            # i1, i2 = status.index(segment1), status.index(segment2)
            # print(segment1, segment2, i1, i2)

    def printStatus():
        print("Status")
        for seg in status:
            print(seg.id, seg)

    while len(events) != 0:
        event = events.pop()
        if event.type == EventType.BEGIN:
            index = bisect.bisect_left(status, event.segment)
            status.insert(index, event.segment)
            print("Begin", event.segment.id)
            printStatus()

            if indexInList(index - 1, status):
                processIntersection(event.segment, status[index - 1])
            if indexInList(index + 1, status):
                processIntersection(event.segment, status[index + 1])
        elif event.type == EventType.END:
            index = status.index(event.segment)
            if indexInList(index - 1, status) and indexInList(index + 1, status):
                processIntersection(status[index - 1], status[index + 1])
            del status[index]

            print("End", event.segment.id)
            printStatus()
        elif event.type == EventType.INTERSECTION:
            segment1, segment2 = event.segment
            i1, i2 = status.index(segment1), status.index(segment2)
            segment1.current_y = event.point.y
            segment2.current_y = event.point.y
            swap_items_by_index(status, i1, i2)

            minI = min(i1, i2)
            if indexInList(minI - 1, status):
                processIntersection(status[minI - 1], status[minI])

            maxI = max(i1, i2)
            if indexInList(maxI + 1, status):
                processIntersection(status[maxI + 1], status[minI])

            print("Intersection", segment1.id, segment2.id)
            printStatus()
        else:
            raise Exception("Unknown event type")

    return intersections


def main():
    segments = [
        Segment(Point(0, 0), Point(5, 1)),
        Segment(Point(1, 1), Point(5, 5)),
        Segment(Point(1, 2), Point(7, 2)),
        Segment(Point(2, 3), Point(6, -1)),
        Segment(Point(4, 1), Point(4, 5)),
        Segment(Point(5, 5), Point(5, 0)),
    ]

    print("Segments")
    for segment in segments:
        print(segment.id, segment)

    intersections = bentleyOttmann(segments)
    print("Intersections")
    for point in intersections:
        print(point)

    plotResult(segments, intersections)


if __name__ == "__main__":
    main()
