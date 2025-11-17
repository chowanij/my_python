def paint_letterboxes(start, finish):
    counter_dict = {str(k): 0 for k in range(0, 10)}
    letterbox_symbols = ''.join(str(i) for i in range(start, finish + 1))
    for c in letterbox_symbols:
        counter_dict[c] += 1
    return [ v for k, v in counter_dict.items()]


print (paint_letterboxes(125, 132))
