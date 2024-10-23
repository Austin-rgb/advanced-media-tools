import librosa
import soundfile as sf
from pydub import AudioSegment
import numpy as np
import os

# Load audio files
file1 = 'Nilimpoteza my mum/Nilimpoteza_my_mum.mp3'
file2 = 'Nilimpoteza my mum/accompaniment.wav'

# Load audio files with librosa for BPM detection
y1, sr1 = librosa.load(file1)
y2, sr2 = librosa.load(file2)

# Detect BPM of both tracks
tempo1, _ = librosa.beat.beat_track(y=y1, sr=sr1)
tempo2, _ = librosa.beat.beat_track(y=y2, sr=sr2)

# Ensure tempo1 and tempo2 are scalar values
tempo1 = tempo1.item() if isinstance(tempo1, np.ndarray) else tempo1
tempo2 = tempo2.item() if isinstance(tempo2, np.ndarray) else tempo2

# Calculate the ratio to match BPMs
ratio = float(tempo1) / float(tempo2)

# Adjust the tempo of the second track to match the first track
y2_matched = librosa.effects.time_stretch(y2, rate=ratio)

# Save the tempo-matched track temporarily using soundfile
temp_file2 = "temp_matched.wav"
sf.write(temp_file2, y2_matched, sr2)

# Load tempo-matched audio with pydub
audio1 = AudioSegment.from_file(file1)
audio2 = AudioSegment.from_file(temp_file2)

# Find the max points in both tracks
max_point1 = np.argmax(np.abs(y1))
max_point2 = np.argmax(np.abs(y2_matched))

# Calculate the time difference to align peaks
time_diff = (max_point1 / sr1 * 1000) - (max_point2 / sr2 * 1000)

# Align audio2 with audio1 based on max points
if time_diff > 0:
    audio2 = AudioSegment.silent(duration=time_diff) + audio2
else:
    audio1 = AudioSegment.silent(duration=-time_diff) + audio1

# Overlay the audio files
combined = audio1.overlay(audio2)

# Extract base names (removing directory paths)
base_name1 = os.path.basename(file1)
base_name2 = os.path.basename(file2)

# Create a valid output file name
output_filename = f"{base_name1.split('.')[0]}_overlay_{base_name2.split('.')[0]}.mp3"

# Export the combined audio file
combined.export(output_filename, format="mp3")

print(f"Combined audio saved as {output_filename}")
