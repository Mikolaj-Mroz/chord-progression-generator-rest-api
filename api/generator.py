import enum
from random import choice
from midiutil import MIDIFile


class Scale:
    mode = 0 # major or minor
    key = 0
    notes = []
    chords = {}
    progression = []

    # list of all notes
    all_notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

    # list of all possible chords in a key
    all_chords = {
        'major' : ['Major', 'Major', 'Minor', 'Major', 'Major', 'Minor', 'Minor'], 
        'minor' : ['Minor', 'Dimnished', 'Major', 'Minor', 'Minor', 'Major', 'Major']
        }
    
    # key construction
    constructs = {
        'major' : [2, 2, 1, 2, 2, 2],
        'minor' : [2, 1, 2, 2, 1, 2]
        }

    def __init__(self, key, mode):
        self.key = key
        self.mode = mode

        # set notes in scale
        self.notes.append(self.key)
        note_index = self.all_notes.index(key)
        for step in self.constructs[mode]:
            note_index += step
            self.notes.append(self.all_notes[note_index])
        self.notes.extend(self.notes)
        
        # set chords in scale
        
        for i, name in enumerate(self.all_chords[mode]):
            chord_index = i
            chord = []
            chord_name = f'{self.notes[chord_index]} {name}'
            for i in range(0,3):
                chord.append(self.notes[chord_index])
                chord_index += 2
            self.chords[chord_name] = chord
    
    def generate(self):
        for i in range(0,4):
            chord_choice = choice(list(self.chords.keys()))
            self.progression.append({chord_choice:self.chords[chord_choice]})
        
        base = 60
        degrees = []
        for chords in self.progression:
            for chord in chords:
                for note in chords[chord]:
                    degrees.append(60 + self.all_notes.index(note))
        midi = MIDIFile(1)

        midi.addTempo(0, 0, 140)

        loop_index = 0
        for i in range(0,4):
            for note in range(0,3):
                pitch = degrees[loop_index]
                midi.addNote(0, 0, pitch, 4*i, 4 ,100)
                loop_index += 1
        
        with open("major-scale.mid", "wb") as output_file:
            midi.writeFile(output_file)

        

cminor = Scale('C', 'minor')
cminor.generate()
print(cminor.progression)


## fix chord notation