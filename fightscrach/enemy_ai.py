# krece se do najblize mete ako je meelee, ako je range to max ranga ako je moguce

# 30% da baci spel ako ima mane (100% ako moze kombo)
# 70% da napadne
# ako je range, i ima neprijatelja u 2-3 ranga, pomeri se pa akcija
# ako je range 40% da napadne heroja u backlinu
# ako je range 70% da napadne heroja ispod 30% hp



def find_closest_target(reference_point, targets):

    if not targets:
        return None

    closest_target = None
    closest_distance = float('inf')  # Initialize with positive infinity

    for target in targets:
        # Calculate the distance between the reference point and the current target
        distance = calculate_distance(reference_point, target)

        # Update closest target if the current target is closer
        if distance < closest_distance:
            closest_distance = distance
            closest_target = target

    return closest_target

def calculate_distance(point1, point2):

    x1, y1 = point1
    x2, y2 = point2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5  # Square root of the squared differences


















