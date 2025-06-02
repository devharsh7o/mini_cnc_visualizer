import matplotlib.pyplot as plt
from gcode_parser import parse_gcode

def plot_toolpath(path):
    fig, ax = plt.subplots(figsize=(6, 6))
    xs, ys = [], []
    last = None

    for i, point in enumerate(path):
        if last is not None:
            color = 'red' if point['move'] == 'G0' else 'blue'
            linewidth = 1 if point['move'] == 'G0' else 2
            # Optionally, use Z to change color or linestyle for different layers
            ax.plot([last['x'], point['x']], [last['y'], point['y']],
                    color=color, linewidth=linewidth)
        last = point
        xs.append(point['x'])
        ys.append(point['y'])

    # Mark start and end points
    ax.scatter(xs[0], ys[0], color='green', label='Start', zorder=5)
    ax.scatter(xs[-1], ys[-1], color='orange', label='End', zorder=5)

    ax.set_title('CNC Tool Path Visualization')
    ax.set_xlabel('X (mm)')
    ax.set_ylabel('Y (mm)')
    ax.axis('equal')
    ax.grid(True)
    ax.legend()
    plt.show()

def print_stats(path):
    total_distance = 0
    last = None
    for point in path:
        if last is not None:
            dx = point['x'] - last['x']
            dy = point['y'] - last['y']
            dz = point['z'] - last['z']
            total_distance += (dx**2 + dy**2 + dz**2) ** 0.5
        last = point
    print(f"Total moves: {len(path)}")
    print(f"Total toolpath distance: {total_distance:.2f} mm")

import sys

import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = 'sample_square.gcode'
    toolpath = parse_gcode(filename)
    print_stats(toolpath)
    plot_toolpath(toolpath)

