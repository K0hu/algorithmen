# Der unterschied hier zu den andere ist das es Gewichte gibt. 
# Es ist das gleiche Prinzip von der breitensuche, aber es priorisiert Bestimmte Felder
# Deshalb gibt es jetzt noch im Labyrinth wege die schwerer sind zu begehen. 
# Gewichte:
# . = 1 (Weg)
# * = 2 (Steine)
# % = 3 (Loecher im Boden)
# & = 5 (Falle)
import vis
import labyrinth

# Das Labyrinth
lab = labyrinth.lab3

weight = {"Z": 0, ".": 1, "*": 2, "%": 3, "&": 5, "#": 10} # Zuordnung der Gewichtungen zu den Feldertypen
start = (1, 1) # Start position

queue = [(0, start)] # Die "Warteschlange" 
known = [start] # Liste der besuchten Positionen
parent = {start: None}

def add_neighbors(cost: int, pos: tuple[int]) -> None:
    # Nachbarn auf den Stapel hinzufügen
    global queue
    x, y = pos
    neighbor = [(x+1, y), (x, y-1), (x-1, y), (x, y+1)] 

    for (i, j) in neighbor: # Alle Nachbarn
        if lab[j][i] != "#" and not (i, j) in known: # Ist der Nachbar relevant?
            if (i, j) not in parent: # Keine doppelt hinzufuegen fuer den resultierenden Weg
                parent[(i, j)] = pos
            queue.append((cost + weight[lab[j][i]], (i, j))) # Relevante Nachbarn auf den Stapel tun

add_neighbors(0, start) 

pos = start # Aktuelle position auf Start setzten
while queue: # Solange die Warteschlange nicht leer ist
    queue.sort(key=lambda n: n[0])
    cost, pos = queue.pop(0) # Erstes Element vom Queue nehmen
    x, y = pos

    if pos in known: # Besucht?
        continue # Naechtes aus der Warteschlange

    if lab[y][x] == "Z":
        print("Ziel gefunden:", pos)  # Ziel gefunden
        break  # Schleife verlassen
    add_neighbors(cost, pos)

# Visualizieren des weges
path = vis.print_lab(pos, parent, start, lab)
