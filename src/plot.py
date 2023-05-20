import matplotlib.pyplot as plt
from point import Point

from segment import Segment


def plotResult(segments: list[Segment], points: list[Point]):
    fig, ax = plt.subplots()

    for seg in segments:
        x = [seg.p1.x, seg.p2.x]
        y = [seg.p1.y, seg.p2.y]
        ax.plot(x, y, color="black")

        x_mean = (
            seg.p1.x + seg.p2.x
        ) / 2  # Calculate the x-coordinate of the segment midpoint
        y_mean = (
            seg.p1.y + seg.p2.y
        ) / 2  # Calculate the y-coordinate of the segment midpoint
        ax.annotate(seg.id, (x_mean, y_mean), ha="center", va="center")

    for point in points:
        ax.plot(point.x, point.y, marker="o", markersize=5, color="red")

    ax.set_aspect("equal")
    plt.show()
