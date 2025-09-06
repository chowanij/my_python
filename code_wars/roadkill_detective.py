ANIMALS = ['aardvark', 'alligator', 'armadillo', 'antelope', 'baboon', 'bear', 'bobcat', 'butterfly', 'cat', 'camel', 'cow', 'chameleon', 'dog', 'dolphin', 'duck', 'dragonfly', 'eagle', 'elephant', 'emu', 'echidna', 'fish', 'frog', 'flamingo', 'fox', 'goat', 'giraffe', 'gibbon', 'gecko', 'hyena', 'hippopotamus', 'horse', 'hamster', 'insect', 'impala', 'iguana', 'ibis', 'jackal', 'jaguar', 'jellyfish', 'kangaroo', 'kiwi', 'koala', 'killerwhale', 'lemur', 'leopard', 'llama', 'lion', 'monkey', 'mouse', 'moose', 'meercat', 'numbat', 'newt', 'ostrich', 'otter', 'octopus', 'orangutan', 'penguin', 'panther', 'parrot', 'pig', 'quail', 'quokka', 'quoll', 'rat', 'rhinoceros', 'racoon', 'reindeer', 'rabbit', 'snake', 'squirrel', 'sheep', 'seal', 'turtle', 'tiger', 'turkey', 'tapir', 'unicorn', 'vampirebat', 'vulture', 'wombat', 'walrus', 'wildebeast', 'wallaby', 'yak', 'zebra']

def letter_freq(letters):
    freq = {}
    for letter in letters:
        freq[letter] = freq.get(letter, 0) + 1
    return freq

def prepare_letters(photo):
    return ''.join(filter(lambda letter: letter.isalpha(), photo))

def can_form_animal(animal_name, photo):
    roadkill_letters = prepare_letters(photo)
    roadkill_freq = letter_freq(roadkill_letters)
    animal_freq = letter_freq(animal_name)
    if roadkill_freq.keys() != animal_freq.keys():
        return False
    print(roadkill_freq.keys() != animal_freq.keys())
    print(roadkill_freq.keys())
    print(animal_freq.keys())
    for letter, needed_freq in animal_freq.items():
        if roadkill_freq.get(letter, 0) < needed_freq:
            return False
    return True

def find_animal(photo):
    for animal in ANIMALS:
        if can_form_animal(animal, photo):
            return animal
    return '??'



def road_kill(photo):
    if (' ' in photo):
        return '??'
    return find_animal(photo)

print(road_kill('=======fly===dragon===='))