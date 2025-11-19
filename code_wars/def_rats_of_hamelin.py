def count_deaf_rats(town):
    town = town.replace(' ', '')
    
    piper_pos = town.find('P')
    
    before = deaf_rats_parser(town[:piper_pos])
    after = deaf_rats_parser(town[piper_pos + 1:])
    
    return before.count('O~') + after.count('~O')

def deaf_rats_parser(rats: str):
    return [rats[i:i+2] for i in range(0, len(rats), 2)]

