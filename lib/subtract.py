from pydub import AudioSegment
import sys
original = sys.argv[1]
instrumental = sys.argv[2]

# Load the original and instrumental tracks
original = AudioSegment.from_file(original)
instrumental = AudioSegment.from_file(instrumental)

# Invert the phase of the instrumental
inverted_instrumental = instrumental.invert_phase()

# Mix the inverted instrumental with the original track
vocal_only = original.overlay(inverted_instrumental)

# Export the result
vocal_only.export(f"{original}-minus-{instrument}.mp3", format="mp3")
