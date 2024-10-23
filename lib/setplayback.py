from pydub import AudioSegment
import sys

def change_playback_speed(sound, speed=1.0):
    # Manually adjust frame rate to change playback speed
    sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={
         "frame_rate": int(sound.frame_rate * speed)
     })

    # Convert the altered frame rate sound back to its original frame rate
    return sound_with_altered_frame_rate.set_frame_rate(sound.frame_rate)

# Get the audio file path and playback speed factor from command-line arguments
audio_path = sys.argv[1]
speed_factor = float(sys.argv[2])

# Load the audio file
audio_clip = AudioSegment.from_file(audio_path)

# Adjust the playback speed
adjusted_clip = change_playback_speed(audio_clip, speed=speed_factor)

# Export the modified audio
output_path = "output_audio.wav"
adjusted_clip.export(output_path, format="wav")

print(f"Audio saved to {output_path} with playback speed adjusted by a factor of {speed_factor}.")
