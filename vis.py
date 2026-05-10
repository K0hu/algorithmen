def print_lab(pos: tuple, parent, start, lab) -> list:
    # Weg rekonstruieren
    path = []
    node = pos
    while node is not None:
        path.append(node)
        node = parent[node]
    path.reverse()

    # Visualisierung
    def get_direction(prev, after):
        dx = after[0] - prev[0]
        dy = after[1] - prev[1]
        if   dx == 1:  return 0  # rechts
        elif dy == -1: return 1  # oben
        elif dx == -1: return 2  # links
        elif dy == 1:  return 3  # unten

    RESET  = "\033[0m"
    COLORS = {
        "K": "\033[1;33m",   # Weg: Gelb
        "S": "\033[1;32m",   # Start: Grün
        "Z": "\033[1;31m",   # Ziel: Rot
        "#": "\033[90m",     # Wand: Grau
        "*": "\033[36m",     # Steine: Cyan
        "%": "\033[35m",     # Loecher: Magenta
        "&": "\033[31m",     # Falle: Rot
        ".": "\033[37m",     # Weg: Weiß
    }

    path_set = set(path)
    sx, sy = start
    goal = pos

    for y, row in enumerate(lab):
        line = ""
        for x, cell in enumerate(row):
            if (x, y) == (sx, sy):
                line += COLORS["S"] + "S" + RESET + " "
            elif (x, y) == goal:
                line += COLORS["Z"] + "Z" + RESET + " "
            elif (x, y) in path_set:
                prev = path[path.index((x, y)) - 1]
                match get_direction(prev, (x, y)):
                    case 0:
                        line += COLORS["K"] + ">" + RESET + " "
                    case 1: 
                        line += COLORS["K"] + "^" + RESET + " "
                    case 2:
                        line += COLORS["K"] + "<" + RESET + " "
                    case 3:  
                        line += COLORS["K"] + "v" + RESET + " "
            else:
                line += COLORS.get(cell, "") + cell + RESET + " "
        print(line)
    
    return path
