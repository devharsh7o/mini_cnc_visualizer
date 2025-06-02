def parse_gcode(filename):
    """
    Parses a G-code file and extracts (X, Y, Z, move_type) from G0 and G1 commands.
    Returns a list of dicts: [{'x':..., 'y':..., 'z':..., 'move':...}, ...]
    """
    path = []
    x, y, z = 0, 0, 0
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith(';') or line == '':
                continue
            if line.startswith('G0') or line.startswith('G1'):
                move_type = line[:2]
                parts = line.split()
                for part in parts:
                    if part.startswith('X'):
                        x = float(part[1:])
                    elif part.startswith('Y'):
                        y = float(part[1:])
                    elif part.startswith('Z'):
                        z = float(part[1:])
                path.append({'x': x, 'y': y, 'z': z, 'move': move_type})
    return path

if __name__ == "__main__":
    toolpath = parse_gcode('sample_square.gcode')
    print(toolpath)
