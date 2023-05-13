import matplotlib.pyplot as plt

def plot_result(segments, points):
    fig, ax = plt.subplots()
    
    for seg in segments:
        x = [seg.p1.x, seg.p2.x]
        y = [seg.p1.y, seg.p2.y]
        ax.plot(x, y)

    for point in points:
        ax.plot(point.x, point.y, marker='o', markersize=5, color="red")
    
    ax.set_aspect('equal')
    plt.show()
