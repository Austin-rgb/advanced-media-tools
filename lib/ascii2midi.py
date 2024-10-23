import re
from midiutil import MIDIFile

keys = "abcdefghijklmnopqrstuvwxyz"

def key2note(note, start=50):
    try:
        return start + keys.index(note)
    except:
        return start + 1

def parse_beat(beat):
    note = beat[0]
    duration = float(beat[1:]) if len(beat) > 1 else 1.0
    return note, duration

def convert_string_to_midi(beat_string, bpm=120):
    midi = MIDIFile(1)
    track = 0
    time = 0
    midi.addTempo(track, time, bpm)
    
    # Updated pattern to match fractional durations
    pattern = r'([a-z]\d*\.?\d*)|(\s\d*\.?\d*)'
    matches = re.findall(pattern, beat_string)
    
    for match in matches:
        beat = match[0] if match[0] else match[1]  # Choose the non-empty match
        
        if beat[0].isspace():
            # Handle rest
            _, duration = parse_beat(beat)
            time += duration  # Advance time without adding a note
        else:
            # Handle note
            note, duration = parse_beat(beat)
            midi_note = key2note(note, 60)
            midi.addNote(track, 0, midi_note, time, duration, 100)
            time += duration
    
    with open("output.mid", "wb") as output_file:
        midi.writeFile(output_file)

# Example usage with fractional durations
beat_string = "a0.5 b0.25 c0.75 d1.5 e0.1"
convert_string_to_midi(beat_string)
