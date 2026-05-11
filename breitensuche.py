# In diesen Program soll die Breitensuche erklaert werden
import vis
import labyrinth

def get_direction(prev, after):
    dx = after[0] - prev[0]
    dy = after[1] - prev[1]
    if   dx == 1:  return 0  # rechts
    elif dy == -1: return 1  # oben
    elif dx == -1: return 2  # links
    elif dy == 1:  return 3  # unten

# Das Labyrinth
lab = labyrinth.lab10

start = (1, 1) # Start position (S)
x, y = start
queue = [] # Der Stapel für die Tiefensuche

# Das dritte Element ist die Richtung: 0 = rechts, 1 = oben, 2 = links, 3 = unten
queue.append(start)  # Startposition zum Stapel hinzufügen

known = [start] # Liste der besuchten Positionen
parent = {start: None}

# Nachbarn auf den Stapel hinzufügen
abs_neighbor = [(x+1, y), (x, y-1), (x-1, y), (x, y+1)]
for (i, j) in abs_neighbor: # Alle Nachbarn
    if lab[j][i] != "#" and not (i, j) in known: # Ist der Nachbar relevant?
        parent[(i, j)] = start
        queue.append((i, j)) # Relevante Nachbarn auf den Stapel tun

while queue: # Solange der Stapel nicht leer ist
    current_pos = queue.pop(0)  # Aktuelle Position vom Stapel nehmen (letztes Element)
    x, y = current_pos
    
    if current_pos in known: # Besucht?
        continue  # Wenn die Position bereits besucht wurde, überspringen

    known.append(current_pos)  # Aktuelle Position als besucht markieren
    if lab[y][x] == "Z": # Ziel?
        print("Ziel gefunden:", current_pos)  # Ziel gefunden
        break  # Schleife verlassen
    
    for (i, j) in [(x+1, y), (x, y-1), (x-1, y), (x, y+1)]: # Alle Nachbarn
        if lab[j][i] != "#" and (i, j) not in known: # Ist der Nachbar relevant?
            parent[(i, j)] = current_pos
            queue.append((i, j)) # Relevante Nachbarn auf den Stapel tun

# Visualizieren des weges
path = vis.print_lab(current_pos, parent, start, lab)
print(f"\nWeg: {' -> '.join(str(p) for p in path)}")
