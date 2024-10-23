import librosa

# Load the vocal MP3 file
vocal_file = 'vocals.wav'
y, sr = librosa.load(vocal_file)

# Extract tempo and beat frames
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
print(f'Tempo: {tempo} BPM')

# Extract pitch (optional, if you want to base melody on vocal pitch)
pitches, magnitudes = librosa.core.piptrack(y=y, sr=sr)

from magenta.models.melody_rnn import melody_rnn_sequence_generator
from magenta.protobuf import generator_pb2
from magenta.music import midi_io

# Initialize the model
generator = melody_rnn_sequence_generator.get_generator_map()['basic_rnn'](
    checkpoint='basic_rnn.mag'
)

# Set up the generator options
generator_options = generator_pb2.GeneratorOptions()
generator_options.args['temperature'].float_value = 1.0  # Adjust temperature to control randomness

# Define the melody length based on the vocal track
length_seconds = librosa.get_duration(y=y, sr=sr)
generator_options.generate_sections.add(start_time=0, end_time=length_seconds)

# Generate the melody
sequence = generator.generate(input_sequence=None, generator_options=generator_options)

# Save the melody as a MIDI file
midi_file = 'generated_melody.mid'
midi_io.sequence_proto_to_midi_file(sequence, midi_file)

from pydub import AudioSegment

# Load the vocal track and generated melody
vocal_track = AudioSegment.from_file("vocal.mp3")
melody_track = AudioSegment.from_file("output_melody.wav")

# Adjust the volume levels if necessary
melody_track = melody_track - 10  # Reduce melody volume

# Mix the tracks together
combined = vocal_track.overlay(melody_track)

# Export the final mix
combined.export("final_mix.mp3", format="mp3")
