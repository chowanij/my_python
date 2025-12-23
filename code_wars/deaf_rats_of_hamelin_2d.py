from math import sqrt

s = """
        ↗
P ↓   ↖ ↑
    ←   ↓
  ↖ ↙   ↙
↓ ↓ ↓    
""".strip("\n").split("\n")

direction_dict = {
    '←': (-1, 0),
    '↑': (0, 1),
    '→': (1, 0),
    '↓': (0, -1),
    '↖': (-1, 1),
    '↗': (1, 1),
    '↘': (1, -1),
    '↙': (-1, -1)
}


def count_deaf_rats(s):
    paving_stones = {}
    piper = (0,0)
    deaf_rats = 0
    for y, stones_row  in enumerate(s, 1):
        for x, stone in enumerate(stones_row, 0):
            if direction_dict.get(stone):
                paving_stones[(x, len(s) - y)] = direction_dict.get(stone)
            elif stone == 'P':
                piper = (x, len(s) - y)
    for k, v in paving_stones.items():
        p_d = sqrt((k[0]- piper[0])**2 + (k[1] - piper[1])**2)
        p_n = sqrt((k[0] + v[0] - piper[0])**2 + (k[1] + v[1] - piper[1])**2)
        deaf_rats += 1 if p_n > p_d else 0
    return deaf_rats

print (f' number of deaf rats: {count_deaf_rats(s)}')
