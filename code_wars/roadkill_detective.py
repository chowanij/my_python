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
        self.sequence = []
        current_symbol = Symbol('', 0)
        for letter in self.letter_seqence:
            if letter == current_symbol.letter:
                current_symbol.frequency += 1
            else:
                if current_symbol.frequency > 0:
                    self.sequence.append(current_symbol)
                current_symbol = Symbol(letter, 1)
        if current_symbol.frequency > 0:
            self.sequence.append(current_symbol)
        return self.sequence

    def same_sequence(self, seqence):
        compare_sequence = seqence.copy()
        if len(compare_sequence) != len(self.sequence):
            return False
        
        # Try both normal and reversed order
        def sequences_match(seq1, seq2):
            for i in range(len(seq1)):
                if (seq1[i].letter != seq2[i].letter or 
                    seq1[i].frequency > seq2[i].frequency):
                    return False
            return True
        
        # Try normal order first
        if sequences_match(compare_sequence, self.sequence):
            return True
        
        # Try reversed order
        compare_sequence.reverse()
        return sequences_match(compare_sequence, self.sequence)

def prepare_letters(photo):
    return ''.join(filter(lambda letter: letter.isalpha(), photo))

def can_form_animal(animal_name, photo):
    roadkill_seqence = SymbolSeqenceChecker(prepare_letters(photo))
    animal_seqence = SymbolSeqenceChecker(animal_name)

    return roadkill_seqence.same_sequence(animal_seqence.sequence)

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
    print(f"animal found: {find_animal(photo)}")
    return find_animal(photo)

road_kill('==========h===yyyyyy===eeee=n==a========')
