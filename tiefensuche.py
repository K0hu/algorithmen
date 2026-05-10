# In diesen Program soll die Tiefensuche erklaert werden
# Dieses Beispiel ist Rechts orientiert also prioriziert es rechts.
# Es wird relative von der Richtung (var: richtung) der rechte Nachbar als letztes auf den Stapel gelegt,
# so wird rechts bevorzugt. Es wird immer in die Richtung geguckt in die sich bewegt wurde. (Damit es keine absolute Richtung gibt)
import vis

def get_direction(prev, after):
    dx = after[0] - prev[0]
    dy = after[1] - prev[1]
    if   dx == 1:  return 0  # rechts
    elif dy == -1: return 1  # oben
    elif dx == -1: return 2  # links
    elif dy == 1:  return 3  # unten

# Das Labyrinth
lab = [
    ["#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"],
    ["#",".",".",".","#",".",".",".",".",".","#",".",".",".","#"],
    ["#",".","#",".","#",".","#","#","#",".","#",".","#",".","#"],
    ["#",".","#",".",".",".","#","Z","#",".",".",".","#",".","#"],
    ["#",".","#","#","#","#","#",".","#","#","#","#","#",".","#"],
    ["#",".",".",".",".",".",".",".",".",".",".",".","#",".","#"],
    ["#","#","#",".","#","#","#","#","#","#","#",".","#",".","#"],
    ["#",".",".",".","#",".",".",".",".",".","#",".",".",".","#"],
    ["#",".","#","#","#",".","#","#","#",".","#","#","#","#","#"],
    ["#",".",".",".",".",".","#",".",".",".",".",".",".",".","#"],
    ["#","#","#","#","#",".",".",".",".","#","#","#","#",".","#"],
    ["#",".",".",".",".",".",".","#",".",".",".",".",".",".","#"],
    ["#",".","#","#","#","#","#","#","#",".",".","#","#","#","#"],  
    ["#",".",".",".",".",".",".",".",".",".",".",".",".",".","#"],
    ["#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"],
]

direction = 2 # 0 = rechts, 1 = vorne, 2 = links, 3 = hinten
start = (2, 1) # Start position (S)
x, y = start
stack = [] # Der Stapel für die Tiefensuche

# Das dritte Element ist die Richtung: 0 = rechts, 1 = oben, 2 = links, 3 = unten
stack.append((start, direction))  # Startposition zum Stapel hinzufügen

known = [start] # Liste der besuchten Positionen
parent = {start: None}

# Nachbarn auf den Stapel hinzufügen
abs_neighbor = [(x+1, y), (x, y-1), (x-1, y), (x, y+1)]
relative_neighbor = abs_neighbor[direction:] + abs_neighbor[:direction]
for (i, j) in relative_neighbor: # Alle Nachbarn
    if lab[j][i] in (".", "Z") and not (i, j) in known: # Ist der Nachbar relevant?
        new_direction = get_direction(start, (i, j))
        parent[(i, j)] = start
        stack.append(((i, j), new_direction)) # Relevante Nachbarn auf den Stapel tun

while stack: # Solange der Stapel nicht leer ist
    current_pos, direction = stack.pop()  # Aktuelle Position vom Stapel nehmen (letztes Element)
    x, y = current_pos
    
    if current_pos in known: # Besucht?
        continue  # Wenn die Position bereits besucht wurde, überspringen

    known.append(current_pos)  # Aktuelle Position als besucht markieren
    if lab[y][x] == "Z": # Ziel?
        print("Ziel gefunden:", current_pos)  # Ziel gefunden
        break  # Schleife verlassen
    
    abs_neighbor = [(x+1, y), (x, y-1), (x-1, y), (x, y+1)]
    relative_neighbor = abs_neighbor[direction:] + abs_neighbor[:direction]
    for (i, j) in relative_neighbor: # Alle Nachbarn
        if lab[j][i] in (".", "Z") and (i, j) not in known: # Ist der Nachbar relevant?
            new_direction = get_direction(current_pos, (i, j))
            parent[(i, j)] = current_pos
            stack.append(((i, j), new_direction)) # Relevante Nachbarn auf den Stapel tun

# Visualizieren des weges
path = vis.print_lab(current_pos, parent, start, lab)
print(f"\nWeg: {' -> '.join(str(p) for p in path)}")
