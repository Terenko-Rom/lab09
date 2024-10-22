import string as s
def get_polygon_name(sides):
    alphabet = s.ascii_uppercase
    name = ""
    for i in range(sides):
        name += alphabet[i % len(alphabet)]
    return name
sides = 5
polygon_name = get_polygon_name(sides)
print(f"Назва многокутника: {polygon_name}")