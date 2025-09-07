ANIMALS = ['aardvark', 'alligator', 'armadillo', 'antelope', 'baboon', 'bear', 'bobcat', 'butterfly', 'cat', 'camel', 'cow', 'chameleon', 'dog', 'dolphin', 'duck', 'dragonfly', 'eagle', 'elephant', 'emu', 'echidna', 'fish', 'frog', 'flamingo', 'fox', 'goat', 'giraffe', 'gibbon', 'gecko', 'hyena', 'hippopotamus', 'horse', 'hamster', 'insect', 'impala', 'iguana', 'ibis', 'jackal', 'jaguar', 'jellyfish', 'kangaroo', 'kiwi', 'koala', 'killerwhale', 'lemur', 'leopard', 'llama', 'lion', 'monkey', 'mouse', 'moose', 'meercat', 'numbat', 'newt', 'ostrich', 'otter', 'octopus', 'orangutan', 'penguin', 'panther', 'parrot', 'pig', 'quail', 'quokka', 'quoll', 'rat', 'rhinoceros', 'racoon', 'reindeer', 'rabbit', 'snake', 'squirrel', 'sheep', 'seal', 'turtle', 'tiger', 'turkey', 'tapir', 'unicorn', 'vampirebat', 'vulture', 'wombat', 'walrus', 'wildebeast', 'wallaby', 'yak', 'zebra']

class Symbol:
    def __init__(self, letter, frequency):
        self.letter = letter
        self.frequency = frequency

class SymbolSeqenceChecker:
    def __init__(self, letter_seqence):
        self.letter_seqence = letter_seqence
        self.sequence = self.__build_seqence()
    
    def __build_seqence(self):
        self.sequence = []  # Initialize the sequence list
        current_symbol = Symbol('', 0)
        for letter in self.letter_seqence:
            if letter == current_symbol.letter:
                current_symbol.frequency += 1
            else:
                if current_symbol.frequency > 0:
                    self.sequence.append(current_symbol)
                current_symbol = Symbol(letter, 1)
        # Don't forget to append the last symbol
        if current_symbol.frequency > 0:
            self.sequence.append(current_symbol)
        return self.sequence

    def same_sequence(self, seqence):
        compare_sequence = seqence
        if len(compare_sequence) != len(self.sequence):
            return False
        if compare_sequence[-1].letter == self.sequence[0].letter:
            compare_sequence = compare_sequence.reverse()
        for i in range(len(seqence)):
            if seqence[i].letter != self.sequence[i].letter or seqence[i].frequency != self.sequence[i].frequency:
                return False
        return True
        return seqence == self.sequence
    
    

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
    prepared_photo_letters = prepare_letters(photo)
    symbol_seqence_checker = SymbolSeqenceChecker(prepared_photo_letters)
    for symbol in symbol_seqence_checker.sequence:
        print(symbol.letter, symbol.frequency)
    return find_animal(photo)

road_kill('==========h===yyyyyy===eeee=n==a========')
