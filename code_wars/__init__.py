from re import match

def road_kill(photo):
    remains = photo.replace('=', '')
    
    for animal in ANIMALS:
        parts = '^' + '+'.join(c for c in animal) + '+$'
        if match(parts, remains) or match(parts, remains[::-1]):
            return animal
    return '??'