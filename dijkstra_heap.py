import heapq # Fuer schnellere ergebnisse
import vis
import labyrinth

# Das Labyrinth
lab = labyrinth.lab10

weight = {"Z": 0, ".": 1, "*": 2, "%": 3, "&": 5, "#": 10} # Die Gewichtungen
start = (1, 1) # Start position

queue = [] # Warteschlange
heapq.heappush(queue, (0, start)) 
known = set() # Set fuer keine doppel Positionen
parent = {start: None} 

pos = start # Aktuelle position auf start setzten
while queue:
    cost, pos = heapq.heappop(queue) # "guenstiges" Element der Warteschlange nehmen

    if pos in known: # Schon bekannt?
        continue
    known.add(pos) # Merken

    x, y = pos
    if lab[y][x] == "Z": # Ziel?
        print("Ziel gefunden:", pos)
        break

    for dx, dy in [(1,0),(0,-1),(-1,0),(0,1)]: # Alle Nachbarn positionen
        nx, ny = x+dx, y+dy
        neighbor = (nx, ny) # Nachbar
        if lab[ny][nx] != "#" and neighbor not in known: # Ist der Nachbar relevant?
            if neighbor not in parent: # Keine doppelt hinzufuegen fuer den resultierenden Weg
                parent[neighbor] = pos
            heapq.heappush(queue, (cost + weight[lab[ny][nx]], neighbor)) # Hinzufuegen zur schlange

# visualisieren
path = vis.print_lab(pos, parent, start, lab)
print(f"\nWeg: {' -> '.join(str(p) for p in path)}")
print(f"Gesamtkosten: {cost}")