import random

FIELD_SIZE = 10

def create_empty_field():
    return [['~' for _ in range(FIELD_SIZE)] for _ in range(FIELD_SIZE)]

def print_field(field):
    print("  " + " ".join(str(i) for i in range(FIELD_SIZE)))
    for idx, row in enumerate(field):
        print(chr(65 + idx) + " " + " ".join(row))

def can_place_ship(field, x, y, length, orientation):
    if orientation == 'H':
        if x + length > FIELD_SIZE:
            return False
        return all(field[y][x + i] == '~' for i in range(length))
    elif orientation == 'V':
        if y + length > FIELD_SIZE:
            return False
        return all(field[y + i][x] == '~' for i in range(length))

def place_ship(field, x, y, length, orientation):
    if orientation == 'H':
        for i in range(length):
            field[y][x + i] = '■'
    elif orientation == 'V':
        for i in range(length):
            field[y + i][x] = '■'

def place_all_ships(field):
    ships = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
    for ship_length in ships:
        placed = False
        while not placed:
            x = random.randint(0, FIELD_SIZE - 1)
            y = random.randint(0, FIELD_SIZE - 1)
            orientation = random.choice(['H', 'V'])
            if can_place_ship(field, x, y, ship_length, orientation):
                place_ship(field, x, y, ship_length, orientation)
                placed = True

if __name__ == "__main__":
    field = create_empty_field()
    place_all_ships(field)
    print_field(field)
