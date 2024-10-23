from pydub import AudioSegment
import sys

file = sys.argv[1]
# Load the stereo track
stereo_track = AudioSegment.from_file(file)

# Split into left and right channels
left_channel = stereo_track.split_to_mono()[0]
right_channel = stereo_track.split_to_mono()[1]

# Reduce the volume of the side channels to narrow the stereo field
left_channel = left_channel - 6  # Decrease by 6dB
right_channel = right_channel - 6  # Decrease by 6dB

# Recombine the channels
narrowed_stereo = AudioSegment.from_mono_audiosegments(left_channel, right_channel)

# Save the result
narrowed_stereo.export(f"{file}.narrowed.mp3", format="mp3")
