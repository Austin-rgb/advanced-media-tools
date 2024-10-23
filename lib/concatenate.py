from pydub import AudioSegment
import os

file1 = os.sys.argv[1]
file2 = os.sys.argv[2]
# Load audio files
audio1 = AudioSegment.from_file("file1.mp3")
audio2 = AudioSegment.from_file("file2.mp3")

# Combine audio files
combined = audio1 + audio2

# Extract base names (removing directory paths)
base_name1 = os.path.basename(file1)
base_name2 = os.path.basename(file2)

# Create a valid output file name
output_filename = f"{base_name1.split('.')[0]}_concat_{base_name2.split('.')[0]}.mp3"

# Export the combined audio file
combined.export(output_filename, format="mp3")
