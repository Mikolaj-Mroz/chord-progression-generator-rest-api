from random import choice, getrandbits
from midiutil import MIDIFile


class Scale:
    mode = 0 # major or minor
    key = 0
    notes = []
    chords = {}
    progression = {'chords': []}
    midiname = 0

    # list of all notes
    all_notes = ['c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#', 'a', 'a#', 'b']

    # list of types of chords
    all_chords = {
        'major' : ['major', 'major', 'minor', 'major', 'major', 'minor', 'minor'], 
        'minor' : ['minor', 'dimnished', 'major', 'minor', 'minor', 'major', 'major']
        }
    
    # key construction
    constructs = {
        'major' : [2, 2, 1, 2, 2, 2],
        'minor' : [2, 1, 2, 2, 1, 2]
        }

    def __init__(self, key, mode):
        self.key = key
        self.mode = mode
        self.midiname = getrandbits(32)

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
            chord = {'notes': []}
            chord_name = f'{self.notes[chord_index]} {name}'
            for i in range(0,3):
                chord['notes'].append(self.notes[chord_index])
                chord_index += 2
            self.chords[chord_name] = chord
    
    # generate random progression out of possible chords

    def generate(self):
        for i in range(0,4):
            chord_choice = choice(list(self.chords.keys()))
            self.progression['chords'].append({chord_choice:self.chords[chord_choice]})
        
        base = 60 # key of C5 in midi
        degrees = []

        # add notes to midi
        for chords in self.progression['chords']:
            for chord in chords:
                for note in chords[chord]['notes']:
                    degrees.append(60 + self.all_notes.index(note))
        midi = MIDIFile(1)

        midi.addTempo(0, 0, 140)

        # append chords to file
        loop_index = 0
        for i in range(0,4):
            for note in range(0,3):
                pitch = degrees[loop_index]
                midi.addNote(0, 0, pitch, 4*i, 4 ,100)
                loop_index += 1
        
        with open(f"application/server/static/{self.midiname}.mid", "wb") as output_file:
            midi.writeFile(output_file)
    
